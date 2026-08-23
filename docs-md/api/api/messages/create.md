# Create a Message

Copy page



cURL

# Create a Message

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](get-started.md)

##### Header ParametersExpand Collapse

"anthropic-user-profile-id": optional string

The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

##### Body ParametersJSONExpand Collapse



max\_tokens: number

The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Set to `0` to populate the [prompt cache](build-with-claude/prompt-caching.md) without generating a response.

Different models have different maximum values for this parameter. See [models](about-claude/models/overview.md) for details.

minimum0



messages: array of [MessageParam](api/messages.md) { content, role } 

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

content: string or array of [ContentBlockParam](api/messages.md)

One of the following:

string



array of [ContentBlockParam](api/messages.md)

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

citations: optional array of [TextCitationParam](api/messages.md) or null

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

ImageBlockParam object { source, type, cache\_control, transformations } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url }  or [FileImageSource](api/messages.md) { file\_id, type } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

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

URLImageSource object { type, url } 

type: "url"

url: string



FileImageSource object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

transformations: optional [ImageTransformationsParam](api/messages.md) { oversized\_image }  or null

Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.



oversized\_image: optional "downsize" or "error"

What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

One of the following:

"downsize"

"error"



DocumentBlockParam object { source, type, cache\_control, 3 more } 



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type }  or [ContentBlockSource](api/messages.md) { content, type }  or 2 more

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



ContentBlockSource object { content, type } 



content: string or array of [ContentBlockSourceContent](api/messages.md)

One of the following:

string



ContentBlockSourceContent = array of [ContentBlockSourceContent](api/messages.md)

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

citations: optional array of [TextCitationParam](api/messages.md) or null

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

ImageBlockParam object { source, type, cache\_control, transformations } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url }  or [FileImageSource](api/messages.md) { file\_id, type } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

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

URLImageSource object { type, url } 

type: "url"

url: string



FileImageSource object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

transformations: optional [ImageTransformationsParam](api/messages.md) { oversized\_image }  or null

Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.



oversized\_image: optional "downsize" or "error"

What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

One of the following:

"downsize"

"error"

type: "content"



URLPDFSource object { type, url } 

type: "url"

url: string



