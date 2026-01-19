# Create a Message

Copy page

Kotlin

# Create a Message

messages().create(MessageCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none()) : [Message](api/messages.md)

post/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)

##### ParametersExpand Collapse

params: MessageCreateParams

maxTokens: Long

The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.

minimum1

messages: List<[MessageParam](api/messages.md)>

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

content: Content

Accepts one of the following:

String

List<[ContentBlockParam](api/messages.md)>

Accepts one of the following:

class TextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[TextCitationParam](api/messages.md)>>

Accepts one of the following:

class CitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class CitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class CitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class CitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class CitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class ImageBlockParam:

source: Source

Accepts one of the following:

class Base64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class DocumentBlockParam:

source: Source

Accepts one of the following:

class Base64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class PlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class ContentBlockSource:

content: Content

Accepts one of the following:

String

List<[ContentBlockSourceContent](api/messages.md)>

Accepts one of the following:

class TextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[TextCitationParam](api/messages.md)>>

Accepts one of the following:

class CitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class CitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class CitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class CitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class CitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class ImageBlockParam:

source: Source

Accepts one of the following:

class Base64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

type: JsonValue; "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class UrlPdfSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[CitationsConfigParam](api/messages.md)>

enabled: Optional<Boolean>

context: Optional<String>

title: Optional<String>

class SearchResultBlockParam:

content: List<[TextBlockParam](api/messages.md)>

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[TextCitationParam](api/messages.md)>>

Accepts one of the following:

class CitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class CitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class CitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class CitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class CitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

source: String

title: String

type: JsonValue; "search\_result"constant"search\_result"constant

Accepts one of the following:

SEARCH\_RESULT("search\_result")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[CitationsConfigParam](api/messages.md)>

enabled: Optional<Boolean>

class ThinkingBlockParam:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class RedactedThinkingBlockParam:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class ToolUseBlockParam:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class ToolResultBlockParam:

toolUseId: String

type: JsonValue; "tool\_result"constant"tool\_result"constant

Accepts one of the following:

TOOL\_RESULT("tool\_result")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

content: Optional<Content>

Accepts one of the following:

String

List<Block>

Accepts one of the following:

class TextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[TextCitationParam](api/messages.md)>>

Accepts one of the following:

class CitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class CitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class CitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class CitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class CitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class ImageBlockParam:

source: Source

Accepts one of the following:

class Base64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class SearchResultBlockParam:

content: List<[TextBlockParam](api/messages.md)>

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[TextCitationParam](api/messages.md)>>

Accepts one of the following:

class CitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class CitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class CitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class CitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class CitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

source: String

title: String

type: JsonValue; "search\_result"constant"search\_result"constant

Accepts one of the following:

SEARCH\_RESULT("search\_result")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[CitationsConfigParam](api/messages.md)>

enabled: Optional<Boolean>

class DocumentBlockParam:

source: Source

Accepts one of the following:

class Base64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class PlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class ContentBlockSource:

content: Content

Accepts one of the following:

String

List<[ContentBlockSourceContent](api/messages.md)>

Accepts one of the following:

class TextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[TextCitationParam](api/messages.md)>>

Accepts one of the following:

class CitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class CitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class CitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class CitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class CitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class ImageBlockParam:

source: Source

Accepts one of the following:

class Base64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

type: JsonValue; "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class UrlPdfSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[CitationsConfigParam](api/messages.md)>

enabled: Optional<Boolean>

context: Optional<String>

title: Optional<String>

isError: Optional<Boolean>

class ServerToolUseBlockParam:

id: String

input: Input

name: JsonValue; "web\_search"constant"web\_search"constant

Accepts one of the following:

WEB\_SEARCH("web\_search")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class WebSearchToolResultBlockParam:

content: [WebSearchToolResultBlockParamContent](api/messages.md)

Accepts one of the following:

