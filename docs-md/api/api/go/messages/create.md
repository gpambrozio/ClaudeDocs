# Create a Message

Copy page

Go

# Create a Message

client.Messages.New(ctx, body) (\*[Message](api/messages.md), error)

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)

##### ParametersExpand Collapse

body MessageNewParams

MaxTokens param.Field[int64]

The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.

minimum1

Messages param.Field[[][MessageParamResp](api/messages.md)]

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

Content [][ContentBlockParamUnionResp](api/messages.md)

Accepts one of the following:

[][ContentBlockParamUnionResp](api/messages.md)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [][TextCitationParamUnionResp](api/messages.md)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type DocumentBlockParamResp struct{…}

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

[][ContentBlockSourceContentItemUnion](api/messages.md)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [][TextCitationParamUnionResp](api/messages.md)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

type URLPDFSource struct{…}

Type URL

URL string

Type Document

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](api/messages.md)optional

Enabled booloptional

Context stringoptional

Title stringoptional

type SearchResultBlockParamResp struct{…}

Content [][TextBlockParamResp](api/messages.md)

Text string

Type Text

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [][TextCitationParamUnionResp](api/messages.md)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Source string

Title string

Type SearchResult

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](api/messages.md)optional

Enabled booloptional

type ThinkingBlockParamResp struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlockParamResp struct{…}

Data string

Type RedactedThinking

type ToolUseBlockParamResp struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller ToolUseBlockParamCallerUnionRespoptional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type ToolResultBlockParamResp struct{…}

ToolUseID string

Type ToolResult

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Content []ToolResultBlockParamContentUnionRespoptional

Accepts one of the following:

[]ToolResultBlockParamContentUnionResp

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [][TextCitationParamUnionResp](api/messages.md)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type SearchResultBlockParamResp struct{…}

Content [][TextBlockParamResp](api/messages.md)

Text string

Type Text

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [][TextCitationParamUnionResp](api/messages.md)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Source string

Title string

Type SearchResult

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](api/messages.md)optional

Enabled booloptional

type DocumentBlockParamResp struct{…}

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

[][ContentBlockSourceContentItemUnion](api/messages.md)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [][TextCitationParamUnionResp](api/messages.md)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

type URLPDFSource struct{…}

Type URL

URL string

Type Document

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](api/messages.md)optional

Enabled booloptional

Context stringoptional

Title stringoptional

type ToolReferenceBlockParamResp struct{…}

Tool reference block that can be included in tool\_result content.

ToolName string

Type ToolReference

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

IsError booloptional

type ServerToolUseBlockParamResp struct{…}

ID string

Input map[string, any]

Name ServerToolUseBlockParamName

Accepts one of the following:

const ServerToolUseBlockParamNameWebSearch ServerToolUseBlockParamName = "web\_search"

const ServerToolUseBlockParamNameWebFetch ServerToolUseBlockParamName = "web\_fetch"

const ServerToolUseBlockParamNameCodeExecution ServerToolUseBlockParamName = "code\_execution"

const ServerToolUseBlockParamNameBashCodeExecution ServerToolUseBlockParamName = "bash\_code\_execution"

const ServerToolUseBlockParamNameTextEditorCodeExecution ServerToolUseBlockParamName = "text\_editor\_code\_execution"

const ServerToolUseBlockParamNameToolSearchToolRegex ServerToolUseBlockParamName = "tool\_search\_tool\_regex"

const ServerToolUseBlockParamNameToolSearchToolBm25 ServerToolUseBlockParamName = "tool\_search\_tool\_bm25"

Type ServerToolUse

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller ServerToolUseBlockParamCallerUnionRespoptional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type WebSearchToolResultBlockParamResp struct{…}

Content [WebSearchToolResultBlockParamContentUnionResp](api/messages.md)

Accepts one of the following:

[][WebSearchResultBlockParamResp](api/messages.md)

EncryptedContent string

Title string

Type WebSearchResult

URL string

PageAge stringoptional

type WebSearchToolRequestError struct{…}

ErrorCode [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](api/messages.md) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](api/messages.md) = "max\_uses\_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](api/messages.md) = "query\_too\_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](api/messages.md) = "request\_too\_large"

Type WebSearchToolResultError

ToolUseID string

