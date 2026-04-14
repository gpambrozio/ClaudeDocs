# Session event stream

Copy page

Communication with Claude Managed Agents is event-based. You send user events to the agent, and receive agent and session events back to track status.

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

## Event types

Events flow in two directions.

- **User events** are what you send to the agent to kick off a session and steer it as it progresses.
- **Session events**, **span events**, and **agent events** are sent to you for observability into your session state and agent progress.

Event type strings follow a `{domain}.{action}` naming convention.

User events

User events

Agent events

Agent events

Session events

Session events

Span events

Span events

| Type | Description |
| --- | --- |
| `user.message` | A user message with text content. |
| `user.interrupt` | Stop the agent mid-execution. |
| `user.custom_tool_result` | Response to a custom tool call from the agent. |
| `user.tool_confirmation` | Approve or deny an agent or MCP tool call when a permission policy requires confirmation. |
| `user.define_outcome` | Define an [outcome](managed-agents/define-outcomes.md) for the agent to work toward. |

Every event includes a `processed_at` timestamp indicating when the event was recorded server-side. If `processed_at` is null, it means the event has been queued by the harness and will be handled after preceding events finish processing.

See the [session events API reference](api/beta/sessions/events/stream.md) for the full schema of each event type.

## Integrating events

Sending events

Sending events

Streaming responses

Streaming responses

Listing past events

Listing past events

Send a `user.message` event to start or continue the agent's work:

curlPythonTypeScriptC#GoJavaPHPRuby

```shiki
curl -sS --fail-with-body "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- <<'EOF'
{
  "events": [
    {
      "type": "user.message",
      "content": [
        {"type": "text", "text": "Analyze the performance of the sort function in utils.py"}
      ]
    }
  ]
}
EOF
```

Send a `user.interrupt` event to stop the agent mid-execution, then follow up with a `user.message` event to redirect it:

curlPythonTypeScriptC#GoJavaPHPRuby

```shiki
# Agent is currently analyzing a file...
# Interrupt with a new direction:
curl -sS --fail-with-body "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- <<'EOF'
{
  "events": [
    {"type": "user.interrupt"},
    {
      "type": "user.message",
      "content": [
        {"type": "text", "text": "Instead, focus on fixing the bug in line 42."}
      ]
    }
  ]
}
EOF
```

The agent will acknowledge the interruption and switch to the new task.

## Additional scenarios

### Handling custom tool calls

When the agent invokes a [custom tool](managed-agents/tools.md):

1. The session emits an `agent.custom_tool_use` event containing the tool name and input.
2. The session pauses with a `session.status_idle` event containing `stop_reason: requires_action`. The blocking event IDs are in the `stop_reason.requires_action.event_ids` array.
3. Execute the tool in your system and send a `user.custom_tool_result` event for each, passing the event ID in the `custom_tool_use_id` param along with the result content.
4. Once all blocking events are resolved, the session transitions back to `running`.

curlPythonTypeScriptC#GoJavaPHPRuby

```shiki
exec {fd}< <(curl -sS -N --fail-with-body \
  "https://api.anthropic.com/v1/sessions/$SESSION_ID/stream?beta=true" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -H "Accept: text/event-stream")

while IFS= read -r -u "$fd" line; do
  [[ $line == data:* ]] || continue
  data="${line#data: }"
  [[ $(jq -r '.type' <<<"$data") == "session.status_idle" ]] || continue
  case $(jq -r '.stop_reason.type // empty' <<<"$data") in
    requires_action)
      while IFS= read -r event_id; do
        # Look up the custom tool use event and execute it
        result=$(call_tool "$event_id")
        # Send the result back
        jq -n --arg id "$event_id" --arg result "$result" \
          '{events: [{type: "user.custom_tool_result", custom_tool_use_id: $id, content: [{type: "text", text: $result}]}]}' |
          curl -sS --fail-with-body \
            "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
            -H "x-api-key: $ANTHROPIC_API_KEY" \
            -H "anthropic-version: 2023-06-01" \
            -H "anthropic-beta: managed-agents-2026-04-01" \
            -H "content-type: application/json" \
            -d @-
      done < <(jq -r '.stop_reason.event_ids[]' <<<"$data")
      ;;
    end_turn)
      break
      ;;
  esac
done
exec {fd}<&-
```

### Tool confirmation

When a [permission policy](managed-agents/permission-policies.md) requires confirmation before a tool executes:

1. The session emits an `agent.tool_use` or `agent.mcp_tool_use` event.
2. The session pauses with a `session.status_idle` event containing `stop_reason: requires_action`. The blocking event IDs are in the `stop_reason.requires_action.event_ids` array.
3. Send a `user.tool_confirmation` event for each, passing the event ID in the `tool_use_id` param. Set `result` to `"allow"` or `"deny"`. Use `deny_message` to explain a denial.
4. Once all blocking events are resolved, the session transitions back to `running`.

curlPythonTypeScriptC#GoJavaPHPRuby

```shiki
exec {fd}< <(curl -sS -N --fail-with-body \
  "https://api.anthropic.com/v1/sessions/$SESSION_ID/stream?beta=true" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -H "Accept: text/event-stream")

while IFS= read -r -u "$fd" line; do
  [[ $line == data:* ]] || continue
  data="${line#data: }"
  [[ $(jq -r '.type' <<<"$data") == "session.status_idle" ]] || continue
  case $(jq -r '.stop_reason.type // empty' <<<"$data") in
    requires_action)
      while IFS= read -r event_id; do
        # Approve the pending tool call
        jq -n --arg id "$event_id" \
          '{events: [{type: "user.tool_confirmation", tool_use_id: $id, result: "allow"}]}' |
          curl -sS --fail-with-body \
            "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
            -H "x-api-key: $ANTHROPIC_API_KEY" \
            -H "anthropic-version: 2023-06-01" \
            -H "anthropic-beta: managed-agents-2026-04-01" \
            -H "content-type: application/json" \
            -d @-
      done < <(jq -r '.stop_reason.event_ids[]' <<<"$data")
      ;;
    end_turn)
      break
      ;;
  esac
done
exec {fd}<&-
```

### Tracking usage

The session object includes a `usage` field with cumulative token statistics. Fetch the session after it goes idle to read the latest totals, and use them to track costs, enforce budgets, or monitor consumption.

```shiki
{
  "id": "sesn_01...",
  "status": "idle",
  "usage": {
    "input_tokens": 5000,
    "output_tokens": 3200,
    "cache_creation_input_tokens": 2000,
    "cache_read_input_tokens": 20000
  }
}
```

`input_tokens` reports uncached input tokens and `output_tokens` reports total output tokens across all model calls in the session. The `cache_creation_input_tokens` and `cache_read_input_tokens` fields reflect prompt caching activity. Cache entries use a 5-minute TTL, so back-to-back turns within that window benefit from cache reads, which reduce per-token cost.

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
