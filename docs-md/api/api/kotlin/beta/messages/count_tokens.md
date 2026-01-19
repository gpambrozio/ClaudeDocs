# Count tokens in a Message

Copy page

Kotlin

# Count tokens in a Message

beta().messages().countTokens(MessageCountTokensParamsparams, RequestOptionsrequestOptions = RequestOptions.none()) : [BetaMessageTokensCount](api/beta.md)

post/v1/messages/count\_tokens

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

##### ParametersExpand Collapse

params: MessageCountTokensParams

betas: Optional<List<AnthropicBeta>>

Optional header to specify the beta version(s) you want to use.

MESSAGE\_BATCHES\_2024\_09\_24("message-batches-2024-09-24")

PROMPT\_CACHING\_2024\_07\_31("prompt-caching-2024-07-31")

COMPUTER\_USE\_2024\_10\_22("computer-use-2024-10-22")

COMPUTER\_USE\_2025\_01\_24("computer-use-2025-01-24")

PDFS\_2024\_09\_25("pdfs-2024-09-25")

TOKEN\_COUNTING\_2024\_11\_01("token-counting-2024-11-01")

TOKEN\_EFFICIENT\_TOOLS\_2025\_02\_19("token-efficient-tools-2025-02-19")

OUTPUT\_128K\_2025\_02\_19("output-128k-2025-02-19")

FILES\_API\_2025\_04\_14("files-api-2025-04-14")

MCP\_CLIENT\_2025\_04\_04("mcp-client-2025-04-04")

MCP\_CLIENT\_2025\_11\_20("mcp-client-2025-11-20")

DEV\_FULL\_THINKING\_2025\_05\_14("dev-full-thinking-2025-05-14")

INTERLEAVED\_THINKING\_2025\_05\_14("interleaved-thinking-2025-05-14")

CODE\_EXECUTION\_2025\_05\_22("code-execution-2025-05-22")

EXTENDED\_CACHE\_TTL\_2025\_04\_11("extended-cache-ttl-2025-04-11")

CONTEXT\_1M\_2025\_08\_07("context-1m-2025-08-07")

CONTEXT\_MANAGEMENT\_2025\_06\_27("context-management-2025-06-27")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED\_2025\_08\_26("model-context-window-exceeded-2025-08-26")

SKILLS\_2025\_10\_02("skills-2025-10-02")

messages: List<[BetaMessageParam](api/beta.md)>

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

