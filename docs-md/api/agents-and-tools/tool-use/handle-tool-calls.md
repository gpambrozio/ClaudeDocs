# Handle tool calls

Copy page



This page covers the tool-call lifecycle: reading `tool_use` blocks from Claude's response, formatting `tool_result` blocks in your reply, and signaling errors. For the SDK abstraction that handles this automatically, see [Tool Runner](agents-and-tools/tool-use/tool-runner.md).

Claude's response differs based on whether it uses a [client or server tool](agents-and-tools/tool-use/overview.md).

## Handling results from client tools

The response will have a `stop_reason` of `tool_use` and one or more `tool_use` content blocks that include:

- `id`: A unique identifier for this particular tool use block. This will be used to match up the tool results later.
- `name`: The name of the tool being used.
- `input`: An object containing the input being passed to the tool, conforming to the tool's `input_schema`.

A `tool_use` block for a member of the [computer use](agents-and-tools/tool-use/computer-use-tool.md) or [browser use](agents-and-tools/tool-use/browser-use-tool.md) toolset also carries a `toolset_name` field (`"computer"` or `"browser"`). Its `name` is the member tool Claude is calling, such as `screenshot` or `navigate`, so dispatch those blocks on both fields.

### Example API response with a `tool\_use` content block

JSON



```shiki
{
  "id": "msg_01Aq9w938a90dw8q",
  "model": "claude-opus-5",
  "stop_reason": "tool_use",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "I'll check the current weather in San Francisco for you."
    },
    {
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "get_weather",
      "input": { "location": "San Francisco, CA", "unit": "celsius" }
    }
  ]
}
```

When you receive a tool use response for a client tool, you should:

1. Extract the `name`, `id`, and `input` from the `tool_use` block.
2. Run the actual tool in your codebase corresponding to that tool name, passing in the tool `input`.
3. Continue the conversation by sending a new message with the `role` of `user`, and a `content` block containing the `tool_result` type and the following information:
   - `tool_use_id`: The `id` of the tool use request this is a result for.
   - `content` (optional): The result of the tool, as a string (for example, `"content": "15 degrees"`), a list of nested content blocks (for example, `"content": [{"type": "text", "text": "15 degrees"}]`), or a list of document blocks (for example, `"content": [{"type": "document", "source": {"type": "text", "media_type": "text/plain", "data": "15 degrees"}}]`). These content blocks can use the `text`, `image`, `document`, or [`search_result`](build-with-claude/search-results.md) types.
   - `is_error` (optional): Set to `true` if the tool execution resulted in an error.

A `tool_result` that answers a computer use or browser use member block must also echo the same `toolset_name` value as the `tool_use` block; a member result that omits it is rejected. Its `content` is also narrower: a member result may contain only `text` and `image` blocks, and a browser use result may add one [`browser_state`](agents-and-tools/tool-use/browser-use-tool.md) block (the [tab-management members](agents-and-tools/tool-use/browser-use-tool.md) return only that block).

### Example of successful tool result

JSON



```shiki
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "15 degrees"
    }
  ]
}
```

### Example of tool result with images

JSON



```shiki
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": [
        { "type": "text", "text": "15 degrees" },
        {
          "type": "image",
          "source": {
            "type": "base64",
            "media_type": "image/jpeg",
            "data": "/9j/4AAQSkZJRg..."
          }
        }
      ]
    }
  ]
}
```

### Example of empty tool result

JSON



```shiki
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9"
    }
  ]
}
```

### Example of tool result with documents

JSON



```shiki
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": [
        { "type": "text", "text": "The weather is" },
        {
          "type": "document",
          "source": {
            "type": "text",
            "media_type": "text/plain",
            "data": "15 degrees"
          }
        }
      ]
    }
  ]
}
```

After receiving the tool result, Claude will use that information to continue generating a response to the original user prompt.

## Handling results from server tools

Claude executes the tool internally and incorporates the results directly into its response without requiring additional user interaction.

## Handling errors with is\_error

There are a few different types of errors that can occur when using tools with Claude:

### Tool execution error

If the tool itself throws an error during execution (for example, a network error when fetching weather data), you can return the error message in the `content` along with `"is_error": true`:

JSON



```shiki
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "ConnectionError: the weather service API is not available (HTTP 500)",
      "is_error": true
    }
  ]
}
```

Claude will then incorporate this error into its response to the user. For example: "I'm sorry, I was unable to retrieve the current weather because the weather service API is not available. Please try again later."

### Invalid tool name

If Claude's attempted use of a tool is invalid (for example, missing required parameters), it usually means that there wasn't enough information for Claude to use the tool correctly. Your best bet during development is to try the request again with more-detailed `description` values in your tool definitions.

However, you can also continue the conversation forward with a `tool_result` that indicates the error, and Claude will try to use the tool again with the missing information filled in:

JSON



```shiki
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "Error: Missing required 'location' parameter",
      "is_error": true
    }
  ]
}
```

If a tool request is invalid or missing parameters, Claude will retry 2-3 times with corrections before apologizing to the user.

### Server tool errors

When server tools encounter errors (for example, network issues with Web Search), Claude will transparently handle these errors and attempt to provide an alternative response or explanation to the user. Unlike client tools, you do not need to handle `is_error` results for server tools.

For web search specifically, possible error codes include:

- `too_many_requests`: Rate limit exceeded
- `invalid_input`: Invalid search query parameter
- `max_uses_exceeded`: Maximum web search tool uses exceeded
- `query_too_long`: Query exceeds maximum length
- `unavailable`: An internal error occurred

## Next steps



[Parallel tool use](agents-and-tools/tool-use/parallel-tool-use.md)

Handle responses where Claude calls several tools in a single turn.



[Tool Runner (SDK)](agents-and-tools/tool-use/tool-runner.md)

Let the SDK manage the `tool_use` loop, result formatting, and retries for you.



[Define tools](agents-and-tools/tool-use/define-tools.md)

Write schemas and descriptions that steer Claude toward the right tool.

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
