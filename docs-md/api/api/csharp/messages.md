# Messages

Copy page

C#

# Messages

##### [Create a Message](api/messages/create.md)

[Message](api/messages.md) Messages.Create(MessageCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages

##### [Count tokens in a Message](api/messages/count_tokens.md)

[MessageTokensCount](api/messages.md) Messages.CountTokens(MessageCountTokensParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class CacheControlEphemeral:

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class CacheCreation:

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsConfigParam:

Boolean Enabled

class CitationsDelta:

required Citation Citation

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

JsonElement Type "citations\_delta"constant

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class ContentBlock: A class that can be one of several variants.union

class TextBlock:

required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class ToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

class ServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

JsonElement Name "web\_search"constant

JsonElement Type "server\_tool\_use"constant

class WebSearchToolResultBlock:

required [WebSearchToolResultBlockContent](api/messages.md) Content

Accepts one of the following:

class WebSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

class ContentBlockParam: A class that can be one of several variants.union

Regular text content.

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class DocumentBlockParam:

required Source Source

Accepts one of the following:

class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class ContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

Accepts one of the following:

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title

class SearchResultBlockParam:

required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[CitationsConfigParam](api/messages.md) Citations

Boolean Enabled

class ThinkingBlockParam:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class RedactedThinkingBlockParam:

required string Data

JsonElement Type "redacted\_thinking"constant

class ToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class ToolResultBlockParam:

required string ToolUseID

JsonElement Type "tool\_result"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Content Content

Accepts one of the following:

string

IReadOnlyList<Block>

Accepts one of the following:

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class SearchResultBlockParam:

required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[CitationsConfigParam](api/messages.md) Citations

Boolean Enabled

class DocumentBlockParam:

required Source Source

Accepts one of the following:

class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class ContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

Accepts one of the following:

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title

Boolean IsError

class ServerToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

JsonElement Name "web\_search"constant

JsonElement Type "server\_tool\_use"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class WebSearchToolResultBlockParam:

required [WebSearchToolResultBlockParamContent](api/messages.md) Content

Accepts one of the following:

IReadOnlyList<[WebSearchResultBlockParam](api/messages.md)>

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge

class WebSearchToolRequestError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class ContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

Accepts one of the following:

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class ContentBlockSourceContent: A class that can be one of several variants.union

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class DocumentBlockParam:

required Source Source

Accepts one of the following:

class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class ContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

Accepts one of the following:

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class InputJsonDelta:

required string PartialJson

JsonElement Type "input\_json\_delta"constant

class JsonOutputFormat:

required IReadOnlyDictionary<string, JsonElement> Schema

The JSON schema of the format

JsonElement Type "json\_schema"constant

class Message:

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required IReadOnlyList<[ContentBlock](api/messages.md)> Content

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

required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class ToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

class ServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

JsonElement Name "web\_search"constant

JsonElement Type "server\_tool\_use"constant

class WebSearchToolResultBlock:

required [WebSearchToolResultBlockContent](api/messages.md) Content

Accepts one of the following:

class WebSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3\_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3\_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3\_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3\_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4\_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4\_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4\_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude\_3\_Opus\_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [StopReason](api/messages.md)? StopReason

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

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [Usage](api/messages.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [CacheCreation](api/messages.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

class MessageCountTokensTool: A class that can be one of several variants.union

class Tool:

required InputSchema InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

string Description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Boolean? EagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Type? Type

class ToolBash20250124:

JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash\_20250124"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250124:

JsonElement Name "str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250124"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429:

JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250429"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728:

JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250728"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Long? MaxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20250305:

JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20250305"constant

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

UserLocation? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class MessageDeltaUsage:

required Long? CacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The cumulative number of input tokens read from the cache.

required Long? InputTokens

The cumulative number of input tokens which were used.

required Long OutputTokens

The cumulative number of output tokens which were used.

required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebSearchRequests

The number of web search tool requests.

class MessageParam:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[ContentBlockParam](api/messages.md)>

Accepts one of the following:

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class DocumentBlockParam:

required Source Source

Accepts one of the following:

class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class ContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

Accepts one of the following:

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title

class SearchResultBlockParam:

required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[CitationsConfigParam](api/messages.md) Citations

Boolean Enabled

class ThinkingBlockParam:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class RedactedThinkingBlockParam:

required string Data

JsonElement Type "redacted\_thinking"constant

class ToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class ToolResultBlockParam:

required string ToolUseID

JsonElement Type "tool\_result"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Content Content

Accepts one of the following:

string

IReadOnlyList<Block>

Accepts one of the following:

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class SearchResultBlockParam:

required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[CitationsConfigParam](api/messages.md) Citations

Boolean Enabled

class DocumentBlockParam:

required Source Source

Accepts one of the following:

class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class ContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

Accepts one of the following:

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title

Boolean IsError

class ServerToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

JsonElement Name "web\_search"constant

JsonElement Type "server\_tool\_use"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class WebSearchToolResultBlockParam:

required [WebSearchToolResultBlockParamContent](api/messages.md) Content

Accepts one of the following:

IReadOnlyList<[WebSearchResultBlockParam](api/messages.md)>

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge

class WebSearchToolRequestError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

required Role Role

Accepts one of the following:

"user"User

"assistant"Assistant

class MessageTokensCount:

required Long InputTokens

The total number of tokens across the provided list of messages, system prompt, and tools.

class Metadata:

string? UserID

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

class OutputConfig:

Effort? Effort

All possible effort levels.

Accepts one of the following:

"low"Low

"medium"Medium

"high"High

"max"Max

[JsonOutputFormat](api/messages.md)? Format

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

required IReadOnlyDictionary<string, JsonElement> Schema

The JSON schema of the format

JsonElement Type "json\_schema"constant

class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class RawContentBlockDelta: A class that can be one of several variants.union

class TextDelta:

required string Text

JsonElement Type "text\_delta"constant

class InputJsonDelta:

required string PartialJson

JsonElement Type "input\_json\_delta"constant

class CitationsDelta:

required Citation Citation

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

JsonElement Type "citations\_delta"constant

class ThinkingDelta:

required string Thinking

JsonElement Type "thinking\_delta"constant

class SignatureDelta:

required string Signature

JsonElement Type "signature\_delta"constant

class RawContentBlockDeltaEvent:

required [RawContentBlockDelta](api/messages.md) Delta

Accepts one of the following:

class TextDelta:

required string Text

JsonElement Type "text\_delta"constant

class InputJsonDelta:

required string PartialJson

JsonElement Type "input\_json\_delta"constant

class CitationsDelta:

required Citation Citation

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

JsonElement Type "citations\_delta"constant

class ThinkingDelta:

required string Thinking

JsonElement Type "thinking\_delta"constant

class SignatureDelta:

required string Signature

JsonElement Type "signature\_delta"constant

required Long Index

JsonElement Type "content\_block\_delta"constant

class RawContentBlockStartEvent:

required ContentBlock ContentBlock

Accepts one of the following:

class TextBlock:

required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class ToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

class ServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

JsonElement Name "web\_search"constant

JsonElement Type "server\_tool\_use"constant

class WebSearchToolResultBlock:

required [WebSearchToolResultBlockContent](api/messages.md) Content

Accepts one of the following:

class WebSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

required Long Index

JsonElement Type "content\_block\_start"constant

class RawContentBlockStopEvent:

required Long Index

JsonElement Type "content\_block\_stop"constant

class RawMessageDeltaEvent:

required Delta Delta

required [StopReason](api/messages.md)? StopReason

Accepts one of the following:

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal

required string? StopSequence

JsonElement Type "message\_delta"constant

required [MessageDeltaUsage](api/messages.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required Long? CacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The cumulative number of input tokens read from the cache.

required Long? InputTokens

The cumulative number of input tokens which were used.

required Long OutputTokens

The cumulative number of output tokens which were used.

required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebSearchRequests

The number of web search tool requests.

class RawMessageStartEvent:

required [Message](api/messages.md) Message

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required IReadOnlyList<[ContentBlock](api/messages.md)> Content

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

required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class ToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

class ServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

JsonElement Name "web\_search"constant

JsonElement Type "server\_tool\_use"constant

class WebSearchToolResultBlock:

required [WebSearchToolResultBlockContent](api/messages.md) Content

Accepts one of the following:

class WebSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3\_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3\_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3\_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3\_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4\_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4\_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4\_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude\_3\_Opus\_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [StopReason](api/messages.md)? StopReason

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

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [Usage](api/messages.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [CacheCreation](api/messages.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

JsonElement Type "message\_start"constant

class RawMessageStopEvent:

JsonElement Type "message\_stop"constant

class RawMessageStreamEvent: A class that can be one of several variants.union

class RawMessageStartEvent:

required [Message](api/messages.md) Message

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required IReadOnlyList<[ContentBlock](api/messages.md)> Content

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

required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class ToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

class ServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

JsonElement Name "web\_search"constant

JsonElement Type "server\_tool\_use"constant

class WebSearchToolResultBlock:

required [WebSearchToolResultBlockContent](api/messages.md) Content

Accepts one of the following:

class WebSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3\_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3\_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3\_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3\_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4\_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4\_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4\_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude\_3\_Opus\_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [StopReason](api/messages.md)? StopReason

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

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [Usage](api/messages.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [CacheCreation](api/messages.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

JsonElement Type "message\_start"constant

class RawMessageDeltaEvent:

required Delta Delta

required [StopReason](api/messages.md)? StopReason

Accepts one of the following:

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal

required string? StopSequence

JsonElement Type "message\_delta"constant

required [MessageDeltaUsage](api/messages.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required Long? CacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The cumulative number of input tokens read from the cache.

required Long? InputTokens

The cumulative number of input tokens which were used.

required Long OutputTokens

The cumulative number of output tokens which were used.

required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebSearchRequests

The number of web search tool requests.

class RawMessageStopEvent:

JsonElement Type "message\_stop"constant

class RawContentBlockStartEvent:

required ContentBlock ContentBlock

Accepts one of the following:

class TextBlock:

required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class ToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

class ServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

JsonElement Name "web\_search"constant

JsonElement Type "server\_tool\_use"constant

class WebSearchToolResultBlock:

required [WebSearchToolResultBlockContent](api/messages.md) Content

Accepts one of the following:

class WebSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

required Long Index

JsonElement Type "content\_block\_start"constant

class RawContentBlockDeltaEvent:

required [RawContentBlockDelta](api/messages.md) Delta

Accepts one of the following:

class TextDelta:

required string Text

JsonElement Type "text\_delta"constant

class InputJsonDelta:

required string PartialJson

JsonElement Type "input\_json\_delta"constant

class CitationsDelta:

required Citation Citation

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

JsonElement Type "citations\_delta"constant

class ThinkingDelta:

required string Thinking

JsonElement Type "thinking\_delta"constant

class SignatureDelta:

required string Signature

JsonElement Type "signature\_delta"constant

required Long Index

JsonElement Type "content\_block\_delta"constant

class RawContentBlockStopEvent:

required Long Index

JsonElement Type "content\_block\_stop"constant

class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class RedactedThinkingBlockParam:

required string Data

JsonElement Type "redacted\_thinking"constant

class SearchResultBlockParam:

required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[CitationsConfigParam](api/messages.md) Citations

Boolean Enabled

class ServerToolUsage:

required Long WebSearchRequests

The number of web search tool requests.

class ServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

JsonElement Name "web\_search"constant

JsonElement Type "server\_tool\_use"constant

class ServerToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

JsonElement Name "web\_search"constant

JsonElement Type "server\_tool\_use"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class SignatureDelta:

required string Signature

JsonElement Type "signature\_delta"constant

enum StopReason:

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal

class TextBlock:

required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class TextCitation: A class that can be one of several variants.union

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class TextCitationParam: A class that can be one of several variants.union

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class TextDelta:

required string Text

JsonElement Type "text\_delta"constant

class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class ThinkingBlockParam:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class ThinkingConfigAdaptive:

JsonElement Type "adaptive"constant

class ThinkingConfigDisabled:

JsonElement Type "disabled"constant

class ThinkingConfigEnabled:

required Long BudgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

JsonElement Type "enabled"constant

class ThinkingConfigParam: A class that can be one of several variants.union

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

class ThinkingConfigEnabled:

required Long BudgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

JsonElement Type "enabled"constant

class ThinkingConfigDisabled:

JsonElement Type "disabled"constant

class ThinkingConfigAdaptive:

JsonElement Type "adaptive"constant

class ThinkingDelta:

required string Thinking

JsonElement Type "thinking\_delta"constant

class Tool:

required InputSchema InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

string Description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Boolean? EagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Type? Type

class ToolBash20250124:

JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash\_20250124"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class ToolChoice: A class that can be one of several variants.union

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

class ToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonElement Type "auto"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceAny:

The model will use any available tools.

JsonElement Type "any"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

required string Name

The name of the tool to use.

JsonElement Type "tool"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceNone:

The model will not be allowed to use tools.

JsonElement Type "none"constant

class ToolChoiceAny:

The model will use any available tools.

JsonElement Type "any"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonElement Type "auto"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceNone:

The model will not be allowed to use tools.

JsonElement Type "none"constant

class ToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

required string Name

The name of the tool to use.

JsonElement Type "tool"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolResultBlockParam:

required string ToolUseID

JsonElement Type "tool\_result"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Content Content

Accepts one of the following:

string

IReadOnlyList<Block>

Accepts one of the following:

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class SearchResultBlockParam:

required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[CitationsConfigParam](api/messages.md) Citations

Boolean Enabled

class DocumentBlockParam:

required Source Source

Accepts one of the following:

class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class ContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

Accepts one of the following:

class TextBlockParam:

required string Text

JsonElement Type "text"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

Accepts one of the following:

class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class ImageBlockParam:

required Source Source

Accepts one of the following:

class Base64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title

Boolean IsError

class ToolTextEditor20250124:

JsonElement Name "str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250124"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429:

JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250429"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728:

JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250728"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Long? MaxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class ToolUnion: A class that can be one of several variants.union

class Tool:

required InputSchema InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

string Description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Boolean? EagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Type? Type

class ToolBash20250124:

JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash\_20250124"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250124:

JsonElement Name "str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250124"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429:

JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250429"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728:

JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250728"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Long? MaxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20250305:

JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20250305"constant

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

UserLocation? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class ToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

class ToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class UrlImageSource:

JsonElement Type "url"constant

required string Url

class UrlPdfSource:

JsonElement Type "url"constant

required string Url

class Usage:

required [CacheCreation](api/messages.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

class WebSearchResultBlock:

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

class WebSearchResultBlockParam:

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge

class WebSearchTool20250305:

JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20250305"constant

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

UserLocation? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebSearchToolRequestError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

class WebSearchToolResultBlock:

required [WebSearchToolResultBlockContent](api/messages.md) Content

Accepts one of the following:

class WebSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

class WebSearchToolResultBlockContent: A class that can be one of several variants.union

class WebSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

class WebSearchToolResultBlockParam:

required [WebSearchToolResultBlockParamContent](api/messages.md) Content

Accepts one of the following:

IReadOnlyList<[WebSearchResultBlockParam](api/messages.md)>

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge

class WebSearchToolRequestError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class WebSearchToolResultBlockParamContent: A class that can be one of several variants.union

IReadOnlyList<[WebSearchResultBlockParam](api/messages.md)>

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge

class WebSearchToolRequestError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

class WebSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

#### MessagesBatches

##### [Create a Message Batch](api/messages/batches/create.md)

[MessageBatch](api/messages.md) Messages.Batches.Create(BatchCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/messages/batches/retrieve.md)

[MessageBatch](api/messages.md) Messages.Batches.Retrieve(BatchRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/messages/batches/list.md)

[BatchListPageResponse](api/messages.md) Messages.Batches.List(BatchListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/messages/batches

##### [Cancel a Message Batch](api/messages/batches/cancel.md)

[MessageBatch](api/messages.md) Messages.Batches.Cancel(BatchCancelParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/messages/batches/delete.md)

[DeletedMessageBatch](api/messages.md) Messages.Batches.Delete(BatchDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/messages/batches/results.md)

[MessageBatchIndividualResponse](api/messages.md) Messages.Batches.ResultsStreaming(BatchResultsParamsparameters, CancellationTokencancellationToken = default)

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

class DeletedMessageBatch:

required string ID

ID of the Message Batch.

JsonElement Type "message\_batch\_deleted"constant

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

class MessageBatch:

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required DateTimeOffset? ArchivedAt

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

required DateTimeOffset? CancelInitiatedAt

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

required DateTimeOffset CreatedAt

RFC 3339 datetime string representing the time at which the Message Batch was created.

required DateTimeOffset? EndedAt

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

required DateTimeOffset ExpiresAt

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

required ProcessingStatus ProcessingStatus

Processing status of the Message Batch.

Accepts one of the following:

"in\_progress"InProgress

"canceling"Canceling

"ended"Ended

required [MessageBatchRequestCounts](api/messages.md) RequestCounts

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

required Long Canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

required Long Errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

required Long Expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

required Long Processing

Number of requests in the Message Batch that are processing.

required Long Succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

required string? ResultsUrl

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

JsonElement Type "message\_batch"constant

Object type.

For Message Batches, this is always `"message_batch"`.

class MessageBatchCanceledResult:

JsonElement Type "canceled"constant

class MessageBatchErroredResult:

required [ErrorResponse](api/$shared.md) Error

required [ErrorObject](api/$shared.md) Error

Accepts one of the following:

class InvalidRequestError:

required string Message

JsonElement Type "invalid\_request\_error"constant

class AuthenticationError:

required string Message

JsonElement Type "authentication\_error"constant

class BillingError:

required string Message

JsonElement Type "billing\_error"constant

class PermissionError:

required string Message

JsonElement Type "permission\_error"constant

class NotFoundError:

required string Message

JsonElement Type "not\_found\_error"constant

class RateLimitError:

required string Message

JsonElement Type "rate\_limit\_error"constant

class GatewayTimeoutError:

required string Message

JsonElement Type "timeout\_error"constant

class ApiErrorObject:

required string Message

JsonElement Type "api\_error"constant

class OverloadedError:

required string Message

JsonElement Type "overloaded\_error"constant

required string? RequestID

JsonElement Type "error"constant

JsonElement Type "errored"constant

class MessageBatchExpiredResult:

JsonElement Type "expired"constant

class MessageBatchIndividualResponse:

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

required string CustomID

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

required [MessageBatchResult](api/messages.md) Result

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class MessageBatchSucceededResult:

required [Message](api/messages.md) Message

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required IReadOnlyList<[ContentBlock](api/messages.md)> Content

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

required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class ToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

class ServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

JsonElement Name "web\_search"constant

JsonElement Type "server\_tool\_use"constant

class WebSearchToolResultBlock:

required [WebSearchToolResultBlockContent](api/messages.md) Content

Accepts one of the following:

class WebSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3\_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3\_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3\_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3\_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4\_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4\_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4\_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude\_3\_Opus\_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [StopReason](api/messages.md)? StopReason

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

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [Usage](api/messages.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [CacheCreation](api/messages.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

JsonElement Type "succeeded"constant

class MessageBatchErroredResult:

required [ErrorResponse](api/$shared.md) Error

required [ErrorObject](api/$shared.md) Error

Accepts one of the following:

class InvalidRequestError:

required string Message

JsonElement Type "invalid\_request\_error"constant

class AuthenticationError:

required string Message

JsonElement Type "authentication\_error"constant

class BillingError:

required string Message

JsonElement Type "billing\_error"constant

class PermissionError:

required string Message

JsonElement Type "permission\_error"constant

class NotFoundError:

required string Message

JsonElement Type "not\_found\_error"constant

class RateLimitError:

required string Message

JsonElement Type "rate\_limit\_error"constant

class GatewayTimeoutError:

required string Message

JsonElement Type "timeout\_error"constant

class ApiErrorObject:

required string Message

JsonElement Type "api\_error"constant

class OverloadedError:

required string Message

JsonElement Type "overloaded\_error"constant

required string? RequestID

JsonElement Type "error"constant

JsonElement Type "errored"constant

class MessageBatchCanceledResult:

JsonElement Type "canceled"constant

class MessageBatchExpiredResult:

JsonElement Type "expired"constant

class MessageBatchRequestCounts:

required Long Canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

required Long Errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

required Long Expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

required Long Processing

Number of requests in the Message Batch that are processing.

required Long Succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

class MessageBatchResult: A class that can be one of several variants.union

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

class MessageBatchSucceededResult:

required [Message](api/messages.md) Message

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required IReadOnlyList<[ContentBlock](api/messages.md)> Content

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

required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class ToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

class ServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

JsonElement Name "web\_search"constant

JsonElement Type "server\_tool\_use"constant

class WebSearchToolResultBlock:

required [WebSearchToolResultBlockContent](api/messages.md) Content

Accepts one of the following:

class WebSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3\_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3\_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3\_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3\_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4\_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4\_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4\_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude\_3\_Opus\_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [StopReason](api/messages.md)? StopReason

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

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [Usage](api/messages.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [CacheCreation](api/messages.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

JsonElement Type "succeeded"constant

class MessageBatchErroredResult:

required [ErrorResponse](api/$shared.md) Error

required [ErrorObject](api/$shared.md) Error

Accepts one of the following:

class InvalidRequestError:

required string Message

JsonElement Type "invalid\_request\_error"constant

class AuthenticationError:

required string Message

JsonElement Type "authentication\_error"constant

class BillingError:

required string Message

JsonElement Type "billing\_error"constant

class PermissionError:

required string Message

JsonElement Type "permission\_error"constant

class NotFoundError:

required string Message

JsonElement Type "not\_found\_error"constant

class RateLimitError:

required string Message

JsonElement Type "rate\_limit\_error"constant

class GatewayTimeoutError:

required string Message

JsonElement Type "timeout\_error"constant

class ApiErrorObject:

required string Message

JsonElement Type "api\_error"constant

class OverloadedError:

required string Message

JsonElement Type "overloaded\_error"constant

required string? RequestID

JsonElement Type "error"constant

JsonElement Type "errored"constant

class MessageBatchCanceledResult:

JsonElement Type "canceled"constant

class MessageBatchExpiredResult:

JsonElement Type "expired"constant

class MessageBatchSucceededResult:

required [Message](api/messages.md) Message

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required IReadOnlyList<[ContentBlock](api/messages.md)> Content

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

required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class CitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class CitationsSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class ToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

class ServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

JsonElement Name "web\_search"constant

JsonElement Type "server\_tool\_use"constant

class WebSearchToolResultBlock:

required [WebSearchToolResultBlockContent](api/messages.md) Content

Accepts one of the following:

class WebSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3\_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3\_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3\_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3\_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4\_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4\_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4\_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude\_3\_Opus\_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [StopReason](api/messages.md)? StopReason

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

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [Usage](api/messages.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [CacheCreation](api/messages.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

JsonElement Type "succeeded"constant

---

*Copyright © Anthropic. All rights reserved.*
