# Create a Message

Copy page



TypeScript

# Create a Message

client.beta.messages.create(MessageCreateParamsparams, RequestOptionsoptions?): [BetaMessage](api/beta/messages.md) { id, container, content, 9 more }  | Stream<[BetaRawMessageStreamEvent](api/beta/messages.md)>

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](get-started.md)

##### ParametersExpand Collapse



MessageCreateParams = MessageCreateParamsNonStreaming { stream }  | MessageCreateParamsStreaming { stream } 



MessageCreateParamsBase { max\_tokens, messages, model, 24 more } 



max\_tokens: number

Body param: The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Set to `0` to populate the [prompt cache](build-with-claude/prompt-caching.md) without generating a response.

Different models have different maximum values for this parameter. See [models](about-claude/models/overview.md) for details.

minimum0



messages: Array<[BetaMessageParam](api/beta/messages.md) { content, role } >

Body param: Input messages.

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

content: string | Array<[BetaContentBlockParam](api/beta/messages.md)>

One of the following:

string



Array<[BetaContentBlockParam](api/beta/messages.md)>



BetaTextBlockParam { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: Array<[BetaTextCitationParam](api/beta/messages.md)> | null

One of the following:



BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"



BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta/messages.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta/messages.md) { type, url }  | [BetaFileImageSource](api/beta/messages.md) { file\_id, type } 

One of the following:



BetaBase64ImageSource { data, media\_type, type } 

data: string



media\_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



BetaURLImageSource { type, url } 

type: "url"

url: string



