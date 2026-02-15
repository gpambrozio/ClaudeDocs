# Create a Message

Copy page

C#

# Create a Message

[Message](api/messages.md) Messages.Create(MessageCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)

##### ParametersExpand Collapse

MessageCreateParams parameters

required Long maxTokens

The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.

minimum1

required IReadOnlyList<[MessageParam](api/messages.md)> messages

Input messages.

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

required Content Content

Accepts one of the following:

string

IReadOnlyList<[ContentBlockParam](api/messages.md)>

Accepts one of the following:

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class DocumentBlockParam:

required Source Source

Accepts one of the following:

class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class ContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

Accepts one of the following:

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title

class SearchResultBlockParam:

required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[CitationsConfigParam](api/messages.md) Citations

Boolean Enabled

class ThinkingBlockParam:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class RedactedThinkingBlockParam:

required string Data

JsonElement Type "redacted\_thinking"constant

class ToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class ToolResultBlockParam:

required string ToolUseID

JsonElement Type "tool\_result"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Content Content

Accepts one of the following:

string

IReadOnlyList<Block>

Accepts one of the following:

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class SearchResultBlockParam:

required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[CitationsConfigParam](api/messages.md) Citations

Boolean Enabled

class DocumentBlockParam:

required Source Source

Accepts one of the following:

class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class ContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

Accepts one of the following:

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title

Boolean IsError

class ServerToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

JsonElement Name "web\_search"constant

JsonElement Type "server\_tool\_use"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class WebSearchToolResultBlockParam:

required [WebSearchToolResultBlockParamContent](api/messages.md) Content

Accepts one of the following:

IReadOnlyList<[WebSearchResultBlockParam](api/messages.md)>

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge

class WebSearchToolRequestError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

required Role Role

Accepts one of the following:

"user"User

"assistant"Assistant

required [Model](api/messages.md) model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

string? inferenceGeo

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

[Metadata](api/messages.md) metadata

An object describing metadata about the request.

[OutputConfig](api/messages.md) outputConfig

Configuration options for the model's output, such as the output format.

[ServiceTier](api/messages/create.md) serviceTier

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

"auto"Auto

"standard\_only"StandardOnly

IReadOnlyList<string> stopSequences

Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

[System](api/messages/create.md) system

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

string

IReadOnlyList<[TextBlockParam](api/messages.md)>

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

Double temperature

Amount of randomness injected into the response.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0

[ThinkingConfigParam](api/messages.md) thinking

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

[ToolChoice](api/messages.md) toolChoice

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

IReadOnlyList<[ToolUnion](api/messages.md)> tools

Definitions of tools that the model may use.

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

class Tool:

required InputSchema InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

string Description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Boolean? EagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Type? Type

class ToolBash20250124:

JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash\_20250124"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250124:

JsonElement Name "str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250124"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429:

JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250429"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728:

JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250728"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Long? MaxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20250305:

JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20250305"constant

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

UserLocation? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

Long topK

Only sample from the top K options for each subsequent token.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only. You usually only need to use `temperature`.

minimum0

Double topP

Use nucleus sampling.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

Recommended for advanced use cases only. You usually only need to use `temperature`.

maximum1

minimum0

##### ReturnsExpand Collapse

class Message:

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required IReadOnlyList<[ContentBlock](api/messages.md)> Content

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

Accepts one of the following:

class TextBlock:

required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class ToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

class ServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

JsonElement Name "web\_search"constant

JsonElement Type "server\_tool\_use"constant

class WebSearchToolResultBlock:

required [WebSearchToolResultBlockContent](api/messages.md) Content

Accepts one of the following:

class WebSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3\_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3\_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3\_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3\_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4\_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4\_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4\_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude\_3\_Opus\_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [StopReason](api/messages.md)? StopReason

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [Usage](api/messages.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [CacheCreation](api/messages.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

class RawMessageStreamEvent: A class that can be one of several variants.union

class RawMessageStartEvent:

required [Message](api/messages.md) Message

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required IReadOnlyList<[ContentBlock](api/messages.md)> Content

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

Accepts one of the following:

class TextBlock:

required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class ToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

class ServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

JsonElement Name "web\_search"constant

JsonElement Type "server\_tool\_use"constant

class WebSearchToolResultBlock:

required [WebSearchToolResultBlockContent](api/messages.md) Content

Accepts one of the following:

class WebSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3\_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3\_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3\_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3\_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4\_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4\_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4\_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude\_3\_Opus\_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [StopReason](api/messages.md)? StopReason

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [Usage](api/messages.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [CacheCreation](api/messages.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

JsonElement Type "message\_start"constant

class RawMessageDeltaEvent:

required Delta Delta

required [StopReason](api/messages.md)? StopReason

Accepts one of the following:

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal

required string? StopSequence

JsonElement Type "message\_delta"constant

required [MessageDeltaUsage](api/messages.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required Long? CacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The cumulative number of input tokens read from the cache.

required Long? InputTokens

The cumulative number of input tokens which were used.

required Long OutputTokens

The cumulative number of output tokens which were used.

required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebSearchRequests

The number of web search tool requests.

class RawMessageStopEvent:

JsonElement Type "message\_stop"constant

class RawContentBlockStartEvent:

required ContentBlock ContentBlock

Accepts one of the following:

class TextBlock:

required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class ToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

class ServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

JsonElement Name "web\_search"constant

JsonElement Type "server\_tool\_use"constant

class WebSearchToolResultBlock:

required [WebSearchToolResultBlockContent](api/messages.md) Content

Accepts one of the following:

class WebSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

required Long Index

JsonElement Type "content\_block\_start"constant

class RawContentBlockDeltaEvent:

required [RawContentBlockDelta](api/messages.md) Delta

Accepts one of the following:

class TextDelta:

required string Text

JsonElement Type "text\_delta"constant

class InputJsonDelta:

required string PartialJson

JsonElement Type "input\_json\_delta"constant

class CitationsDelta:

required Citation Citation

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

JsonElement Type "citations\_delta"constant

class ThinkingDelta:

required string Thinking

JsonElement Type "thinking\_delta"constant

class SignatureDelta:

required string Signature

JsonElement Type "signature\_delta"constant

required Long Index

JsonElement Type "content\_block\_delta"constant

class RawContentBlockStopEvent:

required Long Index

JsonElement Type "content\_block\_stop"constant

Create a Message

C#

```shiki
MessageCreateParams parameters = new()
{
    MaxTokens = 1024,
    Messages =
    [
        new()
        {
            Content = "Hello, world",
            Role = Role.User,
        },
    ],
    Model = Model.ClaudeOpus4_6,
};

var message = await client.Messages.Create(parameters);

Console.WriteLine(message);
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
