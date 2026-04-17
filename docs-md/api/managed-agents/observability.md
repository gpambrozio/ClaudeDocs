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

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
events = client.beta.sessions.events.list(session.id)

for event in events:
    print(f"Type: {event.type}")
    print(f"Processed: {event.processed_at}")
    match event.type:
        case "user.message" | "agent.message":
            for block in event.content:
                print(f"  Block: {block.type}")
                if block.type == "text":
                    print(f"  Text: {block.text[:100]}...")
        case "agent.tool_use" | "agent.custom_tool_use" | "agent.mcp_tool_use":
            print(f"  Tool: {event.name}")
    print("---")
```

Use the same event stream to surface errors and track token consumption:

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
events = client.beta.sessions.events.list(session.id)

input_tokens, output_tokens = 0, 0
for event in events:
    match event.type:
        case "session.error":
            print(f"[{event.error.type}] {event.error.message}")
        case "span.model_request_end":
            input_tokens += event.model_usage.input_tokens
            output_tokens += event.model_usage.output_tokens

print(f"Total input tokens: {input_tokens}, output tokens: {output_tokens}")
```

## Debugging tips

- **Check session events** - Session errors are conveyed through the `session.error` event
- **Review tool results** - Tool execution failures often explain unexpected agent behavior
- **Track token usage** - Monitor token consumption to optimize prompts and reduce costs
- **Use system prompts** - Add logging instructions to the system prompt to make the agent explain its reasoning

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
