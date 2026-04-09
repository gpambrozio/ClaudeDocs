# Create a Message

Copy page

CLI

# Create a Message

$ ant beta:messages create

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)

##### ParametersExpand Collapse

--max-tokens: number

Body param: The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.

--message: array of [BetaMessageParam](api/beta.md) { content, role }

Body param: Input messages.

Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

Example with a single `user` message:

```shiki
[{"role": "user", "content": "Hello, Claude"}]
```

Example with multiple conversational turns:

```shiki
[
  {"role": "user", "content": "Hello there."},
  {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
  {"role": "user", "content": "Can you explain LLMs in plain English?"},
]
```

Example with a partially-filled response from Claude:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("},
]
```

Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

```shiki
{"role": "user", "content": "Hello, Claude"}
```

```shiki
{"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
```

See [input examples](https://docs.claude.com/en/api/messages-examples).

Note that if you want to include a [system prompt](https://docs.claude.com/en/docs/system-prompts), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

There is a limit of 100,000 messages in a single request.

--model: "claude-mythos-preview" or "claude-opus-4-6" or "claude-sonnet-4-6" or 13 more or string

Body param: The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

--cache-control: optional object { type, ttl }

Body param: Top-level cache control automatically applies a cache\_control marker to the last cacheable block in the request.

--container: optional [BetaContainerParams](api/beta.md) { id, skills }  or string

Body param: Container identifier for reuse across requests.

--context-management: optional object { edits }

Body param: Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

--inference-geo: optional string

Body param: Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

--mcp-server: optional array of [BetaRequestMCPServerURLDefinition](api/beta.md) { name, type, url, 2 more }

Body param: MCP servers to be utilized in this request

--metadata: optional object { user\_id }

Body param: An object describing metadata about the request.

--output-config: optional object { effort, format }

Body param: Configuration options for the model's output, such as the output format.

--output-format: optional object { schema, type }

Body param: Deprecated: Use `output_config.format` instead. See [structured outputs](build-with-claude/structured-outputs.md)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

--service-tier: optional "auto" or "standard\_only"

Body param: Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

--speed: optional "standard" or "fast"

Body param: The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

--stop-sequence: optional array of string

Body param: Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

--system: optional string or array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }

Body param: System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

Deprecated--temperature: optional number

Body param: Amount of randomness injected into the response.

Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

--thinking: optional [BetaThinkingConfigEnabled](api/beta.md) { budget\_tokens, type, display }  or [BetaThinkingConfigDisabled](api/beta.md) { type }  or [BetaThinkingConfigAdaptive](api/beta.md) { type, display }

Body param: Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

--tool-choice: optional [BetaToolChoiceAuto](api/beta.md) { type, disable\_parallel\_tool\_use }  or [BetaToolChoiceAny](api/beta.md) { type, disable\_parallel\_tool\_use }  or [BetaToolChoiceTool](api/beta.md) { name, type, disable\_parallel\_tool\_use }  or [BetaToolChoiceNone](api/beta.md) { type }

Body param: How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

--tool: optional array of [BetaToolUnion](api/beta.md)

Body param: Definitions of tools that the model may use.

If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview#server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool)).

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

Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

See our [guide](https://docs.claude.com/en/docs/tool-use) for more details.

Deprecated--top-k: optional number

Body param: Only sample from the top K options for each subsequent token.

Deprecated. Models released after Claude Opus 4.6 do not accept top\_k; any value will be rejected with a 400 error.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only. You usually only need to use `temperature`.

Deprecated--top-p: optional number

Body param: Use nucleus sampling.

Deprecated. Models released after Claude Opus 4.6 do not support setting top\_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

Recommended for advanced use cases only. You usually only need to use `temperature`.

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

beta\_message: object { id, container, content, 8 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: object { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](api/beta.md)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```

beta\_text\_block: object { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

beta\_thinking\_block: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

beta\_redacted\_thinking\_block: object { data, type }

data: string

type: "redacted\_thinking"

beta\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_server\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

beta\_web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_block: object { content, retrieved\_at, type, url }

content: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type }

content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type }

union\_member\_0: string

beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

beta\_container\_upload\_block: object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

