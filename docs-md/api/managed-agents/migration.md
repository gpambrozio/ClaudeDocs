# Migration

Copy page

Claude Managed Agents replaces your hand-written agent loop with managed infrastructure. This page covers what changes when you migrate from a custom loop built on the [Messages API](build-with-claude/working-with-messages.md) or from the [Claude Agent SDK](agent-sdk/overview.md).

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

## From a Messages API agent loop

If you built an agent by calling `messages.create` in a `while` loop, executing tool calls yourself, and appending results to the conversation history, most of that code goes away.

### What you stop managing

| Before | After |
| --- | --- |
| You maintain the conversation history array and pass it back on every turn. | The session stores history server-side. Send events, receive events. |
| You parse `stop_reason: "tool_use"`, execute the tool, and loop back with a `tool_result` message. | Pre-built tools execute inside the container automatically. You only handle custom tools via `agent.custom_tool_use` events. |
| You provision your own sandbox for running agent-generated code. | The session container handles code execution, file operations, and bash. |
| You decide when the loop is done. | The session emits `session.status_idle` when the agent has nothing more to do. |

### Code comparison

**Before** (Messages API loop, simplified):

Python

```shiki
messages = [{"role": "user", "content": task}]
while True:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=messages,
        tools=tools,
    )
    messages.append({"role": "assistant", "content": response.content})
    if response.stop_reason == "end_turn":
        break
    for block in response.content:
        if block.type == "tool_use":
            result = execute_tool(block.name, block.input)
            messages.append(
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result,
                        }
                    ],
                }
            )
```

**After** (Claude Managed Agents):

curl

```shiki
agent=$(
  curl --fail-with-body -sS "https://api.anthropic.com/v1/agents?beta=true" \
    -H "x-api-key: ${ANTHROPIC_API_KEY}" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    --json '{
      "name": "Task Runner",
      "model": "claude-sonnet-4-6",
      "tools": [{"type": "agent_toolset_20260401"}]
    }'
)
agent_id=$(jq -r '.id' <<< "${agent}")

session_id=$(
  curl --fail-with-body -sS "https://api.anthropic.com/v1/sessions?beta=true" \
    -H "x-api-key: ${ANTHROPIC_API_KEY}" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    --json "$(jq -n --argjson a "${agent}" --arg env "${environment_id}" \
      '{agent: {type: "agent", id: $a.id, version: $a.version}, environment_id: $env}')" \
  | jq -r '.id'
)

# Open the SSE stream in the background, then send the user message.
stream_log=$(mktemp)
curl --fail-with-body -sS -N \
  "https://api.anthropic.com/v1/sessions/${session_id}/stream?beta=true" \
  -H "x-api-key: ${ANTHROPIC_API_KEY}" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  > "${stream_log}" &
stream_pid=$!

curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/sessions/${session_id}/events?beta=true" \
  -H "x-api-key: ${ANTHROPIC_API_KEY}" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  --json "$(jq -n --arg text "${task}" \
    '{events: [{type: "user.message", content: [{type: "text", text: $text}]}]}')" \
  > /dev/null

# Read events until the session goes idle.
while IFS= read -r line; do
  [[ ${line} == data:* ]] || continue
  event_type=$(jq -r '.type // empty' 2>/dev/null <<< "${line#data: }" || true)
  [[ ${event_type} == "session.status_idle" ]] && break
done < <(tail -f -n +1 "${stream_log}")

kill "${stream_pid}" 2>/dev/null || true
```

### What you still control

- **System prompt and model:** Same fields, now on the agent definition.
- **Custom tools:** Still declared with JSON Schema. Execution moves from inline handling to responding to `agent.custom_tool_use` events. See [Session event stream](managed-agents/events-and-streaming.md).
- **Context:** You can still inject context via the system prompt, [file resources](managed-agents/files.md), or [skills](managed-agents/skills.md).

## From the Claude Agent SDK

If you built with the [Claude Agent SDK](agent-sdk/overview.md), you're already working with agents, tools, and sessions as concepts. The difference is where they run: the SDK executes in a process you operate, while Managed Agents runs in Anthropic's infrastructure. Most of the migration is mapping SDK configuration objects to their API-side equivalents.

### What changes

| Agent SDK | Managed Agents |
| --- | --- |
| `ClaudeAgentOptions(...)` constructed per run | `client.beta.agents.create(...)` once; the Agent is persisted and versioned server-side. See [Agent setup](managed-agents/agent-setup.md). |
| `async with ClaudeSDKClient(...)` or `query(...)` | `client.beta.sessions.create(...)` then send and receive [events](managed-agents/events-and-streaming.md). |
| `@tool`-decorated functions dispatched automatically by the SDK | Declare as `{"type": "custom", ...}` on the Agent; your client handles `agent.custom_tool_use` events and replies with `user.custom_tool_result`. See [Tools](managed-agents/tools.md). |
| Built-in tools run in your process against your filesystem | `{"type": "agent_toolset_20260401"}` runs the same tools inside the session container against `/workspace`. |
| `cwd`, `add_dirs` point at local paths | Upload or mount [files](managed-agents/files.md) as session resources. |
| `system_prompt` and the `CLAUDE.md` hierarchy | A single `system` string on the Agent. Each update produces a new server-side version; pin sessions to a specific version to promote or roll back without a deploy. See [Agent setup](managed-agents/agent-setup.md). |
| `mcp_servers` configured and authenticated in one place | Declare servers on the Agent; provide credentials through a [Vault](managed-agents/vaults.md) on the Session. |
| `permission_mode`, `can_use_tool` | Per-tool [`permission_policy`](managed-agents/permission-policies.md); respond to `user.tool_confirmation` events for `always_ask` tools. |

