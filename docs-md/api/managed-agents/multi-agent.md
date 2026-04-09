# Multiagent sessions

Copy page

Multiagent is a Research Preview feature. [Request access](https://claude.com/form/claude-managed-agents) to try it.

Multi-agent orchestration lets one agent coordinate with others to complete complex work. Agents can act in parallel with their own isolated context, which helps improve output quality and improve time to completion.

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. An additional beta header is needed for research preview features. The SDK sets these beta headers automatically.

## How it works

All agents share the same container and filesystem, but each agent runs in its own session **thread**, a context-isolated event stream with its own conversation history. The coordinator reports activity in the **primary thread** (which is the same as the session-level event stream); additional threads are spawned at runtime when the coordinator decides to delegate.

Threads are persistent: the coordinator can send a follow-up to an agent it called earlier, and that agent retains everything from its previous turns.

Each agent uses its own configuration (model, system prompt, tools, MCP servers, and skills) as defined when that agent was created. Tools and context are not shared.

### What to delegate

Multiagent sessions work best when there are multiple well-scoped, specialized tasks in an overall goal:

- **Code review:** A reviewer agent with a focused system prompt and read-only tools.
- **Test generation:** A test agent that writes and runs tests without touching production code.
- **Research:** A search agent with web tools that summarizes findings back to the coordinator.

## Declare callable agents

When [defining your agent](managed-agents/agent-setup.md), list additional IDs of agents it is permitted to call:

CLI

```shiki
ant beta:agents create <<YAML
name: Engineering Lead
model: claude-sonnet-4-6
system: You coordinate engineering work. Delegate code review to the reviewer agent and test writing to the test agent.
tools:
  - type: agent_toolset_20260401
callable_agents:
  - type: agent
    id: $REVIEWER_AGENT_ID
    version: $REVIEWER_AGENT_VERSION
  - type: agent
    id: $TEST_WRITER_AGENT_ID
    version: $TEST_WRITER_AGENT_VERSION
YAML
```

Each entry in `callable_agents` must be the ID of an existing agent. Only one level of delegation is supported: the coordinator can call other agents, but those agents cannot call agents of their own.

Then create a session referencing the orchestrator:

curl

```shiki
session=$(curl -fsS https://api.anthropic.com/v1/sessions \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d '{"agent": "'$ORCHESTRATOR_ID'", "environment_id": "'$ENVIRONMENT_ID'"}')
```

The callable agents are resolved from the orchestrator's configuration. You don't need to reference them at session creation.

## Session threads

The **session-level event stream** (`/v1/sessions/:id/stream`) is considered the **primary thread**, containing an condensed view of all activity across all threads. You won't see called agents' individual traces, but you will see the start and end of their work. **Session threads** are where you drill into a specific agent's reasoning and tool calls.

The session status also is an aggregation of all agent activity; if at least one thread is `running`, then the overall session status will be `running` as well.

List all threads in a session as follows:

curl

```shiki
curl -fsS "https://api.anthropic.com/v1/sessions/$SESSION_ID/threads" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  | jq -r '.data[] | "[\(.agent_name)] \(.status)"'
```

Stream events from a specific thread:

curl

```shiki
curl -fsSN "https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID/stream" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" |
  while IFS= read -r line; do
    [[ $line == data:* ]] || continue
    json=${line#data: }
    case $(jq -r '.type' <<<"$json") in
      agent.message)
        printf '%s' "$(jq -j '.content[] | select(.type == "text") | .text' <<<"$json")"
        ;;
      session.thread_idle)
        break
        ;;
    esac
  done
```

List past events for a thread:

curl

```shiki
curl -fsS "https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID/events" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  | jq -r '.data[] | "[\(.type)] \(.processed_at)"'
```

## Multiagent event types

These events surface multiagent activity on the top-level session stream.

| Type | Description |
| --- | --- |
| `session.thread_created` | The coordinator spawned a new thread. Includes the `session_thread_id` and `model`. |
| `session.thread_idle` | An agent thread finished its current work. |
| `agent.thread_message_sent` | An agent sent a message to another thread. Includes `to_thread_id` and `content`. |
| `agent.thread_message_received` | An agent received a message from another thread. Includes `from_thread_id` and `content`. |

## Tool permissions and custom tools in threads

When a `callable_agent` thread needs something from your client ([permission](managed-agents/events-and-streaming.md) to run an `always_ask` tool, or the [result of a custom tool](managed-agents/events-and-streaming.md)) the request surfaces on the **session stream** with a `session_thread_id` field. Include the same `session_thread_id` when you post your response so the platform routes it back to the waiting thread.

- **`session_thread_id` is present:** the event originated in a subagent thread. Echo it on your reply.
- **`session_thread_id` is absent:** the event came from the primary thread. Reply without the field.
- Match on `tool_use_id` to pair requests with responses.

The example below extends the [tool confirmation handler](managed-agents/events-and-streaming.md) to route replies. The same pattern applies to `user.custom_tool_result`.

curl

```shiki
while IFS= read -r event_id; do
  pending=$(jq -r --arg id "$event_id" '.[$id]' <<<"$events_by_id")
  thread_id=$(jq -r '.session_thread_id // empty' <<<"$pending")
  jq -n --arg id "$event_id" --arg thread "$thread_id" '
    {events: [
      {type: "user.tool_confirmation", tool_use_id: $id, result: "allow"}
      + (if $thread != "" then {session_thread_id: $thread} else {} end)
    ]}' |
    curl -fsS "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -H "anthropic-beta: managed-agents-2026-04-01" \
      -H "content-type: application/json" \
      -d @-
done < <(jq -r '.stop_reason.event_ids[]' <<<"$data")
```

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