List<[BetaContentBlockParam](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

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

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

class BetaRequestDocumentBlock:

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaContentBlockSource:

content: Content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

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

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

class BetaUrlPdfSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileDocumentSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

context: Optional<String>

title: Optional<String>

class BetaSearchResultBlockParam:

content: List<[BetaTextBlockParam](api/beta.md)>

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

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

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

class BetaThinkingBlockParam:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlockParam:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class BetaToolUseBlockParam:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaToolResultBlockParam:

toolUseId: String

type: JsonValue; "tool\_result"constant"tool\_result"constant

Accepts one of the following:

TOOL\_RESULT("tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

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

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

class BetaSearchResultBlockParam:

content: List<[BetaTextBlockParam](api/beta.md)>

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

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

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

class BetaRequestDocumentBlock:

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaContentBlockSource:

content: Content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

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

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

class BetaUrlPdfSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileDocumentSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

context: Optional<String>

title: Optional<String>

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

isError: Optional<Boolean>

class BetaServerToolUseBlockParam:

id: String

input: Input

name: Name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaWebSearchToolResultBlockParam:

content: [BetaWebSearchToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

List<[BetaWebSearchResultBlockParam](api/beta.md)>

encryptedContent: String

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

pageAge: Optional<String>

class BetaWebSearchToolRequestError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

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

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

class BetaWebFetchToolResultBlockParam:

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchBlockParam:

content: [BetaRequestDocumentBlock](api/beta.md)

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaContentBlockSource:

content: Content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

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

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

class BetaUrlPdfSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileDocumentSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

context: Optional<String>

title: Optional<String>

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

toolUseId: String

type: JsonValue; "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT("web\_fetch\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

class BetaCodeExecutionToolResultBlockParam:

content: [BetaCodeExecutionToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlockParam:

content: List<[BetaCodeExecutionOutputBlockParam](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

toolUseId: String

type: JsonValue; "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT("code\_execution\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

class BetaBashCodeExecutionToolResultBlockParam:

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionResultBlockParam:

content: List<[BetaBashCodeExecutionOutputBlockParam](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

toolUseId: String

type: JsonValue; "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT("bash\_code\_execution\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

class BetaTextEditorCodeExecutionToolResultBlockParam:

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

errorMessage: Optional<String>

class BetaTextEditorCodeExecutionViewResultBlockParam:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

class BetaTextEditorCodeExecutionCreateResultBlockParam:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

toolUseId: String

type: JsonValue; "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT("text\_editor\_code\_execution\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

class BetaToolSearchToolResultBlockParam:

content: Content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlockParam:

toolReferences: List<[BetaToolReferenceBlockParam](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

toolUseId: String

type: JsonValue; "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT("tool\_search\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

class BetaMcpToolUseBlockParam:

id: String

input: Input

name: String

serverName: String

The name of the MCP server

type: JsonValue; "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Accepts one of the following:

MCP\_TOOL\_USE("mcp\_tool\_use")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

class BetaRequestMcpToolResultBlockParam:

toolUseId: String

type: JsonValue; "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Accepts one of the following:

MCP\_TOOL\_RESULT("mcp\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

List<[BetaTextBlockParam](api/beta.md)>

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

isError: Optional<Boolean>

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

fileId: String

type: JsonValue; "container\_upload"constant"container\_upload"constant

Accepts one of the following:

CONTAINER\_UPLOAD("container\_upload")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

contextManagement: Optional<[BetaContextManagementConfig](api/beta.md)>

Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

mcpServers: Optional<List<[BetaRequestMcpServerUrlDefinition](api/beta.md)>>

MCP servers to be utilized in this request

name: String

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

authorizationToken: Optional<String>

toolConfiguration: Optional<[BetaRequestMcpServerToolConfiguration](api/beta.md)>

allowedTools: Optional<List<String>>

enabled: Optional<Boolean>

outputConfig: Optional<[BetaOutputConfig](api/beta.md)>

Configuration options for the model's output. Controls aspects like how much effort the model puts into its response.

outputFormat: Optional<[BetaJsonOutputFormat](api/beta.md)>

A schema to specify Claude's output format in responses.

system: Optional<System>

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

String

List<[BetaTextBlockParam](api/beta.md)>

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

thinking: Optional<[BetaThinkingConfigParam](api/beta.md)>

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

toolChoice: Optional<[BetaToolChoice](api/beta.md)>

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

tools: Optional<List<Tool>>

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

class BetaTool:

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

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

description: Optional<String>

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

type: Optional<Type>

Accepts one of the following:

CUSTOM("custom")

class BetaToolBash20241022:

name: JsonValue; "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

BASH("bash")

type: JsonValue; "bash\_20241022"constant"bash\_20241022"constant

Accepts one of the following:

BASH\_20241022("bash\_20241022")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolBash20250124:

name: JsonValue; "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

BASH("bash")

type: JsonValue; "bash\_20250124"constant"bash\_20250124"constant

Accepts one of the following:

BASH\_20250124("bash\_20250124")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaCodeExecutionTool20250522:

name: JsonValue; "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

CODE\_EXECUTION("code\_execution")

type: JsonValue; "code\_execution\_20250522"constant"code\_execution\_20250522"constant

Accepts one of the following:

CODE\_EXECUTION\_20250522("code\_execution\_20250522")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional<Boolean>

class BetaCodeExecutionTool20250825:

name: JsonValue; "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

CODE\_EXECUTION("code\_execution")

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional<Boolean>

class BetaToolComputerUse20241022:

displayHeightPx: Long

The height of the display in pixels.

minimum1

displayWidthPx: Long

The width of the display in pixels.

minimum1

name: JsonValue; "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

type: JsonValue; "computer\_20241022"constant"computer\_20241022"constant

Accepts one of the following:

COMPUTER\_20241022("computer\_20241022")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

displayNumber: Optional<Long>

The X11 display number (e.g. 0, 1) for the display.

minimum0

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaMemoryTool20250818:

name: JsonValue; "memory"constant"memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

MEMORY("memory")

type: JsonValue; "memory\_20250818"constant"memory\_20250818"constant

Accepts one of the following:

MEMORY\_20250818("memory\_20250818")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolComputerUse20250124:

displayHeightPx: Long

The height of the display in pixels.

minimum1

displayWidthPx: Long

The width of the display in pixels.

minimum1

name: JsonValue; "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

type: JsonValue; "computer\_20250124"constant"computer\_20250124"constant

Accepts one of the following:

COMPUTER\_20250124("computer\_20250124")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

displayNumber: Optional<Long>

The X11 display number (e.g. 0, 1) for the display.

minimum0

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolTextEditor20241022:

name: JsonValue; "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_EDITOR("str\_replace\_editor")

type: JsonValue; "text\_editor\_20241022"constant"text\_editor\_20241022"constant

Accepts one of the following:

TEXT\_EDITOR\_20241022("text\_editor\_20241022")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolComputerUse20251124:

displayHeightPx: Long

The height of the display in pixels.

minimum1

displayWidthPx: Long

The width of the display in pixels.

minimum1

name: JsonValue; "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

type: JsonValue; "computer\_20251124"constant"computer\_20251124"constant

Accepts one of the following:

COMPUTER\_20251124("computer\_20251124")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

displayNumber: Optional<Long>

The X11 display number (e.g. 0, 1) for the display.

minimum0

enableZoom: Optional<Boolean>

Whether to enable an action to take a zoomed-in screenshot of the screen.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolTextEditor20250124:

name: JsonValue; "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_EDITOR("str\_replace\_editor")

type: JsonValue; "text\_editor\_20250124"constant"text\_editor\_20250124"constant

Accepts one of the following:

TEXT\_EDITOR\_20250124("text\_editor\_20250124")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolTextEditor20250429:

name: JsonValue; "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_BASED\_EDIT\_TOOL("str\_replace\_based\_edit\_tool")

type: JsonValue; "text\_editor\_20250429"constant"text\_editor\_20250429"constant

Accepts one of the following:

TEXT\_EDITOR\_20250429("text\_editor\_20250429")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolTextEditor20250728:

name: JsonValue; "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_BASED\_EDIT\_TOOL("str\_replace\_based\_edit\_tool")

type: JsonValue; "text\_editor\_20250728"constant"text\_editor\_20250728"constant

Accepts one of the following:

TEXT\_EDITOR\_20250728("text\_editor\_20250728")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

maxCharacters: Optional<Long>

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict: Optional<Boolean>

class BetaWebSearchTool20250305:

name: JsonValue; "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

WEB\_SEARCH("web\_search")

type: JsonValue; "web\_search\_20250305"constant"web\_search\_20250305"constant

Accepts one of the following:

WEB\_SEARCH\_20250305("web\_search\_20250305")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

allowedDomains: Optional<List<String>>

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blockedDomains: Optional<List<String>>

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

maxUses: Optional<Long>

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: Optional<Boolean>

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

class BetaWebFetchTool20250910:

name: JsonValue; "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

WEB\_FETCH("web\_fetch")

type: JsonValue; "web\_fetch\_20250910"constant"web\_fetch\_20250910"constant

Accepts one of the following:

WEB\_FETCH\_20250910("web\_fetch\_20250910")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

allowedDomains: Optional<List<String>>

List of domains to allow fetching from

blockedDomains: Optional<List<String>>

List of domains to block fetching from

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional<Boolean>

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

maxContentTokens: Optional<Long>

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

exclusiveMinimum0

maxUses: Optional<Long>

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: Optional<Boolean>

class BetaToolSearchToolBm25\_20251119:

name: JsonValue; "tool\_search\_tool\_bm25"constant"tool\_search\_tool\_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: Type

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_BM25\_20251119("tool\_search\_tool\_bm25\_20251119")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional<Boolean>

class BetaToolSearchToolRegex20251119:

name: JsonValue; "tool\_search\_tool\_regex"constant"tool\_search\_tool\_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

type: Type

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_REGEX\_20251119("tool\_search\_tool\_regex\_20251119")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional<Boolean>

class BetaMcpToolset:

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcpServerName: String

Name of the MCP server to configure tools for

maxLength255

minLength1

type: JsonValue; "mcp\_toolset"constant"mcp\_toolset"constant

Accepts one of the following:

MCP\_TOOLSET("mcp\_toolset")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

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

configs: Optional<Configs>

Configuration overrides for specific tools, keyed by tool name

deferLoading: Optional<Boolean>

enabled: Optional<Boolean>

defaultConfig: Optional<[BetaMcpToolDefaultConfig](api/beta.md)>

Default configuration applied to all tools from this server

deferLoading: Optional<Boolean>

enabled: Optional<Boolean>

##### ReturnsExpand Collapse

class BetaMessageTokensCount:

contextManagement: Optional<[BetaCountTokensContextManagementResponse](api/beta.md)>

Information about context management applied to the message.

originalInputTokens: Long

The original token count before context management was applied

inputTokens: Long

The total number of tokens across the provided list of messages, system prompt, and tools.

Count tokens in a Message

Kotlin

```shiki
package com.anthropic.example

import com.anthropic.client.AnthropicClient
import com.anthropic.client.okhttp.AnthropicOkHttpClient
import com.anthropic.models.beta.messages.BetaMessageTokensCount
import com.anthropic.models.beta.messages.MessageCountTokensParams
import com.anthropic.models.messages.Model

fun main() {
    val client: AnthropicClient = AnthropicOkHttpClient.fromEnv()

    val params: MessageCountTokensParams = MessageCountTokensParams.builder()
        .addUserMessage("Hello, world")
        .model(Model.CLAUDE_OPUS_4_5_20251101)
        .build()
    val betaMessageTokensCount: BetaMessageTokensCount = client.beta().messages().countTokens(params)
}
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

---

*Copyright © Anthropic. All rights reserved.*