### Code comparison

**Before** (Agent SDK):

```shiki
from claude_agent_sdk import (
    ClaudeAgentOptions,
    ClaudeSDKClient,
    create_sdk_mcp_server,
    tool,
)

@tool("get_weather", "Get the current weather for a city.", {"city": str})
async def get_weather(args: dict) -> dict:
    return {"content": [{"type": "text", "text": f"{args['city']}: 18°C, clear"}]}

options = ClaudeAgentOptions(
    model="claude-sonnet-4-6",
    system_prompt="You are a concise weather assistant.",
    mcp_servers={
        "weather": create_sdk_mcp_server("weather", "1.0", tools=[get_weather])
    },
)

async with ClaudeSDKClient(options=options) as agent:
    await agent.query("What's the weather in Tokyo?")
    async for msg in agent.receive_response():
        print(msg)
```

**After** (Managed Agents):

```shiki
from anthropic import Anthropic

client = Anthropic()

agent = client.beta.agents.create(
    name="weather-agent",
    model="claude-sonnet-4-6",
    system="You are a concise weather assistant.",
    tools=[
        {
            "type": "custom",
            "name": "get_weather",
            "description": "Get the current weather for a city.",
            "input_schema": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
            },
        }
    ],
)
environment = client.beta.environments.create(
    name="weather-env",
    config={"type": "cloud", "networking": {"type": "unrestricted"}},
)

session = client.beta.sessions.create(
    agent={"type": "agent", "id": agent.id, "version": agent.version},
    environment_id=environment.id,
)

def get_weather(city: str) -> str:
    return f"{city}: 18°C, clear"

with client.beta.sessions.events.stream(session.id) as stream:
    client.beta.sessions.events.send(
        session.id,
        events=[
            {
                "type": "user.message",
                "content": [{"type": "text", "text": "What's the weather in Tokyo?"}],
            }
        ],
    )
    for ev in stream:
        if ev.type == "agent.message":
            print("".join(b.text for b in ev.content))
        elif ev.type == "agent.custom_tool_use":
            result = get_weather(**ev.input)
            client.beta.sessions.events.send(
                session.id,
                events=[
                    {
                        "type": "user.custom_tool_result",
                        "custom_tool_use_id": ev.id,
                        "content": [{"type": "text", "text": result}],
                    }
                ],
            )
        elif ev.type == "session.status_idle" and ev.stop_reason.type == "end_turn":
            break
```

The Agent and Environment are created once and reused across sessions. The tool function still runs in your process; the difference is that you read the `agent.custom_tool_use` event and send the result explicitly instead of the SDK dispatching it for you.

### Features that move to your client

The tradeoff for Anthropic running the agent loop is that a few things the SDK handled automatically become your client's responsibility.

| SDK feature | Managed Agents approach |
| --- | --- |
| Plan mode | Run a planning-only session first, then a second session to execute. |
| Output styles, slash commands | Apply in your client before sending `user.message` or after receiving `agent.message`. |
| `PreToolUse` / `PostToolUse` hooks | Your client already sees every `agent.custom_tool_use` event before responding; put the logic there. For built-in tools, use `permission_policy: always_ask`. |
| `max_turns` | Count turns client-side. |

## Migration checklist

1. [Create an environment](managed-agents/environments.md) with the networking and runtimes your agent needs.
2. Port your system prompt and tool selection to an [agent definition](managed-agents/agent-setup.md).
3. Replace your loop with [`sessions.create`](managed-agents/sessions.md) and [`sessions.stream`](managed-agents/events-and-streaming.md).
4. For any local files the agent reads, upload them via the [Files API](managed-agents/files.md) and mount them as `resources`.
5. For any custom tool handlers, move execution into your event loop as responses to `agent.custom_tool_use` events.
6. Verify with a test session before pointing production traffic at the new flow.

## Migrating between model versions

When a new Claude model is released, migrating a Claude Managed Agents integration is typically a one-field change: update `model` on your [agent definition](managed-agents/agent-setup.md) and the change takes effect on the next session you create.

CLI

```shiki
ant beta:agents update \
  --agent-id "$AGENT_ID" \
  --version "$AGENT_VERSION" \
  --model claude-sonnet-4-6
```

Most model-level behavior changes documented in the [Messages API migration guide](about-claude/models/migration-guide.md) do not require action on your side:

- **Request parameter changes** (`max_tokens` defaults, `thinking` configuration) are handled by the Claude Managed Agents runtime. These fields are not exposed on the agent definition.
- **Assistant message prefilling** does not exist in the event-based session model, so its removal on newer models is a no-op.
- **Tool argument JSON escaping** is parsed by the runtime before you receive `agent.custom_tool_use` events. You see structured data, not raw strings.

The behavior descriptions in the Messages API guide (what the model does differently) still apply. The migration steps (how to change your request code) do not.

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