FileDocumentSource object { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

citations: optional [CitationsConfigParam](api/messages.md) { enabled }  or null

enabled: optional boolean

context: optional string or null

title: optional string or null



SearchResultBlockParam object { content, source, title, 3 more } 



content: array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

citations: optional array of [TextCitationParam](api/messages.md) or null

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

enabled: optional boolean



ThinkingBlockParam object { signature, thinking, type } 



signature: string

The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

thinking: string

The `thinking` text of this block as returned by the API.

type: "thinking"



RedactedThinkingBlockParam object { data, type } 

data: string

The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

type: "redacted\_thinking"



ToolUseBlockParam object { id, input, name, 4 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

caller: optional [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

toolset\_name: optional string or null

For a toolset member tool\_use, the toolset family this member belongs to.



ToolResultBlockParam object { tool\_use\_id, type, cache\_control, 3 more } 

tool\_use\_id: string

type: "tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

content: optional string or array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  or [ImageBlockParam](api/messages.md) { source, type, cache\_control, transformations }  or [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  or 3 more

One of the following:

string



array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  or [ImageBlockParam](api/messages.md) { source, type, cache\_control, transformations }  or [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  or 3 more

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

citations: optional array of [TextCitationParam](api/messages.md) or null

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

ImageBlockParam object { source, type, cache\_control, transformations } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url }  or [FileImageSource](api/messages.md) { file\_id, type } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

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

URLImageSource object { type, url } 

type: "url"

url: string



FileImageSource object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

transformations: optional [ImageTransformationsParam](api/messages.md) { oversized\_image }  or null

Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.



oversized\_image: optional "downsize" or "error"

What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

One of the following:

"downsize"

"error"



SearchResultBlockParam object { content, source, title, 3 more } 



content: array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

citations: optional array of [TextCitationParam](api/messages.md) or null

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

enabled: optional boolean



DocumentBlockParam object { source, type, cache\_control, 3 more } 



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type }  or [ContentBlockSource](api/messages.md) { content, type }  or 2 more

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



ContentBlockSource object { content, type } 



content: string or array of [ContentBlockSourceContent](api/messages.md)

One of the following:

string



ContentBlockSourceContent = array of [ContentBlockSourceContent](api/messages.md)

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

citations: optional array of [TextCitationParam](api/messages.md) or null

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

ImageBlockParam object { source, type, cache\_control, transformations } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url }  or [FileImageSource](api/messages.md) { file\_id, type } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

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

URLImageSource object { type, url } 

type: "url"

url: string



FileImageSource object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

transformations: optional [ImageTransformationsParam](api/messages.md) { oversized\_image }  or null

Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.



oversized\_image: optional "downsize" or "error"

What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

One of the following:

"downsize"

"error"

type: "content"



URLPDFSource object { type, url } 

type: "url"

url: string



FileDocumentSource object { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

citations: optional [CitationsConfigParam](api/messages.md) { enabled }  or null

enabled: optional boolean

context: optional string or null

title: optional string or null



ToolReferenceBlockParam object { tool\_name, type, cache\_control } 

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

BrowserStateBlockParam object { tabs, type, cache\_control, state\_changes } 

The caller's browser state after a browser toolset member call —
the full inventory of open tabs, which tab is active, and any side
effects (tabs opened, download state changes) the call produced.

At most one per `tool_result`, only on a non-error result answering a
browser toolset member `tool_use`. The server renders the
model-visible text from it; the model never sees the raw fields.



tabs: array of [BrowserStateTabEntry](api/messages.md) { tab\_id, title, url, active } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

state\_changes: optional array of [BrowserStateChange](api/messages.md) or null

Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

maxItems200

minItems1

One of the following:



BrowserStateChangeTabOpened object { tab\_id, type } 

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

BrowserStateChangeDownloadStarted object { download\_id, type, url } 

A file download that started during this call.

download\_id: string

The caller-assigned identifier for this download, stable across the state changes reporting it.

type: "download\_started"

url: string

The final post-redirect URL the download was served from.



BrowserStateChangeDownloadCompleted object { download\_id, type, url, 2 more } 

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

BrowserStateChangeDownloadFailed object { download\_id, type, url, error } 

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

ServerToolUseBlockParam object { id, input, name, 3 more } 

id: string

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

caller: optional [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



WebSearchToolResultBlockParam object { content, tool\_use\_id, type, 2 more } 



content: [WebSearchToolResultBlockParamContent](api/messages.md)

One of the following:



WebSearchToolResultBlockItem = array of [WebSearchResultBlockParam](api/messages.md) { encrypted\_content, title, type, 2 more } 

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string or null



WebSearchToolRequestError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

caller: optional [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



WebFetchToolResultBlockParam object { content, tool\_use\_id, type, 2 more } 



content: [WebFetchToolResultErrorBlockParam](api/messages.md) { error\_code, type }  or [WebFetchBlockParam](api/messages.md) { content, type, url, retrieved\_at } 

One of the following:



WebFetchToolResultErrorBlockParam object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

WebFetchBlockParam object { content, type, url, retrieved\_at } 



content: [DocumentBlockParam](api/messages.md) { source, type, cache\_control, 3 more } 



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type }  or [ContentBlockSource](api/messages.md) { content, type }  or 2 more

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



ContentBlockSource object { content, type } 



content: string or array of [ContentBlockSourceContent](api/messages.md)

One of the following:

string



ContentBlockSourceContent = array of [ContentBlockSourceContent](api/messages.md)

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

citations: optional array of [TextCitationParam](api/messages.md) or null

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

ImageBlockParam object { source, type, cache\_control, transformations } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url }  or [FileImageSource](api/messages.md) { file\_id, type } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

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

URLImageSource object { type, url } 

type: "url"

url: string



FileImageSource object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

transformations: optional [ImageTransformationsParam](api/messages.md) { oversized\_image }  or null

Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.



oversized\_image: optional "downsize" or "error"

What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

One of the following:

"downsize"

"error"

type: "content"



URLPDFSource object { type, url } 

type: "url"

url: string



FileDocumentSource object { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

citations: optional [CitationsConfigParam](api/messages.md) { enabled }  or null

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

caller: optional [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



CodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [CodeExecutionToolResultBlockParamContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultErrorParam object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlockParam object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlockParam object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

BashCodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [BashCodeExecutionToolResultErrorParam](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlockParam](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultErrorParam object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlockParam object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

TextEditorCodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [TextEditorCodeExecutionToolResultErrorParam](api/messages.md) { error\_code, type, error\_message }  or [TextEditorCodeExecutionViewResultBlockParam](api/messages.md) { content, file\_type, type, 3 more }  or [TextEditorCodeExecutionCreateResultBlockParam](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlockParam](api/messages.md) { type, lines, new\_lines, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultErrorParam object { error\_code, type, error\_message } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string or null



TextEditorCodeExecutionViewResultBlockParam object { content, file\_type, type, 3 more } 

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

TextEditorCodeExecutionCreateResultBlockParam object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlockParam object { type, lines, new\_lines, 3 more } 

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string or null

new\_lines: optional number or null

new\_start: optional number or null

old\_lines: optional number or null

old\_start: optional number or null

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

ToolSearchToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [ToolSearchToolResultErrorParam](api/messages.md) { error\_code, type, error\_message }  or [ToolSearchToolSearchResultBlockParam](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultErrorParam object { error\_code, type, error\_message } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

error\_message: optional string or null



ToolSearchToolSearchResultBlockParam object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlockParam](api/messages.md) { tool\_name, type, cache\_control } 

tool\_name: string

type: "tool\_reference"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

ContainerUploadBlockParam object { file\_id, type, cache\_control } 

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

container: optional [MessageCreateParamsContainer](api/messages.md) or null

Container identifier for reuse across requests.

One of the following:



ContainerParams object { id, skills } 

Container parameters with skills to be loaded.

id: optional string or null

Container id



skills: optional array of [SkillParams](api/messages.md) { skill\_id, type, version }  or null

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

inference\_geo: optional string or null

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.



metadata: optional [Metadata](api/messages.md) { user\_id } 

An object describing metadata about the request.



user\_id: optional string or null

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



output\_config: optional [OutputConfig](api/messages.md) { effort, format } 

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

format: optional [JSONOutputFormat](api/messages.md) { schema, type }  or null

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

schema: map[unknown]

The JSON schema of the format

type: "json\_schema"



service\_tier: optional "auto" or "standard\_only"

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](api/service-tiers.md) for details.

One of the following:

"auto"

"standard\_only"

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

system: optional string or array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations } 

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](build-with-claude/prompt-engineering/claude-prompting-best-practices.md).

One of the following:

string



array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

citations: optional array of [TextCitationParam](api/messages.md) or null

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

thinking: optional [ThinkingConfigParam](api/messages.md)

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

One of the following:



ThinkingConfigEnabled object { budget\_tokens, type, display } 

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

ThinkingConfigDisabled object { type } 

type: "disabled"



ThinkingConfigAdaptive object { type, display } 

type: "adaptive"



display: optional "summarized" or "omitted" or null

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"



tool\_choice: optional [ToolChoice](api/messages.md)

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



ToolChoiceAuto object { type, disable\_parallel\_tool\_use } 

The model will automatically decide whether to use tools.

type: "auto"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



ToolChoiceAny object { type, disable\_parallel\_tool\_use } 

The model will use any available tools.

type: "any"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



ToolChoiceTool object { name, type, disable\_parallel\_tool\_use } 

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



ToolChoiceNone object { type } 

The model will not be allowed to use tools.

type: "none"



tools: optional array of [ToolUnion](api/messages.md)

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

Tool object { input\_schema, name, allowed\_callers, 7 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

ToolBash20250124 object { name, type, allowed\_callers, 4 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

CodeExecutionTool20250522 object { name, type, allowed\_callers, 3 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

CodeExecutionTool20250825 object { name, type, allowed\_callers, 3 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

CodeExecutionTool20260120 object { name, type, allowed\_callers, 3 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

CodeExecutionTool20260521 object { name, type, allowed\_callers, 3 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

BrowserToolset20260801 object { type, allowed\_callers, cache\_control, configs } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

configs: optional [BrowserToolsetConfigs](api/messages.md) { close\_tab, double\_click, file\_upload, 28 more }  or null

Per-member configuration for `browser_toolset_20260801`: one
optional field per member tool, keyed by the member name — the same
name the member's `tool_use` blocks carry. Every member is an
accepted key, and a member's defaults apply wherever its key is
absent. Unknown keys are rejected: the field set is this toolset
version's complete member set.



close\_tab: optional [BrowserCloseTabConfig](api/messages.md) { defer\_loading, enabled }  or null

`close_tab`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



double\_click: optional [BrowserDoubleClickConfig](api/messages.md) { defer\_loading, enabled }  or null

`double_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



file\_upload: optional [BrowserFileUploadConfig](api/messages.md) { defer\_loading, enabled }  or null

`file_upload`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



find: optional [BrowserFindConfig](api/messages.md) { defer\_loading, enabled }  or null

`find`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



form\_input: optional [BrowserFormInputConfig](api/messages.md) { defer\_loading, enabled }  or null

`form_input`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



get\_page\_text: optional [BrowserGetPageTextConfig](api/messages.md) { defer\_loading, enabled }  or null

`get_page_text`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



hold\_key: optional [BrowserHoldKeyConfig](api/messages.md) { defer\_loading, enabled }  or null

`hold_key`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



hover: optional [BrowserHoverConfig](api/messages.md) { defer\_loading, enabled }  or null

`hover`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



javascript\_exec: optional [BrowserJavascriptExecConfig](api/messages.md) { defer\_loading, enabled }  or null

`javascript_exec`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



key: optional [BrowserKeyConfig](api/messages.md) { defer\_loading, enabled }  or null

`key`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



left\_click: optional [BrowserLeftClickConfig](api/messages.md) { defer\_loading, enabled }  or null

`left_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



left\_click\_drag: optional [BrowserLeftClickDragConfig](api/messages.md) { defer\_loading, enabled }  or null

`left_click_drag`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



left\_mouse\_down: optional [BrowserLeftMouseDownConfig](api/messages.md) { defer\_loading, enabled }  or null

`left_mouse_down`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



left\_mouse\_up: optional [BrowserLeftMouseUpConfig](api/messages.md) { defer\_loading, enabled }  or null

`left_mouse_up`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



list\_tabs: optional [BrowserListTabsConfig](api/messages.md) { defer\_loading, enabled }  or null

`list_tabs`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



middle\_click: optional [BrowserMiddleClickConfig](api/messages.md) { defer\_loading, enabled }  or null

`middle_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



mouse\_move: optional [BrowserMouseMoveConfig](api/messages.md) { defer\_loading, enabled }  or null

`mouse_move`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



navigate: optional [BrowserNavigateConfig](api/messages.md) { defer\_loading, enabled }  or null

`navigate`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



new\_tab: optional [BrowserNewTabConfig](api/messages.md) { defer\_loading, enabled }  or null

`new_tab`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



read\_console: optional [BrowserReadConsoleConfig](api/messages.md) { defer\_loading, enabled }  or null

`read_console`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



read\_network: optional [BrowserReadNetworkConfig](api/messages.md) { defer\_loading, enabled }  or null

`read_network`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



read\_page: optional [BrowserReadPageConfig](api/messages.md) { defer\_loading, enabled }  or null

`read_page`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



right\_click: optional [BrowserRightClickConfig](api/messages.md) { defer\_loading, enabled }  or null

`right_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



screenshot: optional [BrowserScreenshotConfig](api/messages.md) { defer\_loading, enabled }  or null

`screenshot`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



scroll: optional [BrowserScrollConfig](api/messages.md) { defer\_loading, enabled }  or null

`scroll`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



scroll\_to: optional [BrowserScrollToConfig](api/messages.md) { defer\_loading, enabled }  or null

`scroll_to`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



switch\_tab: optional [BrowserSwitchTabConfig](api/messages.md) { defer\_loading, enabled }  or null

`switch_tab`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



triple\_click: optional [BrowserTripleClickConfig](api/messages.md) { defer\_loading, enabled }  or null

`triple_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



type: optional [BrowserTypeConfig](api/messages.md) { defer\_loading, enabled }  or null

`type`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



wait: optional [BrowserWaitConfig](api/messages.md) { defer\_loading, enabled }  or null

`wait`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



zoom: optional [BrowserZoomConfig](api/messages.md) { defer\_loading, enabled }  or null

`zoom`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



MemoryTool20250818 object { name, type, allowed\_callers, 4 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

ComputerToolset20260801 object { type, allowed\_callers, cache\_control, configs } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

configs: optional [ComputerToolsetConfigs](api/messages.md) { cursor\_position, double\_click, hold\_key, 14 more }  or null

Per-member configuration for `computer_toolset_20260801`: one
optional field per member tool, keyed by the member name — the same
name the member's `tool_use` blocks carry. Every member is an
accepted key, and a member's defaults apply wherever its key is
absent. Unknown keys are rejected: the field set is this toolset
version's complete member set.



cursor\_position: optional [ComputerCursorPositionConfig](api/messages.md) { defer\_loading, enabled }  or null

`cursor_position`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



double\_click: optional [ComputerDoubleClickConfig](api/messages.md) { defer\_loading, enabled }  or null

`double_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



hold\_key: optional [ComputerHoldKeyConfig](api/messages.md) { defer\_loading, enabled }  or null

`hold_key`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



key: optional [ComputerKeyConfig](api/messages.md) { defer\_loading, enabled }  or null

`key`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



left\_click: optional [ComputerLeftClickConfig](api/messages.md) { defer\_loading, enabled }  or null

`left_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



left\_click\_drag: optional [ComputerLeftClickDragConfig](api/messages.md) { defer\_loading, enabled }  or null

`left_click_drag`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



left\_mouse\_down: optional [ComputerLeftMouseDownConfig](api/messages.md) { defer\_loading, enabled }  or null

`left_mouse_down`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



left\_mouse\_up: optional [ComputerLeftMouseUpConfig](api/messages.md) { defer\_loading, enabled }  or null

`left_mouse_up`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



middle\_click: optional [ComputerMiddleClickConfig](api/messages.md) { defer\_loading, enabled }  or null

`middle_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



mouse\_move: optional [ComputerMouseMoveConfig](api/messages.md) { defer\_loading, enabled }  or null

`mouse_move`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



right\_click: optional [ComputerRightClickConfig](api/messages.md) { defer\_loading, enabled }  or null

`right_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



screenshot: optional [ComputerScreenshotConfig](api/messages.md) { defer\_loading, enabled }  or null

`screenshot`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



scroll: optional [ComputerScrollConfig](api/messages.md) { defer\_loading, enabled }  or null

`scroll`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



triple\_click: optional [ComputerTripleClickConfig](api/messages.md) { defer\_loading, enabled }  or null

`triple_click`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



type: optional [ComputerTypeConfig](api/messages.md) { defer\_loading, enabled }  or null

`type`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



wait: optional [ComputerWaitConfig](api/messages.md) { defer\_loading, enabled }  or null

`wait`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



zoom: optional [ComputerZoomConfig](api/messages.md) { defer\_loading, enabled }  or null

`zoom`'s config overrides.

defer\_loading: optional boolean or null

Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null

Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



ToolTextEditor20250124 object { name, type, allowed\_callers, 4 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

ToolTextEditor20250429 object { name, type, allowed\_callers, 4 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

ToolTextEditor20250728 object { name, type, allowed\_callers, 5 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

WebSearchTool20250305 object { name, type, allowed\_callers, 7 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

user\_location: optional [UserLocation](api/messages.md) { type, city, country, 2 more }  or null

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

WebFetchTool20250910 object { name, type, allowed\_callers, 8 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

citations: optional [CitationsConfigParam](api/messages.md) { enabled }  or null

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

WebSearchTool20260209 object { name, type, allowed\_callers, 7 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

user\_location: optional [UserLocation](api/messages.md) { type, city, country, 2 more }  or null

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

WebFetchTool20260209 object { name, type, allowed\_callers, 8 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

citations: optional [CitationsConfigParam](api/messages.md) { enabled }  or null

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

WebFetchTool20260309 object { name, type, allowed\_callers, 9 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

citations: optional [CitationsConfigParam](api/messages.md) { enabled }  or null

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

WebSearchTool20260318 object { name, type, allowed\_callers, 8 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

user\_location: optional [UserLocation](api/messages.md) { type, city, country, 2 more }  or null

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

WebFetchTool20260318 object { name, type, allowed\_callers, 10 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

citations: optional [CitationsConfigParam](api/messages.md) { enabled }  or null

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

ToolSearchToolBm25\_20251119 object { name, type, allowed\_callers, 3 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

ToolSearchToolRegex20251119 object { name, type, allowed\_callers, 3 more } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl }  or null

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

Message object { id, container, content, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: [Container](api/messages.md) { id, expires\_at, skills }  or null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



skills: array of [ContainerSkill](api/messages.md) { skill\_id, type, version }  or null

Skills loaded in the container

skill\_id: string

Skill ID



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: string

The resolved version: a skill version ID for custom skills.



content: array of [ContentBlock](api/messages.md)

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

TextBlock object { citations, text, type } 



citations: array of [TextCitation](api/messages.md) or null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

file\_id: string or null

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

file\_id: string or null

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

file\_id: string or null

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

text: string

type: "text"



ThinkingBlock object { signature, thinking, type } 



signature: string

A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

thinking: string

The text of Claude's thinking process for this block.

type: "thinking"



RedactedThinkingBlock object { data, type } 



data: string

The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

type: "redacted\_thinking"



ToolUseBlock object { id, caller, input, 3 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"

toolset\_name: optional string or null

For a toolset member tool\_use, the toolset family.



ServerToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



WebSearchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



WebSearchToolResultError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string or null

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



WebFetchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  or [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



WebFetchToolResultErrorBlock object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

WebFetchBlock object { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled }  or null

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string or null

The title of the document

type: "document"

retrieved\_at: string or null

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



CodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultError object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BashCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultError object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



TextEditorCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultError object { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string or null

type: "text\_editor\_code\_execution\_tool\_result\_error"



TextEditorCodeExecutionViewResultBlock object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number or null

start\_line: number or null

total\_lines: number or null

type: "text\_editor\_code\_execution\_view\_result"



TextEditorCodeExecutionCreateResultBlock object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new\_lines, new\_start, 3 more } 

lines: array of string or null

new\_lines: number or null

new\_start: number or null

old\_lines: number or null

old\_start: number or null

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



ToolSearchToolResultBlock object { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultError object { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string or null

type: "tool\_search\_tool\_result\_error"



ToolSearchToolSearchResultBlock object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlock](api/messages.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



ContainerUploadBlock object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

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

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type }  or null

Structured information about a refusal.



category: "cyber" or "bio" or "frontier\_llm" or 2 more or null

The policy category that triggered a refusal.

One of the following:

"cyber"

The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

"bio"

The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

"frontier\_llm"

The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

"reasoning\_extraction"

The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](build-with-claude/adaptive-thinking.md).

"general\_harms"

The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.



explanation: string or null

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



stop\_reason: [StopReason](api/messages.md) or null

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations
- `"model_context_window_exceeded"`: we exceeded the model's context window

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

"model\_context\_window\_exceeded"



stop\_sequence: string or null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 6 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  or null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number or null

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number or null

The number of input tokens read from the cache.

inference\_geo: string or null

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens }  or null

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

server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests }  or null

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch" or null

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"



RawMessageStreamEvent = [RawMessageStartEvent](api/messages.md) { message, type }  or [RawMessageDeltaEvent](api/messages.md) { delta, type, usage }  or [RawMessageStopEvent](api/messages.md) { type }  or 3 more

One of the following:



RawMessageStartEvent object { message, type } 



message: [Message](api/messages.md) { id, container, content, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: [Container](api/messages.md) { id, expires\_at, skills }  or null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



skills: array of [ContainerSkill](api/messages.md) { skill\_id, type, version }  or null

Skills loaded in the container

skill\_id: string

Skill ID



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: string

The resolved version: a skill version ID for custom skills.



content: array of [ContentBlock](api/messages.md)

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

TextBlock object { citations, text, type } 



citations: array of [TextCitation](api/messages.md) or null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

file\_id: string or null

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

file\_id: string or null

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

file\_id: string or null

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

text: string

type: "text"



ThinkingBlock object { signature, thinking, type } 



signature: string

A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

thinking: string

The text of Claude's thinking process for this block.

type: "thinking"



RedactedThinkingBlock object { data, type } 



data: string

The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

type: "redacted\_thinking"



ToolUseBlock object { id, caller, input, 3 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"

toolset\_name: optional string or null

For a toolset member tool\_use, the toolset family.



ServerToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



WebSearchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



WebSearchToolResultError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string or null

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



WebFetchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  or [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



WebFetchToolResultErrorBlock object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

WebFetchBlock object { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled }  or null

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string or null

The title of the document

type: "document"

retrieved\_at: string or null

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



CodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultError object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BashCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultError object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



TextEditorCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultError object { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string or null

type: "text\_editor\_code\_execution\_tool\_result\_error"



TextEditorCodeExecutionViewResultBlock object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number or null

start\_line: number or null

total\_lines: number or null

type: "text\_editor\_code\_execution\_view\_result"



TextEditorCodeExecutionCreateResultBlock object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new\_lines, new\_start, 3 more } 

lines: array of string or null

new\_lines: number or null

new\_start: number or null

old\_lines: number or null

old\_start: number or null

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



ToolSearchToolResultBlock object { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultError object { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string or null

type: "tool\_search\_tool\_result\_error"



ToolSearchToolSearchResultBlock object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlock](api/messages.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



ContainerUploadBlock object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

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

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type }  or null

Structured information about a refusal.



category: "cyber" or "bio" or "frontier\_llm" or 2 more or null

The policy category that triggered a refusal.

One of the following:

"cyber"

The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

"bio"

The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

"frontier\_llm"

The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

"reasoning\_extraction"

The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](build-with-claude/adaptive-thinking.md).

"general\_harms"

The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.



explanation: string or null

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



stop\_reason: [StopReason](api/messages.md) or null

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations
- `"model_context_window_exceeded"`: we exceeded the model's context window

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

"model\_context\_window\_exceeded"



stop\_sequence: string or null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 6 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  or null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number or null

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number or null

The number of input tokens read from the cache.

inference\_geo: string or null

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens }  or null

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

server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests }  or null

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch" or null

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"

type: "message\_start"



RawMessageDeltaEvent object { delta, type, usage } 



delta: object { container, stop\_details, stop\_reason, stop\_sequence } 



container: [Container](api/messages.md) { id, expires\_at, skills }  or null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



skills: array of [ContainerSkill](api/messages.md) { skill\_id, type, version }  or null

Skills loaded in the container

skill\_id: string

Skill ID



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: string

The resolved version: a skill version ID for custom skills.



stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type }  or null

Structured information about a refusal.



category: "cyber" or "bio" or "frontier\_llm" or 2 more or null

The policy category that triggered a refusal.

One of the following:

"cyber"

The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

"bio"

The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

"frontier\_llm"

The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

"reasoning\_extraction"

The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](build-with-claude/adaptive-thinking.md).

"general\_harms"

The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.



explanation: string or null

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



stop\_reason: [StopReason](api/messages.md) or null

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string or null

type: "message\_delta"



usage: [MessageDeltaUsage](api/messages.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 3 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: number or null

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number or null

The cumulative number of input tokens read from the cache.

input\_tokens: number or null

The cumulative number of input tokens which were used.

output\_tokens: number

The cumulative number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens }  or null

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

server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests }  or null

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



RawMessageStopEvent object { type } 

type: "message\_stop"



RawContentBlockStartEvent object { content\_block, index, type } 



content\_block: [TextBlock](api/messages.md) { citations, text, type }  or [ThinkingBlock](api/messages.md) { signature, thinking, type }  or [RedactedThinkingBlock](api/messages.md) { data, type }  or 9 more

Response model for a file uploaded to the container.

One of the following:



TextBlock object { citations, text, type } 



citations: array of [TextCitation](api/messages.md) or null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

file\_id: string or null

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

file\_id: string or null

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

file\_id: string or null

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

text: string

type: "text"



ThinkingBlock object { signature, thinking, type } 



signature: string

A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

thinking: string

The text of Claude's thinking process for this block.

type: "thinking"



RedactedThinkingBlock object { data, type } 



data: string

The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

type: "redacted\_thinking"



ToolUseBlock object { id, caller, input, 3 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"

toolset\_name: optional string or null

For a toolset member tool\_use, the toolset family.



ServerToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



WebSearchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



WebSearchToolResultError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string or null

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



WebFetchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  or [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



WebFetchToolResultErrorBlock object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

WebFetchBlock object { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled }  or null

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string or null

The title of the document

type: "document"

retrieved\_at: string or null

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



CodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultError object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BashCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultError object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



TextEditorCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultError object { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string or null

type: "text\_editor\_code\_execution\_tool\_result\_error"



TextEditorCodeExecutionViewResultBlock object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number or null

start\_line: number or null

total\_lines: number or null

type: "text\_editor\_code\_execution\_view\_result"



TextEditorCodeExecutionCreateResultBlock object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new\_lines, new\_start, 3 more } 

lines: array of string or null

new\_lines: number or null

new\_start: number or null

old\_lines: number or null

old\_start: number or null

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



ToolSearchToolResultBlock object { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultError object { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string or null

type: "tool\_search\_tool\_result\_error"



ToolSearchToolSearchResultBlock object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlock](api/messages.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



ContainerUploadBlock object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

index: number

type: "content\_block\_start"



RawContentBlockDeltaEvent object { delta, index, type } 



delta: [RawContentBlockDelta](api/messages.md)

One of the following:



TextDelta object { text, type } 

text: string

type: "text\_delta"



InputJSONDelta object { partial\_json, type } 

partial\_json: string

type: "input\_json\_delta"



CitationsDelta object { citation, type } 



citation: [CitationCharLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or [CitationPageLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or [CitationContentBlockLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or 2 more

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_char\_index: number

file\_id: string or null

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string or null

end\_page\_number: number

file\_id: string or null

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

file\_id: string or null

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string or null

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

type: "citations\_delta"



ThinkingDelta object { thinking, type } 

thinking: string

The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

type: "thinking\_delta"



SignatureDelta object { signature, type } 

signature: string

The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

type: "signature\_delta"

index: number

type: "content\_block\_delta"



RawContentBlockStopEvent object { index, type } 

index: number

type: "content\_block\_stop"

Create a Message

cURL

```shiki
curl https://api.anthropic.com/v1/messages \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    --max-time 600 \
    -d '{
          "max_tokens": 1024,
          "messages": [
            {
              "content": "Hello, world",
              "role": "user"
            }
          ],
          "model": "claude-opus-5",
          "stream": false,
          "system": [
            {
              "text": "Today'\''s date is 2024-06-01.",
              "type": "text"
            }
          ],
          "temperature": 1,
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
          ],
          "top_k": 5,
          "top_p": 0.7
        }'
```

Response 200



```shiki
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "container_011CpZohnwH4vuy7gazohgSP",
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
          "cited_text": "The grass is green. The sky is blue.",
          "document_index": 0,
          "document_title": "My Document",
          "end_char_index": 0,
          "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
          "start_char_index": 0,
          "type": "char_location"
        }
      ],
      "text": "Hi! My name is Claude.",
      "type": "text"
    }
  ],
  "model": "claude-opus-5",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "This request was declined because it conflicts with Anthropic's Usage Policy.",
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
    "inference_geo": "global",
    "input_tokens": 2095,
    "output_tokens": 503,
    "output_tokens_details": {
      "thinking_tokens": 0
    },
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    },
    "service_tier": "standard"
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
    "id": "container_011CpZohnwH4vuy7gazohgSP",
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
          "cited_text": "The grass is green. The sky is blue.",
          "document_index": 0,
          "document_title": "My Document",
          "end_char_index": 0,
          "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
          "start_char_index": 0,
          "type": "char_location"
        }
      ],
      "text": "Hi! My name is Claude.",
      "type": "text"
    }
  ],
  "model": "claude-opus-5",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "This request was declined because it conflicts with Anthropic's Usage Policy.",
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
    "inference_geo": "global",
    "input_tokens": 2095,
    "output_tokens": 503,
    "output_tokens_details": {
      "thinking_tokens": 0
    },
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    },
    "service_tier": "standard"
  }
}
```

---

*Copyright © Anthropic. All rights reserved.*
