# Create a Message Batch

Copy page

SDK language

Go

# Create a Message Batch

client.Beta.Messages.Batches.New(ctx, params) (\*[BetaMessageBatch](api/beta.md), error)

POST/v1/messages/batches

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse

params BetaMessageBatchNewParams

Requests param.Field[[]BetaMessageBatchNewParamsRequest]

Body param: List of requests for prompt completion. Each is an individual request to create a Message.

CustomID string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

maxLength64

minLength1

Params BetaMessageBatchNewParamsRequestParams

Messages API creation parameters for the individual request.

See the [Messages API reference](https://docs.claude.com/en/api/messages) for full documentation on available parameters.

MaxTokens int64

The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Set to `0` to populate the [prompt cache](https://docs.claude.com/en/docs/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.

minimum0

Messages [][BetaMessageParamResp](api/beta.md)

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

Content [][BetaContentBlockParamUnionResp](api/beta.md)

One of the following:

[][BetaContentBlockParamUnionResp](api/beta.md)

One of the following:

type BetaTextBlockParamResp struct{…}

Text string

Type Text

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [][BetaTextCitationParamUnionResp](api/beta.md)Optional

One of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation

type BetaImageBlockParamResp struct{…}

Source BetaImageBlockParamSourceUnionResp

One of the following:

type BetaBase64ImageSource struct{…}

Data string

MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64

type BetaURLImageSource struct{…}

Type URL

URL string

type BetaFileImageSource struct{…}

FileID string

Type File

Type Image

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaRequestDocumentBlock struct{…}

Source BetaRequestDocumentBlockSourceUnion

One of the following:

type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type BetaContentBlockSource struct{…}

Content BetaContentBlockSourceContentUnion

One of the following:

string

[][BetaContentBlockSourceContentUnion](api/beta.md)

One of the following:

type BetaTextBlockParamResp struct{…}

Text string

Type Text

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [][BetaTextCitationParamUnionResp](api/beta.md)Optional

One of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation

type BetaImageBlockParamResp struct{…}

Source BetaImageBlockParamSourceUnionResp

One of the following:

type BetaBase64ImageSource struct{…}

Data string

MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64

type BetaURLImageSource struct{…}

Type URL

URL string

type BetaFileImageSource struct{…}

FileID string

Type File

Type Image

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type Content

type BetaURLPDFSource struct{…}

Type URL

URL string

type BetaFileDocumentSource struct{…}

FileID string

Type File

Type Document

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [BetaCitationsConfigParamResp](api/beta.md)Optional

Enabled boolOptional

Context stringOptional

Title stringOptional

type BetaSearchResultBlockParamResp struct{…}

Content [][BetaTextBlockParamResp](api/beta.md)

Text string

Type Text

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [][BetaTextCitationParamUnionResp](api/beta.md)Optional

One of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation

Source string

Title string

Type SearchResult

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [BetaCitationsConfigParamResp](api/beta.md)Optional

Enabled boolOptional

type BetaThinkingBlockParamResp struct{…}

Signature string

Thinking string

Type Thinking

type BetaRedactedThinkingBlockParamResp struct{…}

Data string

Type RedactedThinking

type BetaToolUseBlockParamResp struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Caller BetaToolUseBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:

type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type BetaToolResultBlockParamResp struct{…}

ToolUseID string

Type ToolResult

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Content []BetaToolResultBlockParamContentUnionRespOptional

One of the following:

[]BetaToolResultBlockParamContentUnionResp

One of the following:

type BetaTextBlockParamResp struct{…}

Text string

Type Text

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [][BetaTextCitationParamUnionResp](api/beta.md)Optional

One of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation

type BetaImageBlockParamResp struct{…}

Source BetaImageBlockParamSourceUnionResp

One of the following:

type BetaBase64ImageSource struct{…}

Data string

MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64

type BetaURLImageSource struct{…}

Type URL

URL string

type BetaFileImageSource struct{…}

FileID string

Type File

Type Image

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaSearchResultBlockParamResp struct{…}

Content [][BetaTextBlockParamResp](api/beta.md)

Text string

Type Text

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [][BetaTextCitationParamUnionResp](api/beta.md)Optional

One of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation

Source string

Title string

Type SearchResult

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [BetaCitationsConfigParamResp](api/beta.md)Optional

Enabled boolOptional

type BetaRequestDocumentBlock struct{…}

Source BetaRequestDocumentBlockSourceUnion

One of the following:

type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type BetaContentBlockSource struct{…}

Content BetaContentBlockSourceContentUnion

One of the following:

string

[][BetaContentBlockSourceContentUnion](api/beta.md)

One of the following:

type BetaTextBlockParamResp struct{…}

Text string

Type Text

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [][BetaTextCitationParamUnionResp](api/beta.md)Optional

One of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation

type BetaImageBlockParamResp struct{…}

Source BetaImageBlockParamSourceUnionResp

One of the following:

type BetaBase64ImageSource struct{…}

Data string

MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64

type BetaURLImageSource struct{…}

Type URL

URL string

type BetaFileImageSource struct{…}

FileID string

Type File

Type Image

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type Content

type BetaURLPDFSource struct{…}

Type URL

URL string

type BetaFileDocumentSource struct{…}

FileID string

Type File

Type Document

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [BetaCitationsConfigParamResp](api/beta.md)Optional

Enabled boolOptional

Context stringOptional

Title stringOptional

type BetaToolReferenceBlockParamResp struct{…}

Tool reference block that can be included in tool\_result content.

ToolName string

Type ToolReference

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

IsError boolOptional

type BetaServerToolUseBlockParamResp struct{…}

ID string

Input map[string, any]

Name BetaServerToolUseBlockParamName

One of the following:

const BetaServerToolUseBlockParamNameAdvisor BetaServerToolUseBlockParamName = "advisor"

const BetaServerToolUseBlockParamNameWebSearch BetaServerToolUseBlockParamName = "web\_search"

const BetaServerToolUseBlockParamNameWebFetch BetaServerToolUseBlockParamName = "web\_fetch"

const BetaServerToolUseBlockParamNameCodeExecution BetaServerToolUseBlockParamName = "code\_execution"

const BetaServerToolUseBlockParamNameBashCodeExecution BetaServerToolUseBlockParamName = "bash\_code\_execution"

const BetaServerToolUseBlockParamNameTextEditorCodeExecution BetaServerToolUseBlockParamName = "text\_editor\_code\_execution"

const BetaServerToolUseBlockParamNameToolSearchToolRegex BetaServerToolUseBlockParamName = "tool\_search\_tool\_regex"

const BetaServerToolUseBlockParamNameToolSearchToolBm25 BetaServerToolUseBlockParamName = "tool\_search\_tool\_bm25"

Type ServerToolUse

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Caller BetaServerToolUseBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:

type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type BetaWebSearchToolResultBlockParamResp struct{…}

Content [BetaWebSearchToolResultBlockParamContentUnionResp](api/beta.md)

One of the following:

[][BetaWebSearchResultBlockParamResp](api/beta.md)

EncryptedContent string

Title string

Type WebSearchResult

URL string

PageAge stringOptional

type BetaWebSearchToolRequestError struct{…}

ErrorCode [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta.md) = "request\_too\_large"

Type WebSearchToolResultError

ToolUseID string

Type WebSearchToolResult

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Caller BetaWebSearchToolResultBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:

type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type BetaWebFetchToolResultBlockParamResp struct{…}

Content BetaWebFetchToolResultBlockParamContentUnionResp

One of the following:

type BetaWebFetchToolResultErrorBlockParamResp struct{…}

ErrorCode [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotInPriorContext [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_in\_prior\_context"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta.md) = "unavailable"

Type WebFetchToolResultError

type BetaWebFetchBlockParamResp struct{…}

Content [BetaRequestDocumentBlock](api/beta.md)

Source BetaRequestDocumentBlockSourceUnion

One of the following:

type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type BetaContentBlockSource struct{…}

Content BetaContentBlockSourceContentUnion

One of the following:

string

[][BetaContentBlockSourceContentUnion](api/beta.md)

One of the following:

type BetaTextBlockParamResp struct{…}

Text string

Type Text

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [][BetaTextCitationParamUnionResp](api/beta.md)Optional

One of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation

type BetaImageBlockParamResp struct{…}

Source BetaImageBlockParamSourceUnionResp

One of the following:

type BetaBase64ImageSource struct{…}

Data string

MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64

type BetaURLImageSource struct{…}

Type URL

URL string

type BetaFileImageSource struct{…}

FileID string

Type File

Type Image

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type Content

type BetaURLPDFSource struct{…}

Type URL

URL string

type BetaFileDocumentSource struct{…}

FileID string

Type File

Type Document

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [BetaCitationsConfigParamResp](api/beta.md)Optional

Enabled boolOptional

Context stringOptional

Title stringOptional

Type WebFetchResult

URL string

Fetched content URL

RetrievedAt stringOptional

ISO 8601 timestamp when the content was retrieved

ToolUseID string

Type WebFetchToolResult

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Caller BetaWebFetchToolResultBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:

type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type BetaAdvisorToolResultBlockParamResp struct{…}

Content BetaAdvisorToolResultBlockParamContentUnionResp

One of the following:

type BetaAdvisorToolResultErrorParamResp struct{…}

ErrorCode BetaAdvisorToolResultErrorParamErrorCode

One of the following:

const BetaAdvisorToolResultErrorParamErrorCodeMaxUsesExceeded BetaAdvisorToolResultErrorParamErrorCode = "max\_uses\_exceeded"

const BetaAdvisorToolResultErrorParamErrorCodePromptTooLong BetaAdvisorToolResultErrorParamErrorCode = "prompt\_too\_long"

const BetaAdvisorToolResultErrorParamErrorCodeTooManyRequests BetaAdvisorToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaAdvisorToolResultErrorParamErrorCodeOverloaded BetaAdvisorToolResultErrorParamErrorCode = "overloaded"

const BetaAdvisorToolResultErrorParamErrorCodeUnavailable BetaAdvisorToolResultErrorParamErrorCode = "unavailable"

const BetaAdvisorToolResultErrorParamErrorCodeExecutionTimeExceeded BetaAdvisorToolResultErrorParamErrorCode = "execution\_time\_exceeded"

const BetaAdvisorToolResultErrorParamErrorCodeModelNotFound BetaAdvisorToolResultErrorParamErrorCode = "model\_not\_found"

Type AdvisorToolResultError

type BetaAdvisorResultBlockParamResp struct{…}

Text string

Type AdvisorResult

StopReason stringOptional

type BetaAdvisorRedactedResultBlockParamResp struct{…}

EncryptedContent string

Opaque blob produced by a prior response; must be round-tripped verbatim.

Type AdvisorRedactedResult

StopReason stringOptional

ToolUseID string

Type AdvisorToolResult

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaCodeExecutionToolResultBlockParamResp struct{…}

Content [BetaCodeExecutionToolResultBlockParamContentUnionResp](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:

type BetaCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError

type BetaCodeExecutionResultBlockParamResp struct{…}

Content [][BetaCodeExecutionOutputBlockParamResp](api/beta.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type BetaEncryptedCodeExecutionResultBlockParamResp struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.

Content [][BetaCodeExecutionOutputBlockParamResp](api/beta.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaBashCodeExecutionToolResultBlockParamResp struct{…}

Content BetaBashCodeExecutionToolResultBlockParamContentUnionResp

One of the following:

type BetaBashCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode BetaBashCodeExecutionToolResultErrorParamErrorCode

One of the following:

const BetaBashCodeExecutionToolResultErrorParamErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorParamErrorCode = "invalid\_tool\_input"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorParamErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorParamErrorCode = "execution\_time\_exceeded"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorParamErrorCode = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError

type BetaBashCodeExecutionResultBlockParamResp struct{…}

Content [][BetaBashCodeExecutionOutputBlockParamResp](api/beta.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaTextEditorCodeExecutionToolResultBlockParamResp struct{…}

Content BetaTextEditorCodeExecutionToolResultBlockParamContentUnionResp

One of the following:

type BetaTextEditorCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode BetaTextEditorCodeExecutionToolResultErrorParamErrorCode

One of the following:

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "invalid\_tool\_input"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "execution\_time\_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "file\_not\_found"

Type TextEditorCodeExecutionToolResultError

ErrorMessage stringOptional

type BetaTextEditorCodeExecutionViewResultBlockParamResp struct{…}

Content string

FileType BetaTextEditorCodeExecutionViewResultBlockParamFileType

One of the following:

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypeText BetaTextEditorCodeExecutionViewResultBlockParamFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypeImage BetaTextEditorCodeExecutionViewResultBlockParamFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypePDF BetaTextEditorCodeExecutionViewResultBlockParamFileType = "pdf"

Type TextEditorCodeExecutionViewResult

NumLines int64Optional

StartLine int64Optional

TotalLines int64Optional

type BetaTextEditorCodeExecutionCreateResultBlockParamResp struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type BetaTextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}

Type TextEditorCodeExecutionStrReplaceResult

Lines []stringOptional

NewLines int64Optional

NewStart int64Optional

OldLines int64Optional

OldStart int64Optional

ToolUseID string

Type TextEditorCodeExecutionToolResult

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaToolSearchToolResultBlockParamResp struct{…}

Content BetaToolSearchToolResultBlockParamContentUnionResp

One of the following:

type BetaToolSearchToolResultErrorParamResp struct{…}

ErrorCode BetaToolSearchToolResultErrorParamErrorCode

One of the following:

const BetaToolSearchToolResultErrorParamErrorCodeInvalidToolInput BetaToolSearchToolResultErrorParamErrorCode = "invalid\_tool\_input"

const BetaToolSearchToolResultErrorParamErrorCodeUnavailable BetaToolSearchToolResultErrorParamErrorCode = "unavailable"

const BetaToolSearchToolResultErrorParamErrorCodeTooManyRequests BetaToolSearchToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaToolSearchToolResultErrorParamErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorParamErrorCode = "execution\_time\_exceeded"

Type ToolSearchToolResultError

ErrorMessage stringOptional

type BetaToolSearchToolSearchResultBlockParamResp struct{…}

ToolReferences [][BetaToolReferenceBlockParamResp](api/beta.md)

ToolName string

Type ToolReference

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaMCPToolUseBlockParamResp struct{…}

ID string

Input map[string, any]

Name string

ServerName string

The name of the MCP server

Type MCPToolUse

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaRequestMCPToolResultBlockParamResp struct{…}

ToolUseID string

Type MCPToolResult

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Content BetaRequestMCPToolResultBlockParamContentUnionRespOptional

One of the following:

string

[][BetaTextBlockParamResp](api/beta.md)

Text string

Type Text

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [][BetaTextCitationParamUnionResp](api/beta.md)Optional

One of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation

IsError boolOptional

type BetaContainerUploadBlockParamResp struct{…}

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

FileID string

Type ContainerUpload

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaCompactionBlockParamResp struct{…}

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

Type Compaction

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Content stringOptional

Summary of previously compacted content, or null if compaction failed

EncryptedContent stringOptional

Opaque metadata from prior compaction, to be round-tripped verbatim

type BetaMidConversationSystemBlockParamResp struct{…}

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.

Content [][BetaTextBlockParamResp](api/beta.md)

System instruction text blocks.

Text string

Type Text

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [][BetaTextCitationParamUnionResp](api/beta.md)Optional

One of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation

Type MidConvSystem

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaFallbackBlockParamResp struct{…}

A `fallback` block echoed back from a prior response.

Accepted in `messages[].content` and never rendered into the prompt,
not validated against the request's `fallbacks` chain or top-level
`model`, and stripped before the sticky-routing cache key is computed.

Callers should echo the assistant turn verbatim — block included. The
block's position is load-bearing for thinking verification: the thinking
runs on either side of a fallback hop carry independently-rooted
verification hash chains, and this block is the only record of where one
chain ends and the next begins. When thinking runs flank the boundary,
omitting the block merges the runs into one contiguous span whose hashes
cannot verify (the request is rejected), and moving it into the middle of
a single run splits that run's chain and is likewise rejected; between
non-thinking blocks the block's placement has no verification effect.

From [BetaFallbackInfoParamResp](api/beta.md)

Identifies one hop of a fallback transition.

Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

const ModelClaudeFable5 Model = "claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

const ModelClaudeMythos5 Model = "claude-mythos-5"

Most capable model for cybersecurity and biology research

const ModelClaudeOpus4\_8 Model = "claude-opus-4-8"

Frontier intelligence for long-running agents and coding

const ModelClaudeOpus4\_7 Model = "claude-opus-4-7"

Frontier intelligence for long-running agents and coding

const ModelClaudeMythosPreview Model = "claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

const ModelClaudeOpus4\_6 Model = "claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

To [BetaFallbackInfoParamResp](api/beta.md)

Identifies one hop of a fallback transition.

Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

const ModelClaudeFable5 Model = "claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

const ModelClaudeMythos5 Model = "claude-mythos-5"

Most capable model for cybersecurity and biology research

const ModelClaudeOpus4\_8 Model = "claude-opus-4-8"

Frontier intelligence for long-running agents and coding

const ModelClaudeOpus4\_7 Model = "claude-opus-4-7"

Frontier intelligence for long-running agents and coding

const ModelClaudeMythosPreview Model = "claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

const ModelClaudeOpus4\_6 Model = "claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

Type Fallback

Role BetaMessageParamRole

One of the following:

const BetaMessageParamRoleUser BetaMessageParamRole = "user"

const BetaMessageParamRoleAssistant BetaMessageParamRole = "assistant"

const BetaMessageParamRoleSystem BetaMessageParamRole = "system"

Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

const ModelClaudeFable5 Model = "claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

const ModelClaudeMythos5 Model = "claude-mythos-5"

Most capable model for cybersecurity and biology research

const ModelClaudeOpus4\_8 Model = "claude-opus-4-8"

Frontier intelligence for long-running agents and coding

const ModelClaudeOpus4\_7 Model = "claude-opus-4-7"

Frontier intelligence for long-running agents and coding

const ModelClaudeMythosPreview Model = "claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

const ModelClaudeOpus4\_6 Model = "claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Top-level cache control automatically applies a cache\_control marker to the last cacheable block in the request.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Container BetaMessageBatchNewParamsRequestParamsContainerUnionOptional

Container identifier for reuse across requests.

One of the following:

type BetaContainerParamsResp struct{…}

Container parameters with skills to be loaded.

ID stringOptional

Container id

Skills [][BetaSkillParamsResp](api/beta.md)Optional

List of skills to load in the container

SkillID string

Skill ID

Type BetaSkillParamsType

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

const BetaSkillParamsTypeAnthropic BetaSkillParamsType = "anthropic"

const BetaSkillParamsTypeCustom BetaSkillParamsType = "custom"

Version stringOptional

Skill version or 'latest' for most recent version

string

ContextManagement [BetaContextManagementConfig](api/beta.md)Optional

Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

Edits []BetaContextManagementConfigEditUnionOptional

List of context management edits to apply

One of the following:

type BetaClearToolUses20250919Edit struct{…}

Type ClearToolUses20250919

ClearAtLeast [BetaInputTokensClearAtLeast](api/beta.md)Optional

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

Type InputTokens

Value int64

ClearToolInputs BetaClearToolUses20250919EditClearToolInputsUnionOptional

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

One of the following:

bool

[]string

ExcludeTools []stringOptional

Tool names whose uses are preserved from clearing

Keep [BetaToolUsesKeep](api/beta.md)Optional

Number of tool uses to retain in the conversation

Type ToolUses

Value int64

Trigger BetaClearToolUses20250919EditTriggerUnionOptional

Condition that triggers the context management strategy

One of the following:

type BetaInputTokensTrigger struct{…}

Type InputTokens

Value int64

type BetaToolUsesTrigger struct{…}

Type ToolUses

Value int64

type BetaClearThinking20251015Edit struct{…}

Type ClearThinking20251015

Keep BetaClearThinking20251015EditKeepUnionOptional

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

One of the following:

type BetaThinkingTurns struct{…}

Type ThinkingTurns

Value int64

type BetaAllThinkingTurns struct{…}

Type All

All

type BetaCompact20260112Edit struct{…}

Automatically compact older context when reaching the configured trigger threshold.

Type Compact20260112

Instructions stringOptional

Additional instructions for summarization.

PauseAfterCompaction boolOptional

Whether to pause after compaction and return the compaction block to the user.

Trigger [BetaInputTokensTrigger](api/beta.md)Optional

When to trigger compaction. Defaults to 150000 input tokens.

Type InputTokens

Value int64

Diagnostics [BetaDiagnosticsParamResp](api/beta.md)Optional

Request-level diagnostics. Currently carries the previous response
id for prompt-cache divergence reporting.

PreviousMessageID stringOptional

The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

FallbackCreditToken stringOptional

The `fallback_credit_token` from a prior refusal's `stop_details`.

When a preceding request was refused and returned a `fallback_credit_token`,
pass that code here on the retry to have the retry's cache-creation tokens
for the prefix that was warm on the refused model billed at the cache-read
rate. Must be redeemed by the same organization and workspace, with the same
request body (optionally extended by one appended `assistant` message whose
content is the partial text — with any trailing whitespace stripped from
the final text block — and paired server-tool blocks streamed before the
refusal; the appended-assistant form is not available for requests with
`output_format` set or forced `tool_choice`), on an eligible fallback
model, on the same platform,
and within 5 minutes of the refusal; a mismatch is a 400. A token minted
mid-server-tool-loop whose partial content was continuable may only be
redeemed with the appended-assistant form — if an exact-body retry is
rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry with the appended-assistant form instead.

When the appended-assistant form is used on a model that otherwise disallows
assistant-turn prefill, this token also authorizes that one prefill.

maxLength2048

minLength1

Fallbacks [][BetaFallbackParamResp](api/beta.md)Optional

Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on.

Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

const ModelClaudeFable5 Model = "claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

const ModelClaudeMythos5 Model = "claude-mythos-5"

Most capable model for cybersecurity and biology research

const ModelClaudeOpus4\_8 Model = "claude-opus-4-8"

Frontier intelligence for long-running agents and coding

const ModelClaudeOpus4\_7 Model = "claude-opus-4-7"

Frontier intelligence for long-running agents and coding

const ModelClaudeMythosPreview Model = "claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

const ModelClaudeOpus4\_6 Model = "claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

MaxTokens int64Optional

OutputConfig [BetaOutputConfig](api/beta.md)Optional

Effort BetaOutputConfigEffortOptional

All possible effort levels.

One of the following:

const BetaOutputConfigEffortLow BetaOutputConfigEffort = "low"

const BetaOutputConfigEffortMedium BetaOutputConfigEffort = "medium"

const BetaOutputConfigEffortHigh BetaOutputConfigEffort = "high"

const BetaOutputConfigEffortXhigh BetaOutputConfigEffort = "xhigh"

const BetaOutputConfigEffortMax BetaOutputConfigEffort = "max"

Format [BetaJSONOutputFormat](api/beta.md)Optional

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

Schema map[string, any]

The JSON schema of the format

Type JSONSchema

TaskBudget [BetaTokenTaskBudget](api/beta.md)Optional

User-configurable total token budget across contexts.

Total int64

Total token budget across all contexts in the session.

Type Tokens

The budget type. Currently only 'tokens' is supported.

Remaining int64Optional

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

Speed BetaFallbackParamSpeedOptional

One of the following:

const BetaFallbackParamSpeedStandard BetaFallbackParamSpeed = "standard"

const BetaFallbackParamSpeedFast BetaFallbackParamSpeed = "fast"

Thinking BetaFallbackParamThinkingUnionRespOptional

One of the following:

type BetaThinkingConfigEnabled struct{…}

BudgetTokens int64

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

Type Enabled

Display BetaThinkingConfigEnabledDisplayOptional

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

const BetaThinkingConfigEnabledDisplaySummarized BetaThinkingConfigEnabledDisplay = "summarized"

const BetaThinkingConfigEnabledDisplayOmitted BetaThinkingConfigEnabledDisplay = "omitted"

type BetaThinkingConfigDisabled struct{…}

Type Disabled

type BetaThinkingConfigAdaptive struct{…}

Type Adaptive

Display BetaThinkingConfigAdaptiveDisplayOptional

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

const BetaThinkingConfigAdaptiveDisplaySummarized BetaThinkingConfigAdaptiveDisplay = "summarized"

const BetaThinkingConfigAdaptiveDisplayOmitted BetaThinkingConfigAdaptiveDisplay = "omitted"

InferenceGeo stringOptional

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

MCPServers [][BetaRequestMCPServerURLDefinition](api/beta.md)Optional

MCP servers to be utilized in this request

Name string

Type URL

URL string

AuthorizationToken stringOptional

ToolConfiguration [BetaRequestMCPServerToolConfiguration](api/beta.md)Optional

AllowedTools []stringOptional

Enabled boolOptional

Metadata [BetaMetadata](api/beta.md)Optional

An object describing metadata about the request.

UserID stringOptional

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512

OutputConfig [BetaOutputConfig](api/beta.md)Optional

Configuration options for the model's output, such as the output format.

Effort BetaOutputConfigEffortOptional

All possible effort levels.

One of the following:

const BetaOutputConfigEffortLow BetaOutputConfigEffort = "low"

const BetaOutputConfigEffortMedium BetaOutputConfigEffort = "medium"

const BetaOutputConfigEffortHigh BetaOutputConfigEffort = "high"

const BetaOutputConfigEffortXhigh BetaOutputConfigEffort = "xhigh"

const BetaOutputConfigEffortMax BetaOutputConfigEffort = "max"

Format [BetaJSONOutputFormat](api/beta.md)Optional

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

Schema map[string, any]

The JSON schema of the format

Type JSONSchema

TaskBudget [BetaTokenTaskBudget](api/beta.md)Optional

User-configurable total token budget across contexts.

Total int64

Total token budget across all contexts in the session.

Type Tokens

The budget type. Currently only 'tokens' is supported.

Remaining int64Optional

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

DeprecatedOutputFormat [BetaJSONOutputFormat](api/beta.md)Optional

Deprecated: Use `output_config.format` instead. See [structured outputs](build-with-claude/structured-outputs.md)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

Schema map[string, any]

The JSON schema of the format

Type JSONSchema

ServiceTier stringOptional

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

One of the following:

const BetaMessageBatchNewParamsRequestParamsServiceTierAuto BetaMessageBatchNewParamsRequestParamsServiceTier = "auto"

const BetaMessageBatchNewParamsRequestParamsServiceTierStandardOnly BetaMessageBatchNewParamsRequestParamsServiceTier = "standard\_only"

Speed stringOptional

The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

One of the following:

const BetaMessageBatchNewParamsRequestParamsSpeedStandard BetaMessageBatchNewParamsRequestParamsSpeed = "standard"

const BetaMessageBatchNewParamsRequestParamsSpeedFast BetaMessageBatchNewParamsRequestParamsSpeed = "fast"

StopSequences []stringOptional

Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

Stream boolOptional

Whether to incrementally stream the response using server-sent events.

See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.

System [][BetaTextBlockParamResp](api/beta.md)Optional

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

One of the following:

[][BetaTextBlockParam](api/beta.md)

Text string

Type Text

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [][BetaTextCitationParamUnionResp](api/beta.md)Optional

One of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation

DeprecatedTemperature float64Optional

Amount of randomness injected into the response.

Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0

Thinking [BetaThinkingConfigParamUnionResp](api/beta.md)Optional

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

One of the following:

type BetaThinkingConfigEnabled struct{…}

BudgetTokens int64

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

Type Enabled

Display BetaThinkingConfigEnabledDisplayOptional

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

const BetaThinkingConfigEnabledDisplaySummarized BetaThinkingConfigEnabledDisplay = "summarized"

const BetaThinkingConfigEnabledDisplayOmitted BetaThinkingConfigEnabledDisplay = "omitted"

type BetaThinkingConfigDisabled struct{…}

Type Disabled

type BetaThinkingConfigAdaptive struct{…}

Type Adaptive

Display BetaThinkingConfigAdaptiveDisplayOptional

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

const BetaThinkingConfigAdaptiveDisplaySummarized BetaThinkingConfigAdaptiveDisplay = "summarized"

const BetaThinkingConfigAdaptiveDisplayOmitted BetaThinkingConfigAdaptiveDisplay = "omitted"

ToolChoice [BetaToolChoiceUnion](api/beta.md)Optional

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:

type BetaToolChoiceAuto struct{…}

The model will automatically decide whether to use tools.

Type Auto

DisableParallelToolUse boolOptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

type BetaToolChoiceAny struct{…}

The model will use any available tools.

Type Any

DisableParallelToolUse boolOptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

type BetaToolChoiceTool struct{…}

The model will use the specified tool with `tool_choice.name`.

Name string

The name of the tool to use.

Type Tool

DisableParallelToolUse boolOptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

type BetaToolChoiceNone struct{…}

The model will not be allowed to use tools.

Type None

Tools [][BetaToolUnion](api/beta.md)Optional

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

type BetaTool struct{…}

InputSchema BetaToolInputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

Type Object

Properties map[string, any]Optional

Required []stringOptional

Name string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

AllowedCallers []stringOptional

One of the following:

const BetaToolAllowedCallerDirect BetaToolAllowedCaller = "direct"

const BetaToolAllowedCallerCodeExecution20250825 BetaToolAllowedCaller = "code\_execution\_20250825"

const BetaToolAllowedCallerCodeExecution20260120 BetaToolAllowedCaller = "code\_execution\_20260120"

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Description stringOptional

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

EagerInputStreaming boolOptional

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

Type BetaToolTypeOptional

type BetaToolBash20241022 struct{…}

Name Bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Bash20241022

AllowedCallers []stringOptional

One of the following:

const BetaToolBash20241022AllowedCallerDirect BetaToolBash20241022AllowedCaller = "direct"

const BetaToolBash20241022AllowedCallerCodeExecution20250825 BetaToolBash20241022AllowedCaller = "code\_execution\_20250825"

const BetaToolBash20241022AllowedCallerCodeExecution20260120 BetaToolBash20241022AllowedCaller = "code\_execution\_20260120"

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaToolBash20250124 struct{…}

Name Bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Bash20250124

AllowedCallers []stringOptional

One of the following:

const BetaToolBash20250124AllowedCallerDirect BetaToolBash20250124AllowedCaller = "direct"

const BetaToolBash20250124AllowedCallerCodeExecution20250825 BetaToolBash20250124AllowedCaller = "code\_execution\_20250825"

const BetaToolBash20250124AllowedCallerCodeExecution20260120 BetaToolBash20250124AllowedCaller = "code\_execution\_20260120"

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaCodeExecutionTool20250522 struct{…}

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250522

AllowedCallers []stringOptional

One of the following:

const BetaCodeExecutionTool20250522AllowedCallerDirect BetaCodeExecutionTool20250522AllowedCaller = "direct"

const BetaCodeExecutionTool20250522AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20250522AllowedCaller = "code\_execution\_20250825"

const BetaCodeExecutionTool20250522AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20250522AllowedCaller = "code\_execution\_20260120"

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaCodeExecutionTool20250825 struct{…}

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250825

AllowedCallers []stringOptional

One of the following:

const BetaCodeExecutionTool20250825AllowedCallerDirect BetaCodeExecutionTool20250825AllowedCaller = "direct"

const BetaCodeExecutionTool20250825AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20250825AllowedCaller = "code\_execution\_20250825"

const BetaCodeExecutionTool20250825AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20250825AllowedCaller = "code\_execution\_20260120"

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaCodeExecutionTool20260120 struct{…}

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20260120

AllowedCallers []stringOptional

One of the following:

const BetaCodeExecutionTool20260120AllowedCallerDirect BetaCodeExecutionTool20260120AllowedCaller = "direct"

const BetaCodeExecutionTool20260120AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20260120AllowedCaller = "code\_execution\_20250825"

const BetaCodeExecutionTool20260120AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20260120AllowedCaller = "code\_execution\_20260120"

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaToolComputerUse20241022 struct{…}

DisplayHeightPx int64

The height of the display in pixels.

DisplayWidthPx int64

The width of the display in pixels.

Name Computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Computer20241022

AllowedCallers []stringOptional

One of the following:

const BetaToolComputerUse20241022AllowedCallerDirect BetaToolComputerUse20241022AllowedCaller = "direct"

const BetaToolComputerUse20241022AllowedCallerCodeExecution20250825 BetaToolComputerUse20241022AllowedCaller = "code\_execution\_20250825"

const BetaToolComputerUse20241022AllowedCallerCodeExecution20260120 BetaToolComputerUse20241022AllowedCaller = "code\_execution\_20260120"

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

DisplayNumber int64Optional

The X11 display number (e.g. 0, 1) for the display.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaMemoryTool20250818 struct{…}

Name Memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Memory20250818

AllowedCallers []stringOptional

One of the following:

const BetaMemoryTool20250818AllowedCallerDirect BetaMemoryTool20250818AllowedCaller = "direct"

const BetaMemoryTool20250818AllowedCallerCodeExecution20250825 BetaMemoryTool20250818AllowedCaller = "code\_execution\_20250825"

const BetaMemoryTool20250818AllowedCallerCodeExecution20260120 BetaMemoryTool20250818AllowedCaller = "code\_execution\_20260120"

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaToolComputerUse20250124 struct{…}

DisplayHeightPx int64

The height of the display in pixels.

DisplayWidthPx int64

The width of the display in pixels.

Name Computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Computer20250124

AllowedCallers []stringOptional

One of the following:

const BetaToolComputerUse20250124AllowedCallerDirect BetaToolComputerUse20250124AllowedCaller = "direct"

const BetaToolComputerUse20250124AllowedCallerCodeExecution20250825 BetaToolComputerUse20250124AllowedCaller = "code\_execution\_20250825"

const BetaToolComputerUse20250124AllowedCallerCodeExecution20260120 BetaToolComputerUse20250124AllowedCaller = "code\_execution\_20260120"

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

DisplayNumber int64Optional

The X11 display number (e.g. 0, 1) for the display.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaToolTextEditor20241022 struct{…}

Name StrReplaceEditor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20241022

AllowedCallers []stringOptional

One of the following:

const BetaToolTextEditor20241022AllowedCallerDirect BetaToolTextEditor20241022AllowedCaller = "direct"

const BetaToolTextEditor20241022AllowedCallerCodeExecution20250825 BetaToolTextEditor20241022AllowedCaller = "code\_execution\_20250825"

const BetaToolTextEditor20241022AllowedCallerCodeExecution20260120 BetaToolTextEditor20241022AllowedCaller = "code\_execution\_20260120"

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaToolComputerUse20251124 struct{…}

DisplayHeightPx int64

The height of the display in pixels.

DisplayWidthPx int64

The width of the display in pixels.

Name Computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Computer20251124

AllowedCallers []stringOptional

One of the following:

const BetaToolComputerUse20251124AllowedCallerDirect BetaToolComputerUse20251124AllowedCaller = "direct"

const BetaToolComputerUse20251124AllowedCallerCodeExecution20250825 BetaToolComputerUse20251124AllowedCaller = "code\_execution\_20250825"

const BetaToolComputerUse20251124AllowedCallerCodeExecution20260120 BetaToolComputerUse20251124AllowedCaller = "code\_execution\_20260120"

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

DisplayNumber int64Optional

The X11 display number (e.g. 0, 1) for the display.

EnableZoom boolOptional

Whether to enable an action to take a zoomed-in screenshot of the screen.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaToolTextEditor20250124 struct{…}

Name StrReplaceEditor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250124

AllowedCallers []stringOptional

One of the following:

const BetaToolTextEditor20250124AllowedCallerDirect BetaToolTextEditor20250124AllowedCaller = "direct"

const BetaToolTextEditor20250124AllowedCallerCodeExecution20250825 BetaToolTextEditor20250124AllowedCaller = "code\_execution\_20250825"

const BetaToolTextEditor20250124AllowedCallerCodeExecution20260120 BetaToolTextEditor20250124AllowedCaller = "code\_execution\_20260120"

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaToolTextEditor20250429 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250429

AllowedCallers []stringOptional

One of the following:

const BetaToolTextEditor20250429AllowedCallerDirect BetaToolTextEditor20250429AllowedCaller = "direct"

const BetaToolTextEditor20250429AllowedCallerCodeExecution20250825 BetaToolTextEditor20250429AllowedCaller = "code\_execution\_20250825"

const BetaToolTextEditor20250429AllowedCallerCodeExecution20260120 BetaToolTextEditor20250429AllowedCaller = "code\_execution\_20260120"

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaToolTextEditor20250728 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250728

AllowedCallers []stringOptional

One of the following:

const BetaToolTextEditor20250728AllowedCallerDirect BetaToolTextEditor20250728AllowedCaller = "direct"

const BetaToolTextEditor20250728AllowedCallerCodeExecution20250825 BetaToolTextEditor20250728AllowedCaller = "code\_execution\_20250825"

const BetaToolTextEditor20250728AllowedCallerCodeExecution20260120 BetaToolTextEditor20250728AllowedCaller = "code\_execution\_20260120"

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

MaxCharacters int64Optional

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaWebSearchTool20250305 struct{…}

Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20250305

AllowedCallers []stringOptional

One of the following:

const BetaWebSearchTool20250305AllowedCallerDirect BetaWebSearchTool20250305AllowedCaller = "direct"

const BetaWebSearchTool20250305AllowedCallerCodeExecution20250825 BetaWebSearchTool20250305AllowedCaller = "code\_execution\_20250825"

const BetaWebSearchTool20250305AllowedCallerCodeExecution20260120 BetaWebSearchTool20250305AllowedCaller = "code\_execution\_20260120"

AllowedDomains []stringOptional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains []stringOptional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

UserLocation [BetaUserLocation](api/beta.md)Optional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

City stringOptional

The city of the user.

Country stringOptional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Region stringOptional

The region of the user.

Timezone stringOptional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

type BetaWebFetchTool20250910 struct{…}

Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20250910

AllowedCallers []stringOptional

One of the following:

const BetaWebFetchTool20250910AllowedCallerDirect BetaWebFetchTool20250910AllowedCaller = "direct"

const BetaWebFetchTool20250910AllowedCallerCodeExecution20250825 BetaWebFetchTool20250910AllowedCaller = "code\_execution\_20250825"

const BetaWebFetchTool20250910AllowedCallerCodeExecution20260120 BetaWebFetchTool20250910AllowedCaller = "code\_execution\_20260120"

AllowedDomains []stringOptional

List of domains to allow fetching from

BlockedDomains []stringOptional

List of domains to block fetching from

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [BetaCitationsConfigParamResp](api/beta.md)Optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled boolOptional

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxContentTokens int64Optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaWebSearchTool20260209 struct{…}

Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20260209

AllowedCallers []stringOptional

One of the following:

const BetaWebSearchTool20260209AllowedCallerDirect BetaWebSearchTool20260209AllowedCaller = "direct"

const BetaWebSearchTool20260209AllowedCallerCodeExecution20250825 BetaWebSearchTool20260209AllowedCaller = "code\_execution\_20250825"

const BetaWebSearchTool20260209AllowedCallerCodeExecution20260120 BetaWebSearchTool20260209AllowedCaller = "code\_execution\_20260120"

AllowedDomains []stringOptional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains []stringOptional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

UserLocation [BetaUserLocation](api/beta.md)Optional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

City stringOptional

The city of the user.

Country stringOptional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Region stringOptional

The region of the user.

Timezone stringOptional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

type BetaWebFetchTool20260209 struct{…}

Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20260209

AllowedCallers []stringOptional

One of the following:

const BetaWebFetchTool20260209AllowedCallerDirect BetaWebFetchTool20260209AllowedCaller = "direct"

const BetaWebFetchTool20260209AllowedCallerCodeExecution20250825 BetaWebFetchTool20260209AllowedCaller = "code\_execution\_20250825"

const BetaWebFetchTool20260209AllowedCallerCodeExecution20260120 BetaWebFetchTool20260209AllowedCaller = "code\_execution\_20260120"

AllowedDomains []stringOptional

List of domains to allow fetching from

BlockedDomains []stringOptional

List of domains to block fetching from

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [BetaCitationsConfigParamResp](api/beta.md)Optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled boolOptional

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxContentTokens int64Optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaWebFetchTool20260309 struct{…}

Web fetch tool with use\_cache parameter for bypassing cached content.

Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20260309

AllowedCallers []stringOptional

One of the following:

const BetaWebFetchTool20260309AllowedCallerDirect BetaWebFetchTool20260309AllowedCaller = "direct"

const BetaWebFetchTool20260309AllowedCallerCodeExecution20250825 BetaWebFetchTool20260309AllowedCaller = "code\_execution\_20250825"

const BetaWebFetchTool20260309AllowedCallerCodeExecution20260120 BetaWebFetchTool20260309AllowedCaller = "code\_execution\_20260120"

AllowedDomains []stringOptional

List of domains to allow fetching from

BlockedDomains []stringOptional

List of domains to block fetching from

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [BetaCitationsConfigParamResp](api/beta.md)Optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled boolOptional

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxContentTokens int64Optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

UseCache boolOptional

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

type BetaAdvisorTool20260301 struct{…}

Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

const ModelClaudeFable5 Model = "claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

const ModelClaudeMythos5 Model = "claude-mythos-5"

Most capable model for cybersecurity and biology research

const ModelClaudeOpus4\_8 Model = "claude-opus-4-8"

Frontier intelligence for long-running agents and coding

const ModelClaudeOpus4\_7 Model = "claude-opus-4-7"

Frontier intelligence for long-running agents and coding

const ModelClaudeMythosPreview Model = "claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

const ModelClaudeOpus4\_6 Model = "claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

Name Advisor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Advisor20260301

AllowedCallers []stringOptional

One of the following:

const BetaAdvisorTool20260301AllowedCallerDirect BetaAdvisorTool20260301AllowedCaller = "direct"

const BetaAdvisorTool20260301AllowedCallerCodeExecution20250825 BetaAdvisorTool20260301AllowedCaller = "code\_execution\_20250825"

const BetaAdvisorTool20260301AllowedCallerCodeExecution20260120 BetaAdvisorTool20260301AllowedCaller = "code\_execution\_20260120"

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Caching [BetaCacheControlEphemeral](api/beta.md)Optional

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxTokens int64Optional

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaToolSearchToolBm25\_20251119 struct{…}

Name ToolSearchToolBm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type BetaToolSearchToolBm25\_20251119Type

One of the following:

const BetaToolSearchToolBm25\_20251119TypeToolSearchToolBm25\_20251119 BetaToolSearchToolBm25\_20251119Type = "tool\_search\_tool\_bm25\_20251119"

const BetaToolSearchToolBm25\_20251119TypeToolSearchToolBm25 BetaToolSearchToolBm25\_20251119Type = "tool\_search\_tool\_bm25"

AllowedCallers []stringOptional

One of the following:

const BetaToolSearchToolBm25\_20251119AllowedCallerDirect BetaToolSearchToolBm25\_20251119AllowedCaller = "direct"

const BetaToolSearchToolBm25\_20251119AllowedCallerCodeExecution20250825 BetaToolSearchToolBm25\_20251119AllowedCaller = "code\_execution\_20250825"

const BetaToolSearchToolBm25\_20251119AllowedCallerCodeExecution20260120 BetaToolSearchToolBm25\_20251119AllowedCaller = "code\_execution\_20260120"

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaToolSearchToolRegex20251119 struct{…}

Name ToolSearchToolRegex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type BetaToolSearchToolRegex20251119Type

One of the following:

const BetaToolSearchToolRegex20251119TypeToolSearchToolRegex20251119 BetaToolSearchToolRegex20251119Type = "tool\_search\_tool\_regex\_20251119"

const BetaToolSearchToolRegex20251119TypeToolSearchToolRegex BetaToolSearchToolRegex20251119Type = "tool\_search\_tool\_regex"

AllowedCallers []stringOptional

One of the following:

const BetaToolSearchToolRegex20251119AllowedCallerDirect BetaToolSearchToolRegex20251119AllowedCaller = "direct"

const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20250825 BetaToolSearchToolRegex20251119AllowedCaller = "code\_execution\_20250825"

const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20260120 BetaToolSearchToolRegex20251119AllowedCaller = "code\_execution\_20260120"

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

type BetaMCPToolset struct{…}

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

MCPServerName string

Name of the MCP server to configure tools for

Type MCPToolset

CacheControl [BetaCacheControlEphemeral](api/beta.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Configs map[string, [BetaMCPToolConfig](api/beta.md)]Optional

Configuration overrides for specific tools, keyed by tool name

DeferLoading boolOptional

Enabled boolOptional

DefaultConfig [BetaMCPToolDefaultConfig](api/beta.md)Optional

Default configuration applied to all tools from this server

DeferLoading boolOptional

Enabled boolOptional

DeprecatedTopK int64Optional

Only sample from the top K options for each subsequent token.

Deprecated. Models released after Claude Opus 4.6 do not accept top\_k; any value will be rejected with a 400 error.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only.

minimum0

DeprecatedTopP float64Optional

Use nucleus sampling.

Deprecated. Models released after Claude Opus 4.6 do not support setting top\_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

Recommended for advanced use cases only.

maximum1

minimum0

UserProfileID stringOptional

The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization.

Betas param.Field[[]AnthropicBeta]Optional

Header param: Optional header to specify the beta version(s) you want to use.

string

type AnthropicBeta string

One of the following:

const AnthropicBetaMessageBatches2024\_09\_24 AnthropicBeta = "message-batches-2024-09-24"

const AnthropicBetaPromptCaching2024\_07\_31 AnthropicBeta = "prompt-caching-2024-07-31"

const AnthropicBetaComputerUse2024\_10\_22 AnthropicBeta = "computer-use-2024-10-22"

const AnthropicBetaComputerUse2025\_01\_24 AnthropicBeta = "computer-use-2025-01-24"

const AnthropicBetaPDFs2024\_09\_25 AnthropicBeta = "pdfs-2024-09-25"

const AnthropicBetaTokenCounting2024\_11\_01 AnthropicBeta = "token-counting-2024-11-01"

const AnthropicBetaTokenEfficientTools2025\_02\_19 AnthropicBeta = "token-efficient-tools-2025-02-19"

const AnthropicBetaOutput128k2025\_02\_19 AnthropicBeta = "output-128k-2025-02-19"

const AnthropicBetaFilesAPI2025\_04\_14 AnthropicBeta = "files-api-2025-04-14"

const AnthropicBetaMCPClient2025\_04\_04 AnthropicBeta = "mcp-client-2025-04-04"

const AnthropicBetaMCPClient2025\_11\_20 AnthropicBeta = "mcp-client-2025-11-20"

const AnthropicBetaDevFullThinking2025\_05\_14 AnthropicBeta = "dev-full-thinking-2025-05-14"

const AnthropicBetaInterleavedThinking2025\_05\_14 AnthropicBeta = "interleaved-thinking-2025-05-14"

const AnthropicBetaCodeExecution2025\_05\_22 AnthropicBeta = "code-execution-2025-05-22"

const AnthropicBetaExtendedCacheTTL2025\_04\_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"

const AnthropicBetaContext1m2025\_08\_07 AnthropicBeta = "context-1m-2025-08-07"

const AnthropicBetaContextManagement2025\_06\_27 AnthropicBeta = "context-management-2025-06-27"

const AnthropicBetaModelContextWindowExceeded2025\_08\_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"

const AnthropicBetaSkills2025\_10\_02 AnthropicBeta = "skills-2025-10-02"

const AnthropicBetaFastMode2026\_02\_01 AnthropicBeta = "fast-mode-2026-02-01"

const AnthropicBetaOutput300k2026\_03\_24 AnthropicBeta = "output-300k-2026-03-24"

const AnthropicBetaUserProfiles2026\_03\_24 AnthropicBeta = "user-profiles-2026-03-24"

const AnthropicBetaAdvisorTool2026\_03\_01 AnthropicBeta = "advisor-tool-2026-03-01"

const AnthropicBetaManagedAgents2026\_04\_01 AnthropicBeta = "managed-agents-2026-04-01"

const AnthropicBetaCacheDiagnosis2026\_04\_07 AnthropicBeta = "cache-diagnosis-2026-04-07"

const AnthropicBetaThinkingTokenCount2026\_05\_13 AnthropicBeta = "thinking-token-count-2026-05-13"

const AnthropicBetaServerSideFallback2026\_06\_01 AnthropicBeta = "server-side-fallback-2026-06-01"

const AnthropicBetaFallbackCredit2026\_06\_01 AnthropicBeta = "fallback-credit-2026-06-01"

##### ReturnsExpand Collapse

type BetaMessageBatch struct{…}

ID string

Unique object identifier.

The format and length of IDs may change over time.

ArchivedAt Time

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

CancelInitiatedAt Time

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

CreatedAt Time

RFC 3339 datetime string representing the time at which the Message Batch was created.

EndedAt Time

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

ExpiresAt Time

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

ProcessingStatus BetaMessageBatchProcessingStatus

Processing status of the Message Batch.

One of the following:

const BetaMessageBatchProcessingStatusInProgress BetaMessageBatchProcessingStatus = "in\_progress"

const BetaMessageBatchProcessingStatusCanceling BetaMessageBatchProcessingStatus = "canceling"

const BetaMessageBatchProcessingStatusEnded BetaMessageBatchProcessingStatus = "ended"

RequestCounts [BetaMessageBatchRequestCounts](api/beta.md)

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

Canceled int64

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

Errored int64

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

Expired int64

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

Processing int64

Number of requests in the Message Batch that are processing.

Succeeded int64

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

ResultsURL string

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Type MessageBatch

Object type.

For Message Batches, this is always `"message_batch"`.

Create a Message Batch

Go

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
  betaMessageBatch, err := client.Beta.Messages.Batches.New(context.TODO(), anthropic.BetaMessageBatchNewParams{
    Requests: []anthropic.BetaMessageBatchNewParamsRequest{anthropic.BetaMessageBatchNewParamsRequest{
      CustomID: "my-custom-id-1",
      Params: anthropic.BetaMessageBatchNewParamsRequestParams{
        MaxTokens: 1024,
        Messages: []anthropic.BetaMessageParam{anthropic.BetaMessageParam{
          Content: []anthropic.BetaContentBlockParamUnion{anthropic.BetaContentBlockParamUnion{
            OfText: &anthropic.BetaTextBlockParam{
              Text: "x",
            },
          }},
          Role: anthropic.BetaMessageParamRoleUser,
        }},
        Model: anthropic.ModelClaudeOpus4_6,
      },
    }},
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaMessageBatch.ID)
}
```

Response 200



```shiki
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

---

*Copyright © Anthropic. All rights reserved.*