Type WebSearchToolResult

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller WebSearchToolResultBlockParamCallerUnionRespoptional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type WebFetchToolResultBlockParamResp struct{…}

Content WebFetchToolResultBlockParamContentUnionResp

Accepts one of the following:

type WebFetchToolResultErrorBlockParamResp struct{…}

ErrorCode [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](api/messages.md) = "url\_too\_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](api/messages.md) = "unsupported\_content\_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](api/messages.md) = "max\_uses\_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](api/messages.md) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlockParamResp struct{…}

Content [DocumentBlockParamResp](api/messages.md)

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

[][ContentBlockSourceContentItemUnion](api/messages.md)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [][TextCitationParamUnionResp](api/messages.md)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

type URLPDFSource struct{…}

Type URL

URL string

Type Document

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](api/messages.md)optional

Enabled booloptional

Context stringoptional

Title stringoptional

Type WebFetchResult

URL string

Fetched content URL

RetrievedAt stringoptional

ISO 8601 timestamp when the content was retrieved

ToolUseID string

Type WebFetchToolResult

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller WebFetchToolResultBlockParamCallerUnionRespoptional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type CodeExecutionToolResultBlockParamResp struct{…}

Content [CodeExecutionToolResultBlockParamContentUnionResp](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

type CodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlockParamResp struct{…}

Content [][CodeExecutionOutputBlockParamResp](api/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlockParamResp struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.

Content [][CodeExecutionOutputBlockParamResp](api/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type BashCodeExecutionToolResultBlockParamResp struct{…}

Content BashCodeExecutionToolResultBlockParamContentUnionResp

Accepts one of the following:

type BashCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](api/messages.md) = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlockParamResp struct{…}

Content [][BashCodeExecutionOutputBlockParamResp](api/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type TextEditorCodeExecutionToolResultBlockParamResp struct{…}

Content TextEditorCodeExecutionToolResultBlockParamContentUnionResp

Accepts one of the following:

type TextEditorCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "file\_not\_found"

Type TextEditorCodeExecutionToolResultError

ErrorMessage stringoptional

type TextEditorCodeExecutionViewResultBlockParamResp struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockParamFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockParamFileTypeText TextEditorCodeExecutionViewResultBlockParamFileType = "text"

const TextEditorCodeExecutionViewResultBlockParamFileTypeImage TextEditorCodeExecutionViewResultBlockParamFileType = "image"

const TextEditorCodeExecutionViewResultBlockParamFileTypePDF TextEditorCodeExecutionViewResultBlockParamFileType = "pdf"

Type TextEditorCodeExecutionViewResult

NumLines int64optional

StartLine int64optional

TotalLines int64optional

type TextEditorCodeExecutionCreateResultBlockParamResp struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}

Type TextEditorCodeExecutionStrReplaceResult

Lines []stringoptional

NewLines int64optional

NewStart int64optional

OldLines int64optional

OldStart int64optional

ToolUseID string

Type TextEditorCodeExecutionToolResult

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type ToolSearchToolResultBlockParamResp struct{…}

Content ToolSearchToolResultBlockParamContentUnionResp

Accepts one of the following:

type ToolSearchToolResultErrorParamResp struct{…}

ErrorCode [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](api/messages.md) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlockParamResp struct{…}

ToolReferences [][ToolReferenceBlockParamResp](api/messages.md)

ToolName string

Type ToolReference

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type ContainerUploadBlockParamResp struct{…}

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

FileID string

Type ContainerUpload

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Role MessageParamRole

Accepts one of the following:

const MessageParamRoleUser MessageParamRole = "user"

const MessageParamRoleAssistant MessageParamRole = "assistant"

Model param.Field[Model]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

CacheControl param.Field[[CacheControlEphemeral](api/messages.md)]optional

Top-level cache control automatically applies a cache\_control marker to the last cacheable block in the request.

Container param.Field[string]optional

Container identifier for reuse across requests.

InferenceGeo param.Field[string]optional

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

Metadata param.Field[[Metadata](api/messages.md)]optional

An object describing metadata about the request.

OutputConfig param.Field[[OutputConfig](api/messages.md)]optional

Configuration options for the model's output, such as the output format.

ServiceTier param.Field[[MessageNewParamsServiceTier](api/messages/create.md)]optional

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

const MessageNewParamsServiceTierAuto [MessageNewParamsServiceTier](api/messages/create.md) = "auto"

const MessageNewParamsServiceTierStandardOnly [MessageNewParamsServiceTier](api/messages/create.md) = "standard\_only"

StopSequences param.Field[[]string]optional

Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

System param.Field[[][TextBlockParamResp](api/messages.md)]optional

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

[][TextBlockParam](api/messages.md)

Text string

Type Text

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [][TextCitationParamUnionResp](api/messages.md)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Temperature param.Field[float64]optional

Amount of randomness injected into the response.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0

Thinking param.Field[[ThinkingConfigParamUnionResp](api/messages.md)]optional

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

ToolChoice param.Field[[ToolChoiceUnion](api/messages.md)]optional

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Tools param.Field[[][ToolUnion](api/messages.md)]optional

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

type Tool struct{…}

InputSchema ToolInputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

Type Object

Properties map[string, any]optional

Required []stringoptional

Name string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

AllowedCallers []stringoptional

Accepts one of the following:

const ToolAllowedCallerDirect ToolAllowedCaller = "direct"

const ToolAllowedCallerCodeExecution20250825 ToolAllowedCaller = "code\_execution\_20250825"

const ToolAllowedCallerCodeExecution20260120 ToolAllowedCaller = "code\_execution\_20260120"

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Description stringoptional

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

EagerInputStreaming booloptional

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

InputExamples []map[string, any]optional

Strict booloptional

When true, guarantees schema validation on tool names and inputs

Type ToolTypeoptional

type ToolBash20250124 struct{…}

Name Bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Bash20250124

AllowedCallers []stringoptional

Accepts one of the following:

const ToolBash20250124AllowedCallerDirect ToolBash20250124AllowedCaller = "direct"

const ToolBash20250124AllowedCallerCodeExecution20250825 ToolBash20250124AllowedCaller = "code\_execution\_20250825"

const ToolBash20250124AllowedCallerCodeExecution20260120 ToolBash20250124AllowedCaller = "code\_execution\_20260120"

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]optional

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type CodeExecutionTool20250522 struct{…}

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250522

AllowedCallers []stringoptional

Accepts one of the following:

const CodeExecutionTool20250522AllowedCallerDirect CodeExecutionTool20250522AllowedCaller = "direct"

const CodeExecutionTool20250522AllowedCallerCodeExecution20250825 CodeExecutionTool20250522AllowedCaller = "code\_execution\_20250825"

const CodeExecutionTool20250522AllowedCallerCodeExecution20260120 CodeExecutionTool20250522AllowedCaller = "code\_execution\_20260120"

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type CodeExecutionTool20250825 struct{…}

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250825

AllowedCallers []stringoptional

Accepts one of the following:

const CodeExecutionTool20250825AllowedCallerDirect CodeExecutionTool20250825AllowedCaller = "direct"

const CodeExecutionTool20250825AllowedCallerCodeExecution20250825 CodeExecutionTool20250825AllowedCaller = "code\_execution\_20250825"

const CodeExecutionTool20250825AllowedCallerCodeExecution20260120 CodeExecutionTool20250825AllowedCaller = "code\_execution\_20260120"

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type CodeExecutionTool20260120 struct{…}

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20260120

AllowedCallers []stringoptional

Accepts one of the following:

const CodeExecutionTool20260120AllowedCallerDirect CodeExecutionTool20260120AllowedCaller = "direct"

const CodeExecutionTool20260120AllowedCallerCodeExecution20250825 CodeExecutionTool20260120AllowedCaller = "code\_execution\_20250825"

const CodeExecutionTool20260120AllowedCallerCodeExecution20260120 CodeExecutionTool20260120AllowedCaller = "code\_execution\_20260120"

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type MemoryTool20250818 struct{…}

Name Memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Memory20250818

AllowedCallers []stringoptional

Accepts one of the following:

const MemoryTool20250818AllowedCallerDirect MemoryTool20250818AllowedCaller = "direct"

const MemoryTool20250818AllowedCallerCodeExecution20250825 MemoryTool20250818AllowedCaller = "code\_execution\_20250825"

const MemoryTool20250818AllowedCallerCodeExecution20260120 MemoryTool20250818AllowedCaller = "code\_execution\_20260120"

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]optional

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250124 struct{…}

