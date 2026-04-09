# Session tracing

Copy page

Claude Managed Agents provides observability tools in the [Claude Console](/) to help you monitor, debug, and understand your agent sessions.

## Console observability

The Console provides a visual timeline view of your agent sessions. Navigate to the Claude Managed Agents section in the Console to see:

- **Session list** - All sessions with their status, creation time, and model
- **Tracing view** - A chronological view of events (content, timestamps, token usage) within a session. These are only accessible to Developers and Admins.
- **Tool execution** - Details of each tool call and its result

## Raw events

For programmatic debugging, retrieve raw events via the API:

curl

```shiki
curl -fsSL "https://api.anthropic.com/v1/sessions/$SESSION_ID/events" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
| jq -r '
  .data[]
  | "Type: \(.type)",
    "Processed: \(.processed_at)",
    ( if .type | IN("user.message", "agent.message") then
        .content[]
        | "  Block: \(.type)",
          (select(.type == "text") | "  Text: \(.text[:100])...")
      elif .type | IN("agent.tool_use", "agent.custom_tool_use", "agent.mcp_tool_use") then
        "  Tool: \(.name)"
      else empty end ),
    "---"
'
```

Use the same event stream to surface errors and track token consumption:

curl

```shiki
curl -fsSL "https://api.anthropic.com/v1/sessions/$SESSION_ID/events" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
| jq -r '
  (.data[] | select(.type == "session.error") | "[\(.error.type)] \(.error.message)"),
  (reduce (.data[] | select(.type == "span.model_request_end") | .model_usage) as $u
     ({input: 0, output: 0}; .input += $u.input_tokens | .output += $u.output_tokens)
   | "Total input tokens: \(.input), output tokens: \(.output)")
'
```

## Debugging tips

- **Check session events** - Session errors are conveyed through the `session.error` event
- **Review tool results** - Tool execution failures often explain unexpected agent behavior
- **Track token usage** - Monitor token consumption to optimize prompts and reduce costs
- **Use system prompts** - Add logging instructions to the system prompt to make the agent explain its reasoning

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
