# Create a Message

Copy page

Ruby

# Create a Message

messages.create(\*\*kwargs) -> [Message](api/messages.md) { id, container, content, 7 more }

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)

##### ParametersExpand Collapse

max\_tokens: Integer

The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Set to `0` to populate the [prompt cache](https://docs.claude.com/en/docs/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.

minimum0

messages: Array[[MessageParam](api/messages.md) { content, role } ]

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

content: String | Array[[ContentBlockParam](api/messages.md)]

Accepts one of the following:

String

Array[[ContentBlockParam](api/messages.md)]

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class URLImageSource { type, url }

type: :url

url: String

type: :image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class DocumentBlockParam { source, type, cache\_control, 3 more }

source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type }  | [ContentBlockSource](api/messages.md) { content, type }  | [URLPDFSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class PlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

class ContentBlockSource { content, type }

content: String | Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

String

Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class URLImageSource { type, url }

type: :url

url: String

type: :image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

class URLPDFSource { type, url }

type: :url

url: String

type: :document

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

enabled: bool

context: String

title: String

class SearchResultBlockParam { content, source, title, 3 more }

content: Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations } ]

text: String

type: :text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

source: String

title: String

type: :search\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

enabled: bool

class ThinkingBlockParam { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class RedactedThinkingBlockParam { data, type }

data: String

type: :redacted\_thinking

class ToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class ServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class ToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: String

type: :tool\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

content: String | Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  | [ImageBlockParam](api/messages.md) { source, type, cache\_control }  | [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  | 2 more]

Accepts one of the following:

String

Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  | [ImageBlockParam](api/messages.md) { source, type, cache\_control }  | [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  | 2 more]

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class URLImageSource { type, url }

type: :url

url: String

type: :image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class SearchResultBlockParam { content, source, title, 3 more }

content: Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations } ]

text: String

type: :text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

source: String

title: String

type: :search\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

enabled: bool

class DocumentBlockParam { source, type, cache\_control, 3 more }