Name StrReplaceEditor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250124

AllowedCallers []stringoptional

Accepts one of the following:

const ToolTextEditor20250124AllowedCallerDirect ToolTextEditor20250124AllowedCaller = "direct"

const ToolTextEditor20250124AllowedCallerCodeExecution20250825 ToolTextEditor20250124AllowedCaller = "code\_execution\_20250825"

const ToolTextEditor20250124AllowedCallerCodeExecution20260120 ToolTextEditor20250124AllowedCaller = "code\_execution\_20260120"

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]optional

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250429 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250429

AllowedCallers []stringoptional

Accepts one of the following:

const ToolTextEditor20250429AllowedCallerDirect ToolTextEditor20250429AllowedCaller = "direct"

const ToolTextEditor20250429AllowedCallerCodeExecution20250825 ToolTextEditor20250429AllowedCaller = "code\_execution\_20250825"

const ToolTextEditor20250429AllowedCallerCodeExecution20260120 ToolTextEditor20250429AllowedCaller = "code\_execution\_20260120"

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]optional

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250728 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250728

AllowedCallers []stringoptional

Accepts one of the following:

const ToolTextEditor20250728AllowedCallerDirect ToolTextEditor20250728AllowedCaller = "direct"

const ToolTextEditor20250728AllowedCallerCodeExecution20250825 ToolTextEditor20250728AllowedCaller = "code\_execution\_20250825"

