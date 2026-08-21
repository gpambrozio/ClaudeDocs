# Create a Message Batch

Copy page



cURL

# Create a Message Batch

POST/v1/messages/batches

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](build-with-claude/batch-processing.md)

##### Header ParametersExpand Collapse



"anthropic-beta": optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 31 more

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

"anthropic-user-profile-id": optional string

The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

##### Body ParametersJSONExpand Collapse



requests: array of object { custom\_id, params } 

List of requests for prompt completion. Each is an individual request to create a Message.

maxItems100000

minItems1



custom\_id: string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

maxLength64

minLength1

pattern^[a-zA-Z0-9\_-]{1,64}$



params: object { max\_tokens, messages, model, 22 more } 

Messages API creation parameters for the individual request.

See the [Messages API reference](api/messages.md) for full documentation on available parameters.



max\_tokens: number

The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Set to `0` to populate the [prompt cache](build-with-claude/prompt-caching.md) without generating a response.

Different models have different maximum values for this parameter. See [models](about-claude/models/overview.md) for details.

minimum0



messages: array of [BetaMessageParam](api/beta/messages.md) { content, role } 

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

content: string or array of [BetaContentBlockParam](api/beta/messages.md)

One of the following:

string



array of [BetaContentBlockParam](api/beta/messages.md)

One of the following:



BetaTextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional array of [BetaTextCitationParam](api/beta/messages.md) or null

One of the following:



BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string or null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

title: string or null

type: "search\_result\_location"



BetaImageBlockParam object { source, type, cache\_control, transformations } 



source: [BetaBase64ImageSource](api/beta/messages.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta/messages.md) { type, url }  or [BetaFileImageSource](api/beta/messages.md) { file\_id, type } 

One of the following:



BetaBase64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



BetaURLImageSource object { type, url } 

type: "url"

url: string



BetaFileImageSource object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

transformations: optional [BetaImageTransformationsParam](api/beta/messages.md) { oversized\_image }  or null

Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.



oversized\_image: optional "downsize" or "error"

What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

One of the following:

"downsize"

"error"



BetaRequestDocumentBlock object { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta/messages.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta/messages.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta/messages.md) { content, type }  or 2 more

One of the following:



BetaBase64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



BetaPlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



BetaContentBlockSource object { content, type } 



content: string or array of [BetaContentBlockSourceContent](api/beta/messages.md)

One of the following:

string



BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](api/beta/messages.md)

One of the following:



BetaTextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional array of [BetaTextCitationParam](api/beta/messages.md) or null

One of the following:



BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string or null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

title: string or null

type: "search\_result\_location"



BetaImageBlockParam object { source, type, cache\_control, transformations } 



source: [BetaBase64ImageSource](api/beta/messages.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta/messages.md) { type, url }  or [BetaFileImageSource](api/beta/messages.md) { file\_id, type } 

One of the following:



BetaBase64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



BetaURLImageSource object { type, url } 

type: "url"

url: string



BetaFileImageSource object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

transformations: optional [BetaImageTransformationsParam](api/beta/messages.md) { oversized\_image }  or null

Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.



oversized\_image: optional "downsize" or "error"

What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

One of the following:

"downsize"

"error"

type: "content"



BetaURLPDFSource object { type, url } 

type: "url"

url: string



