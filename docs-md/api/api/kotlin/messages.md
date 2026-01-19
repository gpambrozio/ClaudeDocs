# Messages

Copy page

Kotlin

# Messages

##### [Create a Message](api/messages/create.md)

messages().create(MessageCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none()) : [Message](api/messages.md)

post/v1/messages

##### [Count tokens in a Message](api/messages/count_tokens.md)

messages().countTokens(MessageCountTokensParamsparams, RequestOptionsrequestOptions = RequestOptions.none()) : [MessageTokensCount](api/messages.md)

post/v1/messages/count\_tokens

##### ModelsExpand Collapse

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

class Base64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class CacheControlEphemeral:

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

class CacheCreation:

ephemeral1hInputTokens: Long

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral5mInputTokens: Long

The number of input tokens used to create the 5 minute cache entry.

minimum0

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

class CitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

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

class CitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

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

class CitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

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

class CitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class CitationsConfigParam:

enabled: Optional<Boolean>

class CitationsDelta:

citation: Citation

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

type: JsonValue; "citations\_delta"constant"citations\_delta"constant

Accepts one of the following:

CITATIONS\_DELTA("citations\_delta")

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

class CitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class ContentBlock: A class that can be one of several variants.union

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

class ContentBlockParam: A class that can be one of several variants.union

Regular text content.

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

class ContentBlockSourceContent: A class that can be one of several variants.union

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

class InputJsonDelta:

partialJson: String

type: JsonValue; "input\_json\_delta"constant"input\_json\_delta"constant

Accepts one of the following:

INPUT\_JSON\_DELTA("input\_json\_delta")

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

class MessageCountTokensTool: A class that can be one of several variants.union

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

class MessageDeltaUsage:

cacheCreationInputTokens: Optional<Long>

The cumulative number of input tokens used to create the cache entry.

minimum0

cacheReadInputTokens: Optional<Long>

The cumulative number of input tokens read from the cache.

minimum0

inputTokens: Optional<Long>

The cumulative number of input tokens which were used.

minimum0

outputTokens: Long

The cumulative number of output tokens which were used.

serverToolUse: Optional<[ServerToolUsage](api/messages.md)>

The number of server tool requests.

webSearchRequests: Long

The number of web search tool requests.

minimum0

class MessageParam:

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

class MessageTokensCount:

inputTokens: Long

The total number of tokens across the provided list of messages, system prompt, and tools.

class Metadata:

userId: Optional<String>

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

class PlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class RawContentBlockDelta: A class that can be one of several variants.union

class TextDelta:

text: String

type: JsonValue; "text\_delta"constant"text\_delta"constant

Accepts one of the following:

TEXT\_DELTA("text\_delta")

class InputJsonDelta:

partialJson: String

type: JsonValue; "input\_json\_delta"constant"input\_json\_delta"constant

Accepts one of the following:

INPUT\_JSON\_DELTA("input\_json\_delta")

class CitationsDelta:

citation: Citation

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

type: JsonValue; "citations\_delta"constant"citations\_delta"constant

Accepts one of the following:

CITATIONS\_DELTA("citations\_delta")

class ThinkingDelta:

thinking: String

type: JsonValue; "thinking\_delta"constant"thinking\_delta"constant

Accepts one of the following:

THINKING\_DELTA("thinking\_delta")

class SignatureDelta:

signature: String

type: JsonValue; "signature\_delta"constant"signature\_delta"constant

Accepts one of the following:

SIGNATURE\_DELTA("signature\_delta")

class RawContentBlockDeltaEvent:

delta: [RawContentBlockDelta](api/messages.md)

Accepts one of the following:

class TextDelta:

text: String

type: JsonValue; "text\_delta"constant"text\_delta"constant

Accepts one of the following:

TEXT\_DELTA("text\_delta")

class InputJsonDelta:

partialJson: String

type: JsonValue; "input\_json\_delta"constant"input\_json\_delta"constant

Accepts one of the following:

INPUT\_JSON\_DELTA("input\_json\_delta")

class CitationsDelta:

citation: Citation

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

type: JsonValue; "citations\_delta"constant"citations\_delta"constant

Accepts one of the following:

CITATIONS\_DELTA("citations\_delta")

class ThinkingDelta:

thinking: String

type: JsonValue; "thinking\_delta"constant"thinking\_delta"constant

Accepts one of the following:

THINKING\_DELTA("thinking\_delta")

class SignatureDelta:

signature: String

type: JsonValue; "signature\_delta"constant"signature\_delta"constant

Accepts one of the following:

SIGNATURE\_DELTA("signature\_delta")

index: Long

type: JsonValue; "content\_block\_delta"constant"content\_block\_delta"constant

Accepts one of the following:

CONTENT\_BLOCK\_DELTA("content\_block\_delta")

class RawContentBlockStartEvent:

contentBlock: ContentBlock

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

index: Long

type: JsonValue; "content\_block\_start"constant"content\_block\_start"constant

Accepts one of the following:

CONTENT\_BLOCK\_START("content\_block\_start")

class RawContentBlockStopEvent:

index: Long

type: JsonValue; "content\_block\_stop"constant"content\_block\_stop"constant

Accepts one of the following:

CONTENT\_BLOCK\_STOP("content\_block\_stop")

class RawMessageDeltaEvent:

delta: Delta

stopReason: Optional<[StopReason](api/messages.md)>

Accepts one of the following:

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

REFUSAL("refusal")

stopSequence: Optional<String>

type: JsonValue; "message\_delta"constant"message\_delta"constant

Accepts one of the following:

MESSAGE\_DELTA("message\_delta")