const ToolTextEditor20250728AllowedCallerCodeExecution20260120 ToolTextEditor20250728AllowedCaller = "code\_execution\_20260120"

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]optional

MaxCharacters int64optional

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type WebSearchTool20250305 struct{…}

Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20250305

AllowedCallers []stringoptional

Accepts one of the following:

const WebSearchTool20250305AllowedCallerDirect WebSearchTool20250305AllowedCaller = "direct"

const WebSearchTool20250305AllowedCallerCodeExecution20250825 WebSearchTool20250305AllowedCaller = "code\_execution\_20250825"

const WebSearchTool20250305AllowedCallerCodeExecution20260120 WebSearchTool20250305AllowedCaller = "code\_execution\_20260120"

AllowedDomains []stringoptional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains []stringoptional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxUses int64optional

Maximum number of times the tool can be used in the API request.

Strict booloptional

When true, guarantees schema validation on tool names and inputs

UserLocation [UserLocation](api/messages.md)optional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

City stringoptional

The city of the user.

Country stringoptional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Region stringoptional

The region of the user.

Timezone stringoptional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

type WebFetchTool20250910 struct{…}

Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20250910

AllowedCallers []stringoptional

Accepts one of the following:

const WebFetchTool20250910AllowedCallerDirect WebFetchTool20250910AllowedCaller = "direct"

const WebFetchTool20250910AllowedCallerCodeExecution20250825 WebFetchTool20250910AllowedCaller = "code\_execution\_20250825"

const WebFetchTool20250910AllowedCallerCodeExecution20260120 WebFetchTool20250910AllowedCaller = "code\_execution\_20260120"

AllowedDomains []stringoptional

List of domains to allow fetching from

BlockedDomains []stringoptional

List of domains to block fetching from

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](api/messages.md)optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled booloptional

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxContentTokens int64optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64optional

Maximum number of times the tool can be used in the API request.

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type WebSearchTool20260209 struct{…}

Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20260209

AllowedCallers []stringoptional

Accepts one of the following:

const WebSearchTool20260209AllowedCallerDirect WebSearchTool20260209AllowedCaller = "direct"

const WebSearchTool20260209AllowedCallerCodeExecution20250825 WebSearchTool20260209AllowedCaller = "code\_execution\_20250825"

const WebSearchTool20260209AllowedCallerCodeExecution20260120 WebSearchTool20260209AllowedCaller = "code\_execution\_20260120"

AllowedDomains []stringoptional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains []stringoptional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxUses int64optional

Maximum number of times the tool can be used in the API request.

Strict booloptional

When true, guarantees schema validation on tool names and inputs

UserLocation [UserLocation](api/messages.md)optional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

City stringoptional

The city of the user.

Country stringoptional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Region stringoptional