List<[WebSearchResultBlockParam](api/messages.md)>

encryptedContent: String

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

pageAge: Optional<String>

class WebSearchToolRequestError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

role: Role

Accepts one of the following:

USER("user")

ASSISTANT("assistant")

model: Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

metadata: Optional<[Metadata](api/messages.md)>

An object describing metadata about the request.

serviceTier: Optional<ServiceTier>

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

AUTO("auto")

STANDARD\_ONLY("standard\_only")

stopSequences: Optional<List<String>>

Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

system: Optional<System>

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

String

List<[TextBlockParam](api/messages.md)>

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[TextCitationParam](api/messages.md)>>

Accepts one of the following:

class CitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class CitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class CitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class CitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class CitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

temperature: Optional<Double>

Amount of randomness injected into the response.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0

thinking: Optional<[ThinkingConfigParam](api/messages.md)>

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

toolChoice: Optional<[ToolChoice](api/messages.md)>

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

tools: Optional<List<[ToolUnion](api/messages.md)>>

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

inputSchema: InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: JsonValue; "object"constant"object"constant

Accepts one of the following:

OBJECT("object")

properties: Optional<Properties>

required: Optional<List<String>>

name: String

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

description: Optional<String>

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

type: Optional<Type>

Accepts one of the following:

CUSTOM("custom")

class ToolBash20250124:

name: JsonValue; "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

BASH("bash")

type: JsonValue; "bash\_20250124"constant"bash\_20250124"constant

Accepts one of the following:

BASH\_20250124("bash\_20250124")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class ToolTextEditor20250124:

name: JsonValue; "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_EDITOR("str\_replace\_editor")

type: JsonValue; "text\_editor\_20250124"constant"text\_editor\_20250124"constant

Accepts one of the following:

TEXT\_EDITOR\_20250124("text\_editor\_20250124")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class ToolTextEditor20250429:

name: JsonValue; "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_BASED\_EDIT\_TOOL("str\_replace\_based\_edit\_tool")

type: JsonValue; "text\_editor\_20250429"constant"text\_editor\_20250429"constant

Accepts one of the following:

TEXT\_EDITOR\_20250429("text\_editor\_20250429")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class ToolTextEditor20250728:

name: JsonValue; "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_BASED\_EDIT\_TOOL("str\_replace\_based\_edit\_tool")

type: JsonValue; "text\_editor\_20250728"constant"text\_editor\_20250728"constant

Accepts one of the following:

TEXT\_EDITOR\_20250728("text\_editor\_20250728")

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

maxCharacters: Optional<Long>

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

class WebSearchTool20250305:

name: JsonValue; "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

WEB\_SEARCH("web\_search")

type: JsonValue; "web\_search\_20250305"constant"web\_search\_20250305"constant

Accepts one of the following:

WEB\_SEARCH\_20250305("web\_search\_20250305")