usage: [MessageDeltaUsage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cacheCreationInputTokens: Optional<Long>

The cumulative number of input tokens used to create the cache entry.

minimum0

cacheReadInputTokens: Optional<Long>

The cumulative number of input tokens read from the cache.

minimum0

inputTokens: Optional<Long>

The cumulative number of input tokens which were used.

minimum0

outputTokens: Long

The cumulative number of output tokens which were used.

serverToolUse: Optional<[ServerToolUsage](api/messages.md)>

The number of server tool requests.

webSearchRequests: Long

The number of web search tool requests.

minimum0

class RawMessageStartEvent:

message: [Message](api/messages.md)

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

type: JsonValue; "message\_start"constant"message\_start"constant

Accepts one of the following:

MESSAGE\_START("message\_start")

class RawMessageStopEvent:

type: JsonValue; "message\_stop"constant"message\_stop"constant

Accepts one of the following:

MESSAGE\_STOP("message\_stop")

class RawMessageStreamEvent: A class that can be one of several variants.union

class RawMessageStartEvent:

message: [Message](api/messages.md)

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

type: JsonValue; "message\_start"constant"message\_start"constant

Accepts one of the following:

MESSAGE\_START("message\_start")

class RawMessageDeltaEvent:

delta: Delta

stopReason: Optional<[StopReason](api/messages.md)>

Accepts one of the following:

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

REFUSAL("refusal")

stopSequence: Optional<String>

type: JsonValue; "message\_delta"constant"message\_delta"constant

Accepts one of the following:

MESSAGE\_DELTA("message\_delta")

usage: [MessageDeltaUsage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cacheCreationInputTokens: Optional<Long>

The cumulative number of input tokens used to create the cache entry.

minimum0

cacheReadInputTokens: Optional<Long>

The cumulative number of input tokens read from the cache.

minimum0

inputTokens: Optional<Long>

The cumulative number of input tokens which were used.

minimum0

outputTokens: Long

The cumulative number of output tokens which were used.

serverToolUse: Optional<[ServerToolUsage](api/messages.md)>

The number of server tool requests.

webSearchRequests: Long

The number of web search tool requests.

minimum0

class RawMessageStopEvent:

type: JsonValue; "message\_stop"constant"message\_stop"constant

Accepts one of the following:

MESSAGE\_STOP("message\_stop")

class RawContentBlockStartEvent:

contentBlock: ContentBlock

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

index: Long

type: JsonValue; "content\_block\_start"constant"content\_block\_start"constant

Accepts one of the following:

CONTENT\_BLOCK\_START("content\_block\_start")

class RawContentBlockDeltaEvent:

delta: [RawContentBlockDelta](api/messages.md)

Accepts one of the following:

class TextDelta:

text: String

type: JsonValue; "text\_delta"constant"text\_delta"constant

Accepts one of the following:

TEXT\_DELTA("text\_delta")

class InputJsonDelta:

partialJson: String

type: JsonValue; "input\_json\_delta"constant"input\_json\_delta"constant

Accepts one of the following:

INPUT\_JSON\_DELTA("input\_json\_delta")

class CitationsDelta:

citation: Citation

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

type: JsonValue; "citations\_delta"constant"citations\_delta"constant

Accepts one of the following:

CITATIONS\_DELTA("citations\_delta")

class ThinkingDelta:

thinking: String

type: JsonValue; "thinking\_delta"constant"thinking\_delta"constant

Accepts one of the following:

THINKING\_DELTA("thinking\_delta")

class SignatureDelta:

signature: String

type: JsonValue; "signature\_delta"constant"signature\_delta"constant

Accepts one of the following:

SIGNATURE\_DELTA("signature\_delta")

index: Long

type: JsonValue; "content\_block\_delta"constant"content\_block\_delta"constant

Accepts one of the following:

CONTENT\_BLOCK\_DELTA("content\_block\_delta")

class RawContentBlockStopEvent:

index: Long

type: JsonValue; "content\_block\_stop"constant"content\_block\_stop"constant

Accepts one of the following:

CONTENT\_BLOCK\_STOP("content\_block\_stop")

class RedactedThinkingBlock:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class RedactedThinkingBlockParam:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

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

class ServerToolUsage:

webSearchRequests: Long

The number of web search tool requests.

minimum0

class ServerToolUseBlock:

id: String

input: Input

name: JsonValue; "web\_search"constant"web\_search"constant

Accepts one of the following:

WEB\_SEARCH("web\_search")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

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

class SignatureDelta:

signature: String

type: JsonValue; "signature\_delta"constant"signature\_delta"constant

Accepts one of the following:

SIGNATURE\_DELTA("signature\_delta")

enum class StopReason:

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

REFUSAL("refusal")

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

class TextCitation: A class that can be one of several variants.union

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

class TextCitationParam: A class that can be one of several variants.union

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

class TextDelta:

text: String

type: JsonValue; "text\_delta"constant"text\_delta"constant

Accepts one of the following:

TEXT\_DELTA("text\_delta")

class ThinkingBlock:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class ThinkingBlockParam:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class ThinkingConfigDisabled:

type: JsonValue; "disabled"constant"disabled"constant

Accepts one of the following:

DISABLED("disabled")

class ThinkingConfigEnabled:

budgetTokens: Long

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: JsonValue; "enabled"constant"enabled"constant

Accepts one of the following:

ENABLED("enabled")

class ThinkingConfigParam: A class that can be one of several variants.union

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

class ThinkingConfigEnabled:

budgetTokens: Long

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: JsonValue; "enabled"constant"enabled"constant

Accepts one of the following:

ENABLED("enabled")

class ThinkingConfigDisabled:

type: JsonValue; "disabled"constant"disabled"constant

Accepts one of the following:

DISABLED("disabled")

class ThinkingDelta:

thinking: String

type: JsonValue; "thinking\_delta"constant"thinking\_delta"constant

Accepts one of the following:

THINKING\_DELTA("thinking\_delta")

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

class ToolChoice: A class that can be one of several variants.union

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

class ToolChoiceAuto:

The model will automatically decide whether to use tools.

type: JsonValue; "auto"constant"auto"constant

Accepts one of the following:

AUTO("auto")

disableParallelToolUse: Optional<Boolean>

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceAny:

The model will use any available tools.

type: JsonValue; "any"constant"any"constant

Accepts one of the following:

ANY("any")

disableParallelToolUse: Optional<Boolean>

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: JsonValue; "tool"constant"tool"constant

Accepts one of the following:

TOOL("tool")

disableParallelToolUse: Optional<Boolean>

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceNone:

The model will not be allowed to use tools.

type: JsonValue; "none"constant"none"constant

Accepts one of the following:

NONE("none")

class ToolChoiceAny:

The model will use any available tools.

type: JsonValue; "any"constant"any"constant

Accepts one of the following:

ANY("any")

disableParallelToolUse: Optional<Boolean>

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceAuto:

The model will automatically decide whether to use tools.

type: JsonValue; "auto"constant"auto"constant

Accepts one of the following:

AUTO("auto")

disableParallelToolUse: Optional<Boolean>

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceNone:

The model will not be allowed to use tools.

type: JsonValue; "none"constant"none"constant

Accepts one of the following:

NONE("none")

class ToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: JsonValue; "tool"constant"tool"constant

Accepts one of the following:

TOOL("tool")

disableParallelToolUse: Optional<Boolean>

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

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

class ToolUnion: A class that can be one of several variants.union

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

class ToolUseBlock:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

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

class UrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class UrlPdfSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class Usage:

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

class WebSearchResultBlock:

encryptedContent: String

pageAge: Optional<String>

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

class WebSearchResultBlockParam:

encryptedContent: String

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

pageAge: Optional<String>

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

class WebSearchToolResultBlockContent: A class that can be one of several variants.union

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

class WebSearchToolResultBlockParamContent: A class that can be one of several variants.union

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

#### MessagesBatches

##### [Create a Message Batch](api/messages/batches/create.md)

messages().batches().create(BatchCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none()) : [MessageBatch](api/messages.md)

post/v1/messages/batches

##### [Retrieve a Message Batch](api/messages/batches/retrieve.md)

messages().batches().retrieve(BatchRetrieveParamsparams = BatchRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [MessageBatch](api/messages.md)

get/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/messages/batches/list.md)

messages().batches().list(BatchListParamsparams = BatchListParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : BatchListPage

get/v1/messages/batches

##### [Cancel a Message Batch](api/messages/batches/cancel.md)

messages().batches().cancel(BatchCancelParamsparams = BatchCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [MessageBatch](api/messages.md)

post/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/messages/batches/delete.md)

messages().batches().delete(BatchDeleteParamsparams = BatchDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [DeletedMessageBatch](api/messages.md)

delete/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/messages/batches/results.md)

messages().batches().resultsStreaming(BatchResultsParamsparams = BatchResultsParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [MessageBatchIndividualResponse](api/messages.md)

get/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

class DeletedMessageBatch:

id: String

ID of the Message Batch.

type: JsonValue; "message\_batch\_deleted"constant"message\_batch\_deleted"constant

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

MESSAGE\_BATCH\_DELETED("message\_batch\_deleted")

class MessageBatch:

id: String

Unique object identifier.

The format and length of IDs may change over time.

archivedAt: Optional<LocalDateTime>

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

formatdate-time

cancelInitiatedAt: Optional<LocalDateTime>

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

formatdate-time

createdAt: LocalDateTime

RFC 3339 datetime string representing the time at which the Message Batch was created.

formatdate-time

endedAt: Optional<LocalDateTime>

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expiresAt: LocalDateTime

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

formatdate-time

processingStatus: ProcessingStatus

Processing status of the Message Batch.

Accepts one of the following:

IN\_PROGRESS("in\_progress")

CANCELING("canceling")

ENDED("ended")

requestCounts: [MessageBatchRequestCounts](api/messages.md)

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

canceled: Long

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: Long

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: Long

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Long

Number of requests in the Message Batch that are processing.

succeeded: Long

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

resultsUrl: Optional<String>

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: JsonValue; "message\_batch"constant"message\_batch"constant

Object type.

For Message Batches, this is always `"message_batch"`.

Accepts one of the following:

MESSAGE\_BATCH("message\_batch")

class MessageBatchCanceledResult:

type: JsonValue; "canceled"constant"canceled"constant

Accepts one of the following:

CANCELED("canceled")

class MessageBatchErroredResult:

error: [ErrorResponse](api/$shared.md)

error: [ErrorObject](api/$shared.md)

Accepts one of the following:

class InvalidRequestError:

message: String

type: JsonValue; "invalid\_request\_error"constant"invalid\_request\_error"constant

Accepts one of the following:

INVALID\_REQUEST\_ERROR("invalid\_request\_error")

class AuthenticationError:

message: String

type: JsonValue; "authentication\_error"constant"authentication\_error"constant

Accepts one of the following:

AUTHENTICATION\_ERROR("authentication\_error")

class BillingError:

message: String

type: JsonValue; "billing\_error"constant"billing\_error"constant

Accepts one of the following:

BILLING\_ERROR("billing\_error")

class PermissionError:

message: String

type: JsonValue; "permission\_error"constant"permission\_error"constant

Accepts one of the following:

PERMISSION\_ERROR("permission\_error")

class NotFoundError:

message: String

type: JsonValue; "not\_found\_error"constant"not\_found\_error"constant

Accepts one of the following:

NOT\_FOUND\_ERROR("not\_found\_error")

class RateLimitError:

message: String

type: JsonValue; "rate\_limit\_error"constant"rate\_limit\_error"constant

Accepts one of the following:

RATE\_LIMIT\_ERROR("rate\_limit\_error")

class GatewayTimeoutError:

message: String

type: JsonValue; "timeout\_error"constant"timeout\_error"constant

Accepts one of the following:

TIMEOUT\_ERROR("timeout\_error")

class ApiErrorObject:

message: String

type: JsonValue; "api\_error"constant"api\_error"constant

Accepts one of the following:

API\_ERROR("api\_error")

class OverloadedError:

message: String

type: JsonValue; "overloaded\_error"constant"overloaded\_error"constant

Accepts one of the following:

OVERLOADED\_ERROR("overloaded\_error")

requestId: Optional<String>

type: JsonValue; "error"constant"error"constant

Accepts one of the following:

ERROR("error")

type: JsonValue; "errored"constant"errored"constant

Accepts one of the following:

ERRORED("errored")

class MessageBatchExpiredResult:

type: JsonValue; "expired"constant"expired"constant

Accepts one of the following:

EXPIRED("expired")

class MessageBatchIndividualResponse:

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

customId: String

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [MessageBatchResult](api/messages.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class MessageBatchSucceededResult:

message: [Message](api/messages.md)

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

type: JsonValue; "succeeded"constant"succeeded"constant

Accepts one of the following:

SUCCEEDED("succeeded")

class MessageBatchErroredResult:

error: [ErrorResponse](api/$shared.md)

error: [ErrorObject](api/$shared.md)

Accepts one of the following:

class InvalidRequestError:

message: String

type: JsonValue; "invalid\_request\_error"constant"invalid\_request\_error"constant

Accepts one of the following:

INVALID\_REQUEST\_ERROR("invalid\_request\_error")

class AuthenticationError:

message: String

type: JsonValue; "authentication\_error"constant"authentication\_error"constant

Accepts one of the following:

AUTHENTICATION\_ERROR("authentication\_error")

class BillingError:

message: String

type: JsonValue; "billing\_error"constant"billing\_error"constant

Accepts one of the following:

BILLING\_ERROR("billing\_error")

class PermissionError:

message: String

type: JsonValue; "permission\_error"constant"permission\_error"constant

Accepts one of the following:

PERMISSION\_ERROR("permission\_error")

class NotFoundError:

message: String

type: JsonValue; "not\_found\_error"constant"not\_found\_error"constant

Accepts one of the following:

NOT\_FOUND\_ERROR("not\_found\_error")

class RateLimitError:

message: String

type: JsonValue; "rate\_limit\_error"constant"rate\_limit\_error"constant

Accepts one of the following:

RATE\_LIMIT\_ERROR("rate\_limit\_error")

class GatewayTimeoutError:

message: String

type: JsonValue; "timeout\_error"constant"timeout\_error"constant

Accepts one of the following:

TIMEOUT\_ERROR("timeout\_error")

class ApiErrorObject:

message: String

type: JsonValue; "api\_error"constant"api\_error"constant

Accepts one of the following:

API\_ERROR("api\_error")

class OverloadedError:

message: String

type: JsonValue; "overloaded\_error"constant"overloaded\_error"constant

Accepts one of the following:

OVERLOADED\_ERROR("overloaded\_error")

requestId: Optional<String>

type: JsonValue; "error"constant"error"constant

Accepts one of the following:

ERROR("error")

type: JsonValue; "errored"constant"errored"constant

Accepts one of the following:

ERRORED("errored")

class MessageBatchCanceledResult:

type: JsonValue; "canceled"constant"canceled"constant

Accepts one of the following:

CANCELED("canceled")

class MessageBatchExpiredResult:

type: JsonValue; "expired"constant"expired"constant

Accepts one of the following:

EXPIRED("expired")

class MessageBatchRequestCounts:

canceled: Long

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: Long

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: Long

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Long

Number of requests in the Message Batch that are processing.

succeeded: Long

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

class MessageBatchResult: A class that can be one of several variants.union

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

class MessageBatchSucceededResult:

message: [Message](api/messages.md)

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

type: JsonValue; "succeeded"constant"succeeded"constant

Accepts one of the following:

SUCCEEDED("succeeded")

class MessageBatchErroredResult:

error: [ErrorResponse](api/$shared.md)

error: [ErrorObject](api/$shared.md)

Accepts one of the following:

class InvalidRequestError:

message: String

type: JsonValue; "invalid\_request\_error"constant"invalid\_request\_error"constant

Accepts one of the following:

INVALID\_REQUEST\_ERROR("invalid\_request\_error")

class AuthenticationError:

message: String

type: JsonValue; "authentication\_error"constant"authentication\_error"constant

Accepts one of the following:

AUTHENTICATION\_ERROR("authentication\_error")

class BillingError:

message: String

type: JsonValue; "billing\_error"constant"billing\_error"constant

Accepts one of the following:

BILLING\_ERROR("billing\_error")

class PermissionError:

message: String

type: JsonValue; "permission\_error"constant"permission\_error"constant

Accepts one of the following:

PERMISSION\_ERROR("permission\_error")

class NotFoundError:

message: String

type: JsonValue; "not\_found\_error"constant"not\_found\_error"constant

Accepts one of the following:

NOT\_FOUND\_ERROR("not\_found\_error")

class RateLimitError:

message: String

type: JsonValue; "rate\_limit\_error"constant"rate\_limit\_error"constant

Accepts one of the following:

RATE\_LIMIT\_ERROR("rate\_limit\_error")

class GatewayTimeoutError:

message: String

type: JsonValue; "timeout\_error"constant"timeout\_error"constant

Accepts one of the following:

TIMEOUT\_ERROR("timeout\_error")

class ApiErrorObject:

message: String

type: JsonValue; "api\_error"constant"api\_error"constant

Accepts one of the following:

API\_ERROR("api\_error")

class OverloadedError:

message: String

type: JsonValue; "overloaded\_error"constant"overloaded\_error"constant

Accepts one of the following:

OVERLOADED\_ERROR("overloaded\_error")

requestId: Optional<String>

type: JsonValue; "error"constant"error"constant

Accepts one of the following:

ERROR("error")

type: JsonValue; "errored"constant"errored"constant

Accepts one of the following:

ERRORED("errored")

class MessageBatchCanceledResult:

type: JsonValue; "canceled"constant"canceled"constant

Accepts one of the following:

CANCELED("canceled")

class MessageBatchExpiredResult:

type: JsonValue; "expired"constant"expired"constant

Accepts one of the following:

EXPIRED("expired")

class MessageBatchSucceededResult:

message: [Message](api/messages.md)

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

type: JsonValue; "succeeded"constant"succeeded"constant

Accepts one of the following:

SUCCEEDED("succeeded")

---

*Copyright © Anthropic. All rights reserved.*