The region of the user.

Timezone stringoptional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

type WebFetchTool20260209 struct{…}

Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20260209

AllowedCallers []stringoptional

Accepts one of the following:

const WebFetchTool20260209AllowedCallerDirect WebFetchTool20260209AllowedCaller = "direct"

const WebFetchTool20260209AllowedCallerCodeExecution20250825 WebFetchTool20260209AllowedCaller = "code\_execution\_20250825"

const WebFetchTool20260209AllowedCallerCodeExecution20260120 WebFetchTool20260209AllowedCaller = "code\_execution\_20260120"

AllowedDomains []stringoptional

List of domains to allow fetching from

BlockedDomains []stringoptional

List of domains to block fetching from

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](api/messages.md)optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled booloptional

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxContentTokens int64optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64optional

Maximum number of times the tool can be used in the API request.

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type ToolSearchToolBm25\_20251119 struct{…}

Name ToolSearchToolBm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type ToolSearchToolBm25\_20251119Type

Accepts one of the following:

const ToolSearchToolBm25\_20251119TypeToolSearchToolBm25\_20251119 ToolSearchToolBm25\_20251119Type = "tool\_search\_tool\_bm25\_20251119"

const ToolSearchToolBm25\_20251119TypeToolSearchToolBm25 ToolSearchToolBm25\_20251119Type = "tool\_search\_tool\_bm25"

AllowedCallers []stringoptional

Accepts one of the following:

const ToolSearchToolBm25\_20251119AllowedCallerDirect ToolSearchToolBm25\_20251119AllowedCaller = "direct"

const ToolSearchToolBm25\_20251119AllowedCallerCodeExecution20250825 ToolSearchToolBm25\_20251119AllowedCaller = "code\_execution\_20250825"

const ToolSearchToolBm25\_20251119AllowedCallerCodeExecution20260120 ToolSearchToolBm25\_20251119AllowedCaller = "code\_execution\_20260120"

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type ToolSearchToolRegex20251119 struct{…}

Name ToolSearchToolRegex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type ToolSearchToolRegex20251119Type

Accepts one of the following:

const ToolSearchToolRegex20251119TypeToolSearchToolRegex20251119 ToolSearchToolRegex20251119Type = "tool\_search\_tool\_regex\_20251119"

const ToolSearchToolRegex20251119TypeToolSearchToolRegex ToolSearchToolRegex20251119Type = "tool\_search\_tool\_regex"

AllowedCallers []stringoptional

Accepts one of the following:

const ToolSearchToolRegex20251119AllowedCallerDirect ToolSearchToolRegex20251119AllowedCaller = "direct"

const ToolSearchToolRegex20251119AllowedCallerCodeExecution20250825 ToolSearchToolRegex20251119AllowedCaller = "code\_execution\_20250825"

const ToolSearchToolRegex20251119AllowedCallerCodeExecution20260120 ToolSearchToolRegex20251119AllowedCaller = "code\_execution\_20260120"

CacheControl [CacheControlEphemeral](api/messages.md)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict booloptional

When true, guarantees schema validation on tool names and inputs

TopK param.Field[int64]optional

Only sample from the top K options for each subsequent token.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only. You usually only need to use `temperature`.

minimum0

TopP param.Field[float64]optional

Use nucleus sampling.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

Recommended for advanced use cases only. You usually only need to use `temperature`.

maximum1

minimum0

##### ReturnsExpand Collapse

type Message struct{…}

ID string

Unique object identifier.

The format and length of IDs may change over time.

Container [Container](api/messages.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

Content [][ContentBlockUnion](api/messages.md)

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

type TextBlock struct{…}

Citations [][TextCitationUnion](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Text string

Type Text

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

type ToolUseBlock struct{…}

ID string

Caller ToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map[string, any]

Name string

Type ToolUse

type ServerToolUseBlock struct{…}

ID string

Caller ServerToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map[string, any]

Name ServerToolUseBlockName

Accepts one of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web\_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web\_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code\_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash\_code\_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text\_editor\_code\_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool\_search\_tool\_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse

type WebSearchToolResultBlock struct{…}

Caller WebSearchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content [WebSearchToolResultBlockContentUnion](api/messages.md)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](api/messages.md) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](api/messages.md) = "max\_uses\_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](api/messages.md) = "query\_too\_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](api/messages.md) = "request\_too\_large"

