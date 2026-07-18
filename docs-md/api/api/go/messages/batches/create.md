# Create a Message Batch

Copy page



Go

# Create a Message Batch

client.Messages.Batches.New(ctx, params) (\*[MessageBatch](api/messages/batches.md), error)

POST/v1/messages/batches

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](build-with-claude/batch-processing.md)

##### ParametersExpand Collapse



params MessageBatchNewParams



Requests param.Field[[]MessageBatchNewParamsRequest]

Body param: List of requests for prompt completion. Each is an individual request to create a Message.



CustomID string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

maxLength64

minLength1



Params MessageBatchNewParamsRequestParams

Messages API creation parameters for the individual request.

See the [Messages API reference](api/messages.md) for full documentation on available parameters.



MaxTokens int64

The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Set to `0` to populate the [prompt cache](build-with-claude/prompt-caching.md) without generating a response.

Different models have different maximum values for this parameter. See [models](about-claude/models/overview.md) for details.

minimum0



Messages [][MessageParamResp](api/messages.md)

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

See [input examples](build-with-claude/working-with-messages.md).

Note that if you want to include a [system prompt](build-with-claude/prompt-engineering/claude-prompting-best-practices.md), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

There is a limit of 100,000 messages in a single request.



Content [][ContentBlockParamUnionResp](api/messages.md)

One of the following:



[][ContentBlockParamUnionResp](api/messages.md)

One of the following:



type TextBlockParamResp struct{…}

Text string

Type Text



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [][TextCitationParamUnionResp](api/messages.md)Optional

One of the following:



type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationSearchResultLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation



type ImageBlockParamResp struct{…}



Source ImageBlockParamSourceUnionResp

One of the following:



type Base64ImageSource struct{…}

Data string



MediaType Base64ImageSourceMediaType

One of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64



type URLImageSource struct{…}

Type URL

URL string

Type Image



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



type DocumentBlockParamResp struct{…}



Source DocumentBlockParamSourceUnionResp

One of the following:



type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text



type ContentBlockSource struct{…}



Content ContentBlockSourceContentUnion

One of the following:

string



[][ContentBlockSourceContentItemUnion](api/messages.md)

One of the following:



type TextBlockParamResp struct{…}

Text string

Type Text



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [][TextCitationParamUnionResp](api/messages.md)Optional

One of the following:



type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationSearchResultLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation



type ImageBlockParamResp struct{…}



Source ImageBlockParamSourceUnionResp

One of the following:



type Base64ImageSource struct{…}

Data string



MediaType Base64ImageSourceMediaType

One of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64



type URLImageSource struct{…}

Type URL

URL string

Type Image



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content



type URLPDFSource struct{…}

Type URL

URL string

Type Document



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [CitationsConfigParamResp](api/messages.md)Optional

Enabled boolOptional

Context stringOptional

Title stringOptional



type SearchResultBlockParamResp struct{…}



Content [][TextBlockParamResp](api/messages.md)

Text string

Type Text



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [][TextCitationParamUnionResp](api/messages.md)Optional

One of the following:



type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationSearchResultLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation

Source string

Title string

Type SearchResult



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [CitationsConfigParamResp](api/messages.md)Optional

Enabled boolOptional



type ThinkingBlockParamResp struct{…}

Signature string

Thinking string

Type Thinking



type RedactedThinkingBlockParamResp struct{…}

Data string

Type RedactedThinking



type ToolUseBlockParamResp struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Caller ToolUseBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:



type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type ToolResultBlockParamResp struct{…}

ToolUseID string

Type ToolResult



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Content []ToolResultBlockParamContentUnionRespOptional

One of the following:



[]ToolResultBlockParamContentUnionResp

One of the following:



type TextBlockParamResp struct{…}

Text string

Type Text



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [][TextCitationParamUnionResp](api/messages.md)Optional

One of the following:



type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationSearchResultLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation



type ImageBlockParamResp struct{…}



Source ImageBlockParamSourceUnionResp

One of the following:



type Base64ImageSource struct{…}

Data string



MediaType Base64ImageSourceMediaType

One of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64



type URLImageSource struct{…}

Type URL

URL string

Type Image



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



type SearchResultBlockParamResp struct{…}



Content [][TextBlockParamResp](api/messages.md)

Text string

Type Text



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [][TextCitationParamUnionResp](api/messages.md)Optional

One of the following:



type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationSearchResultLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation

Source string

Title string

Type SearchResult



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [CitationsConfigParamResp](api/messages.md)Optional

Enabled boolOptional