source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type }  | [ContentBlockSource](api/messages.md) { content, type }  | [URLPDFSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class PlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

class ContentBlockSource { content, type }

content: String | Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

String

Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class URLImageSource { type, url }

type: :url

url: String

type: :image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

class URLPDFSource { type, url }

type: :url

url: String

type: :document

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

enabled: bool

context: String

title: String

class ToolReferenceBlockParam { tool\_name, type, cache\_control }

Tool reference block that can be included in tool\_result content.

tool\_name: String

type: :tool\_reference

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

is\_error: bool

class ServerToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash[Symbol, untyped]

name: :web\_search | :web\_fetch | :code\_execution | 4 more

Accepts one of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class ServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class WebSearchToolResultBlockParam { content, tool\_use\_id, type, 2 more }

content: [WebSearchToolResultBlockParamContent](api/messages.md)

Accepts one of the following:

Array[[WebSearchResultBlockParam](api/messages.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

url: String

page\_age: String

class WebSearchToolRequestError { error\_code, type }

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

tool\_use\_id: String

type: :web\_search\_tool\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class ServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class WebFetchToolResultBlockParam { content, tool\_use\_id, type, 2 more }

content: [WebFetchToolResultErrorBlockParam](api/messages.md) { error\_code, type }  | [WebFetchBlockParam](api/messages.md) { content, type, url, retrieved\_at }

Accepts one of the following:

class WebFetchToolResultErrorBlockParam { error\_code, type }

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class WebFetchBlockParam { content, type, url, retrieved\_at }

content: [DocumentBlockParam](api/messages.md) { source, type, cache\_control, 3 more }

source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type }  | [ContentBlockSource](api/messages.md) { content, type }  | [URLPDFSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class PlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

class ContentBlockSource { content, type }

content: String | Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

String

Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class URLImageSource { type, url }

type: :url

url: String

type: :image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

class URLPDFSource { type, url }

type: :url

url: String

type: :document

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

enabled: bool

context: String

title: String

type: :web\_fetch\_result

url: String

Fetched content URL

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: String

type: :web\_fetch\_tool\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class ServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class CodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [CodeExecutionToolResultBlockParamContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultErrorParam { error\_code, type }

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class CodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[CodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class EncryptedCodeExecutionResultBlockParam { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[CodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BashCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BashCodeExecutionToolResultErrorParam](api/messages.md) { error\_code, type }  | [BashCodeExecutionResultBlockParam](api/messages.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BashCodeExecutionToolResultErrorParam { error\_code, type }

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BashCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BashCodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class TextEditorCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [TextEditorCodeExecutionToolResultErrorParam](api/messages.md) { error\_code, type, error\_message }  | [TextEditorCodeExecutionViewResultBlockParam](api/messages.md) { content, file\_type, type, 3 more }  | [TextEditorCodeExecutionCreateResultBlockParam](api/messages.md) { is\_file\_update, type }  | [TextEditorCodeExecutionStrReplaceResultBlockParam](api/messages.md) { type, lines, new\_lines, 3 more }

Accepts one of the following:

class TextEditorCodeExecutionToolResultErrorParam { error\_code, type, error\_message }

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

type: :text\_editor\_code\_execution\_tool\_result\_error

error\_message: String

class TextEditorCodeExecutionViewResultBlockParam { content, file\_type, type, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

type: :text\_editor\_code\_execution\_view\_result

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

class TextEditorCodeExecutionCreateResultBlockParam { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class TextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new\_lines, 3 more }

type: :text\_editor\_code\_execution\_str\_replace\_result

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class ToolSearchToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [ToolSearchToolResultErrorParam](api/messages.md) { error\_code, type }  | [ToolSearchToolSearchResultBlockParam](api/messages.md) { tool\_references, type }

Accepts one of the following:

class ToolSearchToolResultErrorParam { error\_code, type }

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :tool\_search\_tool\_result\_error

class ToolSearchToolSearchResultBlockParam { tool\_references, type }

tool\_references: Array[[ToolReferenceBlockParam](api/messages.md) { tool\_name, type, cache\_control } ]

tool\_name: String

type: :tool\_reference

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class ContainerUploadBlockParam { file\_id, type, cache\_control }

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: String

type: :container\_upload

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

role: :user | :assistant

Accepts one of the following:

:user

:assistant

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7" | :"claude-mythos-preview" | :"claude-opus-4-6" | 14 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

:"claude-opus-4-0"

Powerful model for complex tasks

:"claude-opus-4-20250514"

Powerful model for complex tasks

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-3-haiku-20240307"

Fast and cost-effective model

String

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Top-level cache control automatically applies a cache\_control marker to the last cacheable block in the request.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

container: String

Container identifier for reuse across requests.

inference\_geo: String

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

metadata: [Metadata](api/messages.md) { user\_id }

An object describing metadata about the request.

user\_id: String

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512

output\_config: [OutputConfig](api/messages.md) { effort, format\_ }

Configuration options for the model's output, such as the output format.

effort: :low | :medium | :high | 2 more

All possible effort levels.

Accepts one of the following:

:low

:medium

:high

:xhigh

:max

format\_: [JSONOutputFormat](api/messages.md) { schema, type }

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

schema: Hash[Symbol, untyped]

The JSON schema of the format

type: :json\_schema

service\_tier: :auto | :standard\_only

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

Accepts one of the following:

:auto

:standard\_only

stop\_sequences: Array[String]

Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

stream: bool

Whether to incrementally stream the response using server-sent events.

See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.

system\_: String | Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations } ]

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

Accepts one of the following:

String

Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations } ]

text: String

type: :text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Deprecatedtemperature: Float

Amount of randomness injected into the response.

Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0

thinking: [ThinkingConfigParam](api/messages.md)

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

class ThinkingConfigEnabled { budget\_tokens, type, display\_ }

budget\_tokens: Integer

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: :enabled

display\_: :summarized | :omitted

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

:summarized

:omitted

class ThinkingConfigDisabled { type }

type: :disabled

class ThinkingConfigAdaptive { type, display\_ }

type: :adaptive

display\_: :summarized | :omitted

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

:summarized

:omitted

tool\_choice: [ToolChoice](api/messages.md)

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

class ToolChoiceAuto { type, disable\_parallel\_tool\_use }

The model will automatically decide whether to use tools.

type: :auto

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceAny { type, disable\_parallel\_tool\_use }

The model will use any available tools.

type: :any

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceTool { name, type, disable\_parallel\_tool\_use }

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: :tool

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceNone { type }

The model will not be allowed to use tools.

type: :none

tools: Array[[ToolUnion](api/messages.md)]

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

Accepts one of the following:

class Tool { input\_schema, name, allowed\_callers, 7 more }

input\_schema: { type, properties, required}

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: :object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

description: String

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: bool

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

type: :custom

class ToolBash20250124 { name, type, allowed\_callers, 4 more }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :bash\_20250124

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class CodeExecutionTool20250522 { name, type, allowed\_callers, 3 more }

name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20250522

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class CodeExecutionTool20250825 { name, type, allowed\_callers, 3 more }

name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20250825

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class CodeExecutionTool20260120 { name, type, allowed\_callers, 3 more }

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20260120

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class MemoryTool20250818 { name, type, allowed\_callers, 4 more }

name: :memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :memory\_20250818

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250124 { name, type, allowed\_callers, 4 more }

name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250124

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429 { name, type, allowed\_callers, 4 more }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250429

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728 { name, type, allowed\_callers, 5 more }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250728

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

max\_characters: Integer

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: bool

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20250305 { name, type, allowed\_callers, 7 more }

name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_search\_20250305

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

user\_location: [UserLocation](api/messages.md) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

city: String

The city of the user.

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: String

The region of the user.

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebFetchTool20250910 { name, type, allowed\_callers, 8 more }

name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20250910

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20260209 { name, type, allowed\_callers, 7 more }

name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_search\_20260209

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

user\_location: [UserLocation](api/messages.md) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

city: String

The city of the user.

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: String

The region of the user.

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebFetchTool20260209 { name, type, allowed\_callers, 8 more }

name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20260209

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

class WebFetchTool20260309 { name, type, allowed\_callers, 9 more }

Web fetch tool with use\_cache parameter for bypassing cached content.

name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20260309

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

use\_cache: bool

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

class ToolSearchToolBm25\_20251119 { name, type, allowed\_callers, 3 more }

name: :tool\_search\_tool\_bm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :tool\_search\_tool\_bm25\_20251119 | :tool\_search\_tool\_bm25

Accepts one of the following:

:tool\_search\_tool\_bm25\_20251119

:tool\_search\_tool\_bm25

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class ToolSearchToolRegex20251119 { name, type, allowed\_callers, 3 more }

name: :tool\_search\_tool\_regex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :tool\_search\_tool\_regex\_20251119 | :tool\_search\_tool\_regex

Accepts one of the following:

:tool\_search\_tool\_regex\_20251119

:tool\_search\_tool\_regex

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

Deprecatedtop\_k: Integer

Only sample from the top K options for each subsequent token.

Deprecated. Models released after Claude Opus 4.6 do not accept top\_k; any value will be rejected with a 400 error.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only.

minimum0

Deprecatedtop\_p: Float

Use nucleus sampling.

Deprecated. Models released after Claude Opus 4.6 do not support setting top\_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

Recommended for advanced use cases only.

maximum1

minimum0

##### ReturnsExpand Collapse

class Message { id, container, content, 7 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [Container](api/messages.md) { id, expires\_at }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

content: Array[[ContentBlock](api/messages.md)]

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

class TextBlock { citations, text, type }

citations: Array[[TextCitation](api/messages.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

class ToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class ServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

class ServerToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class ServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

input: Hash[Symbol, untyped]

name: :web\_search | :web\_fetch | :code\_execution | 4 more

Accepts one of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use

class WebSearchToolResultBlock { caller\_, content, tool\_use\_id, type }

caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class ServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError { error\_code, type }

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

class WebFetchToolResultBlock { caller\_, content, tool\_use\_id, type }

caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class ServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  | [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url }

Accepts one of the following:

class WebFetchToolResultErrorBlock { error\_code, type }

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class WebFetchBlock { content, retrieved\_at, type, url }

content: [DocumentBlock](api/messages.md) { citations, source, title, type }

citations: [CitationsConfig](api/messages.md) { enabled }

Citation configuration for the document

enabled: bool

source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type }

Accepts one of the following:

class Base64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class PlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

class CodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultError { error\_code, type }

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class CodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class EncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

class BashCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  | [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BashCodeExecutionToolResultError { error\_code, type }

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

class TextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  | [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  | [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  | [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

class TextEditorCodeExecutionToolResultError { error\_code, error\_message, type }

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error

class TextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result

class TextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class TextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

class ToolSearchToolResultBlock { content, tool\_use\_id, type }

content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  | [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type }

Accepts one of the following:

class ToolSearchToolResultError { error\_code, error\_message, type }

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error

class ToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[ToolReferenceBlock](api/messages.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

class ContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7" | :"claude-mythos-preview" | :"claude-opus-4-6" | 14 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

:"claude-opus-4-0"

Powerful model for complex tasks

:"claude-opus-4-20250514"

Powerful model for complex tasks

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-3-haiku-20240307"

Fast and cost-effective model

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type }

Structured information about a refusal.

category: :cyber | :bio

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

:cyber

:bio

explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: :refusal

stop\_reason: [StopReason](api/messages.md)

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

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:refusal

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

RawMessageStreamEvent = [RawMessageStartEvent](api/messages.md) { message, type }  | [RawMessageDeltaEvent](api/messages.md) { delta, type, usage }  | [RawMessageStopEvent](api/messages.md) { type }  | 3 more

Accepts one of the following:

class RawMessageStartEvent { message, type }

message: [Message](api/messages.md) { id, container, content, 7 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [Container](api/messages.md) { id, expires\_at }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

content: Array[[ContentBlock](api/messages.md)]

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

class TextBlock { citations, text, type }

citations: Array[[TextCitation](api/messages.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

class ToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class ServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

class ServerToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class ServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

input: Hash[Symbol, untyped]

name: :web\_search | :web\_fetch | :code\_execution | 4 more

Accepts one of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use

class WebSearchToolResultBlock { caller\_, content, tool\_use\_id, type }

caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class ServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError { error\_code, type }

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

class WebFetchToolResultBlock { caller\_, content, tool\_use\_id, type }

caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class ServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  | [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url }

Accepts one of the following:

class WebFetchToolResultErrorBlock { error\_code, type }

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class WebFetchBlock { content, retrieved\_at, type, url }

content: [DocumentBlock](api/messages.md) { citations, source, title, type }

citations: [CitationsConfig](api/messages.md) { enabled }

Citation configuration for the document

enabled: bool

source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type }

Accepts one of the following:

class Base64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class PlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

class CodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultError { error\_code, type }

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class CodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class EncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

class BashCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  | [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BashCodeExecutionToolResultError { error\_code, type }

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

class TextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  | [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  | [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  | [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

class TextEditorCodeExecutionToolResultError { error\_code, error\_message, type }

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error

class TextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result

class TextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class TextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

class ToolSearchToolResultBlock { content, tool\_use\_id, type }

content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  | [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type }

Accepts one of the following:

class ToolSearchToolResultError { error\_code, error\_message, type }

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error

class ToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[ToolReferenceBlock](api/messages.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

class ContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7" | :"claude-mythos-preview" | :"claude-opus-4-6" | 14 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

:"claude-opus-4-0"

Powerful model for complex tasks

:"claude-opus-4-20250514"

Powerful model for complex tasks

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-3-haiku-20240307"

Fast and cost-effective model

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type }

Structured information about a refusal.

category: :cyber | :bio

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

:cyber

:bio

explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: :refusal

stop\_reason: [StopReason](api/messages.md)

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

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:refusal

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

type: :message\_start

class RawMessageDeltaEvent { delta, type, usage }

delta: { container, stop\_details, stop\_reason, stop\_sequence}

container: [Container](api/messages.md) { id, expires\_at }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type }

Structured information about a refusal.

category: :cyber | :bio

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

:cyber

:bio

explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: :refusal

stop\_reason: [StopReason](api/messages.md)

Accepts one of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:refusal

stop\_sequence: String

type: :message\_delta

usage: [MessageDeltaUsage](api/messages.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: Integer

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The cumulative number of input tokens read from the cache.

input\_tokens: Integer

The cumulative number of input tokens which were used.

output\_tokens: Integer

The cumulative number of output tokens which were used.

server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

class RawMessageStopEvent { type }

type: :message\_stop

class RawContentBlockStartEvent { content\_block, index, type }

content\_block: [TextBlock](api/messages.md) { citations, text, type }  | [ThinkingBlock](api/messages.md) { signature, thinking, type }  | [RedactedThinkingBlock](api/messages.md) { data, type }  | 9 more

Response model for a file uploaded to the container.

Accepts one of the following:

class TextBlock { citations, text, type }

citations: Array[[TextCitation](api/messages.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

class ToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class ServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

class ServerToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class ServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

input: Hash[Symbol, untyped]

name: :web\_search | :web\_fetch | :code\_execution | 4 more

Accepts one of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use

class WebSearchToolResultBlock { caller\_, content, tool\_use\_id, type }

caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class ServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError { error\_code, type }

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

class WebFetchToolResultBlock { caller\_, content, tool\_use\_id, type }

caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class ServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  | [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url }

Accepts one of the following:

class WebFetchToolResultErrorBlock { error\_code, type }

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class WebFetchBlock { content, retrieved\_at, type, url }

content: [DocumentBlock](api/messages.md) { citations, source, title, type }

citations: [CitationsConfig](api/messages.md) { enabled }

Citation configuration for the document

enabled: bool

source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type }

Accepts one of the following:

class Base64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class PlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

class CodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultError { error\_code, type }

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class CodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class EncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

class BashCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  | [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BashCodeExecutionToolResultError { error\_code, type }

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

class TextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  | [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  | [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  | [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

class TextEditorCodeExecutionToolResultError { error\_code, error\_message, type }

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error

class TextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result

class TextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class TextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

class ToolSearchToolResultBlock { content, tool\_use\_id, type }

content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  | [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type }

Accepts one of the following:

class ToolSearchToolResultError { error\_code, error\_message, type }

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error

class ToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[ToolReferenceBlock](api/messages.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

class ContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

index: Integer

type: :content\_block\_start

class RawContentBlockDeltaEvent { delta, index, type }

delta: [RawContentBlockDelta](api/messages.md)

Accepts one of the following:

class TextDelta { text, type }

text: String

type: :text\_delta

class InputJSONDelta { partial\_json, type }

partial\_json: String

type: :input\_json\_delta

class CitationsDelta { citation, type }

citation: [CitationCharLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | [CitationPageLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | [CitationContentBlockLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | 2 more

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

type: :citations\_delta

class ThinkingDelta { thinking, type }

thinking: String

type: :thinking\_delta

class SignatureDelta { signature, type }

signature: String

type: :signature\_delta

index: Integer

type: :content\_block\_delta

class RawContentBlockStopEvent { index, type }

index: Integer

type: :content\_block\_stop

Create a Message

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

message = anthropic.messages.create(
  max_tokens: 1024,
  messages: [{content: "Hello, world", role: :user}],
  model: :"claude-opus-4-6"
)

puts(message)
```

Response 200

```shiki
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "id",
    "expires_at": "2019-12-27T18:11:19.117Z"
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
    "output_tokens": 503,
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

```shiki
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "id",
    "expires_at": "2019-12-27T18:11:19.117Z"
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
    "output_tokens": 503,
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
