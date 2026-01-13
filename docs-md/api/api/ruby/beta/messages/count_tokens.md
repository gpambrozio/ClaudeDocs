# Count tokens in a Message

Copy page

Ruby

# Count tokens in a Message

beta.messages.count\_tokens(\*\*kwargs) -> [BetaMessageTokensCount](api/beta.md) { context\_management, input\_tokens }

post/v1/messages/count\_tokens

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

##### ParametersExpand Collapse

messages: Array[[BetaMessageParam](api/beta.md) { content, role } ]

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

content: String | Array[[BetaContentBlockParam](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockParam](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaRequestDocumentBlock { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:content

class BetaURLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :document

Accepts one of the following:

:document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

context: String

title: String

class BetaSearchResultBlockParam { content, source, title, 3 more }

content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

source: String

title: String

type: :search\_result

Accepts one of the following:

:search\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

class BetaThinkingBlockParam { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class BetaRedactedThinkingBlockParam { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class BetaToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: String

type: :tool\_result

Accepts one of the following:

:tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

content: String | Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  | [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  | 2 more]

Accepts one of the following:

String

Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  | [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  | 2 more]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaSearchResultBlockParam { content, source, title, 3 more }

content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

source: String

title: String

type: :search\_result

Accepts one of the following:

:search\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

class BetaRequestDocumentBlock { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:content

class BetaURLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :document

Accepts one of the following:

:document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

context: String

title: String

class BetaToolReferenceBlockParam { tool\_name, type, cache\_control }

Tool reference block that can be included in tool\_result content.

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaServerToolUseBlockParam { id, input, name, 3 more }

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

Accepts one of the following:

:server\_tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaWebSearchToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaWebSearchToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

Array[[BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

page\_age: String

class BetaWebSearchToolRequestError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaWebFetchToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaWebFetchToolResultErrorBlockParam](api/beta.md) { error\_code, type }  | [BetaWebFetchBlockParam](api/beta.md) { content, type, url, retrieved\_at }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

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

Accepts one of the following:

:web\_fetch\_tool\_result\_error

class BetaWebFetchBlockParam { content, type, url, retrieved\_at }

content: [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:content

class BetaURLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :document

Accepts one of the following:

:document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

context: String

title: String

type: :web\_fetch\_result

Accepts one of the following:

:web\_fetch\_result

url: String

Fetched content URL

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: String

type: :web\_fetch\_tool\_result

Accepts one of the following:

:web\_fetch\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaCodeExecutionToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

Accepts one of the following:

:code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

Accepts one of the following:

:code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaBashCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaBashCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

Accepts one of the following:

:bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

Accepts one of the following:

:bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

Accepts one of the following:

:bash\_code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaTextEditorCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaTextEditorCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  | [BetaTextEditorCodeExecutionViewResultBlockParam](api/beta.md) { content, file\_type, type, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta.md) { type, lines, new\_lines, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam { error\_code, type, error\_message }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

type: :text\_editor\_code\_execution\_tool\_result\_error

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result\_error

error\_message: String

class BetaTextEditorCodeExecutionViewResultBlockParam { content, file\_type, type, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

type: :text\_editor\_code\_execution\_view\_result

Accepts one of the following:

:text\_editor\_code\_execution\_view\_result

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

class BetaTextEditorCodeExecutionCreateResultBlockParam { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

Accepts one of the following:

:text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new\_lines, 3 more }

type: :text\_editor\_code\_execution\_str\_replace\_result

Accepts one of the following:

:text\_editor\_code\_execution\_str\_replace\_result

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaToolSearchToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaToolSearchToolResultErrorParam](api/beta.md) { error\_code, type }  | [BetaToolSearchToolSearchResultBlockParam](api/beta.md) { tool\_references, type }

Accepts one of the following:

class BetaToolSearchToolResultErrorParam { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :tool\_search\_tool\_result\_error

Accepts one of the following:

:tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlockParam { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control } ]

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

Accepts one of the following:

:tool\_search\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaMCPToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash[Symbol, untyped]

name: String

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

Accepts one of the following:

:mcp\_tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaRequestMCPToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: String

type: :mcp\_tool\_result

Accepts one of the following:

:mcp\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

content: String | Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

Accepts one of the following:

String

Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

is\_error: bool

class BetaContainerUploadBlockParam { file\_id, type, cache\_control }

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: String

type: :container\_upload

Accepts one of the following:

:container\_upload

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

:"claude-opus-4-5-20251101" | :"claude-opus-4-5" | :"claude-3-7-sonnet-latest" | 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

context\_management: [BetaContextManagementConfig](api/beta.md) { edits }

Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

edits: Array[[BetaClearToolUses20250919Edit](api/beta.md) { type, clear\_at\_least, clear\_tool\_inputs, 3 more }  | [BetaClearThinking20251015Edit](api/beta.md) { type, keep } ]

List of context management edits to apply

Accepts one of the following:

class BetaClearToolUses20250919Edit { type, clear\_at\_least, clear\_tool\_inputs, 3 more }

type: :clear\_tool\_uses\_20250919

Accepts one of the following:

:clear\_tool\_uses\_20250919

clear\_at\_least: [BetaInputTokensClearAtLeast](api/beta.md) { type, value }

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: :input\_tokens

Accepts one of the following:

:input\_tokens

value: Integer

clear\_tool\_inputs: bool | Array[String]

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

bool

Array[String]

exclude\_tools: Array[String]

Tool names whose uses are preserved from clearing

keep: [BetaToolUsesKeep](api/beta.md) { type, value }

Number of tool uses to retain in the conversation

type: :tool\_uses

Accepts one of the following:

:tool\_uses

value: Integer

trigger: [BetaInputTokensTrigger](api/beta.md) { type, value }  | [BetaToolUsesTrigger](api/beta.md) { type, value }

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger { type, value }

type: :input\_tokens

Accepts one of the following:

:input\_tokens

value: Integer

class BetaToolUsesTrigger { type, value }

type: :tool\_uses

Accepts one of the following:

:tool\_uses

value: Integer

class BetaClearThinking20251015Edit { type, keep }

type: :clear\_thinking\_20251015

Accepts one of the following:

:clear\_thinking\_20251015

keep: [BetaThinkingTurns](api/beta.md) { type, value }  | [BetaAllThinkingTurns](api/beta.md) { type }  | :all

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns { type, value }

type: :thinking\_turns

Accepts one of the following:

:thinking\_turns

value: Integer

class BetaAllThinkingTurns { type }

type: :all

Accepts one of the following:

:all

Keep = :all

Accepts one of the following:

:all

mcp\_servers: Array[[BetaRequestMCPServerURLDefinition](api/beta.md) { name, type, url, 2 more } ]

MCP servers to be utilized in this request

name: String

type: :url

Accepts one of the following:

:url

url: String

authorization\_token: String

tool\_configuration: [BetaRequestMCPServerToolConfiguration](api/beta.md) { allowed\_tools, enabled }

allowed\_tools: Array[String]

enabled: bool

output\_config: [BetaOutputConfig](api/beta.md) { effort }

Configuration options for the model's output. Controls aspects like how much effort the model puts into its response.

effort: :low | :medium | :high

All possible effort levels.

Accepts one of the following:

:low

:medium

:high

output\_format: [BetaJSONOutputFormat](api/beta.md) { schema, type }

A schema to specify Claude's output format in responses.

schema: Hash[Symbol, untyped]

The JSON schema of the format

type: :json\_schema

Accepts one of the following:

:json\_schema

system\_: String | Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

Accepts one of the following:

String

Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

thinking: [BetaThinkingConfigParam](api/beta.md)

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

class BetaThinkingConfigEnabled { budget\_tokens, type }

budget\_tokens: Integer

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: :enabled

Accepts one of the following:

:enabled

class BetaThinkingConfigDisabled { type }

type: :disabled

Accepts one of the following:

:disabled

tool\_choice: [BetaToolChoice](api/beta.md)

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

class BetaToolChoiceAuto { type, disable\_parallel\_tool\_use }

The model will automatically decide whether to use tools.

type: :auto

Accepts one of the following:

:auto

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceAny { type, disable\_parallel\_tool\_use }

The model will use any available tools.

type: :any

Accepts one of the following:

:any

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceTool { name, type, disable\_parallel\_tool\_use }

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: :tool

Accepts one of the following:

:tool

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceNone { type }

The model will not be allowed to use tools.

type: :none

Accepts one of the following:

:none

tools: Array[[BetaTool](api/beta.md) { input\_schema, name, allowed\_callers, 6 more }  | [BetaToolBash20241022](api/beta.md) { name, type, allowed\_callers, 4 more }  | [BetaToolBash20250124](api/beta.md) { name, type, allowed\_callers, 4 more }  | 15 more]

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

class BetaTool { input\_schema, name, allowed\_callers, 6 more }

input\_schema: { type, properties, required}

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: :object

Accepts one of the following:

:object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

type: :custom

Accepts one of the following:

:custom

class BetaToolBash20241022 { name, type, allowed\_callers, 4 more }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:bash

type: :bash\_20241022

Accepts one of the following:

:bash\_20241022

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolBash20250124 { name, type, allowed\_callers, 4 more }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:bash

type: :bash\_20250124

Accepts one of the following:

:bash\_20250124

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaCodeExecutionTool20250522 { name, type, allowed\_callers, 3 more }

name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:code\_execution

type: :code\_execution\_20250522

Accepts one of the following:

:code\_execution\_20250522

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaCodeExecutionTool20250825 { name, type, allowed\_callers, 3 more }

name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:code\_execution

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolComputerUse20241022 { display\_height\_px, display\_width\_px, name, 7 more }

display\_height\_px: Integer

The height of the display in pixels.

minimum1

display\_width\_px: Integer

The width of the display in pixels.

minimum1

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:computer

type: :computer\_20241022

Accepts one of the following:

:computer\_20241022

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

display\_number: Integer

The X11 display number (e.g. 0, 1) for the display.

minimum0

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

class BetaMemoryTool20250818 { name, type, allowed\_callers, 4 more }

name: :memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:memory

type: :memory\_20250818

Accepts one of the following:

:memory\_20250818

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolComputerUse20250124 { display\_height\_px, display\_width\_px, name, 7 more }

display\_height\_px: Integer

The height of the display in pixels.

minimum1

display\_width\_px: Integer

The width of the display in pixels.

minimum1

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:computer

type: :computer\_20250124

Accepts one of the following:

:computer\_20250124

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

display\_number: Integer

The X11 display number (e.g. 0, 1) for the display.

minimum0

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

class BetaToolTextEditor20241022 { name, type, allowed\_callers, 4 more }

name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_editor

type: :text\_editor\_20241022

Accepts one of the following:

:text\_editor\_20241022

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolComputerUse20251124 { display\_height\_px, display\_width\_px, name, 8 more }

display\_height\_px: Integer

The height of the display in pixels.

minimum1

display\_width\_px: Integer

The width of the display in pixels.

minimum1

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:computer

type: :computer\_20251124

Accepts one of the following:

:computer\_20251124

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

display\_number: Integer

The X11 display number (e.g. 0, 1) for the display.

minimum0

enable\_zoom: bool

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

class BetaToolTextEditor20250124 { name, type, allowed\_callers, 4 more }

name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_editor

type: :text\_editor\_20250124

Accepts one of the following:

:text\_editor\_20250124

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolTextEditor20250429 { name, type, allowed\_callers, 4 more }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_based\_edit\_tool

type: :text\_editor\_20250429

Accepts one of the following:

:text\_editor\_20250429

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolTextEditor20250728 { name, type, allowed\_callers, 5 more }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_based\_edit\_tool

type: :text\_editor\_20250728

Accepts one of the following:

:text\_editor\_20250728

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

minimum1

strict: bool

class BetaWebSearchTool20250305 { name, type, allowed\_callers, 7 more }

name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:web\_search

type: :web\_search\_20250305

Accepts one of the following:

:web\_search\_20250305

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

exclusiveMinimum0

strict: bool

user\_location: { type, city, country, 2 more}

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

Accepts one of the following:

:approximate

city: String

The city of the user.

maxLength255

minLength1

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: String

The region of the user.

maxLength255

minLength1

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class BetaWebFetchTool20250910 { name, type, allowed\_callers, 8 more }

name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:web\_fetch

type: :web\_fetch\_20250910

Accepts one of the following:

:web\_fetch\_20250910

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

exclusiveMinimum0

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: bool

class BetaToolSearchToolBm25\_20251119 { name, type, allowed\_callers, 3 more }

name: :tool\_search\_tool\_bm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:tool\_search\_tool\_bm25

type: :tool\_search\_tool\_bm25\_20251119 | :tool\_search\_tool\_bm25

Accepts one of the following:

:tool\_search\_tool\_bm25\_20251119

:tool\_search\_tool\_bm25

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolSearchToolRegex20251119 { name, type, allowed\_callers, 3 more }

name: :tool\_search\_tool\_regex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:tool\_search\_tool\_regex

type: :tool\_search\_tool\_regex\_20251119 | :tool\_search\_tool\_regex

Accepts one of the following:

:tool\_search\_tool\_regex\_20251119

:tool\_search\_tool\_regex

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaMCPToolset { mcp\_server\_name, type, cache\_control, 2 more }

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcp\_server\_name: String

Name of the MCP server to configure tools for

maxLength255

minLength1

type: :mcp\_toolset

Accepts one of the following:

:mcp\_toolset

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

configs: Hash[Symbol, [BetaMCPToolConfig](api/beta.md) { defer\_loading, enabled } ]

Configuration overrides for specific tools, keyed by tool name

defer\_loading: bool

enabled: bool

default\_config: [BetaMCPToolDefaultConfig](api/beta.md) { defer\_loading, enabled }

Default configuration applied to all tools from this server

defer\_loading: bool

enabled: bool

anthropic\_beta: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

String

:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 16 more

Accepts one of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

##### ReturnsExpand Collapse

class BetaMessageTokensCount { context\_management, input\_tokens }

context\_management: [BetaCountTokensContextManagementResponse](api/beta.md) { original\_input\_tokens }

Information about context management applied to the message.

original\_input\_tokens: Integer

The original token count before context management was applied

input\_tokens: Integer

The total number of tokens across the provided list of messages, system prompt, and tools.

Count tokens in a Message

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_message_tokens_count = anthropic.beta.messages.count_tokens(
  messages: [{content: "string", role: :user}],
  model: :"claude-opus-4-5-20251101"
)

puts(beta_message_tokens_count)
```

Response 200

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

```shiki
{
  "context_management": {
    "original_input_tokens": 0
  },
  "input_tokens": 2095
}
```