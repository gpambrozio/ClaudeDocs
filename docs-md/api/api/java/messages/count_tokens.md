# Count tokens in a Message

Copy page

Java

# Count tokens in a Message

[MessageTokensCount](api/messages.md) messages().countTokens(MessageCountTokensParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

post/v1/messages/count\_tokens

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

##### ParametersExpand Collapse

MessageCountTokensParams params

List<[MessageParam](api/messages.md)> messages

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

Content content

Accepts one of the following:

String

List<[ContentBlockParam](api/messages.md)>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[TextCitationParam](api/messages.md)>> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class DocumentBlockParam:

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class ContentBlockSource:

Content content

Accepts one of the following:

String

List<[ContentBlockSourceContent](api/messages.md)>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[TextCitationParam](api/messages.md)>> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class UrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[CitationsConfigParam](api/messages.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title

class SearchResultBlockParam:

List<[TextBlockParam](api/messages.md)> content

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[TextCitationParam](api/messages.md)>> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

String source

String title

JsonValue; type "search\_result"constant"search\_result"constant

Accepts one of the following:

SEARCH\_RESULT("search\_result")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[CitationsConfigParam](api/messages.md)> citations

Optional<Boolean> enabled

class ThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class RedactedThinkingBlockParam:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class ToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class ToolResultBlockParam:

String toolUseId

JsonValue; type "tool\_result"constant"tool\_result"constant

Accepts one of the following:

TOOL\_RESULT("tool\_result")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Content> content

Accepts one of the following:

String

List<Block>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[TextCitationParam](api/messages.md)>> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class SearchResultBlockParam:

List<[TextBlockParam](api/messages.md)> content

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[TextCitationParam](api/messages.md)>> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

String source

String title

JsonValue; type "search\_result"constant"search\_result"constant

Accepts one of the following:

SEARCH\_RESULT("search\_result")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[CitationsConfigParam](api/messages.md)> citations

Optional<Boolean> enabled

class DocumentBlockParam:

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class ContentBlockSource:

Content content

Accepts one of the following:

String

List<[ContentBlockSourceContent](api/messages.md)>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[TextCitationParam](api/messages.md)>> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class UrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[CitationsConfigParam](api/messages.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title

Optional<Boolean> isError

class ServerToolUseBlockParam:

String id

Input input

JsonValue; name "web\_search"constant"web\_search"constant

Accepts one of the following:

WEB\_SEARCH("web\_search")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class WebSearchToolResultBlockParam:

[WebSearchToolResultBlockParamContent](api/messages.md) content

Accepts one of the following:

List<[WebSearchResultBlockParam](api/messages.md)>

String encryptedContent

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

String url

Optional<String> pageAge

class WebSearchToolRequestError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Role role

Accepts one of the following:

USER("user")

ASSISTANT("assistant")

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Optional<System> system

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

String

List<[TextBlockParam](api/messages.md)>

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[TextCitationParam](api/messages.md)>> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

Optional<[ThinkingConfigParam](api/messages.md)> thinking

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Optional<[ToolChoice](api/messages.md)> toolChoice

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Optional<List<[MessageCountTokensTool](api/messages.md)>> tools

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

InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonValue; type "object"constant"object"constant

Accepts one of the following:

OBJECT("object")

Optional<Properties> properties

Optional<List<String>> required

String name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<String> description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Optional<Type> type

Accepts one of the following:

CUSTOM("custom")

class ToolBash20250124:

JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

BASH("bash")

JsonValue; type "bash\_20250124"constant"bash\_20250124"constant

Accepts one of the following:

BASH\_20250124("bash\_20250124")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class ToolTextEditor20250124:

JsonValue; name "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_EDITOR("str\_replace\_editor")

JsonValue; type "text\_editor\_20250124"constant"text\_editor\_20250124"constant

Accepts one of the following:

TEXT\_EDITOR\_20250124("text\_editor\_20250124")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class ToolTextEditor20250429:

JsonValue; name "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_BASED\_EDIT\_TOOL("str\_replace\_based\_edit\_tool")

JsonValue; type "text\_editor\_20250429"constant"text\_editor\_20250429"constant

Accepts one of the following:

TEXT\_EDITOR\_20250429("text\_editor\_20250429")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class ToolTextEditor20250728:

JsonValue; name "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_BASED\_EDIT\_TOOL("str\_replace\_based\_edit\_tool")

JsonValue; type "text\_editor\_20250728"constant"text\_editor\_20250728"constant

Accepts one of the following:

TEXT\_EDITOR\_20250728("text\_editor\_20250728")

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Long> maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

class WebSearchTool20250305:

JsonValue; name "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

WEB\_SEARCH("web\_search")

JsonValue; type "web\_search\_20250305"constant"web\_search\_20250305"constant

Accepts one of the following:

WEB\_SEARCH\_20250305("web\_search\_20250305")

Optional<List<String>> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional<List<String>> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

Optional<[CacheControlEphemeral](api/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

Optional<UserLocation> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant"approximate"constant

Accepts one of the following:

APPROXIMATE("approximate")

Optional<String> city

The city of the user.

maxLength255

minLength1

Optional<String> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

Optional<String> region

The region of the user.

maxLength255

minLength1

Optional<String> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

##### ReturnsExpand Collapse

class MessageTokensCount:

long inputTokens

The total number of tokens across the provided list of messages, system prompt, and tools.

Count tokens in a Message

Java

```shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.MessageCountTokensParams;
import com.anthropic.models.messages.MessageTokensCount;
import com.anthropic.models.messages.Model;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCountTokensParams params = MessageCountTokensParams.builder()
            .addUserMessage("Hello, world")
            .model(Model.CLAUDE_OPUS_4_5_20251101)
            .build();
        MessageTokensCount messageTokensCount = client.messages().countTokens(params);
    }
}
```

Response 200

```shiki
{
  "input_tokens": 2095
}
```

##### Returns Examples

Response 200

```shiki
{
  "input_tokens": 2095
}
```