BetaFileImageSource { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



BetaRequestDocumentBlock { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta/messages.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta/messages.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta/messages.md) { content, type }  | 2 more

One of the following:



BetaBase64PDFSource { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



BetaPlainTextSource { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



BetaContentBlockSource { content, type } 



content: string | Array<[BetaContentBlockSourceContent](api/beta/messages.md)>

One of the following:

string



Array<[BetaContentBlockSourceContent](api/beta/messages.md)>



BetaTextBlockParam { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: Array<[BetaTextCitationParam](api/beta/messages.md)> | null

One of the following:



BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"



BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta/messages.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta/messages.md) { type, url }  | [BetaFileImageSource](api/beta/messages.md) { file\_id, type } 

One of the following:



BetaBase64ImageSource { data, media\_type, type } 

data: string



media\_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



BetaURLImageSource { type, url } 

type: "url"

url: string



BetaFileImageSource { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: "content"



BetaURLPDFSource { type, url } 

type: "url"

url: string



BetaFileDocumentSource { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: [BetaCitationsConfigParam](api/beta/messages.md) { enabled }  | null

enabled?: boolean

context?: string | null

title?: string | null



BetaSearchResultBlockParam { content, source, title, 3 more } 



content: Array<[BetaTextBlockParam](api/beta/messages.md) { text, type, cache\_control, citations } >

text: string

type: "text"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: Array<[BetaTextCitationParam](api/beta/messages.md)> | null

One of the following:



BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"

source: string

title: string

type: "search\_result"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: [BetaCitationsConfigParam](api/beta/messages.md) { enabled } 

enabled?: boolean



BetaThinkingBlockParam { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



BetaRedactedThinkingBlockParam { data, type } 

data: string

type: "redacted\_thinking"



BetaToolUseBlockParam { id, input, name, 3 more } 

id: string

input: Record<string, unknown>

name: string

type: "tool\_use"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caller?: [BetaDirectCaller](api/beta/messages.md) { type }  | [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: string

type: "tool\_result"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



content?: string | Array<[BetaTextBlockParam](api/beta/messages.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta/messages.md) { source, type, cache\_control }  | [BetaSearchResultBlockParam](api/beta/messages.md) { content, source, title, 3 more }  | 2 more>

One of the following:

string



Array<[BetaTextBlockParam](api/beta/messages.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta/messages.md) { source, type, cache\_control }  | [BetaSearchResultBlockParam](api/beta/messages.md) { content, source, title, 3 more }  | 2 more>



BetaTextBlockParam { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: Array<[BetaTextCitationParam](api/beta/messages.md)> | null

One of the following:



BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"



BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta/messages.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta/messages.md) { type, url }  | [BetaFileImageSource](api/beta/messages.md) { file\_id, type } 

One of the following:



BetaBase64ImageSource { data, media\_type, type } 

data: string



media\_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



BetaURLImageSource { type, url } 

type: "url"

url: string



BetaFileImageSource { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



BetaSearchResultBlockParam { content, source, title, 3 more } 



content: Array<[BetaTextBlockParam](api/beta/messages.md) { text, type, cache\_control, citations } >

text: string

type: "text"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: Array<[BetaTextCitationParam](api/beta/messages.md)> | null

One of the following:



BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"

source: string

title: string

type: "search\_result"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: [BetaCitationsConfigParam](api/beta/messages.md) { enabled } 

enabled?: boolean



BetaRequestDocumentBlock { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta/messages.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta/messages.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta/messages.md) { content, type }  | 2 more

One of the following:



BetaBase64PDFSource { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



BetaPlainTextSource { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



BetaContentBlockSource { content, type } 



content: string | Array<[BetaContentBlockSourceContent](api/beta/messages.md)>

One of the following:

string



Array<[BetaContentBlockSourceContent](api/beta/messages.md)>



BetaTextBlockParam { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: Array<[BetaTextCitationParam](api/beta/messages.md)> | null

One of the following:



BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"



BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta/messages.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta/messages.md) { type, url }  | [BetaFileImageSource](api/beta/messages.md) { file\_id, type } 

One of the following:



BetaBase64ImageSource { data, media\_type, type } 

data: string



media\_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



BetaURLImageSource { type, url } 

type: "url"

url: string



BetaFileImageSource { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: "content"



BetaURLPDFSource { type, url } 

type: "url"

url: string



BetaFileDocumentSource { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: [BetaCitationsConfigParam](api/beta/messages.md) { enabled }  | null

enabled?: boolean

context?: string | null

title?: string | null



BetaToolReferenceBlockParam { tool\_name, type, cache\_control } 

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

is\_error?: boolean



BetaServerToolUseBlockParam { id, input, name, 3 more } 

id: string

input: Record<string, unknown>



name: "advisor" | "web\_search" | "web\_fetch" | 5 more

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caller?: [BetaDirectCaller](api/beta/messages.md) { type }  | [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaWebSearchToolResultBlockParam { content, tool\_use\_id, type, 2 more } 



content: [BetaWebSearchToolResultBlockParamContent](api/beta/messages.md)

One of the following:



Array<[BetaWebSearchResultBlockParam](api/beta/messages.md) { encrypted\_content, title, type, 2 more } >

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age?: string | null



BetaWebSearchToolRequestError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

tool\_use\_id: string

type: "web\_search\_tool\_result"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caller?: [BetaDirectCaller](api/beta/messages.md) { type }  | [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaWebFetchToolResultBlockParam { content, tool\_use\_id, type, 2 more } 



content: [BetaWebFetchToolResultErrorBlockParam](api/beta/messages.md) { error\_code, type }  | [BetaWebFetchBlockParam](api/beta/messages.md) { content, type, url, retrieved\_at } 

One of the following:



BetaWebFetchToolResultErrorBlockParam { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



BetaWebFetchBlockParam { content, type, url, retrieved\_at } 



content: [BetaRequestDocumentBlock](api/beta/messages.md) { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta/messages.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta/messages.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta/messages.md) { content, type }  | 2 more

One of the following:



BetaBase64PDFSource { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



BetaPlainTextSource { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



BetaContentBlockSource { content, type } 



content: string | Array<[BetaContentBlockSourceContent](api/beta/messages.md)>

One of the following:

string



Array<[BetaContentBlockSourceContent](api/beta/messages.md)>



BetaTextBlockParam { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: Array<[BetaTextCitationParam](api/beta/messages.md)> | null

One of the following:



BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"



BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta/messages.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta/messages.md) { type, url }  | [BetaFileImageSource](api/beta/messages.md) { file\_id, type } 

One of the following:



BetaBase64ImageSource { data, media\_type, type } 

data: string



media\_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



BetaURLImageSource { type, url } 

type: "url"

url: string



BetaFileImageSource { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: "content"



BetaURLPDFSource { type, url } 

type: "url"

url: string



BetaFileDocumentSource { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: [BetaCitationsConfigParam](api/beta/messages.md) { enabled }  | null

enabled?: boolean

context?: string | null

title?: string | null

type: "web\_fetch\_result"

url: string

Fetched content URL

retrieved\_at?: string | null

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caller?: [BetaDirectCaller](api/beta/messages.md) { type }  | [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaAdvisorToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaAdvisorToolResultErrorParam](api/beta/messages.md) { error\_code, type }  | [BetaAdvisorResultBlockParam](api/beta/messages.md) { text, type, stop\_reason }  | [BetaAdvisorRedactedResultBlockParam](api/beta/messages.md) { encrypted\_content, type, stop\_reason } 

One of the following:



BetaAdvisorToolResultErrorParam { error\_code, type } 



error\_code: "max\_uses\_exceeded" | "prompt\_too\_long" | "too\_many\_requests" | 4 more

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



BetaAdvisorResultBlockParam { text, type, stop\_reason } 

text: string

type: "advisor\_result"

stop\_reason?: string | null



BetaAdvisorRedactedResultBlockParam { encrypted\_content, type, stop\_reason } 

encrypted\_content: string

Opaque blob produced by a prior response; must be round-tripped verbatim.

type: "advisor\_redacted\_result"

stop\_reason?: string | null

tool\_use\_id: string

type: "advisor\_tool\_result"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



BetaCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaCodeExecutionToolResultBlockParamContent](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



BetaCodeExecutionToolResultErrorParam { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



BetaCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more } 



content: Array<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md) { file\_id, type } >

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



BetaEncryptedCodeExecutionResultBlockParam { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md) { file\_id, type } >

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



BetaBashCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaBashCodeExecutionToolResultErrorParam](api/beta/messages.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlockParam](api/beta/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BetaBashCodeExecutionToolResultErrorParam { error\_code, type } 



error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BetaBashCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more } 



content: Array<[BetaBashCodeExecutionOutputBlockParam](api/beta/messages.md) { file\_id, type } >

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



BetaTextEditorCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaTextEditorCodeExecutionToolResultErrorParam](api/beta/messages.md) { error\_code, type, error\_message }  | [BetaTextEditorCodeExecutionViewResultBlockParam](api/beta/messages.md) { content, file\_type, type, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta/messages.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta/messages.md) { type, lines, new\_lines, 3 more } 

One of the following:



BetaTextEditorCodeExecutionToolResultErrorParam { error\_code, type, error\_message } 



error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message?: string | null



BetaTextEditorCodeExecutionViewResultBlockParam { content, file\_type, type, 3 more } 

content: string



file\_type: "text" | "image" | "pdf"

One of the following:

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines?: number | null

start\_line?: number | null

total\_lines?: number | null



BetaTextEditorCodeExecutionCreateResultBlockParam { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new\_lines, 3 more } 

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines?: Array<string> | null

new\_lines?: number | null

new\_start?: number | null

old\_lines?: number | null

old\_start?: number | null

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



BetaToolSearchToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaToolSearchToolResultErrorParam](api/beta/messages.md) { error\_code, type, error\_message }  | [BetaToolSearchToolSearchResultBlockParam](api/beta/messages.md) { tool\_references, type } 

One of the following:



BetaToolSearchToolResultErrorParam { error\_code, type, error\_message } 



error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | "execution\_time\_exceeded"

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

error\_message?: string | null



BetaToolSearchToolSearchResultBlockParam { tool\_references, type } 



tool\_references: Array<[BetaToolReferenceBlockParam](api/beta/messages.md) { tool\_name, type, cache\_control } >

tool\_name: string

type: "tool\_reference"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



BetaMCPToolUseBlockParam { id, input, name, 3 more } 

id: string

input: Record<string, unknown>

name: string

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



BetaRequestMCPToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: string

type: "mcp\_tool\_result"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



content?: string | Array<[BetaTextBlockParam](api/beta/messages.md) { text, type, cache\_control, citations } >

One of the following:

string



Array<[BetaTextBlockParam](api/beta/messages.md) { text, type, cache\_control, citations } >

text: string

type: "text"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: Array<[BetaTextCitationParam](api/beta/messages.md)> | null

One of the following:



BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"

is\_error?: boolean



BetaContainerUploadBlockParam { file\_id, type, cache\_control } 

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



BetaCompactionBlockParam { type, cache\_control, content, encrypted\_content } 

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

type: "compaction"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

content?: string | null

Summary of previously compacted content, or null if compaction failed

encrypted\_content?: string | null

Opaque metadata from prior compaction, to be round-tripped verbatim



BetaMidConversationSystemBlockParam { content, type, cache\_control } 

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



content: Array<[BetaTextBlockParam](api/beta/messages.md) { text, type, cache\_control, citations } >

System instruction text blocks.

text: string

type: "text"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: Array<[BetaTextCitationParam](api/beta/messages.md)> | null

One of the following:



BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"

type: "mid\_conv\_system"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



BetaFallbackBlockParam { from, to, type, trigger } 

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

from: [BetaFallbackInfoParam](api/beta/messages.md) { model } 

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})



to: [BetaFallbackInfoParam](api/beta/messages.md) { model } 

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})

type: "fallback"

trigger?: unknown

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



role: "user" | "assistant" | "system"

One of the following:

"user"

"assistant"

"system"



model: [Model](api/messages.md)

Body param: The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Body param: Top-level cache control automatically applies a cache\_control marker to the last cacheable block in the request.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



container?: [BetaContainerParams](api/beta/messages.md) { id, skills }  | string | null

Body param: Container identifier for reuse across requests.

One of the following:



BetaContainerParams { id, skills } 

Container parameters with skills to be loaded.

id?: string | null

Container id



skills?: Array<[BetaSkillParams](api/beta/messages.md) { skill\_id, type, version } > | null

List of skills to load in the container

skill\_id: string

Skill ID



type: "anthropic" | "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version?: string

Skill version or 'latest' for most recent version

string



context\_management?: [BetaContextManagementConfig](api/beta/messages.md) { edits }  | null

Body param: Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.



edits?: Array<[BetaClearToolUses20250919Edit](api/beta/messages.md) { type, clear\_at\_least, clear\_tool\_inputs, 3 more }  | [BetaClearThinking20251015Edit](api/beta/messages.md) { type, keep }  | [BetaCompact20260112Edit](api/beta/messages.md) { type, instructions, pause\_after\_compaction, trigger } >

List of context management edits to apply

One of the following:



BetaClearToolUses20250919Edit { type, clear\_at\_least, clear\_tool\_inputs, 3 more } 

type: "clear\_tool\_uses\_20250919"



clear\_at\_least?: [BetaInputTokensClearAtLeast](api/beta/messages.md) { type, value }  | null

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: "input\_tokens"

value: number



clear\_tool\_inputs?: boolean | Array<string> | null

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

One of the following:

boolean

Array<string>

exclude\_tools?: Array<string> | null

Tool names whose uses are preserved from clearing



keep?: [BetaToolUsesKeep](api/beta/messages.md) { type, value } 

Number of tool uses to retain in the conversation

type: "tool\_uses"

value: number



trigger?: [BetaInputTokensTrigger](api/beta/messages.md) { type, value }  | [BetaToolUsesTrigger](api/beta/messages.md) { type, value } 

Condition that triggers the context management strategy

One of the following:



BetaInputTokensTrigger { type, value } 

type: "input\_tokens"

value: number



BetaToolUsesTrigger { type, value } 

type: "tool\_uses"

value: number



BetaClearThinking20251015Edit { type, keep } 

type: "clear\_thinking\_20251015"



keep?: [BetaThinkingTurns](api/beta/messages.md) { type, value }  | [BetaAllThinkingTurns](api/beta/messages.md) { type }  | "all"

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

One of the following:



BetaThinkingTurns { type, value } 

type: "thinking\_turns"

value: number



BetaAllThinkingTurns { type } 

type: "all"



"all"

"all"



BetaCompact20260112Edit { type, instructions, pause\_after\_compaction, trigger } 

Automatically compact older context when reaching the configured trigger threshold.

type: "compact\_20260112"

instructions?: string | null

Additional instructions for summarization.

pause\_after\_compaction?: boolean

Whether to pause after compaction and return the compaction block to the user.



trigger?: [BetaInputTokensTrigger](api/beta/messages.md) { type, value }  | null

When to trigger compaction. Defaults to 150000 input tokens.

type: "input\_tokens"

value: number



diagnostics?: [BetaDiagnosticsParam](api/beta/messages.md) { previous\_message\_id }  | null

Body param: Request-level diagnostics. Currently carries the previous response
id for prompt-cache divergence reporting.

previous\_message\_id?: string | null

The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.



fallback\_credit\_token?: string | null

Body param: The `fallback_credit_token` from a prior refusal's `stop_details`.

When a preceding request was refused and returned a `fallback_credit_token`,
pass that code here on the retry to have the retry's cache-creation tokens
for the prefix that was warm on the refused model billed at the cache-read
rate. Must be redeemed by the same organization and workspace, with the same
request body (optionally extended by one appended `assistant` message whose
content is the partial text — with any trailing whitespace stripped from
the final text block — and paired server-tool blocks streamed before the
refusal; the appended-assistant form is not available for requests with
`output_format` set or forced `tool_choice`), on an eligible fallback
model, on the same platform,
and within 5 minutes of the refusal; a mismatch is a 400. A token minted
mid-server-tool-loop whose partial content was continuable may only be
redeemed with the appended-assistant form — if an exact-body retry is
rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry with the appended-assistant form instead.

When the appended-assistant form is used on a model that otherwise disallows
assistant-turn prefill, this token also authorizes that one prefill.

maxLength2048

minLength1



fallbacks?: Array<[BetaFallbackParam](api/beta/messages.md) { model, max\_tokens, output\_config, 2 more } > | null

Body param: Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})

max\_tokens?: number | null



output\_config?: [BetaOutputConfig](api/beta/messages.md) { effort, format, task\_budget }  | null



effort?: "low" | "medium" | "high" | 2 more | null

All possible effort levels.

One of the following:

"low"

"medium"

"high"

"xhigh"

"max"



format?: [BetaJSONOutputFormat](api/beta/messages.md) { schema, type }  | null

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

schema: Record<string, unknown>

The JSON schema of the format

type: "json\_schema"



task\_budget?: [BetaTokenTaskBudget](api/beta/messages.md) { total, type, remaining }  | null

User-configurable total token budget across contexts.

total: number

Total token budget across all contexts in the session.

type: "tokens"

The budget type. Currently only 'tokens' is supported.

remaining?: number | null

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



speed?: "standard" | "fast" | null

One of the following:

"standard"

"fast"



thinking?: [BetaThinkingConfigEnabled](api/beta/messages.md) { budget\_tokens, type, display }  | [BetaThinkingConfigDisabled](api/beta/messages.md) { type }  | [BetaThinkingConfigAdaptive](api/beta/messages.md) { type, display }  | null

One of the following:



BetaThinkingConfigEnabled { budget\_tokens, type, display } 



budget\_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

type: "enabled"



display?: "summarized" | "omitted" | null

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"



BetaThinkingConfigDisabled { type } 

type: "disabled"



BetaThinkingConfigAdaptive { type, display } 

type: "adaptive"



display?: "summarized" | "omitted" | null

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"

inference\_geo?: string | null

Body param: Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.



mcp\_servers?: Array<[BetaRequestMCPServerURLDefinition](api/beta/messages.md) { name, type, url, 2 more } >

Body param: MCP servers to be utilized in this request

name: string

type: "url"

url: string

authorization\_token?: string | null



tool\_configuration?: [BetaRequestMCPServerToolConfiguration](api/beta/messages.md) { allowed\_tools, enabled }  | null

allowed\_tools?: Array<string> | null

enabled?: boolean | null



metadata?: [BetaMetadata](api/beta/messages.md) { user\_id } 

Body param: An object describing metadata about the request.



user\_id?: string | null

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



output\_config?: [BetaOutputConfig](api/beta/messages.md) { effort, format, task\_budget } 

Body param: Configuration options for the model's output, such as the output format.



effort?: "low" | "medium" | "high" | 2 more | null

All possible effort levels.

One of the following:

"low"

"medium"

"high"

"xhigh"

"max"



format?: [BetaJSONOutputFormat](api/beta/messages.md) { schema, type }  | null

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

schema: Record<string, unknown>

The JSON schema of the format

type: "json\_schema"



task\_budget?: [BetaTokenTaskBudget](api/beta/messages.md) { total, type, remaining }  | null

User-configurable total token budget across contexts.

total: number

Total token budget across all contexts in the session.

type: "tokens"

The budget type. Currently only 'tokens' is supported.

remaining?: number | null

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



service\_tier?: "auto" | "standard\_only"

Body param: Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](api/service-tiers.md) for details.

One of the following:

"auto"

"standard\_only"



speed?: "standard" | "fast" | null

Body param: The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

One of the following:

"standard"

"fast"



stop\_sequences?: Array<string>

Body param: Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.



stream?: false

Body param: Whether to incrementally stream the response using server-sent events.

See [streaming](build-with-claude/streaming.md) for details.



system?: string | Array<[BetaTextBlockParam](api/beta/messages.md) { text, type, cache\_control, citations } >

Body param: System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](build-with-claude/prompt-engineering/claude-prompting-best-practices.md).

One of the following:

string



Array<[BetaTextBlockParam](api/beta/messages.md) { text, type, cache\_control, citations } >

text: string

type: "text"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: Array<[BetaTextCitationParam](api/beta/messages.md)> | null

One of the following:



BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"



thinking?: [BetaThinkingConfigParam](api/beta/messages.md)

Body param: Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

One of the following:



BetaThinkingConfigEnabled { budget\_tokens, type, display } 



budget\_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

type: "enabled"



display?: "summarized" | "omitted" | null

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"



BetaThinkingConfigDisabled { type } 

type: "disabled"



BetaThinkingConfigAdaptive { type, display } 

type: "adaptive"



display?: "summarized" | "omitted" | null

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"



tool\_choice?: [BetaToolChoice](api/beta/messages.md)

Body param: How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



BetaToolChoiceAuto { type, disable\_parallel\_tool\_use } 

The model will automatically decide whether to use tools.

type: "auto"



disable\_parallel\_tool\_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



BetaToolChoiceAny { type, disable\_parallel\_tool\_use } 

The model will use any available tools.

type: "any"



disable\_parallel\_tool\_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



BetaToolChoiceTool { name, type, disable\_parallel\_tool\_use } 

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"



disable\_parallel\_tool\_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



BetaToolChoiceNone { type } 

The model will not be allowed to use tools.

type: "none"



tools?: Array<[BetaToolUnion](api/beta/messages.md)>

Body param: Definitions of tools that the model may use.

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

BetaTool { input\_schema, name, allowed\_callers, 7 more } 



input\_schema: InputSchema { type, properties, required } 

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

properties?: Record<string, unknown> | null

required?: Array<string> | null



name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



description?: string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming?: boolean | null

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples?: Array<Record<string, unknown>>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

type?: "custom" | null



BetaToolBash20241022 { name, type, allowed\_callers, 4 more } 



name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20241022"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples?: Array<Record<string, unknown>>

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaToolBash20250124 { name, type, allowed\_callers, 4 more } 



name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20250124"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples?: Array<Record<string, unknown>>

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaCodeExecutionTool20250522 { name, type, allowed\_callers, 3 more } 



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250522"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaCodeExecutionTool20250825 { name, type, allowed\_callers, 3 more } 



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250825"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaCodeExecutionTool20260120 { name, type, allowed\_callers, 3 more } 

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20260120"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaCodeExecutionTool20260521 { name, type, allowed\_callers, 3 more } 

Code execution tool with REPL state persistence.



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20260521"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaToolComputerUse20241022 { display\_height\_px, display\_width\_px, name, 7 more } 

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.



name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20241022"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number?: number | null

The X11 display number (e.g. 0, 1) for the display.

input\_examples?: Array<Record<string, unknown>>

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaMemoryTool20250818 { name, type, allowed\_callers, 4 more } 



name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "memory\_20250818"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples?: Array<Record<string, unknown>>

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaToolComputerUse20250124 { display\_height\_px, display\_width\_px, name, 7 more } 

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.



name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20250124"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number?: number | null

The X11 display number (e.g. 0, 1) for the display.

input\_examples?: Array<Record<string, unknown>>

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaToolTextEditor20241022 { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20241022"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples?: Array<Record<string, unknown>>

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaToolComputerUse20251124 { display\_height\_px, display\_width\_px, name, 8 more } 

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.



name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20251124"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number?: number | null

The X11 display number (e.g. 0, 1) for the display.

enable\_zoom?: boolean

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples?: Array<Record<string, unknown>>

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaToolTextEditor20250124 { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250124"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples?: Array<Record<string, unknown>>

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaToolTextEditor20250429 { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250429"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples?: Array<Record<string, unknown>>

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaToolTextEditor20250728 { name, type, allowed\_callers, 5 more } 



name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250728"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples?: Array<Record<string, unknown>>

max\_characters?: number | null

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaWebSearchTool20250305 { name, type, allowed\_callers, 7 more } 



name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20250305"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains?: Array<string> | null

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains?: Array<string> | null

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses?: number | null

Maximum number of times the tool can be used in the API request.

strict?: boolean

When true, guarantees schema validation on tool names and inputs



user\_location?: [BetaUserLocation](api/beta/messages.md) { type, city, country, 2 more }  | null

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city?: string | null

The city of the user.

country?: string | null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region?: string | null

The region of the user.

timezone?: string | null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



BetaWebFetchTool20250910 { name, type, allowed\_callers, 8 more } 



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20250910"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains?: Array<string> | null

List of domains to allow fetching from

blocked\_domains?: Array<string> | null

List of domains to block fetching from



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: [BetaCitationsConfigParam](api/beta/messages.md) { enabled }  | null

Citations configuration for fetched documents. Citations are disabled by default.

enabled?: boolean

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens?: number | null

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses?: number | null

Maximum number of times the tool can be used in the API request.

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaWebSearchTool20260209 { name, type, allowed\_callers, 7 more } 



name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20260209"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains?: Array<string> | null

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains?: Array<string> | null

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses?: number | null

Maximum number of times the tool can be used in the API request.

strict?: boolean

When true, guarantees schema validation on tool names and inputs



user\_location?: [BetaUserLocation](api/beta/messages.md) { type, city, country, 2 more }  | null

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city?: string | null

The city of the user.

country?: string | null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region?: string | null

The region of the user.

timezone?: string | null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



BetaWebFetchTool20260209 { name, type, allowed\_callers, 8 more } 



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260209"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains?: Array<string> | null

List of domains to allow fetching from

blocked\_domains?: Array<string> | null

List of domains to block fetching from



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: [BetaCitationsConfigParam](api/beta/messages.md) { enabled }  | null

Citations configuration for fetched documents. Citations are disabled by default.

enabled?: boolean

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens?: number | null

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses?: number | null

Maximum number of times the tool can be used in the API request.

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaWebFetchTool20260309 { name, type, allowed\_callers, 9 more } 

Web fetch tool with use\_cache parameter for bypassing cached content.



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260309"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains?: Array<string> | null

List of domains to allow fetching from

blocked\_domains?: Array<string> | null

List of domains to block fetching from



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: [BetaCitationsConfigParam](api/beta/messages.md) { enabled }  | null

Citations configuration for fetched documents. Citations are disabled by default.

enabled?: boolean

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens?: number | null

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses?: number | null

Maximum number of times the tool can be used in the API request.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

use\_cache?: boolean

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



BetaWebSearchTool20260318 { name, type, allowed\_callers, 8 more } 



name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20260318"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains?: Array<string> | null

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains?: Array<string> | null

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses?: number | null

Maximum number of times the tool can be used in the API request.



response\_inclusion?: "full" | "excluded"

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"

"excluded"

strict?: boolean

When true, guarantees schema validation on tool names and inputs



user\_location?: [BetaUserLocation](api/beta/messages.md) { type, city, country, 2 more }  | null

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city?: string | null

The city of the user.

country?: string | null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region?: string | null

The region of the user.

timezone?: string | null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



BetaWebFetchTool20260318 { name, type, allowed\_callers, 10 more } 



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260318"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains?: Array<string> | null

List of domains to allow fetching from

blocked\_domains?: Array<string> | null

List of domains to block fetching from



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations?: [BetaCitationsConfigParam](api/beta/messages.md) { enabled }  | null

Citations configuration for fetched documents. Citations are disabled by default.

enabled?: boolean

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens?: number | null

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses?: number | null

Maximum number of times the tool can be used in the API request.



response\_inclusion?: "full" | "excluded"

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"

"excluded"

strict?: boolean

When true, guarantees schema validation on tool names and inputs

use\_cache?: boolean

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



BetaAdvisorTool20260301 { model, name, type, 7 more } 



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})



name: "advisor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "advisor\_20260301"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caching?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_tokens?: number | null

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

max\_uses?: number | null

Maximum number of times the tool can be used in the API request.

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaToolSearchToolBm25\_20251119 { name, type, allowed\_callers, 3 more } 



name: "tool\_search\_tool\_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: "tool\_search\_tool\_bm25\_20251119" | "tool\_search\_tool\_bm25"

One of the following:

"tool\_search\_tool\_bm25\_20251119"

"tool\_search\_tool\_bm25"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaToolSearchToolRegex20251119 { name, type, allowed\_callers, 3 more } 



name: "tool\_search\_tool\_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: "tool\_search\_tool\_regex\_20251119" | "tool\_search\_tool\_regex"

One of the following:

"tool\_search\_tool\_regex\_20251119"

"tool\_search\_tool\_regex"



allowed\_callers?: Array<"direct" | "code\_execution\_20250825" | "code\_execution\_20260120" | "code\_execution\_20260521">

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict?: boolean

When true, guarantees schema validation on tool names and inputs



BetaMCPToolset { mcp\_server\_name, type, cache\_control, 2 more } 

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcp\_server\_name: string

Name of the MCP server to configure tools for

type: "mcp\_toolset"



cache\_control?: [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  | null

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl?: "5m" | "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



configs?: Record<string, [BetaMCPToolConfig](api/beta/messages.md) { defer\_loading, enabled } > | null

Configuration overrides for specific tools, keyed by tool name

defer\_loading?: boolean

enabled?: boolean



default\_config?: [BetaMCPToolDefaultConfig](api/beta/messages.md) { defer\_loading, enabled } 

Default configuration applied to all tools from this server

defer\_loading?: boolean

enabled?: boolean



betas?: Array<[AnthropicBeta](api/beta.md)>

Header param: Optional header to specify the beta version(s) you want to use.

One of the following:

(string & {})



"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 26 more

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

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

"agent-memory-2026-07-22"

user\_profile\_id?: string

Header param: The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.



output\_format?: [BetaJSONOutputFormat](api/beta/messages.md) { schema, type }  | null⁠Deprecated

Body param: Deprecated: Use `output_config.format` instead. See [structured outputs](build-with-claude/structured-outputs.md)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

schema: Record<string, unknown>

The JSON schema of the format

type: "json\_schema"



temperature?: number⁠Deprecated

Body param: Amount of randomness injected into the response.

Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0



top\_k?: number⁠Deprecated

Body param: Only sample from the top K options for each subsequent token.

Deprecated. Models released after Claude Opus 4.6 do not accept top\_k; any value will be rejected with a 400 error.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only.

minimum0



top\_p?: number⁠Deprecated

Body param: Use nucleus sampling.

Deprecated. Models released after Claude Opus 4.6 do not support setting top\_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

Recommended for advanced use cases only.

maximum1

minimum0



MessageCreateParamsNonStreaming extends MessageCreateParamsBase { max\_tokens, messages, model, 24 more }  { stream } 



stream?: false

Body param: Whether to incrementally stream the response using server-sent events.

See [streaming](build-with-claude/streaming.md) for details.



MessageCreateParamsStreaming extends MessageCreateParamsBase { max\_tokens, messages, model, 24 more }  { stream } 



stream: true

Body param: Whether to incrementally stream the response using server-sent events.

See [streaming](build-with-claude/streaming.md) for details.

##### ReturnsExpand Collapse



BetaMessage { id, container, content, 9 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: [BetaContainer](api/beta/messages.md) { id, expires\_at, skills }  | null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



skills: Array<[BetaSkill](api/beta/messages.md) { skill\_id, type, version } > | null

Skills loaded in the container

skill\_id: string

Skill ID



type: "anthropic" | "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version



content: Array<[BetaContentBlock](api/beta/messages.md)>

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```



If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```



Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```



One of the following:



BetaTextBlock { citations, text, type } 



citations: Array<[BetaTextCitation](api/beta/messages.md)> | null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

file\_id: string | null

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

file\_id: string | null

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string | null

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"

text: string

type: "text"



BetaThinkingBlock { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



BetaRedactedThinkingBlock { data, type } 

data: string

type: "redacted\_thinking"



BetaToolUseBlock { id, input, name, 2 more } 

id: string

input: Record<string, unknown>

name: string

type: "tool\_use"



caller?: [BetaDirectCaller](api/beta/messages.md) { type }  | [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaServerToolUseBlock { id, input, name, 2 more } 

id: string

input: Record<string, unknown>



name: "advisor" | "web\_search" | "web\_fetch" | 5 more

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



caller?: [BetaDirectCaller](api/beta/messages.md) { type }  | [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller } 



content: [BetaWebSearchToolResultBlockContent](api/beta/messages.md)

One of the following:



BetaWebSearchToolResultError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



Array<[BetaWebSearchResultBlock](api/beta/messages.md) { encrypted\_content, page\_age, title, 2 more } >

encrypted\_content: string

page\_age: string | null

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



caller?: [BetaDirectCaller](api/beta/messages.md) { type }  | [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller } 



content: [BetaWebFetchToolResultErrorBlock](api/beta/messages.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta/messages.md) { content, retrieved\_at, type, url } 

One of the following:



BetaWebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



BetaWebFetchBlock { content, retrieved\_at, type, url } 



content: [BetaDocumentBlock](api/beta/messages.md) { citations, source, title, type } 



citations: [BetaCitationConfig](api/beta/messages.md) { enabled }  | null

Citation configuration for the document

enabled: boolean



source: [BetaBase64PDFSource](api/beta/messages.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta/messages.md) { data, media\_type, type } 

One of the following:



BetaBase64PDFSource { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



BetaPlainTextSource { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string | null

The title of the document

type: "document"

retrieved\_at: string | null

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



caller?: [BetaDirectCaller](api/beta/messages.md) { type }  | [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaAdvisorToolResultBlock { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta/messages.md) { error\_code, type }  | [BetaAdvisorResultBlock](api/beta/messages.md) { stop\_reason, text, type }  | [BetaAdvisorRedactedResultBlock](api/beta/messages.md) { encrypted\_content, stop\_reason, type } 

One of the following:



BetaAdvisorToolResultError { error\_code, type } 



error\_code: "max\_uses\_exceeded" | "prompt\_too\_long" | "too\_many\_requests" | 4 more

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



BetaAdvisorResultBlock { stop\_reason, text, type } 

stop\_reason: string | null

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: string

type: "advisor\_result"



BetaAdvisorRedactedResultBlock { encrypted\_content, stop\_reason, type } 

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: string | null

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: "advisor\_redacted\_result"

tool\_use\_id: string

type: "advisor\_tool\_result"



BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultBlockContent](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



BetaCodeExecutionToolResultError { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array<[BetaCodeExecutionOutputBlock](api/beta/messages.md) { file\_id, type } >

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array<[BetaCodeExecutionOutputBlock](api/beta/messages.md) { file\_id, type } >

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta/messages.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BetaBashCodeExecutionToolResultError { error\_code, type } 



error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array<[BetaBashCodeExecutionOutputBlock](api/beta/messages.md) { file\_id, type } >

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta/messages.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta/messages.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta/messages.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string | null

type: "text\_editor\_code\_execution\_tool\_result\_error"



BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" | "image" | "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number | null

start\_line: number | null

total\_lines: number | null

type: "text\_editor\_code\_execution\_view\_result"



BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array<string> | null

new\_lines: number | null

new\_start: number | null

old\_lines: number | null

old\_start: number | null

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



BetaToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta/messages.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta/messages.md) { tool\_references, type } 

One of the following:



BetaToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | "execution\_time\_exceeded"

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string | null

type: "tool\_search\_tool\_result\_error"



BetaToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array<[BetaToolReferenceBlock](api/beta/messages.md) { tool\_name, type } >

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



BetaMCPToolUseBlock { id, input, name, 2 more } 

id: string

input: Record<string, unknown>

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type } 



content: string | Array<[BetaTextBlock](api/beta/messages.md) { citations, text, type } >

One of the following:

string



Array<[BetaTextBlock](api/beta/messages.md) { citations, text, type } >



citations: Array<[BetaTextCitation](api/beta/messages.md)> | null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

file\_id: string | null

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

file\_id: string | null

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string | null

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"



BetaContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



BetaCompactionBlock { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string | null

Summary of compacted content, or null if compaction failed

encrypted\_content: string | null

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction"



BetaFallbackBlock { from, to, trigger, type } 

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



from: [BetaFallbackInfo](api/beta/messages.md) { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})



to: [BetaFallbackInfo](api/beta/messages.md) { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})



trigger: [BetaFallbackRefusalTrigger](api/beta/messages.md) { category, type } 

What caused the `from` model to hand over at this hop.



category: "cyber" | "bio" | "frontier\_llm" | "reasoning\_extraction" | null

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

type: "refusal"

type: "fallback"



context\_management: [BetaContextManagementResponse](api/beta/messages.md) { applied\_edits }  | null

Context management response.

Information about context management strategies applied during the request.



applied\_edits: Array<[BetaClearToolUses20250919EditResponse](api/beta/messages.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta/messages.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } >

List of context management edits that were applied.

One of the following:



BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.



BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.



diagnostics: [BetaDiagnostics](api/beta/messages.md) { cache\_miss\_reason }  | null

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: [BetaCacheMissModelChanged](api/beta/messages.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissSystemChanged](api/beta/messages.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissToolsChanged](api/beta/messages.md) { cache\_missed\_input\_tokens, type }  | 3 more | null

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



BetaCacheMissModelChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "model\_changed"



BetaCacheMissSystemChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "system\_changed"



BetaCacheMissToolsChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "tools\_changed"



BetaCacheMissMessagesChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "messages\_changed"



BetaCacheMissPreviousMessageNotFound { type } 

type: "previous\_message\_not\_found"



BetaCacheMissUnavailable { type } 

type: "unavailable"



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [BetaRefusalStopDetails](api/beta/messages.md) { category, explanation, fallback\_credit\_token, 3 more }  | null

Structured information about a refusal.



category: "cyber" | "bio" | "frontier\_llm" | "reasoning\_extraction" | null

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string | null

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: string | null

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



fallback\_has\_prefill\_claim: boolean | null

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

recommended\_model: string | null

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: "refusal"



stop\_reason: [BetaStopReason](api/beta/messages.md) | null

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"



stop\_sequence: string | null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: [BetaUsage](api/beta/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 8 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [BetaCacheCreation](api/beta/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number | null

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number | null

The number of input tokens read from the cache.

inference\_geo: string | null

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.



iterations: [BetaIterationsUsage](api/beta/messages.md) | null

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: [BetaCacheCreation](api/beta/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration



BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: [BetaCacheCreation](api/beta/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration



BetaAdvisorMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: [BetaCacheCreation](api/beta/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration



BetaFallbackMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: [BetaCacheCreation](api/beta/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})

output\_tokens: number

The number of output tokens which were used.

type: "fallback\_message"

Usage for the fallback-model attempt that served the response

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: [BetaOutputTokensDetails](api/beta/messages.md) { thinking\_tokens }  | null

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [BetaServerToolUsage](api/beta/messages.md) { web\_fetch\_requests, web\_search\_requests }  | null

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" | "priority" | "batch" | null

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"



speed: "standard" | "fast" | null

The inference speed mode used for this request.

One of the following:

"standard"

"fast"



BetaRawMessageStreamEvent = [BetaRawMessageStartEvent](api/beta/messages.md) { message, type }  | [BetaRawMessageDeltaEvent](api/beta/messages.md) { context\_management, delta, type, usage }  | [BetaRawMessageStopEvent](api/beta/messages.md) { type }  | 3 more

One of the following:



BetaRawMessageStartEvent { message, type } 



message: [BetaMessage](api/beta/messages.md) { id, container, content, 9 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: [BetaContainer](api/beta/messages.md) { id, expires\_at, skills }  | null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



skills: Array<[BetaSkill](api/beta/messages.md) { skill\_id, type, version } > | null

Skills loaded in the container

skill\_id: string

Skill ID



type: "anthropic" | "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version



content: Array<[BetaContentBlock](api/beta/messages.md)>

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```



If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```



Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```



One of the following:



BetaTextBlock { citations, text, type } 



citations: Array<[BetaTextCitation](api/beta/messages.md)> | null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

file\_id: string | null

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

file\_id: string | null

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string | null

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"

text: string

type: "text"



BetaThinkingBlock { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



BetaRedactedThinkingBlock { data, type } 

data: string

type: "redacted\_thinking"



BetaToolUseBlock { id, input, name, 2 more } 

id: string

input: Record<string, unknown>

name: string

type: "tool\_use"



caller?: [BetaDirectCaller](api/beta/messages.md) { type }  | [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaServerToolUseBlock { id, input, name, 2 more } 

id: string

input: Record<string, unknown>



name: "advisor" | "web\_search" | "web\_fetch" | 5 more

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



caller?: [BetaDirectCaller](api/beta/messages.md) { type }  | [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller } 



content: [BetaWebSearchToolResultBlockContent](api/beta/messages.md)

One of the following:



BetaWebSearchToolResultError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



Array<[BetaWebSearchResultBlock](api/beta/messages.md) { encrypted\_content, page\_age, title, 2 more } >

encrypted\_content: string

page\_age: string | null

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



caller?: [BetaDirectCaller](api/beta/messages.md) { type }  | [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller } 



content: [BetaWebFetchToolResultErrorBlock](api/beta/messages.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta/messages.md) { content, retrieved\_at, type, url } 

One of the following:



BetaWebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



BetaWebFetchBlock { content, retrieved\_at, type, url } 



content: [BetaDocumentBlock](api/beta/messages.md) { citations, source, title, type } 



citations: [BetaCitationConfig](api/beta/messages.md) { enabled }  | null

Citation configuration for the document

enabled: boolean



source: [BetaBase64PDFSource](api/beta/messages.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta/messages.md) { data, media\_type, type } 

One of the following:



BetaBase64PDFSource { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



BetaPlainTextSource { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string | null

The title of the document

type: "document"

retrieved\_at: string | null

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



caller?: [BetaDirectCaller](api/beta/messages.md) { type }  | [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaAdvisorToolResultBlock { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta/messages.md) { error\_code, type }  | [BetaAdvisorResultBlock](api/beta/messages.md) { stop\_reason, text, type }  | [BetaAdvisorRedactedResultBlock](api/beta/messages.md) { encrypted\_content, stop\_reason, type } 

One of the following:



BetaAdvisorToolResultError { error\_code, type } 



error\_code: "max\_uses\_exceeded" | "prompt\_too\_long" | "too\_many\_requests" | 4 more

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



BetaAdvisorResultBlock { stop\_reason, text, type } 

stop\_reason: string | null

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: string

type: "advisor\_result"



BetaAdvisorRedactedResultBlock { encrypted\_content, stop\_reason, type } 

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: string | null

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: "advisor\_redacted\_result"

tool\_use\_id: string

type: "advisor\_tool\_result"



BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultBlockContent](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



BetaCodeExecutionToolResultError { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array<[BetaCodeExecutionOutputBlock](api/beta/messages.md) { file\_id, type } >

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array<[BetaCodeExecutionOutputBlock](api/beta/messages.md) { file\_id, type } >

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta/messages.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BetaBashCodeExecutionToolResultError { error\_code, type } 



error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array<[BetaBashCodeExecutionOutputBlock](api/beta/messages.md) { file\_id, type } >

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta/messages.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta/messages.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta/messages.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string | null

type: "text\_editor\_code\_execution\_tool\_result\_error"



BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" | "image" | "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number | null

start\_line: number | null

total\_lines: number | null

type: "text\_editor\_code\_execution\_view\_result"



BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array<string> | null

new\_lines: number | null

new\_start: number | null

old\_lines: number | null

old\_start: number | null

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



BetaToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta/messages.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta/messages.md) { tool\_references, type } 

One of the following:



BetaToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | "execution\_time\_exceeded"

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string | null

type: "tool\_search\_tool\_result\_error"



BetaToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array<[BetaToolReferenceBlock](api/beta/messages.md) { tool\_name, type } >

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



BetaMCPToolUseBlock { id, input, name, 2 more } 

id: string

input: Record<string, unknown>

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type } 



content: string | Array<[BetaTextBlock](api/beta/messages.md) { citations, text, type } >

One of the following:

string



Array<[BetaTextBlock](api/beta/messages.md) { citations, text, type } >



citations: Array<[BetaTextCitation](api/beta/messages.md)> | null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

file\_id: string | null

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

file\_id: string | null

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string | null

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"



BetaContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



BetaCompactionBlock { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string | null

Summary of compacted content, or null if compaction failed

encrypted\_content: string | null

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction"



BetaFallbackBlock { from, to, trigger, type } 

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



from: [BetaFallbackInfo](api/beta/messages.md) { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})



to: [BetaFallbackInfo](api/beta/messages.md) { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})



trigger: [BetaFallbackRefusalTrigger](api/beta/messages.md) { category, type } 

What caused the `from` model to hand over at this hop.



category: "cyber" | "bio" | "frontier\_llm" | "reasoning\_extraction" | null

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

type: "refusal"

type: "fallback"



context\_management: [BetaContextManagementResponse](api/beta/messages.md) { applied\_edits }  | null

Context management response.

Information about context management strategies applied during the request.



applied\_edits: Array<[BetaClearToolUses20250919EditResponse](api/beta/messages.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta/messages.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } >

List of context management edits that were applied.

One of the following:



BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.



BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.



diagnostics: [BetaDiagnostics](api/beta/messages.md) { cache\_miss\_reason }  | null

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: [BetaCacheMissModelChanged](api/beta/messages.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissSystemChanged](api/beta/messages.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissToolsChanged](api/beta/messages.md) { cache\_missed\_input\_tokens, type }  | 3 more | null

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



BetaCacheMissModelChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "model\_changed"



BetaCacheMissSystemChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "system\_changed"



BetaCacheMissToolsChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "tools\_changed"



BetaCacheMissMessagesChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "messages\_changed"



BetaCacheMissPreviousMessageNotFound { type } 

type: "previous\_message\_not\_found"



BetaCacheMissUnavailable { type } 

type: "unavailable"



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [BetaRefusalStopDetails](api/beta/messages.md) { category, explanation, fallback\_credit\_token, 3 more }  | null

Structured information about a refusal.



category: "cyber" | "bio" | "frontier\_llm" | "reasoning\_extraction" | null

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string | null

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: string | null

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



fallback\_has\_prefill\_claim: boolean | null

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

recommended\_model: string | null

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: "refusal"



stop\_reason: [BetaStopReason](api/beta/messages.md) | null

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"



stop\_sequence: string | null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: [BetaUsage](api/beta/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 8 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [BetaCacheCreation](api/beta/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number | null

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number | null

The number of input tokens read from the cache.

inference\_geo: string | null

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.



iterations: [BetaIterationsUsage](api/beta/messages.md) | null

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: [BetaCacheCreation](api/beta/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration



BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: [BetaCacheCreation](api/beta/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration



BetaAdvisorMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: [BetaCacheCreation](api/beta/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration



BetaFallbackMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: [BetaCacheCreation](api/beta/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})

output\_tokens: number

The number of output tokens which were used.

type: "fallback\_message"

Usage for the fallback-model attempt that served the response

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: [BetaOutputTokensDetails](api/beta/messages.md) { thinking\_tokens }  | null

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [BetaServerToolUsage](api/beta/messages.md) { web\_fetch\_requests, web\_search\_requests }  | null

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" | "priority" | "batch" | null

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"



speed: "standard" | "fast" | null

The inference speed mode used for this request.

One of the following:

"standard"

"fast"

type: "message\_start"



BetaRawMessageDeltaEvent { context\_management, delta, type, usage } 



context\_management: [BetaContextManagementResponse](api/beta/messages.md) { applied\_edits }  | null

Information about context management strategies applied during the request



applied\_edits: Array<[BetaClearToolUses20250919EditResponse](api/beta/messages.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta/messages.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } >

List of context management edits that were applied.

One of the following:



BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.



BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.



delta: Delta { container, stop\_details, stop\_reason, stop\_sequence } 



container: [BetaContainer](api/beta/messages.md) { id, expires\_at, skills }  | null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



skills: Array<[BetaSkill](api/beta/messages.md) { skill\_id, type, version } > | null

Skills loaded in the container

skill\_id: string

Skill ID



type: "anthropic" | "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version



stop\_details: [BetaRefusalStopDetails](api/beta/messages.md) { category, explanation, fallback\_credit\_token, 3 more }  | null

Structured information about a refusal.



category: "cyber" | "bio" | "frontier\_llm" | "reasoning\_extraction" | null

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string | null

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: string | null

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



fallback\_has\_prefill\_claim: boolean | null

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

recommended\_model: string | null

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: "refusal"



stop\_reason: [BetaStopReason](api/beta/messages.md) | null

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string | null

type: "message\_delta"



usage: [BetaMessageDeltaUsage](api/beta/messages.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 4 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: number | null

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number | null

The cumulative number of input tokens read from the cache.

input\_tokens: number | null

The cumulative number of input tokens which were used.



iterations: [BetaIterationsUsage](api/beta/messages.md) | null

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: [BetaCacheCreation](api/beta/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration



BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: [BetaCacheCreation](api/beta/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration



BetaAdvisorMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: [BetaCacheCreation](api/beta/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration



BetaFallbackMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: [BetaCacheCreation](api/beta/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})

output\_tokens: number

The number of output tokens which were used.

type: "fallback\_message"

Usage for the fallback-model attempt that served the response

output\_tokens: number

The cumulative number of output tokens which were used.



output\_tokens\_details: [BetaOutputTokensDetails](api/beta/messages.md) { thinking\_tokens }  | null

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [BetaServerToolUsage](api/beta/messages.md) { web\_fetch\_requests, web\_search\_requests }  | null

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



BetaRawMessageStopEvent { type } 

type: "message\_stop"



BetaRawContentBlockStartEvent { content\_block, index, type } 



content\_block: [BetaTextBlock](api/beta/messages.md) { citations, text, type }  | [BetaThinkingBlock](api/beta/messages.md) { signature, thinking, type }  | [BetaRedactedThinkingBlock](api/beta/messages.md) { data, type }  | 14 more

Response model for a file uploaded to the container.

One of the following:



BetaTextBlock { citations, text, type } 



citations: Array<[BetaTextCitation](api/beta/messages.md)> | null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

file\_id: string | null

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

file\_id: string | null

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string | null

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"

text: string

type: "text"



BetaThinkingBlock { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



BetaRedactedThinkingBlock { data, type } 

data: string

type: "redacted\_thinking"



BetaToolUseBlock { id, input, name, 2 more } 

id: string

input: Record<string, unknown>

name: string

type: "tool\_use"



caller?: [BetaDirectCaller](api/beta/messages.md) { type }  | [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaServerToolUseBlock { id, input, name, 2 more } 

id: string

input: Record<string, unknown>



name: "advisor" | "web\_search" | "web\_fetch" | 5 more

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



caller?: [BetaDirectCaller](api/beta/messages.md) { type }  | [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller } 



content: [BetaWebSearchToolResultBlockContent](api/beta/messages.md)

One of the following:



BetaWebSearchToolResultError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



Array<[BetaWebSearchResultBlock](api/beta/messages.md) { encrypted\_content, page\_age, title, 2 more } >

encrypted\_content: string

page\_age: string | null

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



caller?: [BetaDirectCaller](api/beta/messages.md) { type }  | [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller } 



content: [BetaWebFetchToolResultErrorBlock](api/beta/messages.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta/messages.md) { content, retrieved\_at, type, url } 

One of the following:



BetaWebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



BetaWebFetchBlock { content, retrieved\_at, type, url } 



content: [BetaDocumentBlock](api/beta/messages.md) { citations, source, title, type } 



citations: [BetaCitationConfig](api/beta/messages.md) { enabled }  | null

Citation configuration for the document

enabled: boolean



source: [BetaBase64PDFSource](api/beta/messages.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta/messages.md) { data, media\_type, type } 

One of the following:



BetaBase64PDFSource { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



BetaPlainTextSource { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string | null

The title of the document

type: "document"

retrieved\_at: string | null

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



caller?: [BetaDirectCaller](api/beta/messages.md) { type }  | [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaAdvisorToolResultBlock { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta/messages.md) { error\_code, type }  | [BetaAdvisorResultBlock](api/beta/messages.md) { stop\_reason, text, type }  | [BetaAdvisorRedactedResultBlock](api/beta/messages.md) { encrypted\_content, stop\_reason, type } 

One of the following:



BetaAdvisorToolResultError { error\_code, type } 



error\_code: "max\_uses\_exceeded" | "prompt\_too\_long" | "too\_many\_requests" | 4 more

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



BetaAdvisorResultBlock { stop\_reason, text, type } 

stop\_reason: string | null

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: string

type: "advisor\_result"



BetaAdvisorRedactedResultBlock { encrypted\_content, stop\_reason, type } 

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: string | null

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: "advisor\_redacted\_result"

tool\_use\_id: string

type: "advisor\_tool\_result"



BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultBlockContent](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



BetaCodeExecutionToolResultError { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array<[BetaCodeExecutionOutputBlock](api/beta/messages.md) { file\_id, type } >

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array<[BetaCodeExecutionOutputBlock](api/beta/messages.md) { file\_id, type } >

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta/messages.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BetaBashCodeExecutionToolResultError { error\_code, type } 



error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array<[BetaBashCodeExecutionOutputBlock](api/beta/messages.md) { file\_id, type } >

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta/messages.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta/messages.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta/messages.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string | null

type: "text\_editor\_code\_execution\_tool\_result\_error"



BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" | "image" | "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number | null

start\_line: number | null

total\_lines: number | null

type: "text\_editor\_code\_execution\_view\_result"



BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array<string> | null

new\_lines: number | null

new\_start: number | null

old\_lines: number | null

old\_start: number | null

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



BetaToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta/messages.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta/messages.md) { tool\_references, type } 

One of the following:



BetaToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | "execution\_time\_exceeded"

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string | null

type: "tool\_search\_tool\_result\_error"



BetaToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array<[BetaToolReferenceBlock](api/beta/messages.md) { tool\_name, type } >

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



BetaMCPToolUseBlock { id, input, name, 2 more } 

id: string

input: Record<string, unknown>

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type } 



content: string | Array<[BetaTextBlock](api/beta/messages.md) { citations, text, type } >

One of the following:

string



Array<[BetaTextBlock](api/beta/messages.md) { citations, text, type } >



citations: Array<[BetaTextCitation](api/beta/messages.md)> | null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

file\_id: string | null

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

file\_id: string | null

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string | null

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"



BetaContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



BetaCompactionBlock { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string | null

Summary of compacted content, or null if compaction failed

encrypted\_content: string | null

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction"



BetaFallbackBlock { from, to, trigger, type } 

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



from: [BetaFallbackInfo](api/beta/messages.md) { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})



to: [BetaFallbackInfo](api/beta/messages.md) { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})



trigger: [BetaFallbackRefusalTrigger](api/beta/messages.md) { category, type } 

What caused the `from` model to hand over at this hop.



category: "cyber" | "bio" | "frontier\_llm" | "reasoning\_extraction" | null

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

type: "refusal"

type: "fallback"

index: number

type: "content\_block\_start"



BetaRawContentBlockDeltaEvent { delta, index, type } 



delta: [BetaRawContentBlockDelta](api/beta/messages.md)

One of the following:



BetaTextDelta { text, type } 

text: string

type: "text\_delta"



BetaInputJSONDelta { partial\_json, type } 

partial\_json: string

type: "input\_json\_delta"



BetaCitationsDelta { citation, type } 



citation: [BetaCitationCharLocation](api/beta/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationPageLocation](api/beta/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationContentBlockLocation](api/beta/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | 2 more

One of the following:



BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

file\_id: string | null

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

file\_id: string | null

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string | null

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"

type: "citations\_delta"



BetaThinkingDelta { estimated\_tokens, thinking, type } 

estimated\_tokens: number | null

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

thinking: string

type: "thinking\_delta"



BetaSignatureDelta { signature, type } 

signature: string

type: "signature\_delta"



BetaCompactionContentBlockDelta { content, encrypted\_content, type } 

content: string | null

encrypted\_content: string | null

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction\_delta"

index: number

type: "content\_block\_delta"



BetaRawContentBlockStopEvent { index, type } 

index: number

type: "content\_block\_stop"

Create a Message

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaMessage = await client.beta.messages.create({
  max_tokens: 1024,
  messages: [{ content: 'Hello, world', role: 'user' }],
  model: 'claude-opus-4-6',
});

console.log(betaMessage.id);
```

Response 200



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
  "diagnostics": {
    "cache_miss_reason": {
      "cache_missed_input_tokens": 0,
      "type": "model_changed"
    }
  },
  "model": "claude-opus-4-6",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "explanation",
    "fallback_credit_token": "fallback_credit_token",
    "fallback_has_prefill_claim": true,
    "recommended_model": "recommended_model",
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
        "model": "claude-sonnet-5",
        "output_tokens": 0,
        "type": "message"
      }
    ],
    "output_tokens": 503,
    "output_tokens_details": {
      "thinking_tokens": 0
    },
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



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
  "diagnostics": {
    "cache_miss_reason": {
      "cache_missed_input_tokens": 0,
      "type": "model_changed"
    }
  },
  "model": "claude-opus-4-6",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "explanation",
    "fallback_credit_token": "fallback_credit_token",
    "fallback_has_prefill_claim": true,
    "recommended_model": "recommended_model",
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
        "model": "claude-sonnet-5",
        "output_tokens": 0,
        "type": "message"
      }
    ],
    "output_tokens": 503,
    "output_tokens_details": {
      "thinking_tokens": 0
    },
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