type DocumentBlockParamResp struct{…}



Source DocumentBlockParamSourceUnionResp

One of the following:



type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text



type ContentBlockSource struct{…}



Content ContentBlockSourceContentUnion

One of the following:

string



[][ContentBlockSourceContentItemUnion](api/messages.md)

One of the following:



type TextBlockParamResp struct{…}

Text string

Type Text



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [][TextCitationParamUnionResp](api/messages.md)Optional

One of the following:



type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationSearchResultLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation



type ImageBlockParamResp struct{…}



Source ImageBlockParamSourceUnionResp

One of the following:



type Base64ImageSource struct{…}

Data string



MediaType Base64ImageSourceMediaType

One of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64



type URLImageSource struct{…}

Type URL

URL string

Type Image



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content



type URLPDFSource struct{…}

Type URL

URL string

Type Document



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [CitationsConfigParamResp](api/messages.md)Optional

Enabled boolOptional

Context stringOptional

Title stringOptional



type ToolReferenceBlockParamResp struct{…}

Tool reference block that can be included in tool\_result content.

ToolName string

Type ToolReference



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

IsError boolOptional



type ServerToolUseBlockParamResp struct{…}

ID string

Input map[string, any]



Name ServerToolUseBlockParamName

One of the following:

const ServerToolUseBlockParamNameWebSearch ServerToolUseBlockParamName = "web\_search"

const ServerToolUseBlockParamNameWebFetch ServerToolUseBlockParamName = "web\_fetch"

const ServerToolUseBlockParamNameCodeExecution ServerToolUseBlockParamName = "code\_execution"

const ServerToolUseBlockParamNameBashCodeExecution ServerToolUseBlockParamName = "bash\_code\_execution"

const ServerToolUseBlockParamNameTextEditorCodeExecution ServerToolUseBlockParamName = "text\_editor\_code\_execution"

const ServerToolUseBlockParamNameToolSearchToolRegex ServerToolUseBlockParamName = "tool\_search\_tool\_regex"

const ServerToolUseBlockParamNameToolSearchToolBm25 ServerToolUseBlockParamName = "tool\_search\_tool\_bm25"

Type ServerToolUse



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Caller ServerToolUseBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:



type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type WebSearchToolResultBlockParamResp struct{…}



Content [WebSearchToolResultBlockParamContentUnionResp](api/messages.md)

One of the following:



[][WebSearchResultBlockParamResp](api/messages.md)

EncryptedContent string

Title string

Type WebSearchResult

URL string

PageAge stringOptional



type WebSearchToolRequestError struct{…}



ErrorCode [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](api/messages.md) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](api/messages.md) = "max\_uses\_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](api/messages.md) = "query\_too\_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](api/messages.md) = "request\_too\_large"

Type WebSearchToolResultError

ToolUseID string

Type WebSearchToolResult



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Caller WebSearchToolResultBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:



type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type WebFetchToolResultBlockParamResp struct{…}



Content WebFetchToolResultBlockParamContentUnionResp

One of the following:



type WebFetchToolResultErrorBlockParamResp struct{…}



ErrorCode [WebFetchToolResultErrorCode](api/messages.md)

One of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](api/messages.md) = "url\_too\_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_allowed"

const WebFetchToolResultErrorCodeURLNotInPriorContext [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_in\_prior\_context"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](api/messages.md) = "unsupported\_content\_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](api/messages.md) = "max\_uses\_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](api/messages.md) = "unavailable"

Type WebFetchToolResultError



type WebFetchBlockParamResp struct{…}



Content [DocumentBlockParamResp](api/messages.md)



Source DocumentBlockParamSourceUnionResp

One of the following:



type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text



type ContentBlockSource struct{…}



Content ContentBlockSourceContentUnion

One of the following:

string



[][ContentBlockSourceContentItemUnion](api/messages.md)

One of the following:



type TextBlockParamResp struct{…}

Text string

Type Text



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [][TextCitationParamUnionResp](api/messages.md)Optional

One of the following:



type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationSearchResultLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation



type ImageBlockParamResp struct{…}



Source ImageBlockParamSourceUnionResp

One of the following:



type Base64ImageSource struct{…}

Data string



MediaType Base64ImageSourceMediaType

One of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64



type URLImageSource struct{…}

Type URL

URL string

Type Image



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content



type URLPDFSource struct{…}

Type URL

URL string

Type Document



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [CitationsConfigParamResp](api/messages.md)Optional

Enabled boolOptional

Context stringOptional

Title stringOptional

Type WebFetchResult

URL string

