# Handle tool calls

Copy page



This page covers the tool-call lifecycle: reading `tool_use` blocks from Claude's response, formatting `tool_result` blocks in your reply, and signaling errors. For the SDK abstraction that handles this automatically, see [Tool Runner](agents-and-tools/tool-use/tool-runner.md).



**Simpler with Tool Runner**: The manual tool handling described on this page is automatically managed by [Tool Runner](agents-and-tools/tool-use/tool-runner.md). Use this page when you need custom control over tool execution.

Claude's response differs based on whether it uses a [client or server tool](agents-and-tools/tool-use/overview.md).

##  Handling results from client tools

The response will have a `stop_reason` of `tool_use` and one or more `tool_use` content blocks that include:

- `id`: A unique identifier for this particular tool use block. This will be used to match up the tool results later.
- `name`: The name of the tool being used.
- `input`: An object containing the input being passed to the tool, conforming to the tool's `input_schema`.

### Example API response with a `tool\_use` content block

When you receive a tool use response for a client tool, you should:

1. Extract the `name`, `id`, and `input` from the `tool_use` block.
2. Run the actual tool in your codebase corresponding to that tool name, passing in the tool `input`.
3. Continue the conversation by sending a new message with the `role` of `user`, and a `content` block containing the `tool_result` type and the following information:
   - `tool_use_id`: The `id` of the tool use request this is a result for.
   - `content` (optional): The result of the tool, as a string (for example, `"content": "15 degrees"`), a list of nested content blocks (for example, `"content": [{"type": "text", "text": "15 degrees"}]`), or a list of document blocks (for example, `"content": [{"type": "document", "source": {"type": "text", "media_type": "text/plain", "data": "15 degrees"}}]`). These content blocks can use the `text`, `image`, `document`, or [`search_result`](build-with-claude/search-results.md) types.
   - `is_error` (optional): Set to `true` if the tool execution resulted in an error.



**Important formatting requirements**:

- Tool result blocks must immediately follow their corresponding tool use blocks in the message history. You cannot include any messages between the assistant's tool use message and the user's tool result message.
- In the user message containing tool results, the tool\_result blocks must come FIRST in the content array. Any text must come AFTER all tool results.
- If the assistant turn also called a [server tool](agents-and-tools/tool-use/server-tools.md) that has no result block yet, the user message must contain only `tool_result` blocks. Text after the results ends the turn early; for a server tool Claude called directly, the request then fails with a 400 error that names the unresolved server tool. See [Stop reasons and fallback](build-with-claude/handling-stop-reasons.md).

For example, this will cause a 400 error:

```shiki
{
  "role": "user",
  "content": [
    { "type": "text", "text": "Here are the results:" }, // ❌ Text before tool_result
    { "type": "tool_result", "tool_use_id": "toolu_01" /* ... */ }
  ]
}
```



This is correct when the assistant turn calls only client tools:

```shiki
{
  "role": "user",
  "content": [
    { "type": "tool_result", "tool_use_id": "toolu_01" /* ... */ },
    { "type": "text", "text": "What should I do next?" } // ✅ Text after tool_result
  ]
}
```



If you receive an error like "tool\_use ids were found without tool\_result blocks immediately after", check that your tool results are formatted correctly.



Tool results often carry content from sources outside your control: web pages, inbound email, user uploads, third-party APIs. Treat that content as untrusted: an attacker who can influence it may embed instructions that try to redirect Claude (indirect prompt injection). Keep untrusted content inside `tool_result` blocks rather than `system` prompts or plain user `text` blocks, and see [Mitigate jailbreaks and prompt injections](test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks.md) for further hardening.

### Example of successful tool result

### Example of tool result with images

### Example of empty tool result

### Example of tool result with documents

After receiving the tool result, Claude will use that information to continue generating a response to the original user prompt.

##  Handling results from server tools

Claude executes the tool internally and incorporates the results directly into its response without requiring additional user interaction.



A response can contain both a client `tool_use` block and a `server_tool_use` block that has no result block. That server tool call is not finished yet, and its result block arrives in a later response. Reply with a user message that contains only the `tool_result` blocks for the client tools and keep the same `tools` array; for a server tool Claude called directly, the API runs it on that request and the next response starts with its result block. See [Stop reasons and fallback](build-with-claude/handling-stop-reasons.md).



**Differences from other APIs**

Unlike APIs that separate tool use or use special roles like `tool` or `function`, the Claude API integrates tools directly into the `user` and `assistant` message structure.

Messages contain arrays of `text`, `image`, `tool_use`, and `tool_result` blocks. `user` messages include client content and `tool_result`, while `assistant` messages contain AI-generated content and `tool_use`.

##  Handling errors with is\_error

There are a few different types of errors that can occur when using tools with Claude:

### Tool execution error

### Invalid tool name

### Server tool errors

##  Next steps

[Parallel tool use

Handle responses where Claude calls several tools in a single turn.](agents-and-tools/tool-use/parallel-tool-use.md)[

Tool Runner (SDK)

Let the SDK manage the `tool_use` loop, result formatting, and retries for you.](agents-and-tools/tool-use/tool-runner.md)[Define tools

Write schemas and descriptions that steer Claude toward the right tool.](agents-and-tools/tool-use/define-tools.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