beta\_compaction\_block: object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context\_management: object { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

model: "claude-mythos-preview" or "claude-opus-4-6" or "claude-sonnet-4-6" or 13 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: object { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

"standard"

"fast"

beta\_raw\_message\_stream\_event: [BetaRawMessageStartEvent](api/beta.md) { message, type }  or [BetaRawMessageDeltaEvent](api/beta.md) { context\_management, delta, type, usage }  or [BetaRawMessageStopEvent](api/beta.md) { type }  or 3 more

beta\_raw\_message\_start\_event: object { message, type }

message: object { id, container, content, 8 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: object { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](api/beta.md)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```

beta\_text\_block: object { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

beta\_thinking\_block: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

beta\_redacted\_thinking\_block: object { data, type }

data: string

type: "redacted\_thinking"

beta\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_server\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

beta\_web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_block: object { content, retrieved\_at, type, url }

content: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type }

content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type }

union\_member\_0: string

beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

beta\_container\_upload\_block: object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

beta\_compaction\_block: object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context\_management: object { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

model: "claude-mythos-preview" or "claude-opus-4-6" or "claude-sonnet-4-6" or 13 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: object { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

"standard"

"fast"

type: "message\_start"

beta\_raw\_message\_delta\_event: object { context\_management, delta, type, usage }

context\_management: object { applied\_edits }

Information about context management strategies applied during the request

applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

delta: object { container, stop\_details, stop\_reason, stop\_sequence }

container: object { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

stop\_details: object { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

type: "message\_delta"

usage: object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 3 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: number

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The cumulative number of input tokens read from the cache.

input\_tokens: number

The cumulative number of input tokens which were used.

iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The cumulative number of output tokens which were used.

server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

beta\_raw\_message\_stop\_event: object { type }

type: "message\_stop"

beta\_raw\_content\_block\_start\_event: object { content\_block, index, type }

content\_block: [BetaTextBlock](api/beta.md) { citations, text, type }  or [BetaThinkingBlock](api/beta.md) { signature, thinking, type }  or [BetaRedactedThinkingBlock](api/beta.md) { data, type }  or 12 more

Response model for a file uploaded to the container.

beta\_text\_block: object { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

beta\_thinking\_block: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

beta\_redacted\_thinking\_block: object { data, type }

data: string

type: "redacted\_thinking"

beta\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_server\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

beta\_web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_block: object { content, retrieved\_at, type, url }

content: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type }

content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type }

union\_member\_0: string

beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

beta\_container\_upload\_block: object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

beta\_compaction\_block: object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

index: number

type: "content\_block\_start"

beta\_raw\_content\_block\_delta\_event: object { delta, index, type }

delta: [BetaTextDelta](api/beta.md) { text, type }  or [BetaInputJSONDelta](api/beta.md) { partial\_json, type }  or [BetaCitationsDelta](api/beta.md) { citation, type }  or 3 more

beta\_text\_delta: object { text, type }

text: string

type: "text\_delta"

beta\_input\_json\_delta: object { partial\_json, type }

partial\_json: string

type: "input\_json\_delta"

beta\_citations\_delta: object { citation, type }

citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or 2 more

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

type: "citations\_delta"

beta\_thinking\_delta: object { thinking, type }

thinking: string

type: "thinking\_delta"

beta\_signature\_delta: object { signature, type }

signature: string

type: "signature\_delta"

beta\_compaction\_content\_block\_delta: object { content, type }

content: string

type: "compaction\_delta"

index: number

type: "content\_block\_delta"

beta\_raw\_content\_block\_stop\_event: object { index, type }

index: number

type: "content\_block\_stop"

Create a Message

CLI

```shiki
ant beta:messages create \
  --api-key my-anthropic-api-key \
  --max-tokens 1024 \
  --message '{content: [{text: x, type: text}], role: user}' \
  --model claude-opus-4-6
```

Response 200

```shiki
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "id",
    "expires_at": "2019-12-27T18:11:19.117Z",
    "skills": [
      {
        "skill_id": "pdf",
        "type": "anthropic",
        "version": "latest"
      }
    ]
  },
  "content": [
    {
      "citations": [
        {
          "cited_text": "cited_text",
          "document_index": 0,
          "document_title": "document_title",
          "end_char_index": 0,
          "file_id": "file_id",
          "start_char_index": 0,
          "type": "char_location"
        }
      ],
      "text": "Hi! My name is Claude.",
      "type": "text"
    }
  ],
  "context_management": {
    "applied_edits": [
      {
        "cleared_input_tokens": 0,
        "cleared_tool_uses": 0,
        "type": "clear_tool_uses_20250919"
      }
    ]
  },
  "model": "claude-opus-4-6",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "explanation",
    "type": "refusal"
  },
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "type": "message",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_creation_input_tokens": 2051,
    "cache_read_input_tokens": 2051,
    "inference_geo": "inference_geo",
    "input_tokens": 2095,
    "iterations": [
      {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "type": "message"
      }
    ],
    "output_tokens": 503,
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    },
    "service_tier": "standard",
    "speed": "standard"
  }
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "id",
    "expires_at": "2019-12-27T18:11:19.117Z",
    "skills": [
      {
        "skill_id": "pdf",
        "type": "anthropic",
        "version": "latest"
      }
    ]
  },
  "content": [
    {
      "citations": [
        {
          "cited_text": "cited_text",
          "document_index": 0,
          "document_title": "document_title",
          "end_char_index": 0,
          "file_id": "file_id",
          "start_char_index": 0,
          "type": "char_location"
        }
      ],
      "text": "Hi! My name is Claude.",
      "type": "text"
    }
  ],
  "context_management": {
    "applied_edits": [
      {
        "cleared_input_tokens": 0,
        "cleared_tool_uses": 0,
        "type": "clear_tool_uses_20250919"
      }
    ]
  },
  "model": "claude-opus-4-6",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "explanation",
    "type": "refusal"
  },
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "type": "message",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_creation_input_tokens": 2051,
    "cache_read_input_tokens": 2051,
    "inference_geo": "inference_geo",
    "input_tokens": 2095,
    "iterations": [
      {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "type": "message"
      }
    ],
    "output_tokens": 503,
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    },
    "service_tier": "standard",
    "speed": "standard"
  }
}
```

---

*Copyright © Anthropic. All rights reserved.*
