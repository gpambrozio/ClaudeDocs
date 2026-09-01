# Count tokens in a Message

Copy page



cURL

# Count tokens in a Message

POST/v1/messages/count\_tokens

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](build-with-claude/token-counting.md)

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](api/http/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"user-profiles-2026-08-18"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"dreaming-2026-04-21"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"server-side-fallback-2026-07-01"

"fallback-credit-2026-06-01"

"fallback-credit-2026-07-01"

"agent-memory-2026-07-22"

"mid-conversation-tool-changes-2026-07-01"

"compact-2026-01-12"

"computer-use-2025-11-24"

"mcp-tunnels-2026-06-22"

"structured-outputs-2025-11-13"

"task-budgets-2026-03-13"

"thinking-display-updates-2026-08-18"

"ce-user-management-2026-07-13"

"anthropic-user-profile-id": optional string

The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

##### Body



messages: array of [BetaMessageParam](api/http/beta/messages.md) { content, role }

Input messages.

Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

Example with a single `user` message:

```shiki
[{"role": "user", "content": "Hello, Claude"}]
```



Example with multiple conversational turns:

```shiki
[
  {"role": "user", "content": "Hello there."},
  {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
  {"role": "user", "content": "Can you explain LLMs in plain English?"},
]
```



Example with a partially-filled response from Claude:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("},
]
```



Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

```shiki
{"role": "user", "content": "Hello, Claude"}
```



```shiki
{"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
```



See [input examples](build-with-claude/working-with-messages.md).

Note that if you want to include a [system prompt](build-with-claude/prompt-engineering/claude-prompting-best-practices.md), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

There is a limit of 100,000 messages in a single request.



content: string or array of [BetaContentBlockParam](api/http/beta/messages.md)

One of the following:

string



array of [BetaContentBlockParam](api/http/beta/messages.md)

One of the following:



BetaTextBlockParam object{ text, type, cache\_control, citations }



BetaImageBlockParam object{ source, type, cache\_control, transformations }



BetaRequestDocumentBlock object{ source, type, cache\_control, 3 more }



BetaSearchResultBlockParam object{ content, source, title, 3 more }



BetaThinkingBlockParam object{ signature, thinking, type }



signature: string

The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

thinking: string

The `thinking` text of this block as returned by the API.

type: "thinking"



BetaRedactedThinkingBlockParam object{ data, type }

data: string

The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

type: "redacted\_thinking"



BetaToolUseBlockParam object{ id, input, name, 4 more }



BetaToolResultBlockParam object{ tool\_use\_id, type, cache\_control, 3 more }



BetaServerToolUseBlockParam object{ id, input, name, 3 more }



BetaWebSearchToolResultBlockParam object{ content, tool\_use\_id, type, 2 more }



BetaWebFetchToolResultBlockParam object{ content, tool\_use\_id, type, 2 more }



BetaAdvisorToolResultBlockParam object{ content, tool\_use\_id, type, cache\_control }



BetaCodeExecutionToolResultBlockParam object{ content, tool\_use\_id, type, cache\_control }



content: [BetaCodeExecutionToolResultBlockParamContent](api/http/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



tool\_use\_id: string

pattern^srvtoolu\_[a-zA-Z0-9\_]+$

type: "code\_execution\_tool\_result"



cache\_control: optional [BetaCacheControlEphemeral](api/http/beta/messages.md) { type, ttl } or null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



BetaBashCodeExecutionToolResultBlockParam object{ content, tool\_use\_id, type, cache\_control }



BetaTextEditorCodeExecutionToolResultBlockParam object{ content, tool\_use\_id, type, cache\_control }



BetaToolSearchToolResultBlockParam object{ content, tool\_use\_id, type, cache\_control }



BetaMCPToolUseBlockParam object{ id, input, name, 3 more }



BetaRequestMCPToolResultBlockParam object{ tool\_use\_id, type, cache\_control, 2 more }



BetaContainerUploadBlockParam object{ file\_id, type, cache\_control }

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"



cache\_control: optional [BetaCacheControlEphemeral](api/http/beta/messages.md) { type, ttl } or null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



BetaCompactionBlockParam object{ type, cache\_control, content, encrypted\_content }

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

type: "compaction"



cache\_control: optional [BetaCacheControlEphemeral](api/http/beta/messages.md) { type, ttl } or null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

content: optional string or null

Summary of previously compacted content, or null if compaction failed

encrypted\_content: optional string or null

Opaque metadata from prior compaction, to be round-tripped verbatim



BetaRequestToolAdditionBlock object{ tool, type, cache\_control }

Mid-conversation directive to surface a declared tool.

`tool` references a tool (or MCP toolset) by name from the request's
`tools`; it is offered to the model from this point in the
conversation onward.



BetaRequestToolRemovalBlock object{ tool, type, cache\_control }

Mid-conversation directive to withdraw a tool.

`tool` references a tool (or MCP toolset) by name from the request's
`tools`; it is no longer offered to the model from this point in the
conversation onward.



BetaFallbackBlockParam object{ from, to, type, trigger }

A `fallback` block echoed back from a prior response.

Accepted in `messages[].content` and not rendered into the prompt; not
validated against the request's `fallbacks` chain or top-level `model`.

Echo the assistant turn back verbatim, including this block in its
original position. The block marks the boundary between content produced
before and after a fallback hop, and the server relies on that boundary
to validate the turn: when thinking runs flank the boundary, omitting
the block merges them into one span the server cannot validate (the
request is rejected), and moving it into the middle of a single run is
likewise rejected; between non-thinking blocks the block's placement has
no validation effect.



from: [BetaFallbackInfoParam](api/http/beta/messages.md) { model }

Identifies one hop of a fallback transition.



to: [BetaFallbackInfoParam](api/http/beta/messages.md) { model }

Identifies one hop of a fallback transition.

type: "fallback"

trigger: optional unknown

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



role: "user" or "assistant" or "system"

One of the following:

"user"

"assistant"

"system"



model: [Model](api/http/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-5"

Powerful intelligence for long-running agents and coding

"claude-opus-4-8"

Powerful intelligence for long-running agents and coding

"claude-opus-4-7"

Powerful intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Powerful intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Powerful intelligence for long-running agents and coding

"claude-opus-4-5-20251101"

Powerful intelligence for long-running agents and coding

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string



cache\_control: optional [BetaCacheControlEphemeral](api/http/beta/messages.md) { type, ttl } or null

Top-level cache control automatically applies a cache\_control marker to the last cacheable block in the request.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



context\_management: optional [BetaContextManagementConfig](api/http/beta/messages.md) { edits } or null

Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.



mcp\_servers: optional array of [BetaRequestMCPServerURLDefinition](api/http/beta/messages.md) { name, type, url, 2 more }

MCP servers to be utilized in this request

maxItems20

name: string

type: "url"

url: string

authorization\_token: optional string or null



tool\_configuration: optional [BetaRequestMCPServerToolConfiguration](api/http/beta/messages.md) { allowed\_tools, enabled } or null

allowed\_tools: optional array of string or null

enabled: optional boolean or null



output\_config: optional [BetaOutputConfig](api/http/beta/messages.md) { effort, format, task\_budget }

Configuration options for the model's output, such as the output format.



speed: optional "standard" or "fast" or null

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



system: optional string or array of [BetaTextBlockParam](api/http/beta/messages.md) { text, type, cache\_control, citations }

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](build-with-claude/prompt-engineering/claude-prompting-best-practices.md).

One of the following:

string



array of [BetaTextBlockParam](api/http/beta/messages.md) { text, type, cache\_control, citations }



text: string

minLength1

type: "text"



cache\_control: optional [BetaCacheControlEphemeral](api/http/beta/messages.md) { type, ttl } or null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/http/beta/messages.md) or null

One of the following:



BetaCitationCharLocationParam object{ cited\_text, document\_index, document\_title, 3 more }

cited\_text: string



document\_index: number

minimum0



document\_title: string or null

maxLength500

minLength1

end\_char\_index: number



start\_char\_index: number

minimum0

type: "char\_location"



BetaCitationPageLocationParam object{ cited\_text, document\_index, document\_title, 3 more }

cited\_text: string



document\_index: number

minimum0



document\_title: string or null

maxLength500

minLength1

end\_page\_number: number



start\_page\_number: number

minimum1

type: "page\_location"



BetaCitationContentBlockLocationParam object{ cited\_text, document\_index, document\_title, 3 more }



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



document\_index: number

minimum0



document\_title: string or null

maxLength500

minLength1



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

minimum0

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam object{ cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string



title: string or null

maxLength512

minLength1

type: "web\_search\_result\_location"



url: string

minLength1



BetaCitationSearchResultLocationParam object{ cited\_text, end\_block\_index, search\_result\_index, 4 more }



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string



start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

minimum0

title: string or null

type: "search\_result\_location"



thinking: optional [BetaThinkingConfigParam](api/http/beta/messages.md)

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

One of the following:



tool\_choice: optional [BetaToolChoice](api/http/beta/messages.md)

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



tools: optional array of [BetaTool](api/http/beta/messages.md) { input\_schema, name, allowed\_callers, 7 more } or [BetaToolBash20241022](api/http/beta/messages.md) { name, type, allowed\_callers, 4 more } or [BetaToolBash20250124](api/http/beta/messages.md) { name, type, allowed\_callers, 4 more } or 25 more

Definitions of tools that the model may use.

If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](agents-and-tools/tool-use/server-tools.md), see their individual documentation as each has its own behavior (e.g., the [web search tool](agents-and-tools/tool-use/web-search-tool.md)).

Each tool definition includes:

- `name`: Name of the tool.
- `description`: Optional, but strongly-recommended description of the tool.
- `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the tool `input` shape that the model will produce in `tool_use` output content blocks.

For example, if you defined `tools` as:

```shiki
[
  {
    "name": "get_stock_price",
    "description": "Get the current stock price for a given ticker symbol.",
    "input_schema": {
      "type": "object",
      "properties": {
        "ticker": {
          "type": "string",
          "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
        }
      },
      "required": ["ticker"]
    }
  }
]
```



And then asked the model "What's the S&P 500 at today?", the model might produce `tool_use` content blocks in the response like this:

```shiki
[
  {
    "type": "tool_use",
    "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "name": "get_stock_price",
    "input": { "ticker": "^GSPC" }
  }
]
```



You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an input, and return the following back to the model in a subsequent `user` message:

```shiki
[
  {
    "type": "tool_result",
    "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "content": "259.75 USD"
  }
]
```



Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

See our [guide](agents-and-tools/tool-use/overview.md) for more details.

One of the following:



BetaTool object{ input\_schema, name, allowed\_callers, 7 more }



BetaToolBash20241022 object{ name, type, allowed\_callers, 4 more }



BetaToolBash20250124 object{ name, type, allowed\_callers, 4 more }



BetaCodeExecutionTool20250522 object{ name, type, allowed\_callers, 3 more }



BetaCodeExecutionTool20250825 object{ name, type, allowed\_callers, 3 more }



BetaCodeExecutionTool20260120 object{ name, type, allowed\_callers, 3 more }

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



BetaCodeExecutionTool20260521 object{ name, type, allowed\_callers, 3 more }

Code execution tool with REPL state persistence.



BetaBrowserToolset20260801 object{ type, allowed\_callers, cache\_control, configs }

The browser toolset: a single `tools[]` entry (carrying no
`name`) that declares the browser tool family. The model is served
the family's tool with any members disabled via `configs` removed
from its schema.



BetaToolComputerUse20241022 object{ display\_height\_px, display\_width\_px, name, 7 more }



BetaMemoryTool20250818 object{ name, type, allowed\_callers, 4 more }



BetaToolComputerUse20250124 object{ display\_height\_px, display\_width\_px, name, 7 more }



BetaToolTextEditor20241022 object{ name, type, allowed\_callers, 4 more }



BetaToolComputerUse20251124 object{ display\_height\_px, display\_width\_px, name, 8 more }



BetaComputerToolset20260801 object{ type, allowed\_callers, cache\_control, configs }

The computer toolset: a single `tools[]` entry (carrying no
`name`) that declares the computer tool family. The model is
served the family's tool with any members disabled via `configs`
removed from its schema. Every member is enabled by default, zoom
included. The single-tool options `display_number` and
`enable_zoom` are not fields of a toolset entry — it carries only
`type`, `configs`, and `cache_control`; zoom is controlled
via `configs.zoom.enabled`.



BetaToolTextEditor20250124 object{ name, type, allowed\_callers, 4 more }



BetaToolTextEditor20250429 object{ name, type, allowed\_callers, 4 more }



BetaToolTextEditor20250728 object{ name, type, allowed\_callers, 5 more }



BetaWebSearchTool20250305 object{ name, type, allowed\_callers, 7 more }



BetaWebFetchTool20250910 object{ name, type, allowed\_callers, 8 more }



BetaWebSearchTool20260209 object{ name, type, allowed\_callers, 7 more }



BetaWebFetchTool20260209 object{ name, type, allowed\_callers, 8 more }



BetaWebFetchTool20260309 object{ name, type, allowed\_callers, 9 more }

Web fetch tool with use\_cache parameter for bypassing cached content.



BetaWebSearchTool20260318 object{ name, type, allowed\_callers, 8 more }



BetaWebFetchTool20260318 object{ name, type, allowed\_callers, 10 more }



BetaAdvisorTool20260301 object{ model, name, type, 7 more }



BetaToolSearchToolBm25\_20251119 object{ name, type, allowed\_callers, 3 more }



BetaToolSearchToolRegex20251119 object{ name, type, allowed\_callers, 3 more }



BetaMCPToolset object{ mcp\_server\_name, type, cache\_control, 2 more }

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.



output\_format: optional [BetaJSONOutputFormat](api/http/beta/messages.md) { schema, type } or null⁠Deprecated

Deprecated: Use `output_config.format` instead. See [structured outputs](build-with-claude/structured-outputs.md)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

schema: map[unknown]

The JSON schema of the format

type: "json\_schema"

##### Returns



BetaMessageTokensCount object{ context\_management, input\_tokens }



context\_management: [BetaCountTokensContextManagementResponse](api/http/beta/messages.md) { original\_input\_tokens } or null

Information about context management applied to the message.

original\_input\_tokens: number

The original token count before context management was applied

input\_tokens: number

The total number of tokens across the provided list of messages, system prompt, and tools.

Count tokens in a Message

cURL

```shiki
curl https://api.anthropic.com/v1/messages/count_tokens \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "messages": [
            {
              "content": "Hello, world",
              "role": "user"
            }
          ],
          "model": "claude-opus-5",
          "system": [
            {
              "text": "Today'\''s date is 2024-06-01.",
              "type": "text"
            }
          ],
          "thinking": {
            "type": "adaptive"
          },
          "tools": [
            {
              "input_schema": {
                "type": "object",
                "properties": {
                  "location": "bar",
                  "unit": "bar"
                },
                "required": [
                  "location"
                ]
              },
              "name": "name"
            }
          ]
        }'
```

Response 200



```shiki
{
  "context_management": {
    "original_input_tokens": 0
  },
  "input_tokens": 2095
}
```

##### Returns Examples

Response 200



```shiki
{
  "context_management": {
    "original_input_tokens": 0
  },
  "input_tokens": 2095
}
```

---

*Copyright © Anthropic. All rights reserved.*