Fetched content URL

RetrievedAt stringOptional

ISO 8601 timestamp when the content was retrieved

ToolUseID string

Type WebFetchToolResult



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Caller WebFetchToolResultBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:



type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type CodeExecutionToolResultBlockParamResp struct{…}



Content [CodeExecutionToolResultBlockParamContentUnionResp](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type CodeExecutionToolResultErrorParamResp struct{…}



ErrorCode [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type CodeExecutionResultBlockParamResp struct{…}



Content [][CodeExecutionOutputBlockParamResp](api/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type EncryptedCodeExecutionResultBlockParamResp struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][CodeExecutionOutputBlockParamResp](api/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



type BashCodeExecutionToolResultBlockParamResp struct{…}



Content BashCodeExecutionToolResultBlockParamContentUnionResp

One of the following:



type BashCodeExecutionToolResultErrorParamResp struct{…}



ErrorCode [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](api/messages.md) = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError



type BashCodeExecutionResultBlockParamResp struct{…}



Content [][BashCodeExecutionOutputBlockParamResp](api/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



type TextEditorCodeExecutionToolResultBlockParamResp struct{…}



Content TextEditorCodeExecutionToolResultBlockParamContentUnionResp

One of the following:



type TextEditorCodeExecutionToolResultErrorParamResp struct{…}



ErrorCode [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "file\_not\_found"

Type TextEditorCodeExecutionToolResultError

ErrorMessage stringOptional



type TextEditorCodeExecutionViewResultBlockParamResp struct{…}

Content string



FileType TextEditorCodeExecutionViewResultBlockParamFileType

One of the following:

const TextEditorCodeExecutionViewResultBlockParamFileTypeText TextEditorCodeExecutionViewResultBlockParamFileType = "text"

const TextEditorCodeExecutionViewResultBlockParamFileTypeImage TextEditorCodeExecutionViewResultBlockParamFileType = "image"

const TextEditorCodeExecutionViewResultBlockParamFileTypePDF TextEditorCodeExecutionViewResultBlockParamFileType = "pdf"

Type TextEditorCodeExecutionViewResult

NumLines int64Optional

StartLine int64Optional

TotalLines int64Optional



type TextEditorCodeExecutionCreateResultBlockParamResp struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type TextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}

Type TextEditorCodeExecutionStrReplaceResult

Lines []stringOptional

NewLines int64Optional

NewStart int64Optional

OldLines int64Optional

OldStart int64Optional

ToolUseID string

Type TextEditorCodeExecutionToolResult



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



type ToolSearchToolResultBlockParamResp struct{…}



Content ToolSearchToolResultBlockParamContentUnionResp

One of the following:



type ToolSearchToolResultErrorParamResp struct{…}



ErrorCode [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](api/messages.md) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type ToolSearchToolResultError

ErrorMessage stringOptional



type ToolSearchToolSearchResultBlockParamResp struct{…}



ToolReferences [][ToolReferenceBlockParamResp](api/messages.md)

ToolName string

Type ToolReference



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



type ContainerUploadBlockParamResp struct{…}

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

FileID string

Type ContainerUpload



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



type MidConversationSystemBlockParamResp struct{…}

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



Content [][TextBlockParamResp](api/messages.md)

System instruction text blocks.

Text string

Type Text



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [][TextCitationParamUnionResp](api/messages.md)Optional

One of the following:



type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationSearchResultLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation

Type MidConvSystem



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Role MessageParamRole

One of the following:

const MessageParamRoleUser MessageParamRole = "user"

const MessageParamRoleAssistant MessageParamRole = "assistant"

const MessageParamRoleSystem MessageParamRole = "system"



Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

const ModelClaudeSonnet5 Model = "claude-sonnet-5"

High-performance model for coding and agents

const ModelClaudeFable5 Model = "claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

const ModelClaudeMythos5 Model = "claude-mythos-5"

Most capable model for cybersecurity and biology research

const ModelClaudeOpus4\_8 Model = "claude-opus-4-8"

Frontier intelligence for long-running agents and coding

const ModelClaudeOpus4\_7 Model = "claude-opus-4-7"

Frontier intelligence for long-running agents and coding

const ModelClaudeMythosPreview Model = "claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

const ModelClaudeOpus4\_6 Model = "claude-opus-4-6"

Frontier intelligence for long-running agents and coding

const ModelClaudeSonnet4\_6 Model = "claude-sonnet-4-6"

Best combination of speed and intelligence

const ModelClaudeHaiku4\_5 Model = "claude-haiku-4-5"

Fastest model with near-frontier intelligence

const ModelClaudeHaiku4\_5\_20251001 Model = "claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

const ModelClaudeOpus4\_5 Model = "claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

const ModelClaudeOpus4\_5\_20251101 Model = "claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

const ModelClaudeSonnet4\_5 Model = "claude-sonnet-4-5"

High-performance model for agents and coding

const ModelClaudeSonnet4\_5\_20250929 Model = "claude-sonnet-4-5-20250929"

High-performance model for agents and coding

const ModelClaudeOpus4\_1 Model = "claude-opus-4-1"

Exceptional model for specialized complex tasks

const ModelClaudeOpus4\_1\_20250805 Model = "claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

string



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Top-level cache control automatically applies a cache\_control marker to the last cacheable block in the request.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Container stringOptional

Container identifier for reuse across requests.

InferenceGeo stringOptional

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.



Metadata [Metadata](api/messages.md)Optional

An object describing metadata about the request.



UserID stringOptional

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



OutputConfig [OutputConfig](api/messages.md)Optional

Configuration options for the model's output, such as the output format.



Effort OutputConfigEffortOptional

All possible effort levels.

One of the following:

const OutputConfigEffortLow OutputConfigEffort = "low"

const OutputConfigEffortMedium OutputConfigEffort = "medium"

const OutputConfigEffortHigh OutputConfigEffort = "high"

const OutputConfigEffortXhigh OutputConfigEffort = "xhigh"

const OutputConfigEffortMax OutputConfigEffort = "max"



Format [JSONOutputFormat](api/messages.md)Optional

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

Schema map[string, any]

The JSON schema of the format

Type JSONSchema



ServiceTier stringOptional

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](api/service-tiers.md) for details.

One of the following:

const MessageBatchNewParamsRequestParamsServiceTierAuto MessageBatchNewParamsRequestParamsServiceTier = "auto"

const MessageBatchNewParamsRequestParamsServiceTierStandardOnly MessageBatchNewParamsRequestParamsServiceTier = "standard\_only"



StopSequences []stringOptional

Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.



Stream boolOptional

Whether to incrementally stream the response using server-sent events.

See [streaming](build-with-claude/streaming.md) for details.



System [][TextBlockParamResp](api/messages.md)Optional

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](build-with-claude/prompt-engineering/claude-prompting-best-practices.md).

One of the following:



[][TextBlockParam](api/messages.md)

Text string

Type Text



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [][TextCitationParamUnionResp](api/messages.md)Optional

One of the following:



type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

DocumentIndex int64

DocumentTitle string



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationSearchResultLocationParamResp struct{…}



CitedText string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



EndBlockIndex int64

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



SearchResultIndex int64

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

Source string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Title string

Type SearchResultLocation



Thinking [ThinkingConfigParamUnionResp](api/messages.md)Optional

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

One of the following:



type ThinkingConfigEnabled struct{…}



BudgetTokens int64

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

Type Enabled



Display ThinkingConfigEnabledDisplayOptional

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

const ThinkingConfigEnabledDisplaySummarized ThinkingConfigEnabledDisplay = "summarized"

const ThinkingConfigEnabledDisplayOmitted ThinkingConfigEnabledDisplay = "omitted"



type ThinkingConfigDisabled struct{…}

Type Disabled



type ThinkingConfigAdaptive struct{…}

Type Adaptive



Display ThinkingConfigAdaptiveDisplayOptional

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

const ThinkingConfigAdaptiveDisplaySummarized ThinkingConfigAdaptiveDisplay = "summarized"

const ThinkingConfigAdaptiveDisplayOmitted ThinkingConfigAdaptiveDisplay = "omitted"



ToolChoice [ToolChoiceUnion](api/messages.md)Optional

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



type ToolChoiceAuto struct{…}

The model will automatically decide whether to use tools.

Type Auto



DisableParallelToolUse boolOptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



type ToolChoiceAny struct{…}

The model will use any available tools.

Type Any



DisableParallelToolUse boolOptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



type ToolChoiceTool struct{…}

The model will use the specified tool with `tool_choice.name`.

Name string

The name of the tool to use.

Type Tool



DisableParallelToolUse boolOptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



type ToolChoiceNone struct{…}

The model will not be allowed to use tools.

Type None



Tools [][ToolUnion](api/messages.md)Optional

Definitions of tools that the model may use.

If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](agents-and-tools/tool-use/server-tools.md), see their individual documentation as each has its own behavior (e.g., the [web search tool](agents-and-tools/tool-use/web-search-tool.md)).

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

See our [guide](agents-and-tools/tool-use/overview.md) for more details.

One of the following:



type Tool struct{…}



InputSchema ToolInputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

Type Object

Properties map[string, any]Optional

Required []stringOptional



Name string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1



AllowedCallers []stringOptional

One of the following:

const ToolAllowedCallerDirect ToolAllowedCaller = "direct"

const ToolAllowedCallerCodeExecution20250825 ToolAllowedCaller = "code\_execution\_20250825"

const ToolAllowedCallerCodeExecution20260120 ToolAllowedCaller = "code\_execution\_20260120"

const ToolAllowedCallerCodeExecution20260521 ToolAllowedCaller = "code\_execution\_20260521"



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



Description stringOptional

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

EagerInputStreaming boolOptional

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

Type ToolTypeOptional



type ToolBash20250124 struct{…}



Name Bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Bash20250124



AllowedCallers []stringOptional

One of the following:

const ToolBash20250124AllowedCallerDirect ToolBash20250124AllowedCaller = "direct"

const ToolBash20250124AllowedCallerCodeExecution20250825 ToolBash20250124AllowedCaller = "code\_execution\_20250825"

const ToolBash20250124AllowedCallerCodeExecution20260120 ToolBash20250124AllowedCaller = "code\_execution\_20260120"

const ToolBash20250124AllowedCallerCodeExecution20260521 ToolBash20250124AllowedCaller = "code\_execution\_20260521"



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type CodeExecutionTool20250522 struct{…}



Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250522



AllowedCallers []stringOptional

One of the following:

const CodeExecutionTool20250522AllowedCallerDirect CodeExecutionTool20250522AllowedCaller = "direct"

const CodeExecutionTool20250522AllowedCallerCodeExecution20250825 CodeExecutionTool20250522AllowedCaller = "code\_execution\_20250825"

const CodeExecutionTool20250522AllowedCallerCodeExecution20260120 CodeExecutionTool20250522AllowedCaller = "code\_execution\_20260120"

const CodeExecutionTool20250522AllowedCallerCodeExecution20260521 CodeExecutionTool20250522AllowedCaller = "code\_execution\_20260521"



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type CodeExecutionTool20250825 struct{…}



Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250825



AllowedCallers []stringOptional

One of the following:

const CodeExecutionTool20250825AllowedCallerDirect CodeExecutionTool20250825AllowedCaller = "direct"

const CodeExecutionTool20250825AllowedCallerCodeExecution20250825 CodeExecutionTool20250825AllowedCaller = "code\_execution\_20250825"

const CodeExecutionTool20250825AllowedCallerCodeExecution20260120 CodeExecutionTool20250825AllowedCaller = "code\_execution\_20260120"

const CodeExecutionTool20250825AllowedCallerCodeExecution20260521 CodeExecutionTool20250825AllowedCaller = "code\_execution\_20260521"



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type CodeExecutionTool20260120 struct{…}

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20260120



AllowedCallers []stringOptional

One of the following:

const CodeExecutionTool20260120AllowedCallerDirect CodeExecutionTool20260120AllowedCaller = "direct"

const CodeExecutionTool20260120AllowedCallerCodeExecution20250825 CodeExecutionTool20260120AllowedCaller = "code\_execution\_20250825"

const CodeExecutionTool20260120AllowedCallerCodeExecution20260120 CodeExecutionTool20260120AllowedCaller = "code\_execution\_20260120"

const CodeExecutionTool20260120AllowedCallerCodeExecution20260521 CodeExecutionTool20260120AllowedCaller = "code\_execution\_20260521"



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type CodeExecutionTool20260521 struct{…}

Code execution tool with REPL state persistence.



Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20260521



AllowedCallers []stringOptional

One of the following:

const CodeExecutionTool20260521AllowedCallerDirect CodeExecutionTool20260521AllowedCaller = "direct"

const CodeExecutionTool20260521AllowedCallerCodeExecution20250825 CodeExecutionTool20260521AllowedCaller = "code\_execution\_20250825"

const CodeExecutionTool20260521AllowedCallerCodeExecution20260120 CodeExecutionTool20260521AllowedCaller = "code\_execution\_20260120"

const CodeExecutionTool20260521AllowedCallerCodeExecution20260521 CodeExecutionTool20260521AllowedCaller = "code\_execution\_20260521"



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type MemoryTool20250818 struct{…}



Name Memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Memory20250818



AllowedCallers []stringOptional

One of the following:

const MemoryTool20250818AllowedCallerDirect MemoryTool20250818AllowedCaller = "direct"

const MemoryTool20250818AllowedCallerCodeExecution20250825 MemoryTool20250818AllowedCaller = "code\_execution\_20250825"

const MemoryTool20250818AllowedCallerCodeExecution20260120 MemoryTool20250818AllowedCaller = "code\_execution\_20260120"

const MemoryTool20250818AllowedCallerCodeExecution20260521 MemoryTool20250818AllowedCaller = "code\_execution\_20260521"



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type ToolTextEditor20250124 struct{…}



Name StrReplaceEditor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250124



AllowedCallers []stringOptional

One of the following:

const ToolTextEditor20250124AllowedCallerDirect ToolTextEditor20250124AllowedCaller = "direct"

const ToolTextEditor20250124AllowedCallerCodeExecution20250825 ToolTextEditor20250124AllowedCaller = "code\_execution\_20250825"

const ToolTextEditor20250124AllowedCallerCodeExecution20260120 ToolTextEditor20250124AllowedCaller = "code\_execution\_20260120"

const ToolTextEditor20250124AllowedCallerCodeExecution20260521 ToolTextEditor20250124AllowedCaller = "code\_execution\_20260521"



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type ToolTextEditor20250429 struct{…}



Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250429



AllowedCallers []stringOptional

One of the following:

const ToolTextEditor20250429AllowedCallerDirect ToolTextEditor20250429AllowedCaller = "direct"

const ToolTextEditor20250429AllowedCallerCodeExecution20250825 ToolTextEditor20250429AllowedCaller = "code\_execution\_20250825"

const ToolTextEditor20250429AllowedCallerCodeExecution20260120 ToolTextEditor20250429AllowedCaller = "code\_execution\_20260120"

const ToolTextEditor20250429AllowedCallerCodeExecution20260521 ToolTextEditor20250429AllowedCaller = "code\_execution\_20260521"



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type ToolTextEditor20250728 struct{…}



Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250728



AllowedCallers []stringOptional

One of the following:

const ToolTextEditor20250728AllowedCallerDirect ToolTextEditor20250728AllowedCaller = "direct"

const ToolTextEditor20250728AllowedCallerCodeExecution20250825 ToolTextEditor20250728AllowedCaller = "code\_execution\_20250825"

const ToolTextEditor20250728AllowedCallerCodeExecution20260120 ToolTextEditor20250728AllowedCaller = "code\_execution\_20260120"

const ToolTextEditor20250728AllowedCallerCodeExecution20260521 ToolTextEditor20250728AllowedCaller = "code\_execution\_20260521"



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

MaxCharacters int64Optional

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type WebSearchTool20250305 struct{…}



Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20250305



AllowedCallers []stringOptional

One of the following:

const WebSearchTool20250305AllowedCallerDirect WebSearchTool20250305AllowedCaller = "direct"

const WebSearchTool20250305AllowedCallerCodeExecution20250825 WebSearchTool20250305AllowedCaller = "code\_execution\_20250825"

const WebSearchTool20250305AllowedCallerCodeExecution20260120 WebSearchTool20250305AllowedCaller = "code\_execution\_20260120"

const WebSearchTool20250305AllowedCallerCodeExecution20260521 WebSearchTool20250305AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains []stringOptional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



UserLocation [UserLocation](api/messages.md)Optional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

City stringOptional

The city of the user.

Country stringOptional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Region stringOptional

The region of the user.

Timezone stringOptional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



type WebFetchTool20250910 struct{…}



Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20250910



AllowedCallers []stringOptional

One of the following:

const WebFetchTool20250910AllowedCallerDirect WebFetchTool20250910AllowedCaller = "direct"

const WebFetchTool20250910AllowedCallerCodeExecution20250825 WebFetchTool20250910AllowedCaller = "code\_execution\_20250825"

const WebFetchTool20250910AllowedCallerCodeExecution20260120 WebFetchTool20250910AllowedCaller = "code\_execution\_20260120"

const WebFetchTool20250910AllowedCallerCodeExecution20260521 WebFetchTool20250910AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

List of domains to allow fetching from

BlockedDomains []stringOptional

List of domains to block fetching from



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [CitationsConfigParamResp](api/messages.md)Optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled boolOptional

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxContentTokens int64Optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type WebSearchTool20260209 struct{…}



Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20260209



AllowedCallers []stringOptional

One of the following:

const WebSearchTool20260209AllowedCallerDirect WebSearchTool20260209AllowedCaller = "direct"

const WebSearchTool20260209AllowedCallerCodeExecution20250825 WebSearchTool20260209AllowedCaller = "code\_execution\_20250825"

const WebSearchTool20260209AllowedCallerCodeExecution20260120 WebSearchTool20260209AllowedCaller = "code\_execution\_20260120"

const WebSearchTool20260209AllowedCallerCodeExecution20260521 WebSearchTool20260209AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains []stringOptional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



UserLocation [UserLocation](api/messages.md)Optional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

City stringOptional

The city of the user.

Country stringOptional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Region stringOptional

The region of the user.

Timezone stringOptional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



type WebFetchTool20260209 struct{…}



Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20260209



AllowedCallers []stringOptional

One of the following:

const WebFetchTool20260209AllowedCallerDirect WebFetchTool20260209AllowedCaller = "direct"

const WebFetchTool20260209AllowedCallerCodeExecution20250825 WebFetchTool20260209AllowedCaller = "code\_execution\_20250825"

const WebFetchTool20260209AllowedCallerCodeExecution20260120 WebFetchTool20260209AllowedCaller = "code\_execution\_20260120"

const WebFetchTool20260209AllowedCallerCodeExecution20260521 WebFetchTool20260209AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

List of domains to allow fetching from

BlockedDomains []stringOptional

List of domains to block fetching from



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [CitationsConfigParamResp](api/messages.md)Optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled boolOptional

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxContentTokens int64Optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type WebFetchTool20260309 struct{…}

Web fetch tool with use\_cache parameter for bypassing cached content.



Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20260309



AllowedCallers []stringOptional

One of the following:

const WebFetchTool20260309AllowedCallerDirect WebFetchTool20260309AllowedCaller = "direct"

const WebFetchTool20260309AllowedCallerCodeExecution20250825 WebFetchTool20260309AllowedCaller = "code\_execution\_20250825"

const WebFetchTool20260309AllowedCallerCodeExecution20260120 WebFetchTool20260309AllowedCaller = "code\_execution\_20260120"

const WebFetchTool20260309AllowedCallerCodeExecution20260521 WebFetchTool20260309AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

List of domains to allow fetching from

BlockedDomains []stringOptional

List of domains to block fetching from



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [CitationsConfigParamResp](api/messages.md)Optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled boolOptional

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxContentTokens int64Optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

UseCache boolOptional

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



type WebSearchTool20260318 struct{…}



Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20260318



AllowedCallers []stringOptional

One of the following:

const WebSearchTool20260318AllowedCallerDirect WebSearchTool20260318AllowedCaller = "direct"

const WebSearchTool20260318AllowedCallerCodeExecution20250825 WebSearchTool20260318AllowedCaller = "code\_execution\_20250825"

const WebSearchTool20260318AllowedCallerCodeExecution20260120 WebSearchTool20260318AllowedCaller = "code\_execution\_20260120"

const WebSearchTool20260318AllowedCallerCodeExecution20260521 WebSearchTool20260318AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains []stringOptional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.



ResponseInclusion WebSearchTool20260318ResponseInclusionOptional

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

const WebSearchTool20260318ResponseInclusionFull WebSearchTool20260318ResponseInclusion = "full"

const WebSearchTool20260318ResponseInclusionExcluded WebSearchTool20260318ResponseInclusion = "excluded"

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



UserLocation [UserLocation](api/messages.md)Optional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

City stringOptional

The city of the user.

Country stringOptional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Region stringOptional

The region of the user.

Timezone stringOptional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



type WebFetchTool20260318 struct{…}



Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20260318



AllowedCallers []stringOptional

One of the following:

const WebFetchTool20260318AllowedCallerDirect WebFetchTool20260318AllowedCaller = "direct"

const WebFetchTool20260318AllowedCallerCodeExecution20250825 WebFetchTool20260318AllowedCaller = "code\_execution\_20250825"

const WebFetchTool20260318AllowedCallerCodeExecution20260120 WebFetchTool20260318AllowedCaller = "code\_execution\_20260120"

const WebFetchTool20260318AllowedCallerCodeExecution20260521 WebFetchTool20260318AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

List of domains to allow fetching from

BlockedDomains []stringOptional

List of domains to block fetching from



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"



Citations [CitationsConfigParamResp](api/messages.md)Optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled boolOptional

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxContentTokens int64Optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.



ResponseInclusion WebFetchTool20260318ResponseInclusionOptional

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

const WebFetchTool20260318ResponseInclusionFull WebFetchTool20260318ResponseInclusion = "full"

const WebFetchTool20260318ResponseInclusionExcluded WebFetchTool20260318ResponseInclusion = "excluded"

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

UseCache boolOptional

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



type ToolSearchToolBm25\_20251119 struct{…}



Name ToolSearchToolBm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



Type ToolSearchToolBm25\_20251119Type

One of the following:

const ToolSearchToolBm25\_20251119TypeToolSearchToolBm25\_20251119 ToolSearchToolBm25\_20251119Type = "tool\_search\_tool\_bm25\_20251119"

const ToolSearchToolBm25\_20251119TypeToolSearchToolBm25 ToolSearchToolBm25\_20251119Type = "tool\_search\_tool\_bm25"



AllowedCallers []stringOptional

One of the following:

const ToolSearchToolBm25\_20251119AllowedCallerDirect ToolSearchToolBm25\_20251119AllowedCaller = "direct"

const ToolSearchToolBm25\_20251119AllowedCallerCodeExecution20250825 ToolSearchToolBm25\_20251119AllowedCaller = "code\_execution\_20250825"

const ToolSearchToolBm25\_20251119AllowedCallerCodeExecution20260120 ToolSearchToolBm25\_20251119AllowedCaller = "code\_execution\_20260120"

const ToolSearchToolBm25\_20251119AllowedCallerCodeExecution20260521 ToolSearchToolBm25\_20251119AllowedCaller = "code\_execution\_20260521"



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type ToolSearchToolRegex20251119 struct{…}



Name ToolSearchToolRegex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



Type ToolSearchToolRegex20251119Type

One of the following:

const ToolSearchToolRegex20251119TypeToolSearchToolRegex20251119 ToolSearchToolRegex20251119Type = "tool\_search\_tool\_regex\_20251119"

const ToolSearchToolRegex20251119TypeToolSearchToolRegex ToolSearchToolRegex20251119Type = "tool\_search\_tool\_regex"



AllowedCallers []stringOptional

One of the following:

const ToolSearchToolRegex20251119AllowedCallerDirect ToolSearchToolRegex20251119AllowedCaller = "direct"

const ToolSearchToolRegex20251119AllowedCallerCodeExecution20250825 ToolSearchToolRegex20251119AllowedCaller = "code\_execution\_20250825"

const ToolSearchToolRegex20251119AllowedCallerCodeExecution20260120 ToolSearchToolRegex20251119AllowedCaller = "code\_execution\_20260120"

const ToolSearchToolRegex20251119AllowedCallerCodeExecution20260521 ToolSearchToolRegex20251119AllowedCaller = "code\_execution\_20260521"



CacheControl [CacheControlEphemeral](api/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL CacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



Temperature float64⁠DeprecatedOptional

Amount of randomness injected into the response.

Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0



TopK int64⁠DeprecatedOptional

Only sample from the top K options for each subsequent token.

Deprecated. Models released after Claude Opus 4.6 do not accept top\_k; any value will be rejected with a 400 error.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only.

minimum0



TopP float64⁠DeprecatedOptional

Use nucleus sampling.

Deprecated. Models released after Claude Opus 4.6 do not support setting top\_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

Recommended for advanced use cases only.

maximum1

minimum0

UserProfileID param.Field[string]Optional

Header param: The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

##### ReturnsExpand Collapse



type MessageBatch struct{…}



ID string

Unique object identifier.

The format and length of IDs may change over time.

ArchivedAt Time

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

CancelInitiatedAt Time

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

CreatedAt Time

RFC 3339 datetime string representing the time at which the Message Batch was created.



EndedAt Time

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

ExpiresAt Time

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.



ProcessingStatus MessageBatchProcessingStatus

Processing status of the Message Batch.

One of the following:

const MessageBatchProcessingStatusInProgress MessageBatchProcessingStatus = "in\_progress"

const MessageBatchProcessingStatusCanceling MessageBatchProcessingStatus = "canceling"

const MessageBatchProcessingStatusEnded MessageBatchProcessingStatus = "ended"



RequestCounts [MessageBatchRequestCounts](api/messages/batches.md)

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.



Canceled int64

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



Errored int64

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



Expired int64

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

Processing int64

Number of requests in the Message Batch that are processing.



Succeeded int64

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



ResultsURL string

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.



Type MessageBatch

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
  messageBatch, err := client.Messages.Batches.New(context.TODO(), anthropic.MessageBatchNewParams{
    Requests: []anthropic.MessageBatchNewParamsRequest{anthropic.MessageBatchNewParamsRequest{
      CustomID: "my-custom-id-1",
      Params: anthropic.MessageBatchNewParamsRequestParams{
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
      },
    }},
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", messageBatch.ID)
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