Type WebSearchToolResultError

type WebSearchToolResultBlockContentArray [][WebSearchResultBlock](api/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult

type WebFetchToolResultBlock struct{…}

Caller WebFetchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content WebFetchToolResultBlockContentUnion

Accepts one of the following:

type WebFetchToolResultErrorBlock struct{…}

ErrorCode [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](api/messages.md) = "url\_too\_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](api/messages.md) = "unsupported\_content\_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](api/messages.md) = "max\_uses\_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](api/messages.md) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlock struct{…}

Content [DocumentBlock](api/messages.md)

Citations [CitationsConfig](api/messages.md)

Citation configuration for the document

Enabled bool

Source DocumentBlockSourceUnion

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

type CodeExecutionToolResultBlock struct{…}

Content [CodeExecutionToolResultBlockContentUnion](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

type CodeExecutionToolResultError struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlock struct{…}

Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.

Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

type BashCodeExecutionToolResultBlock struct{…}

Content BashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BashCodeExecutionToolResultError struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](api/messages.md) = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlock struct{…}

Content [][BashCodeExecutionOutputBlock](api/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

type TextEditorCodeExecutionToolResultBlock struct{…}

Content TextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type TextEditorCodeExecutionToolResultError struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

type TextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult

type ToolSearchToolResultBlock struct{…}

Content ToolSearchToolResultBlockContentUnion

Accepts one of the following:

type ToolSearchToolResultError struct{…}

ErrorCode [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](api/messages.md) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlock struct{…}

ToolReferences [][ToolReferenceBlock](api/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

const ModelClaudeOpus4\_6 Model = "claude-opus-4-6"

Most intelligent model for building agents and coding

const ModelClaudeSonnet4\_6 Model = "claude-sonnet-4-6"

Best combination of speed and intelligence

const ModelClaudeHaiku4\_5 Model = "claude-haiku-4-5"

Fastest model with near-frontier intelligence

const ModelClaudeHaiku4\_5\_20251001 Model = "claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

const ModelClaudeOpus4\_5 Model = "claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

const ModelClaudeOpus4\_5\_20251101 Model = "claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

const ModelClaudeSonnet4\_5 Model = "claude-sonnet-4-5"

High-performance model for agents and coding

const ModelClaudeSonnet4\_5\_20250929 Model = "claude-sonnet-4-5-20250929"

High-performance model for agents and coding

const ModelClaudeOpus4\_1 Model = "claude-opus-4-1"

Exceptional model for specialized complex tasks

const ModelClaudeOpus4\_1\_20250805 Model = "claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

string

Role Assistant

Conversational role of the generated message.

This will always be `"assistant"`.

StopReason [StopReason](api/messages.md)

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

const StopReasonEndTurn [StopReason](api/messages.md) = "end\_turn"

const StopReasonMaxTokens [StopReason](api/messages.md) = "max\_tokens"

const StopReasonStopSequence [StopReason](api/messages.md) = "stop\_sequence"

const StopReasonToolUse [StopReason](api/messages.md) = "tool\_use"

const StopReasonPauseTurn [StopReason](api/messages.md) = "pause\_turn"

const StopReasonRefusal [StopReason](api/messages.md) = "refusal"

StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

Type Message

Object type.

For Messages, this is always `"message"`.

Usage [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreation [CacheCreation](api/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

ServerToolUse [ServerToolUsage](api/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

type MessageStreamEventUnion interface{…}

Accepts one of the following:

type MessageStartEvent struct{…}

Message [Message](api/messages.md)

ID string

Unique object identifier.

The format and length of IDs may change over time.

Container [Container](api/messages.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

Content [][ContentBlockUnion](api/messages.md)

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

type TextBlock struct{…}

Citations [][TextCitationUnion](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Text string

Type Text

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

type ToolUseBlock struct{…}

ID string

Caller ToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map[string, any]

Name string

Type ToolUse

type ServerToolUseBlock struct{…}

ID string

Caller ServerToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map[string, any]

Name ServerToolUseBlockName

Accepts one of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web\_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web\_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code\_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash\_code\_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text\_editor\_code\_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool\_search\_tool\_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse

type WebSearchToolResultBlock struct{…}

Caller WebSearchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content [WebSearchToolResultBlockContentUnion](api/messages.md)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](api/messages.md) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](api/messages.md) = "max\_uses\_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](api/messages.md) = "query\_too\_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](api/messages.md) = "request\_too\_large"

Type WebSearchToolResultError

type WebSearchToolResultBlockContentArray [][WebSearchResultBlock](api/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult

type WebFetchToolResultBlock struct{…}

Caller WebFetchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content WebFetchToolResultBlockContentUnion

Accepts one of the following:

type WebFetchToolResultErrorBlock struct{…}

ErrorCode [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](api/messages.md) = "url\_too\_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](api/messages.md) = "unsupported\_content\_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](api/messages.md) = "max\_uses\_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](api/messages.md) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlock struct{…}

Content [DocumentBlock](api/messages.md)

Citations [CitationsConfig](api/messages.md)

Citation configuration for the document

Enabled bool

Source DocumentBlockSourceUnion

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

type CodeExecutionToolResultBlock struct{…}

Content [CodeExecutionToolResultBlockContentUnion](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

type CodeExecutionToolResultError struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlock struct{…}

Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.

Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

type BashCodeExecutionToolResultBlock struct{…}

Content BashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BashCodeExecutionToolResultError struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](api/messages.md) = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlock struct{…}

Content [][BashCodeExecutionOutputBlock](api/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

type TextEditorCodeExecutionToolResultBlock struct{…}

Content TextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type TextEditorCodeExecutionToolResultError struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

type TextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult

type ToolSearchToolResultBlock struct{…}

Content ToolSearchToolResultBlockContentUnion

Accepts one of the following:

type ToolSearchToolResultError struct{…}

ErrorCode [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](api/messages.md) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlock struct{…}

ToolReferences [][ToolReferenceBlock](api/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

const ModelClaudeOpus4\_6 Model = "claude-opus-4-6"

Most intelligent model for building agents and coding

const ModelClaudeSonnet4\_6 Model = "claude-sonnet-4-6"

Best combination of speed and intelligence

const ModelClaudeHaiku4\_5 Model = "claude-haiku-4-5"

Fastest model with near-frontier intelligence

const ModelClaudeHaiku4\_5\_20251001 Model = "claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

const ModelClaudeOpus4\_5 Model = "claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

const ModelClaudeOpus4\_5\_20251101 Model = "claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

const ModelClaudeSonnet4\_5 Model = "claude-sonnet-4-5"

High-performance model for agents and coding

const ModelClaudeSonnet4\_5\_20250929 Model = "claude-sonnet-4-5-20250929"

High-performance model for agents and coding

const ModelClaudeOpus4\_1 Model = "claude-opus-4-1"

Exceptional model for specialized complex tasks

const ModelClaudeOpus4\_1\_20250805 Model = "claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

string

Role Assistant

Conversational role of the generated message.

This will always be `"assistant"`.

StopReason [StopReason](api/messages.md)

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

const StopReasonEndTurn [StopReason](api/messages.md) = "end\_turn"

const StopReasonMaxTokens [StopReason](api/messages.md) = "max\_tokens"

const StopReasonStopSequence [StopReason](api/messages.md) = "stop\_sequence"

const StopReasonToolUse [StopReason](api/messages.md) = "tool\_use"

const StopReasonPauseTurn [StopReason](api/messages.md) = "pause\_turn"

const StopReasonRefusal [StopReason](api/messages.md) = "refusal"

StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

Type Message

Object type.

For Messages, this is always `"message"`.

Usage [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreation [CacheCreation](api/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

ServerToolUse [ServerToolUsage](api/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type MessageStart

type MessageDeltaEvent struct{…}

Delta MessageDeltaEventDelta

Container [Container](api/messages.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

StopReason [StopReason](api/messages.md)

Accepts one of the following:

const StopReasonEndTurn [StopReason](api/messages.md) = "end\_turn"

const StopReasonMaxTokens [StopReason](api/messages.md) = "max\_tokens"

const StopReasonStopSequence [StopReason](api/messages.md) = "stop\_sequence"

const StopReasonToolUse [StopReason](api/messages.md) = "tool\_use"

const StopReasonPauseTurn [StopReason](api/messages.md) = "pause\_turn"

const StopReasonRefusal [StopReason](api/messages.md) = "refusal"

StopSequence string

Type MessageDelta

Usage [MessageDeltaUsage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreationInputTokens int64

The cumulative number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The cumulative number of input tokens read from the cache.

InputTokens int64

The cumulative number of input tokens which were used.

OutputTokens int64

The cumulative number of output tokens which were used.

ServerToolUse [ServerToolUsage](api/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.

type MessageStopEvent struct{…}

Type MessageStop

type ContentBlockStartEvent struct{…}

ContentBlock ContentBlockStartEventContentBlockUnion

Response model for a file uploaded to the container.

Accepts one of the following:

type TextBlock struct{…}

Citations [][TextCitationUnion](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Text string

Type Text

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

type ToolUseBlock struct{…}

ID string

Caller ToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map[string, any]

Name string

Type ToolUse

type ServerToolUseBlock struct{…}

ID string

Caller ServerToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map[string, any]

Name ServerToolUseBlockName

Accepts one of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web\_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web\_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code\_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash\_code\_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text\_editor\_code\_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool\_search\_tool\_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse

type WebSearchToolResultBlock struct{…}

Caller WebSearchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content [WebSearchToolResultBlockContentUnion](api/messages.md)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](api/messages.md) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](api/messages.md) = "max\_uses\_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](api/messages.md) = "query\_too\_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](api/messages.md) = "request\_too\_large"

Type WebSearchToolResultError

type WebSearchToolResultBlockContentArray [][WebSearchResultBlock](api/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult

type WebFetchToolResultBlock struct{…}

Caller WebFetchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content WebFetchToolResultBlockContentUnion

Accepts one of the following:

type WebFetchToolResultErrorBlock struct{…}

ErrorCode [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](api/messages.md) = "url\_too\_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](api/messages.md) = "unsupported\_content\_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](api/messages.md) = "max\_uses\_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](api/messages.md) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlock struct{…}

Content [DocumentBlock](api/messages.md)

Citations [CitationsConfig](api/messages.md)

Citation configuration for the document

Enabled bool

Source DocumentBlockSourceUnion

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

type CodeExecutionToolResultBlock struct{…}

Content [CodeExecutionToolResultBlockContentUnion](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

type CodeExecutionToolResultError struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlock struct{…}

Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.

Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

type BashCodeExecutionToolResultBlock struct{…}

Content BashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BashCodeExecutionToolResultError struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](api/messages.md) = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlock struct{…}

Content [][BashCodeExecutionOutputBlock](api/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

type TextEditorCodeExecutionToolResultBlock struct{…}

Content TextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type TextEditorCodeExecutionToolResultError struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

type TextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult

type ToolSearchToolResultBlock struct{…}

Content ToolSearchToolResultBlockContentUnion

Accepts one of the following:

type ToolSearchToolResultError struct{…}

ErrorCode [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](api/messages.md) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlock struct{…}

ToolReferences [][ToolReferenceBlock](api/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

Index int64

Type ContentBlockStart

type ContentBlockDeltaEvent struct{…}

Delta [RawContentBlockDeltaUnion](api/messages.md)

Accepts one of the following:

type TextDelta struct{…}

Text string

Type TextDelta

type InputJSONDelta struct{…}

PartialJSON string

Type InputJSONDelta

type CitationsDelta struct{…}

Citation CitationsDeltaCitationUnion

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Type CitationsDelta

type ThinkingDelta struct{…}

Thinking string

Type ThinkingDelta

type SignatureDelta struct{…}

Signature string

Type SignatureDelta

Index int64

Type ContentBlockDelta

type ContentBlockStopEvent struct{…}

Index int64

Type ContentBlockStop

Create a Message

Go

```shiki
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
    MaxTokens: 1024,
    Messages: []anthropic.MessageParam{anthropic.MessageParam{
      Content: []anthropic.ContentBlockParamUnion{anthropic.ContentBlockParamUnion{
        OfText: &anthropic.TextBlockParam{
          Text: "x",
        },
      }},
      Role: anthropic.MessageParamRoleUser,
    }},
    Model: anthropic.ModelClaudeOpus4_6,
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", message.ID)
}
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