BetaFileDocumentSource object { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional [BetaCitationsConfigParam](api/beta/messages.md) { enabled }  or null

enabled: optional boolean

context: optional string or null

title: optional string or null



BetaSearchResultBlockParam object { content, source, title, 3 more } 



content: array of [BetaTextBlockParam](api/beta/messages.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional array of [BetaTextCitationParam](api/beta/messages.md) or null

One of the following:



BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string or null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

title: string or null

type: "search\_result\_location"

source: string

title: string

type: "search\_result"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional [BetaCitationsConfigParam](api/beta/messages.md) { enabled } 

enabled: optional boolean



BetaThinkingBlockParam object { signature, thinking, type } 



signature: string

The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

thinking: string

The `thinking` text of this block as returned by the API.

type: "thinking"



BetaRedactedThinkingBlockParam object { data, type } 

data: string

The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

type: "redacted\_thinking"



BetaToolUseBlockParam object { id, input, name, 4 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

caller: optional [BetaDirectCaller](api/beta/messages.md) { type }  or [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

toolset\_name: optional string or null

For a toolset member tool\_use, the toolset family this member belongs to.



BetaToolResultBlockParam object { tool\_use\_id, type, cache\_control, 3 more } 

tool\_use\_id: string

type: "tool\_result"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

content: optional string or array of [BetaTextBlockParam](api/beta/messages.md) { text, type, cache\_control, citations }  or [BetaImageBlockParam](api/beta/messages.md) { source, type, cache\_control, transformations }  or [BetaSearchResultBlockParam](api/beta/messages.md) { content, source, title, 3 more }  or 3 more

One of the following:

string



array of [BetaTextBlockParam](api/beta/messages.md) { text, type, cache\_control, citations }  or [BetaImageBlockParam](api/beta/messages.md) { source, type, cache\_control, transformations }  or [BetaSearchResultBlockParam](api/beta/messages.md) { content, source, title, 3 more }  or 3 more

One of the following:



BetaTextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional array of [BetaTextCitationParam](api/beta/messages.md) or null

One of the following:



BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string or null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

title: string or null

type: "search\_result\_location"



BetaImageBlockParam object { source, type, cache\_control, transformations } 



source: [BetaBase64ImageSource](api/beta/messages.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta/messages.md) { type, url }  or [BetaFileImageSource](api/beta/messages.md) { file\_id, type } 

One of the following:



BetaBase64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



BetaURLImageSource object { type, url } 

type: "url"

url: string



BetaFileImageSource object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

transformations: optional [BetaImageTransformationsParam](api/beta/messages.md) { oversized\_image }  or null

Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.



oversized\_image: optional "downsize" or "error"

What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

One of the following:

"downsize"

"error"



BetaSearchResultBlockParam object { content, source, title, 3 more } 



content: array of [BetaTextBlockParam](api/beta/messages.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional array of [BetaTextCitationParam](api/beta/messages.md) or null

One of the following:



BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string or null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

title: string or null

type: "search\_result\_location"

source: string

title: string

type: "search\_result"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional [BetaCitationsConfigParam](api/beta/messages.md) { enabled } 

enabled: optional boolean



BetaRequestDocumentBlock object { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta/messages.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta/messages.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta/messages.md) { content, type }  or 2 more

One of the following:



BetaBase64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



BetaPlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



BetaContentBlockSource object { content, type } 



content: string or array of [BetaContentBlockSourceContent](api/beta/messages.md)

One of the following:

string



BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](api/beta/messages.md)

One of the following:



BetaTextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional array of [BetaTextCitationParam](api/beta/messages.md) or null

One of the following:



BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string or null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

title: string or null

type: "search\_result\_location"



BetaImageBlockParam object { source, type, cache\_control, transformations } 



source: [BetaBase64ImageSource](api/beta/messages.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta/messages.md) { type, url }  or [BetaFileImageSource](api/beta/messages.md) { file\_id, type } 

One of the following:



BetaBase64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



BetaURLImageSource object { type, url } 

type: "url"

url: string



BetaFileImageSource object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

transformations: optional [BetaImageTransformationsParam](api/beta/messages.md) { oversized\_image }  or null

Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.



oversized\_image: optional "downsize" or "error"

What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

One of the following:

"downsize"

"error"

type: "content"



BetaURLPDFSource object { type, url } 

type: "url"

url: string



BetaFileDocumentSource object { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional [BetaCitationsConfigParam](api/beta/messages.md) { enabled }  or null

enabled: optional boolean

context: optional string or null

title: optional string or null



BetaToolReferenceBlockParam object { tool\_name, type, cache\_control } 

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

BetaBrowserStateBlockParam object { tabs, type, cache\_control, state\_changes } 

The caller's browser state after a browser toolset member call —
the full inventory of open tabs, which tab is active, and any side
effects (tabs opened, download state changes) the call produced.

At most one per `tool_result`, only on a non-error result answering a
browser toolset member `tool_use`. The server renders the
model-visible text from it; the model never sees the raw fields.



tabs: array of [BetaBrowserStateTabEntry](api/beta/messages.md) { tab\_id, title, url, active } 

All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

maxItems100

tab\_id: string

The caller-assigned identifier for this tab, unique within the inventory.

title: string

The title of the page the tab is showing. May be empty.

url: string

The URL of the page the tab is showing. May be empty.

active: optional boolean

Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

type: "browser\_state"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

state\_changes: optional array of [BetaBrowserStateChange](api/beta/messages.md) or null

Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

maxItems200

minItems1

One of the following:



BetaBrowserStateChangeTabOpened object { tab\_id, type } 

A tab this call's execution opened that remains open at its end —
the creation delta of the `tabs` inventory, not an event log.

Carries only the `tab_id`; the tab's `title` and `url` live on its
`tabs` entry, which must include the same `tab_id`. A tab opened
during a failed call gets no deferred `tab_opened`; it simply appears
in the next result's `tabs` inventory.

tab\_id: string

The `tab_id` of the opened tab, present in `tabs`.

type: "tab\_opened"



BetaBrowserStateChangeDownloadStarted object { download\_id, type, url } 

A file download that started during this call.

download\_id: string

The caller-assigned identifier for this download, stable across the state changes reporting it.

type: "download\_started"

url: string

The final post-redirect URL the download was served from.



BetaBrowserStateChangeDownloadCompleted object { download\_id, type, url, 2 more } 

A file download that finished during this call, reported with the
same `download_id` as its `download_started` — or without a prior
`download_started`, when the download finished during the call that
started it (at most one state change per `download_id` per result).

download\_id: string

The caller-assigned identifier for this download, stable across the state changes reporting it.

type: "download\_completed"

url: string

The final post-redirect URL the download was served from.

path: optional string or null

Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

size\_bytes: optional number or null

The completed download's size.



BetaBrowserStateChangeDownloadFailed object { download\_id, type, url, error } 

A file download that failed — or was cancelled — during this call.

download\_id: string

The caller-assigned identifier for this download, stable across the state changes reporting it.

type: "download\_failed"

url: string

The final post-redirect URL the download was served from.

error: optional string or null

The failure or cancellation detail, when known.

is\_error: optional boolean

toolset\_name: optional string or null

For a toolset member tool\_result, the toolset family of the paired tool\_use.



BetaServerToolUseBlockParam object { id, input, name, 3 more } 

id: string

input: map[unknown]



name: "advisor" or "web\_search" or "web\_fetch" or 5 more

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

cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

caller: optional [BetaDirectCaller](api/beta/messages.md) { type }  or [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaWebSearchToolResultBlockParam object { content, tool\_use\_id, type, 2 more } 



content: [BetaWebSearchToolResultBlockParamContent](api/beta/messages.md)

One of the following:



ResultBlock = array of [BetaWebSearchResultBlockParam](api/beta/messages.md) { encrypted\_content, title, type, 2 more } 

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string or null



BetaWebSearchToolRequestError object { error\_code, type } 

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

cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

caller: optional [BetaDirectCaller](api/beta/messages.md) { type }  or [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaWebFetchToolResultBlockParam object { content, tool\_use\_id, type, 2 more } 



content: [BetaWebFetchToolResultErrorBlockParam](api/beta/messages.md) { error\_code, type }  or [BetaWebFetchBlockParam](api/beta/messages.md) { content, type, url, retrieved\_at } 

One of the following:



BetaWebFetchToolResultErrorBlockParam object { error\_code, type } 

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

BetaWebFetchBlockParam object { content, type, url, retrieved\_at } 



content: [BetaRequestDocumentBlock](api/beta/messages.md) { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta/messages.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta/messages.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta/messages.md) { content, type }  or 2 more

One of the following:



BetaBase64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



BetaPlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



BetaContentBlockSource object { content, type } 



content: string or array of [BetaContentBlockSourceContent](api/beta/messages.md)

One of the following:

string



BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](api/beta/messages.md)

One of the following:



BetaTextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional array of [BetaTextCitationParam](api/beta/messages.md) or null

One of the following:



BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string or null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

title: string or null

type: "search\_result\_location"



BetaImageBlockParam object { source, type, cache\_control, transformations } 



source: [BetaBase64ImageSource](api/beta/messages.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta/messages.md) { type, url }  or [BetaFileImageSource](api/beta/messages.md) { file\_id, type } 

One of the following:



BetaBase64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



BetaURLImageSource object { type, url } 

type: "url"

url: string



BetaFileImageSource object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

transformations: optional [BetaImageTransformationsParam](api/beta/messages.md) { oversized\_image }  or null

Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.



oversized\_image: optional "downsize" or "error"

What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

One of the following:

"downsize"

"error"

type: "content"



BetaURLPDFSource object { type, url } 

type: "url"

url: string



BetaFileDocumentSource object { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional [BetaCitationsConfigParam](api/beta/messages.md) { enabled }  or null

enabled: optional boolean

context: optional string or null

title: optional string or null

type: "web\_fetch\_result"

url: string

Fetched content URL

retrieved\_at: optional string or null

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

caller: optional [BetaDirectCaller](api/beta/messages.md) { type }  or [BetaServerToolCaller](api/beta/messages.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



BetaDirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



BetaServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



BetaServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



BetaAdvisorToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [BetaAdvisorToolResultErrorParam](api/beta/messages.md) { error\_code, type }  or [BetaAdvisorResultBlockParam](api/beta/messages.md) { text, type, stop\_reason }  or [BetaAdvisorRedactedResultBlockParam](api/beta/messages.md) { encrypted\_content, type, stop\_reason } 

One of the following:



BetaAdvisorToolResultErrorParam object { error\_code, type } 



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

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

BetaAdvisorResultBlockParam object { text, type, stop\_reason } 

text: string

type: "advisor\_result"

stop\_reason: optional string or null



BetaAdvisorRedactedResultBlockParam object { encrypted\_content, type, stop\_reason } 

encrypted\_content: string

Opaque blob produced by a prior response; must be round-tripped verbatim.

type: "advisor\_redacted\_result"

stop\_reason: optional string or null

tool\_use\_id: string

type: "advisor\_tool\_result"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

BetaCodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [BetaCodeExecutionToolResultBlockParamContent](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



BetaCodeExecutionToolResultErrorParam object { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



BetaCodeExecutionResultBlockParam object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlockParam](api/beta/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



BetaEncryptedCodeExecutionResultBlockParam object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlockParam](api/beta/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

BetaBashCodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [BetaBashCodeExecutionToolResultErrorParam](api/beta/messages.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlockParam](api/beta/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BetaBashCodeExecutionToolResultErrorParam object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BetaBashCodeExecutionResultBlockParam object { content, return\_code, stderr, 2 more } 



content: array of [BetaBashCodeExecutionOutputBlockParam](api/beta/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

BetaTextEditorCodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [BetaTextEditorCodeExecutionToolResultErrorParam](api/beta/messages.md) { error\_code, type, error\_message }  or [BetaTextEditorCodeExecutionViewResultBlockParam](api/beta/messages.md) { content, file\_type, type, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta/messages.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta/messages.md) { type, lines, new\_lines, 3 more } 

One of the following:



BetaTextEditorCodeExecutionToolResultErrorParam object { error\_code, type, error\_message } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string or null



BetaTextEditorCodeExecutionViewResultBlockParam object { content, file\_type, type, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number or null

start\_line: optional number or null

total\_lines: optional number or null



BetaTextEditorCodeExecutionCreateResultBlockParam object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



BetaTextEditorCodeExecutionStrReplaceResultBlockParam object { type, lines, new\_lines, 3 more } 

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string or null

new\_lines: optional number or null

new\_start: optional number or null

old\_lines: optional number or null

old\_start: optional number or null

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

BetaToolSearchToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [BetaToolSearchToolResultErrorParam](api/beta/messages.md) { error\_code, type, error\_message }  or [BetaToolSearchToolSearchResultBlockParam](api/beta/messages.md) { tool\_references, type } 

One of the following:



BetaToolSearchToolResultErrorParam object { error\_code, type, error\_message } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

error\_message: optional string or null



BetaToolSearchToolSearchResultBlockParam object { tool\_references, type } 



tool\_references: array of [BetaToolReferenceBlockParam](api/beta/messages.md) { tool\_name, type, cache\_control } 

tool\_name: string

type: "tool\_reference"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

BetaMCPToolUseBlockParam object { id, input, name, 3 more } 

id: string

input: map[unknown]

name: string

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

BetaRequestMCPToolResultBlockParam object { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: string

type: "mcp\_tool\_result"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

content: optional string or array of [BetaTextBlockParam](api/beta/messages.md) { text, type, cache\_control, citations } 

One of the following:

string



BetaMCPToolResultBlockParamContent = array of [BetaTextBlockParam](api/beta/messages.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional array of [BetaTextCitationParam](api/beta/messages.md) or null

One of the following:



BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string or null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

title: string or null

type: "search\_result\_location"

is\_error: optional boolean



BetaContainerUploadBlockParam object { file\_id, type, cache\_control } 

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

BetaCompactionBlockParam object { type, cache\_control, content, encrypted\_content } 

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

type: "compaction"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

BetaRequestToolAdditionBlock object { tool, type, cache\_control } 

Mid-conversation directive to surface a declared tool.

`tool` references a tool (or MCP toolset) by name from the request's
`tools`; it is offered to the model from this point in the
conversation onward.



tool: [BetaToolChangeToolReference](api/beta/messages.md) { name, type }  or [BetaToolChangeMCPToolReference](api/beta/messages.md) { name, server\_name, type }  or [BetaToolChangeMCPToolsetReference](api/beta/messages.md) { server\_name, type } 

Reference to a single tool the caller declared directly in
`tools[]`. Does not accept the composed `{server}_{name}` form the
server assigns to MCP-resolved tools — use `mcp_tool_reference` or
`mcp_toolset_reference` for those.

One of the following:



BetaToolChangeToolReference object { name, type } 

Reference to a single tool the caller declared directly in
`tools[]`. Does not accept the composed `{server}_{name}` form the
server assigns to MCP-resolved tools — use `mcp_tool_reference` or
`mcp_toolset_reference` for those.

name: string

type: "tool\_reference"



BetaToolChangeMCPToolReference object { name, server\_name, type } 

Reference to a single MCP tool by its server and remote name — the
same `server_name`/`name` pair `mcp_tool_use` carries.

name: string

server\_name: string

type: "mcp\_tool\_reference"



BetaToolChangeMCPToolsetReference object { server\_name, type } 

Reference to every tool in the named MCP server's toolset.

server\_name: string

type: "mcp\_toolset\_reference"

type: "tool\_addition"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

BetaRequestToolRemovalBlock object { tool, type, cache\_control } 

Mid-conversation directive to withdraw a tool.

`tool` references a tool (or MCP toolset) by name from the request's
`tools`; it is no longer offered to the model from this point in the
conversation onward.



tool: [BetaToolChangeToolReference](api/beta/messages.md) { name, type }  or [BetaToolChangeMCPToolReference](api/beta/messages.md) { name, server\_name, type }  or [BetaToolChangeMCPToolsetReference](api/beta/messages.md) { server\_name, type } 

Reference to a single tool the caller declared directly in
`tools[]`. Does not accept the composed `{server}_{name}` form the
server assigns to MCP-resolved tools — use `mcp_tool_reference` or
`mcp_toolset_reference` for those.

One of the following:



BetaToolChangeToolReference object { name, type } 

Reference to a single tool the caller declared directly in
`tools[]`. Does not accept the composed `{server}_{name}` form the
server assigns to MCP-resolved tools — use `mcp_tool_reference` or
`mcp_toolset_reference` for those.

name: string

type: "tool\_reference"



BetaToolChangeMCPToolReference object { name, server\_name, type } 

Reference to a single MCP tool by its server and remote name — the
same `server_name`/`name` pair `mcp_tool_use` carries.

name: string

server\_name: string

type: "mcp\_tool\_reference"



BetaToolChangeMCPToolsetReference object { server\_name, type } 

Reference to every tool in the named MCP server's toolset.

server\_name: string

type: "mcp\_toolset\_reference"

type: "tool\_removal"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

BetaFallbackBlockParam object { from, to, type, trigger } 

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

to: [BetaFallbackInfoParam](api/beta/messages.md) { model } 

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

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

model: [Model](api/messages.md)

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

cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

container: optional [BetaContainerParams](api/beta/messages.md) { id, skills }  or string or null

Container identifier for reuse across requests.

One of the following:



BetaContainerParams object { id, skills } 

Container parameters with skills to be loaded.

id: optional string or null

Container id



skills: optional array of [BetaSkillParams](api/beta/messages.md) { skill\_id, type, version }  or null

List of skills to load in the container

maxItems20

skill\_id: string

Skill ID



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: optional string

Skill version or 'latest' for most recent version

string



context\_management: optional [BetaContextManagementConfig](api/beta/messages.md) { edits }  or null

Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.



edits: optional array of [BetaClearToolUses20250919Edit](api/beta/messages.md) { type, clear\_at\_least, clear\_tool\_inputs, 3 more }  or [BetaClearThinking20251015Edit](api/beta/messages.md) { type, keep }  or [BetaCompact20260112Edit](api/beta/messages.md) { type, instructions, pause\_after\_compaction, trigger } 

List of context management edits to apply

minItems0

One of the following:



BetaClearToolUses20250919Edit object { type, clear\_at\_least, clear\_tool\_inputs, 3 more } 

type: "clear\_tool\_uses\_20250919"



clear\_at\_least: optional [BetaInputTokensClearAtLeast](api/beta/messages.md) { type, value }  or null

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: "input\_tokens"

value: number



clear\_tool\_inputs: optional boolean or array of string or null

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

One of the following:

boolean

array of string

exclude\_tools: optional array of string or null

Tool names whose uses are preserved from clearing



keep: optional [BetaToolUsesKeep](api/beta/messages.md) { type, value } 

Number of tool uses to retain in the conversation

type: "tool\_uses"

value: number



trigger: optional [BetaInputTokensTrigger](api/beta/messages.md) { type, value }  or [BetaToolUsesTrigger](api/beta/messages.md) { type, value } 

Condition that triggers the context management strategy

One of the following:



BetaInputTokensTrigger object { type, value } 

type: "input\_tokens"

value: number



BetaToolUsesTrigger object { type, value } 

type: "tool\_uses"

value: number



BetaClearThinking20251015Edit object { type, keep } 

type: "clear\_thinking\_20251015"



keep: optional [BetaThinkingTurns](api/beta/messages.md) { type, value }  or [BetaAllThinkingTurns](api/beta/messages.md) { type }  or "all"

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

One of the following:



BetaThinkingTurns object { type, value } 

type: "thinking\_turns"

value: number



BetaAllThinkingTurns object { type } 

type: "all"

"all"



BetaCompact20260112Edit object { type, instructions, pause\_after\_compaction, trigger } 

Automatically compact older context when reaching the configured trigger threshold.

type: "compact\_20260112"

instructions: optional string or null

Additional instructions for summarization.

pause\_after\_compaction: optional boolean

Whether to pause after compaction and return the compaction block to the user.



trigger: optional [BetaInputTokensTrigger](api/beta/messages.md) { type, value }  or null

When to trigger compaction. Defaults to 150000 input tokens.

type: "input\_tokens"

value: number



diagnostics: optional [BetaDiagnosticsParam](api/beta/messages.md) { previous\_message\_id }  or null

Request-level diagnostics. Currently carries the previous response
id for prompt-cache divergence reporting.

previous\_message\_id: optional string or null

The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.



fallback\_credit\_token: optional string or [BetaFallbackCreditTokenParam](api/beta/messages.md) { token, mode }  or null

The `fallback_credit_token` from a prior refusal's `stop_details`.

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

One of the following:

string



BetaFallbackCreditTokenParam object { token, mode } 

Object form of `fallback_credit_token`: the token plus a redemption
mode.

Requires `anthropic-beta: fallback-credit-2026-07-01`; without that
header the field accepts the bare string only. The bare string and the
mode-less object are equivalent (both select `strict`), so wrapping
an existing token changes nothing by itself.

token: string

The opaque `fallback_credit_token` from a prior refusal's `stop_details` — the same string the bare-string form carries.



mode: optional "strict" or "best\_effort"

How a failing token affects the retry. `strict` (the default, and the bare-string behavior): a failing redemption is a 400 and the retry is not served. `best_effort`: the retry is served either way — a token-layer failure no longer rejects the request; the retry proceeds at normal price and the outcome is reported on the response's `usage.fallback_credit`. Two failures stay hard in both modes: a malformed token, and combining `fallback_credit_token` with `fallbacks`.

One of the following:

"strict"

"best\_effort"



fallbacks: optional [BetaFallbacksParam](api/beta/messages.md) or null

Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. The string "default" requests the requested model's server-defined default fallback configuration.

One of the following:



array of [BetaFallbackParam](api/beta/messages.md) { model, max\_tokens, output\_config, 2 more } 



model: [Model](api/messages.md)

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

max\_tokens: optional number or null



output\_config: optional [BetaOutputConfig](api/beta/messages.md) { effort, format, task\_budget }  or null



effort: optional "low" or "medium" or "high" or 2 more or null

All possible effort levels.

One of the following:

"low"

"medium"

"high"

"xhigh"

"max"



format: optional [BetaJSONOutputFormat](api/beta/messages.md) { schema, type }  or null

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

schema: map[unknown]

The JSON schema of the format

type: "json\_schema"



task\_budget: optional [BetaTokenTaskBudget](api/beta/messages.md) { total, type, remaining }  or null

User-configurable total token budget across contexts.

total: number

Total token budget across all contexts in the session.

type: "tokens"

The budget type. Currently only 'tokens' is supported.

remaining: optional number or null

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



speed: optional "standard" or "fast" or null

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



thinking: optional [BetaThinkingConfigEnabled](api/beta/messages.md) { budget\_tokens, type, display }  or [BetaThinkingConfigDisabled](api/beta/messages.md) { type }  or [BetaThinkingConfigAdaptive](api/beta/messages.md) { type, display }  or null

One of the following:



BetaThinkingConfigEnabled object { budget\_tokens, type, display } 



budget\_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

type: "enabled"



display: optional "summarized" or "omitted" or null

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"



BetaThinkingConfigDisabled object { type } 

type: "disabled"



BetaThinkingConfigAdaptive object { type, display } 

type: "adaptive"



display: optional "summarized" or "omitted" or null

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"

Default = "default"

inference\_geo: optional string or null

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.



mcp\_servers: optional array of [BetaRequestMCPServerURLDefinition](api/beta/messages.md) { name, type, url, 2 more } 

MCP servers to be utilized in this request

maxItems20

name: string

type: "url"

url: string

authorization\_token: optional string or null



tool\_configuration: optional [BetaRequestMCPServerToolConfiguration](api/beta/messages.md) { allowed\_tools, enabled }  or null

allowed\_tools: optional array of string or null

enabled: optional boolean or null



metadata: optional [BetaMetadata](api/beta/messages.md) { user\_id } 

An object describing metadata about the request.



user\_id: optional string or null

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



output\_config: optional [BetaOutputConfig](api/beta/messages.md) { effort, format, task\_budget } 

Configuration options for the model's output, such as the output format.



effort: optional "low" or "medium" or "high" or 2 more or null

All possible effort levels.

One of the following:

"low"

"medium"

"high"

"xhigh"

"max"



format: optional [BetaJSONOutputFormat](api/beta/messages.md) { schema, type }  or null

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

schema: map[unknown]

The JSON schema of the format

type: "json\_schema"



task\_budget: optional [BetaTokenTaskBudget](api/beta/messages.md) { total, type, remaining }  or null

User-configurable total token budget across contexts.

total: number

Total token budget across all contexts in the session.

type: "tokens"

The budget type. Currently only 'tokens' is supported.

remaining: optional number or null

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



service\_tier: optional "auto" or "standard\_only"

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](api/service-tiers.md) for details.

One of the following:

"auto"

"standard\_only"



speed: optional "standard" or "fast" or null

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



stop\_sequences: optional array of string

Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.



stream: optional boolean

Whether to incrementally stream the response using server-sent events.

See [streaming](build-with-claude/streaming.md) for details.



system: optional string or array of [BetaTextBlockParam](api/beta/messages.md) { text, type, cache\_control, citations } 

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](build-with-claude/prompt-engineering/claude-prompting-best-practices.md).

One of the following:

string



array of [BetaTextBlockParam](api/beta/messages.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional array of [BetaTextCitationParam](api/beta/messages.md) or null

One of the following:



BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string or null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

title: string or null

type: "search\_result\_location"



thinking: optional [BetaThinkingConfigParam](api/beta/messages.md)

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

One of the following:



BetaThinkingConfigEnabled object { budget\_tokens, type, display } 



budget\_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

type: "enabled"



display: optional "summarized" or "omitted" or null

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"



BetaThinkingConfigDisabled object { type } 

type: "disabled"



BetaThinkingConfigAdaptive object { type, display } 

type: "adaptive"



display: optional "summarized" or "omitted" or null

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"



tool\_choice: optional [BetaToolChoice](api/beta/messages.md)

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



BetaToolChoiceAuto object { type, disable\_parallel\_tool\_use } 

The model will automatically decide whether to use tools.

type: "auto"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



BetaToolChoiceAny object { type, disable\_parallel\_tool\_use } 

The model will use any available tools.

type: "any"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



BetaToolChoiceTool object { name, type, disable\_parallel\_tool\_use } 

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



BetaToolChoiceNone object { type } 

The model will not be allowed to use tools.

type: "none"



tools: optional array of [BetaToolUnion](api/beta/messages.md)

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

BetaTool object { input\_schema, name, allowed\_callers, 7 more } 



input\_schema: object { type, properties, required } 

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

properties: optional map[unknown] or null

required: optional array of string or null



name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

pattern^[a-zA-Z0-9\_-]{1,128}$



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



description: optional string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: optional boolean or null

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

type: optional "custom" or null



BetaToolBash20241022 object { name, type, allowed\_callers, 4 more } 



name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20241022"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaToolBash20250124 object { name, type, allowed\_callers, 4 more } 



name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20250124"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaCodeExecutionTool20250522 object { name, type, allowed\_callers, 3 more } 



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250522"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaCodeExecutionTool20250825 object { name, type, allowed\_callers, 3 more } 



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250825"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaCodeExecutionTool20260120 object { name, type, allowed\_callers, 3 more } 

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20260120"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaCodeExecutionTool20260521 object { name, type, allowed\_callers, 3 more } 

Code execution tool with REPL state persistence.



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20260521"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaBrowserToolset20260801 object { type, allowed\_callers, cache\_control, configs } 

The browser toolset: a single `tools[]` entry (carrying no
`name`) that declares the browser tool family. The model is served
the family's tool with any members disabled via `configs` removed
from its schema.

type: "browser\_toolset\_20260801"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

configs: optional [BetaBrowserToolsetConfigs](api/beta/messages.md) { close\_tab, double\_click, file\_upload, 28 more }  or null

Per-member configuration for `browser_toolset_20260801`: one
optional field per member tool, keyed by the member name — the same
name the member's `tool_use` blocks carry. Every member is an
accepted key, and a member's defaults apply wherever its key is
absent. Unknown keys are rejected: the field set is this toolset
version's complete member set.



close\_tab: optional [BetaBrowserCloseTabConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`close_tab`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



double\_click: optional [BetaBrowserDoubleClickConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`double_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



file\_upload: optional [BetaBrowserFileUploadConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`file_upload`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



find: optional [BetaBrowserFindConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`find`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



form\_input: optional [BetaBrowserFormInputConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`form_input`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



get\_page\_text: optional [BetaBrowserGetPageTextConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`get_page_text`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



hold\_key: optional [BetaBrowserHoldKeyConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`hold_key`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



hover: optional [BetaBrowserHoverConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`hover`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



javascript\_exec: optional [BetaBrowserJavascriptExecConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`javascript_exec`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



key: optional [BetaBrowserKeyConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`key`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



left\_click: optional [BetaBrowserLeftClickConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`left_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



left\_click\_drag: optional [BetaBrowserLeftClickDragConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`left_click_drag`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



left\_mouse\_down: optional [BetaBrowserLeftMouseDownConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`left_mouse_down`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



left\_mouse\_up: optional [BetaBrowserLeftMouseUpConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`left_mouse_up`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



list\_tabs: optional [BetaBrowserListTabsConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`list_tabs`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



middle\_click: optional [BetaBrowserMiddleClickConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`middle_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



mouse\_move: optional [BetaBrowserMouseMoveConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`mouse_move`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



navigate: optional [BetaBrowserNavigateConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`navigate`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



new\_tab: optional [BetaBrowserNewTabConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`new_tab`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



read\_console: optional [BetaBrowserReadConsoleConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`read_console`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



read\_network: optional [BetaBrowserReadNetworkConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`read_network`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



read\_page: optional [BetaBrowserReadPageConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`read_page`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



right\_click: optional [BetaBrowserRightClickConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`right_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



screenshot: optional [BetaBrowserScreenshotConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`screenshot`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



scroll: optional [BetaBrowserScrollConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`scroll`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



scroll\_to: optional [BetaBrowserScrollToConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`scroll_to`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



switch\_tab: optional [BetaBrowserSwitchTabConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`switch_tab`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



triple\_click: optional [BetaBrowserTripleClickConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`triple_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



type: optional [BetaBrowserTypeConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`type`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



wait: optional [BetaBrowserWaitConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`wait`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



zoom: optional [BetaBrowserZoomConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`zoom`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaToolComputerUse20241022 object { display\_height\_px, display\_width\_px, name, 7 more } 

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

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number or null

The X11 display number (e.g. 0, 1) for the display.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaMemoryTool20250818 object { name, type, allowed\_callers, 4 more } 



name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "memory\_20250818"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaToolComputerUse20250124 object { display\_height\_px, display\_width\_px, name, 7 more } 

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

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number or null

The X11 display number (e.g. 0, 1) for the display.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaToolTextEditor20241022 object { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20241022"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaToolComputerUse20251124 object { display\_height\_px, display\_width\_px, name, 8 more } 

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

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number or null

The X11 display number (e.g. 0, 1) for the display.

enable\_zoom: optional boolean

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaComputerToolset20260801 object { type, allowed\_callers, cache\_control, configs } 

The computer toolset: a single `tools[]` entry (carrying no
`name`) that declares the computer tool family. The model is
served the family's tool with any members disabled via `configs`
removed from its schema. Every member is enabled by default, zoom
included. The single-tool options `display_number` and
`enable_zoom` are not fields of a toolset entry — it carries only
`type`, `configs`, and `cache_control`; zoom is controlled
via `configs.zoom.enabled`.

type: "computer\_toolset\_20260801"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

configs: optional [BetaComputerToolsetConfigs](api/beta/messages.md) { cursor\_position, double\_click, hold\_key, 14 more }  or null

Per-member configuration for `computer_toolset_20260801`: one
optional field per member tool, keyed by the member name — the same
name the member's `tool_use` blocks carry. Every member is an
accepted key, and a member's defaults apply wherever its key is
absent. Unknown keys are rejected: the field set is this toolset
version's complete member set.



cursor\_position: optional [BetaComputerCursorPositionConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`cursor_position`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



double\_click: optional [BetaComputerDoubleClickConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`double_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



hold\_key: optional [BetaComputerHoldKeyConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`hold_key`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



key: optional [BetaComputerKeyConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`key`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



left\_click: optional [BetaComputerLeftClickConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`left_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



left\_click\_drag: optional [BetaComputerLeftClickDragConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`left_click_drag`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



left\_mouse\_down: optional [BetaComputerLeftMouseDownConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`left_mouse_down`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



left\_mouse\_up: optional [BetaComputerLeftMouseUpConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`left_mouse_up`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



middle\_click: optional [BetaComputerMiddleClickConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`middle_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



mouse\_move: optional [BetaComputerMouseMoveConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`mouse_move`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



right\_click: optional [BetaComputerRightClickConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`right_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



screenshot: optional [BetaComputerScreenshotConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`screenshot`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



scroll: optional [BetaComputerScrollConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`scroll`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



triple\_click: optional [BetaComputerTripleClickConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`triple_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



type: optional [BetaComputerTypeConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`type`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



wait: optional [BetaComputerWaitConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`wait`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



zoom: optional [BetaComputerZoomConfig](api/beta/messages.md) { defer\_loading, enabled }  or null

`zoom`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaToolTextEditor20250124 object { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250124"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaToolTextEditor20250429 object { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250429"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaToolTextEditor20250728 object { name, type, allowed\_callers, 5 more } 



name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250728"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

max\_characters: optional number or null

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaWebSearchTool20250305 object { name, type, allowed\_callers, 7 more } 



name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20250305"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: optional array of string or null

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string or null

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number or null

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



user\_location: optional [BetaUserLocation](api/beta/messages.md) { type, city, country, 2 more }  or null

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string or null

The city of the user.

country: optional string or null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string or null

The region of the user.

timezone: optional string or null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



BetaWebFetchTool20250910 object { name, type, allowed\_callers, 8 more } 



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20250910"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: optional array of string or null

List of domains to allow fetching from

blocked\_domains: optional array of string or null

List of domains to block fetching from



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional [BetaCitationsConfigParam](api/beta/messages.md) { enabled }  or null

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number or null

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number or null

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaWebSearchTool20260209 object { name, type, allowed\_callers, 7 more } 



name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20260209"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: optional array of string or null

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string or null

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number or null

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



user\_location: optional [BetaUserLocation](api/beta/messages.md) { type, city, country, 2 more }  or null

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string or null

The city of the user.

country: optional string or null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string or null

The region of the user.

timezone: optional string or null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



BetaWebFetchTool20260209 object { name, type, allowed\_callers, 8 more } 



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260209"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: optional array of string or null

List of domains to allow fetching from

blocked\_domains: optional array of string or null

List of domains to block fetching from



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional [BetaCitationsConfigParam](api/beta/messages.md) { enabled }  or null

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number or null

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number or null

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaWebFetchTool20260309 object { name, type, allowed\_callers, 9 more } 

Web fetch tool with use\_cache parameter for bypassing cached content.



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260309"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: optional array of string or null

List of domains to allow fetching from

blocked\_domains: optional array of string or null

List of domains to block fetching from



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional [BetaCitationsConfigParam](api/beta/messages.md) { enabled }  or null

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number or null

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number or null

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

use\_cache: optional boolean

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



BetaWebSearchTool20260318 object { name, type, allowed\_callers, 8 more } 



name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20260318"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: optional array of string or null

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string or null

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number or null

Maximum number of times the tool can be used in the API request.



response\_inclusion: optional "full" or "excluded"

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"

"excluded"

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



user\_location: optional [BetaUserLocation](api/beta/messages.md) { type, city, country, 2 more }  or null

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string or null

The city of the user.

country: optional string or null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string or null

The region of the user.

timezone: optional string or null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



BetaWebFetchTool20260318 object { name, type, allowed\_callers, 10 more } 



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260318"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: optional array of string or null

List of domains to allow fetching from

blocked\_domains: optional array of string or null

List of domains to block fetching from



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

citations: optional [BetaCitationsConfigParam](api/beta/messages.md) { enabled }  or null

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number or null

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number or null

Maximum number of times the tool can be used in the API request.



response\_inclusion: optional "full" or "excluded"

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"

"excluded"

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

use\_cache: optional boolean

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



BetaAdvisorTool20260301 object { model, name, type, 7 more } 



model: [Model](api/messages.md)

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

name: "advisor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "advisor\_20260301"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

caching: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_tokens: optional number or null

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

max\_uses: optional number or null

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaToolSearchToolBm25\_20251119 object { name, type, allowed\_callers, 3 more } 



name: "tool\_search\_tool\_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: "tool\_search\_tool\_bm25\_20251119" or "tool\_search\_tool\_bm25"

One of the following:

"tool\_search\_tool\_bm25\_20251119"

"tool\_search\_tool\_bm25"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaToolSearchToolRegex20251119 object { name, type, allowed\_callers, 3 more } 



name: "tool\_search\_tool\_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: "tool\_search\_tool\_regex\_20251119" or "tool\_search\_tool\_regex"

One of the following:

"tool\_search\_tool\_regex\_20251119"

"tool\_search\_tool\_regex"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



BetaMCPToolset object { mcp\_server\_name, type, cache\_control, 2 more } 

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcp\_server\_name: string

Name of the MCP server to configure tools for

type: "mcp\_toolset"



cache\_control: optional [BetaCacheControlEphemeral](api/beta/messages.md) { type, ttl }  or null

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

configs: optional map[[BetaMCPToolConfig](api/beta/messages.md) { defer\_loading, enabled } ] or null

Configuration overrides for specific tools, keyed by tool name

defer\_loading: optional boolean

enabled: optional boolean



default\_config: optional [BetaMCPToolDefaultConfig](api/beta/messages.md) { defer\_loading, enabled } 

Default configuration applied to all tools from this server

defer\_loading: optional boolean

enabled: optional boolean



output\_format: optional [BetaJSONOutputFormat](api/beta/messages.md) { schema, type }  or null⁠Deprecated

Deprecated: Use `output_config.format` instead. See [structured outputs](build-with-claude/structured-outputs.md)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

schema: map[unknown]

The JSON schema of the format

type: "json\_schema"



temperature: optional number⁠Deprecated

Amount of randomness injected into the response.

Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0



top\_k: optional number⁠Deprecated

Only sample from the top K options for each subsequent token.

Deprecated. Models released after Claude Opus 4.6 do not accept top\_k; any value will be rejected with a 400 error.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only.

minimum0



top\_p: optional number⁠Deprecated

Use nucleus sampling.

Deprecated. Models released after Claude Opus 4.6 do not support setting top\_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

Recommended for advanced use cases only.

maximum1

minimum0

##### ReturnsExpand Collapse



BetaMessageBatch object { id, archived\_at, cancel\_initiated\_at, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.

archived\_at: string or null

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

cancel\_initiated\_at: string or null

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

created\_at: string

RFC 3339 datetime string representing the time at which the Message Batch was created.



ended\_at: string or null

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires\_at: string

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.



processing\_status: "in\_progress" or "canceling" or "ended"

Processing status of the Message Batch.

One of the following:

"in\_progress"

"canceling"

"ended"



request\_counts: [BetaMessageBatchRequestCounts](api/beta/messages/batches.md) { canceled, errored, expired, 2 more } 

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.



canceled: number

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



errored: number

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



expired: number

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: number

Number of requests in the Message Batch that are processing.



succeeded: number

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



results\_url: string or null

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.



type: "message\_batch"

Object type.

For Message Batches, this is always `"message_batch"`.

Create a Message Batch

cURL

```shiki
curl https://api.anthropic.com/v1/messages/batches \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: message-batches-2024-09-24' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "requests": [
            {
              "custom_id": "my-custom-id-1",
              "params": {
                "max_tokens": 1024,
                "messages": [
                  {
                    "content": "Hello, world",
                    "role": "user"
                  }
                ],
                "model": "claude-opus-5"
              }
            }
          ]
        }'
```

Response 200



```shiki
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

---

*Copyright © Anthropic. All rights reserved.*
