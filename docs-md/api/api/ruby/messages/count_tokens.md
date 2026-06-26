# Count tokens in a Message

Copy page



Ruby

# Count tokens in a Message

messages.count\_tokens(\*\*kwargs) -> [MessageTokensCount](api/messages.md) { input\_tokens }

POST/v1/messages/count\_tokens

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

##### ParametersExpand Collapse



messages: Array[[MessageParam](api/messages.md) { content, role } ]

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

See [input examples](https://docs.claude.com/en/api/messages-examples).

Note that if you want to include a [system prompt](https://docs.claude.com/en/docs/system-prompts), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

There is a limit of 100,000 messages in a single request.



content: String | Array[[ContentBlockParam](api/messages.md)]

One of the following:

String = String



UnionMember1 = Array[[ContentBlockParam](api/messages.md)]

One of the following:



class TextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[TextCitationParam](api/messages.md)]

One of the following:



class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class ImageBlockParam { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url } 

One of the following:



class Base64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class URLImageSource { type, url } 

type: :url

url: String

type: :image



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class DocumentBlockParam { source, type, cache\_control, 3 more } 



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type }  | [ContentBlockSource](api/messages.md) { content, type }  | [URLPDFSource](api/messages.md) { type, url } 

One of the following:



class Base64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class PlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text



class ContentBlockSource { content, type } 



content: String | Array[[ContentBlockSourceContent](api/messages.md)]

One of the following:

String = String



ContentBlockSourceContent = Array[[ContentBlockSourceContent](api/messages.md)]

One of the following:



class TextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[TextCitationParam](api/messages.md)]

One of the following:



class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class ImageBlockParam { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url } 

One of the following:



class Base64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class URLImageSource { type, url } 

type: :url

url: String

type: :image



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :content



class URLPDFSource { type, url } 

type: :url

url: String

type: :document



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [CitationsConfigParam](api/messages.md) { enabled } 

enabled: bool

context: String

title: String



class SearchResultBlockParam { content, source, title, 3 more } 



content: Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations } ]

text: String

type: :text



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[TextCitationParam](api/messages.md)]

One of the following:



class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

source: String

title: String

type: :search\_result



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [CitationsConfigParam](api/messages.md) { enabled } 

enabled: bool



class ThinkingBlockParam { signature, thinking, type } 

signature: String

thinking: String

type: :thinking



class RedactedThinkingBlockParam { data, type } 

data: String

type: :redacted\_thinking



class ToolUseBlockParam { id, input, name, 3 more } 

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class DirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class ServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class ToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: String

type: :tool\_result



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



content: String | Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  | [ImageBlockParam](api/messages.md) { source, type, cache\_control }  | [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  | 2 more]

One of the following:

String = String



Content = Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  | [ImageBlockParam](api/messages.md) { source, type, cache\_control }  | [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  | 2 more]

One of the following:



class TextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[TextCitationParam](api/messages.md)]

One of the following:



class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class ImageBlockParam { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url } 

One of the following:



class Base64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class URLImageSource { type, url } 

type: :url

url: String

type: :image



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class SearchResultBlockParam { content, source, title, 3 more } 



content: Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations } ]

text: String

type: :text



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[TextCitationParam](api/messages.md)]

One of the following:



class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

source: String

title: String

type: :search\_result



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [CitationsConfigParam](api/messages.md) { enabled } 

enabled: bool



class DocumentBlockParam { source, type, cache\_control, 3 more } 



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type }  | [ContentBlockSource](api/messages.md) { content, type }  | [URLPDFSource](api/messages.md) { type, url } 

One of the following:



class Base64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class PlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text



class ContentBlockSource { content, type } 



content: String | Array[[ContentBlockSourceContent](api/messages.md)]

One of the following:

String = String



ContentBlockSourceContent = Array[[ContentBlockSourceContent](api/messages.md)]

One of the following:



class TextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[TextCitationParam](api/messages.md)]

One of the following:



class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class ImageBlockParam { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url } 

One of the following:



class Base64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class URLImageSource { type, url } 

type: :url

url: String

type: :image



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :content



class URLPDFSource { type, url } 

type: :url

url: String

type: :document



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [CitationsConfigParam](api/messages.md) { enabled } 

enabled: bool

context: String

title: String



class ToolReferenceBlockParam { tool\_name, type, cache\_control } 

Tool reference block that can be included in tool\_result content.

tool\_name: String

type: :tool\_reference



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

is\_error: bool



class ServerToolUseBlockParam { id, input, name, 3 more } 

id: String

input: Hash[Symbol, untyped]



name: :web\_search | :web\_fetch | :code\_execution | 4 more

One of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class DirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class ServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class WebSearchToolResultBlockParam { content, tool\_use\_id, type, 2 more } 



content: [WebSearchToolResultBlockParamContent](api/messages.md)

One of the following:



WebSearchToolResultBlockItem = Array[[WebSearchResultBlockParam](api/messages.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

url: String

page\_age: String



class WebSearchToolRequestError { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

tool\_use\_id: String

type: :web\_search\_tool\_result



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class DirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class ServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class WebFetchToolResultBlockParam { content, tool\_use\_id, type, 2 more } 



content: [WebFetchToolResultErrorBlockParam](api/messages.md) { error\_code, type }  | [WebFetchBlockParam](api/messages.md) { content, type, url, retrieved\_at } 

One of the following:



class WebFetchToolResultErrorBlockParam { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class WebFetchBlockParam { content, type, url, retrieved\_at } 



content: [DocumentBlockParam](api/messages.md) { source, type, cache\_control, 3 more } 



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type }  | [ContentBlockSource](api/messages.md) { content, type }  | [URLPDFSource](api/messages.md) { type, url } 

One of the following:



class Base64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class PlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text



class ContentBlockSource { content, type } 



content: String | Array[[ContentBlockSourceContent](api/messages.md)]

One of the following:

String = String



ContentBlockSourceContent = Array[[ContentBlockSourceContent](api/messages.md)]

One of the following:



class TextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[TextCitationParam](api/messages.md)]

One of the following:



class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class ImageBlockParam { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url } 

One of the following:



class Base64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class URLImageSource { type, url } 

type: :url

url: String

type: :image



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :content



class URLPDFSource { type, url } 

type: :url

url: String

type: :document



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [CitationsConfigParam](api/messages.md) { enabled } 

enabled: bool

context: String

title: String

type: :web\_fetch\_result

url: String

Fetched content URL

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: String

type: :web\_fetch\_tool\_result



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class DirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class ServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class CodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [CodeExecutionToolResultBlockParamContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultErrorParam { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class CodeExecutionResultBlockParam { content, return\_code, stderr, 2 more } 



content: Array[[CodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class EncryptedCodeExecutionResultBlockParam { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[CodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BashCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BashCodeExecutionToolResultErrorParam](api/messages.md) { error\_code, type }  | [BashCodeExecutionResultBlockParam](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



class BashCodeExecutionToolResultErrorParam { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BashCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more } 



content: Array[[BashCodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class TextEditorCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [TextEditorCodeExecutionToolResultErrorParam](api/messages.md) { error\_code, type, error\_message }  | [TextEditorCodeExecutionViewResultBlockParam](api/messages.md) { content, file\_type, type, 3 more }  | [TextEditorCodeExecutionCreateResultBlockParam](api/messages.md) { is\_file\_update, type }  | [TextEditorCodeExecutionStrReplaceResultBlockParam](api/messages.md) { type, lines, new\_lines, 3 more } 

One of the following:



class TextEditorCodeExecutionToolResultErrorParam { error\_code, type, error\_message } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

type: :text\_editor\_code\_execution\_tool\_result\_error

error\_message: String



class TextEditorCodeExecutionViewResultBlockParam { content, file\_type, type, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

type: :text\_editor\_code\_execution\_view\_result

num\_lines: Integer

start\_line: Integer

total\_lines: Integer



class TextEditorCodeExecutionCreateResultBlockParam { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class TextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new\_lines, 3 more } 

type: :text\_editor\_code\_execution\_str\_replace\_result

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class ToolSearchToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [ToolSearchToolResultErrorParam](api/messages.md) { error\_code, type, error\_message }  | [ToolSearchToolSearchResultBlockParam](api/messages.md) { tool\_references, type } 

One of the following:



class ToolSearchToolResultErrorParam { error\_code, type, error\_message } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :tool\_search\_tool\_result\_error

error\_message: String



class ToolSearchToolSearchResultBlockParam { tool\_references, type } 



tool\_references: Array[[ToolReferenceBlockParam](api/messages.md) { tool\_name, type, cache\_control } ]

tool\_name: String

type: :tool\_reference



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class ContainerUploadBlockParam { file\_id, type, cache\_control } 

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: String

type: :container\_upload



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class MidConversationSystemBlockParam { content, type, cache\_control } 

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



content: Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations } ]

System instruction text blocks.

text: String

type: :text



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[TextCitationParam](api/messages.md)]

One of the following:



class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

type: :mid\_conv\_system



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



role: :user | :assistant | :system

One of the following:

:user

:assistant

:system



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Top-level cache control automatically applies a cache\_control marker to the last cacheable block in the request.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



output\_config: [OutputConfig](api/messages.md) { effort, format\_ } 

Configuration options for the model's output, such as the output format.



effort: :low | :medium | :high | 2 more

All possible effort levels.

One of the following:

:low

:medium

:high

:xhigh

:max



format\_: [JSONOutputFormat](api/messages.md) { schema, type } 

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

schema: Hash[Symbol, untyped]

The JSON schema of the format

type: :json\_schema



system\_: String | Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations } ]

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

One of the following:

String = String



UnionMember1 = Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations } ]

text: String

type: :text



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[TextCitationParam](api/messages.md)]

One of the following:



class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



thinking: [ThinkingConfigParam](api/messages.md)

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

One of the following:



class ThinkingConfigEnabled { budget\_tokens, type, display\_ } 



budget\_tokens: Integer

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: :enabled



display\_: :summarized | :omitted

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

:summarized

:omitted



class ThinkingConfigDisabled { type } 

type: :disabled



class ThinkingConfigAdaptive { type, display\_ } 

type: :adaptive



display\_: :summarized | :omitted

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

:summarized

:omitted



tool\_choice: [ToolChoice](api/messages.md)

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



class ToolChoiceAuto { type, disable\_parallel\_tool\_use } 

The model will automatically decide whether to use tools.

type: :auto



disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



class ToolChoiceAny { type, disable\_parallel\_tool\_use } 

The model will use any available tools.

type: :any



disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class ToolChoiceTool { name, type, disable\_parallel\_tool\_use } 

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: :tool



disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class ToolChoiceNone { type } 

The model will not be allowed to use tools.

type: :none



tools: Array[[MessageCountTokensTool](api/messages.md)]

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

See our [guide](https://docs.claude.com/en/docs/tool-use) for more details.

One of the following:



class Tool { input\_schema, name, allowed\_callers, 7 more } 



input\_schema: InputSchema{ type, properties, required}

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: :object

properties: Hash[Symbol, untyped]

required: Array[String]



name: String

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



description: String

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: bool

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

type: :custom



class ToolBash20250124 { name, type, allowed\_callers, 4 more } 



name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :bash\_20250124



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20250522 { name, type, allowed\_callers, 3 more } 



name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20250522



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20250825 { name, type, allowed\_callers, 3 more } 



name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20250825



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20260120 { name, type, allowed\_callers, 3 more } 

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20260120



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20260521 { name, type, allowed\_callers, 3 more } 

Code execution tool with REPL state persistence.



name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20260521



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs



class MemoryTool20250818 { name, type, allowed\_callers, 4 more } 



name: :memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :memory\_20250818



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class ToolTextEditor20250124 { name, type, allowed\_callers, 4 more } 



name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250124



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class ToolTextEditor20250429 { name, type, allowed\_callers, 4 more } 



name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250429



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class ToolTextEditor20250728 { name, type, allowed\_callers, 5 more } 



name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250728



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

max\_characters: Integer

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: bool

When true, guarantees schema validation on tool names and inputs



class WebSearchTool20250305 { name, type, allowed\_callers, 7 more } 



name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_search\_20250305



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs



user\_location: [UserLocation](api/messages.md) { type, city, country, 2 more } 

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

city: String

The city of the user.

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: String

The region of the user.

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class WebFetchTool20250910 { name, type, allowed\_callers, 8 more } 



name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20250910



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [CitationsConfigParam](api/messages.md) { enabled } 

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs



class WebSearchTool20260209 { name, type, allowed\_callers, 7 more } 



name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_search\_20260209



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs



user\_location: [UserLocation](api/messages.md) { type, city, country, 2 more } 

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

city: String

The city of the user.

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: String

The region of the user.

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class WebFetchTool20260209 { name, type, allowed\_callers, 8 more } 



name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20260209



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [CitationsConfigParam](api/messages.md) { enabled } 

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs



class WebFetchTool20260309 { name, type, allowed\_callers, 9 more } 

Web fetch tool with use\_cache parameter for bypassing cached content.



name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20260309



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [CitationsConfigParam](api/messages.md) { enabled } 

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

use\_cache: bool

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class ToolSearchToolBm25\_20251119 { name, type, allowed\_callers, 3 more } 



name: :tool\_search\_tool\_bm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: :tool\_search\_tool\_bm25\_20251119 | :tool\_search\_tool\_bm25

One of the following:

:tool\_search\_tool\_bm25\_20251119

:tool\_search\_tool\_bm25



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs



class ToolSearchToolRegex20251119 { name, type, allowed\_callers, 3 more } 



name: :tool\_search\_tool\_regex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: :tool\_search\_tool\_regex\_20251119 | :tool\_search\_tool\_regex

One of the following:

:tool\_search\_tool\_regex\_20251119

:tool\_search\_tool\_regex



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

##### ReturnsExpand Collapse



class MessageTokensCount { input\_tokens } 

input\_tokens: Integer

The total number of tokens across the provided list of messages, system prompt, and tools.

Count tokens in a Message

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

message_tokens_count = anthropic.messages.count_tokens(
  messages: [{content: "Hello, world", role: :user}],
  model: :"claude-opus-4-6"
)

puts(message_tokens_count)
```

Response 200



```shiki
{
  "input_tokens": 2095
}
```

##### Returns Examples

Response 200



```shiki
{
  "input_tokens": 2095
}
```

---

*Copyright © Anthropic. All rights reserved.*