allowedDomains: Optional<List<String>>

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blockedDomains: Optional<List<String>>

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cacheControl: Optional<[CacheControlEphemeral](api/messages.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

maxUses: Optional<Long>

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

userLocation: Optional<UserLocation>

Parameters for the user's location. Used to provide more relevant search results.

type: JsonValue; "approximate"constant"approximate"constant

Accepts one of the following:

APPROXIMATE("approximate")

city: Optional<String>

The city of the user.

maxLength255

minLength1

country: Optional<String>

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: Optional<String>

The region of the user.

maxLength255

minLength1

timezone: Optional<String>

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

topK: Optional<Long>

Only sample from the top K options for each subsequent token.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only. You usually only need to use `temperature`.

minimum0

topP: Optional<Double>

Use nucleus sampling.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

Recommended for advanced use cases only. You usually only need to use `temperature`.

maximum1

minimum0

##### ReturnsExpand Collapse

class Message:

id: String

Unique object identifier.

The format and length of IDs may change over time.

content: List<[ContentBlock](api/messages.md)>

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

citations: Optional<List<[TextCitation](api/messages.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class CitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class CitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class CitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class CitationsSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class ThinkingBlock:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class RedactedThinkingBlock:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class ToolUseBlock:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

class ServerToolUseBlock:

id: String

input: Input

name: JsonValue; "web\_search"constant"web\_search"constant

Accepts one of the following:

WEB\_SEARCH("web\_search")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

class WebSearchToolResultBlock:

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

List<[WebSearchResultBlock](api/messages.md)>

encryptedContent: String

pageAge: Optional<String>

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

model: Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_3\_7\_SONNET\_LATEST("claude-3-7-sonnet-latest")

High-performance model with early extended thinking

CLAUDE\_3\_7\_SONNET\_20250219("claude-3-7-sonnet-20250219")

High-performance model with early extended thinking

CLAUDE\_3\_5\_HAIKU\_LATEST("claude-3-5-haiku-latest")

Fastest and most compact model for near-instant responsiveness

CLAUDE\_3\_5\_HAIKU\_20241022("claude-3-5-haiku-20241022")

Our fastest model

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_4\_SONNET\_20250514("claude-4-sonnet-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

Our best model for real-world agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

Our best model for real-world agents and coding

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Our most capable model

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Our most capable model

CLAUDE\_4\_OPUS\_20250514("claude-4-opus-20250514")

Our most capable model

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Our most capable model

CLAUDE\_3\_OPUS\_LATEST("claude-3-opus-latest")

Excels at writing and complex tasks

CLAUDE\_3\_OPUS\_20240229("claude-3-opus-20240229")

Excels at writing and complex tasks

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Our previous most fast and cost-effective

role: JsonValue; "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

ASSISTANT("assistant")

stopReason: Optional<[StopReason](api/messages.md)>

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

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

REFUSAL("refusal")

stopSequence: Optional<String>

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: JsonValue; "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

usage: [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cacheCreation: Optional<[CacheCreation](api/messages.md)>

Breakdown of cached tokens by TTL

ephemeral1hInputTokens: Long

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral5mInputTokens: Long

The number of input tokens used to create the 5 minute cache entry.

minimum0

cacheCreationInputTokens: Optional<Long>

The number of input tokens used to create the cache entry.

minimum0

cacheReadInputTokens: Optional<Long>

The number of input tokens read from the cache.

minimum0

inputTokens: Long

The number of input tokens which were used.

minimum0

outputTokens: Long

The number of output tokens which were used.

minimum0

serverToolUse: Optional<[ServerToolUsage](api/messages.md)>

The number of server tool requests.

webSearchRequests: Long

The number of web search tool requests.

minimum0

serviceTier: Optional<ServiceTier>

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

Create a Message

Kotlin

```shiki
package com.anthropic.example

import com.anthropic.client.AnthropicClient
import com.anthropic.client.okhttp.AnthropicOkHttpClient
import com.anthropic.models.messages.Message
import com.anthropic.models.messages.MessageCreateParams
import com.anthropic.models.messages.Model

fun main() {
    val client: AnthropicClient = AnthropicOkHttpClient.fromEnv()

    val params: MessageCreateParams = MessageCreateParams.builder()
        .maxTokens(1024L)
        .addUserMessage("Hello, world")
        .model(Model.CLAUDE_OPUS_4_5_20251101)
        .build()
    val message: Message = client.messages().create(params)
}
```

Response 200

```shiki
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
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
  "model": "claude-sonnet-4-5-20250929",
  "role": "assistant",
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
    "input_tokens": 2095,
    "output_tokens": 503,
    "server_tool_use": {
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
  "model": "claude-sonnet-4-5-20250929",
  "role": "assistant",
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
    "input_tokens": 2095,
    "output_tokens": 503,
    "server_tool_use": {
      "web_search_requests": 0
    },
    "service_tier": "standard"
  }
}
```

---

*Copyright © Anthropic. All rights reserved.*
