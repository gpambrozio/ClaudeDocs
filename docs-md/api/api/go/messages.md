# Messages

Copy page



Go

# Messages

##### [Create a Message](api/messages/create.md)

client.Messages.New(ctx, params) (\*[Message](api/messages.md), error)

POST/v1/messages

##### [Count tokens in a Message](api/messages/count_tokens.md)

client.Messages.CountTokens(ctx, params) (\*[MessageTokensCount](api/messages.md), error)

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse

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

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BashCodeExecutionOutputBlock struct{…}

FileID string

Type BashCodeExecutionOutput



type BashCodeExecutionOutputBlockParamResp struct{…}

FileID string

Type BashCodeExecutionOutput



type BashCodeExecutionResultBlock struct{…}



Content [][BashCodeExecutionOutputBlock](api/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

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



type BashCodeExecutionToolResultBlock struct{…}



Content BashCodeExecutionToolResultBlockContentUnion

One of the following:



type BashCodeExecutionToolResultError struct{…}

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

type BashCodeExecutionResultBlock struct{…}



Content [][BashCodeExecutionOutputBlock](api/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

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

type BashCodeExecutionToolResultError struct{…}

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

type BashCodeExecutionToolResultErrorCode string

One of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](api/messages.md) = "output\_file\_too\_large"

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

type CacheControlEphemeral struct{…}

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

type CacheCreation struct{…}

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.



type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type CitationContentBlockLocation struct{…}

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

FileID string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation

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

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

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

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationsConfig struct{…}

Enabled bool



type CitationsConfigParamResp struct{…}

Enabled boolOptional



type CitationsDelta struct{…}



Citation CitationsDeltaCitationUnion

One of the following:



type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocation struct{…}

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

FileID string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationsSearchResultLocation struct{…}

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

Type CitationsDelta



type CitationsSearchResultLocation struct{…}

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

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CodeExecutionOutputBlock struct{…}

FileID string

Type CodeExecutionOutput



type CodeExecutionOutputBlockParamResp struct{…}

FileID string

Type CodeExecutionOutput



type CodeExecutionResultBlock struct{…}



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

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

type CodeExecutionToolResultBlock struct{…}



Content [CodeExecutionToolResultBlockContentUnion](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type CodeExecutionToolResultError struct{…}



ErrorCode [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type CodeExecutionResultBlock struct{…}



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



type CodeExecutionToolResultBlockContentUnion interface{…}

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type CodeExecutionToolResultError struct{…}



ErrorCode [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type CodeExecutionResultBlock struct{…}



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

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

type CodeExecutionToolResultBlockParamContentUnionResp interface{…}

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



type CodeExecutionToolResultError struct{…}



ErrorCode [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type CodeExecutionToolResultErrorCode string

One of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

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

type Container struct{…}

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

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

type ContentBlockUnion interface{…}

Response model for a file uploaded to the container.

One of the following:



type TextBlock struct{…}



Citations [][TextCitationUnion](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocation struct{…}

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

FileID string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationsSearchResultLocation struct{…}

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

Text string

Type Text



type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking



type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking



type ToolUseBlock struct{…}

ID string



Caller ToolUseBlockCallerUnion

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

Input map[string, any]

Name string

Type ToolUse



type ServerToolUseBlock struct{…}

ID string



Caller ServerToolUseBlockCallerUnion

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

Input map[string, any]



Name ServerToolUseBlockName

One of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web\_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web\_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code\_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash\_code\_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text\_editor\_code\_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool\_search\_tool\_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse



type WebSearchToolResultBlock struct{…}



Caller WebSearchToolResultBlockCallerUnion

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

Content [WebSearchToolResultBlockContentUnion](api/messages.md)

One of the following:



type WebSearchToolResultError struct{…}

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



type WebSearchToolResultBlockContentArray [][WebSearchResultBlock](api/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult



type WebFetchToolResultBlock struct{…}



Caller WebFetchToolResultBlockCallerUnion

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

Content WebFetchToolResultBlockContentUnion

One of the following:



type WebFetchToolResultErrorBlock struct{…}

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

type WebFetchBlock struct{…}



Content [DocumentBlock](api/messages.md)



Citations [CitationsConfig](api/messages.md)

Citation configuration for the document

Enabled bool



Source DocumentBlockSourceUnion

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

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult



type CodeExecutionToolResultBlock struct{…}



Content [CodeExecutionToolResultBlockContentUnion](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type CodeExecutionToolResultError struct{…}



ErrorCode [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type CodeExecutionResultBlock struct{…}



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



type BashCodeExecutionToolResultBlock struct{…}



Content BashCodeExecutionToolResultBlockContentUnion

One of the following:



type BashCodeExecutionToolResultError struct{…}

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

type BashCodeExecutionResultBlock struct{…}



Content [][BashCodeExecutionOutputBlock](api/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



type TextEditorCodeExecutionToolResultBlock struct{…}



Content TextEditorCodeExecutionToolResultBlockContentUnion

One of the following:



type TextEditorCodeExecutionToolResultError struct{…}



ErrorCode [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type TextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType TextEditorCodeExecutionViewResultBlockFileType

One of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult



type ToolSearchToolResultBlock struct{…}



Content ToolSearchToolResultBlockContentUnion

One of the following:



type ToolSearchToolResultError struct{…}



ErrorCode [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](api/messages.md) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type ToolSearchToolSearchResultBlock struct{…}



ToolReferences [][ToolReferenceBlock](api/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload



type ContentBlockParamUnionResp interface{…}

Regular text content.

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

type ContentBlockSourceContentItemUnion interface{…}

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

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type DocumentBlock struct{…}



Citations [CitationsConfig](api/messages.md)

Citation configuration for the document

Enabled bool



Source DocumentBlockSourceUnion

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

Title string

The title of the document

Type Document

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

type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

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

type InputJSONDelta struct{…}

PartialJSON string

Type InputJSONDelta



type JSONOutputFormat struct{…}

Schema map[string, any]

The JSON schema of the format

Type JSONSchema

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

type Message struct{…}



ID string

Unique object identifier.

The format and length of IDs may change over time.



Container [Container](api/messages.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



Content [][ContentBlockUnion](api/messages.md)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```



If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```



Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```



One of the following:



type TextBlock struct{…}



Citations [][TextCitationUnion](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocation struct{…}

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

FileID string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationsSearchResultLocation struct{…}

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

Text string

Type Text



type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking



type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking



type ToolUseBlock struct{…}

ID string



Caller ToolUseBlockCallerUnion

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

Input map[string, any]

Name string

Type ToolUse



type ServerToolUseBlock struct{…}

ID string



Caller ServerToolUseBlockCallerUnion

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

Input map[string, any]



Name ServerToolUseBlockName

One of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web\_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web\_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code\_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash\_code\_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text\_editor\_code\_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool\_search\_tool\_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse



type WebSearchToolResultBlock struct{…}



Caller WebSearchToolResultBlockCallerUnion

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

Content [WebSearchToolResultBlockContentUnion](api/messages.md)

One of the following:



type WebSearchToolResultError struct{…}

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



type WebSearchToolResultBlockContentArray [][WebSearchResultBlock](api/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult



type WebFetchToolResultBlock struct{…}



Caller WebFetchToolResultBlockCallerUnion

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

Content WebFetchToolResultBlockContentUnion

One of the following:



type WebFetchToolResultErrorBlock struct{…}

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

type WebFetchBlock struct{…}



Content [DocumentBlock](api/messages.md)



Citations [CitationsConfig](api/messages.md)

Citation configuration for the document

Enabled bool



Source DocumentBlockSourceUnion

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

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult



type CodeExecutionToolResultBlock struct{…}



Content [CodeExecutionToolResultBlockContentUnion](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type CodeExecutionToolResultError struct{…}



ErrorCode [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type CodeExecutionResultBlock struct{…}



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



type BashCodeExecutionToolResultBlock struct{…}



Content BashCodeExecutionToolResultBlockContentUnion

One of the following:



type BashCodeExecutionToolResultError struct{…}

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

type BashCodeExecutionResultBlock struct{…}



Content [][BashCodeExecutionOutputBlock](api/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



type TextEditorCodeExecutionToolResultBlock struct{…}



Content TextEditorCodeExecutionToolResultBlockContentUnion

One of the following:



type TextEditorCodeExecutionToolResultError struct{…}



ErrorCode [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type TextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType TextEditorCodeExecutionViewResultBlockFileType

One of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult



type ToolSearchToolResultBlock struct{…}



Content ToolSearchToolResultBlockContentUnion

One of the following:



type ToolSearchToolResultError struct{…}



ErrorCode [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](api/messages.md) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type ToolSearchToolSearchResultBlock struct{…}



ToolReferences [][ToolReferenceBlock](api/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

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

Role Assistant

Conversational role of the generated message.

This will always be `"assistant"`.



StopDetails [RefusalStopDetails](api/messages.md)

Structured information about a refusal.



Category RefusalStopDetailsCategory

The policy category that triggered a refusal.

One of the following:

const RefusalStopDetailsCategoryCyber RefusalStopDetailsCategory = "cyber"

const RefusalStopDetailsCategoryBio RefusalStopDetailsCategory = "bio"

const RefusalStopDetailsCategoryFrontierLLM RefusalStopDetailsCategory = "frontier\_llm"

const RefusalStopDetailsCategoryReasoningExtraction RefusalStopDetailsCategory = "reasoning\_extraction"

const RefusalStopDetailsCategoryMilitaryWeapons RefusalStopDetailsCategory = "military\_weapons"



Explanation string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

Type Refusal



StopReason [StopReason](api/messages.md)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

const StopReasonEndTurn [StopReason](api/messages.md) = "end\_turn"

const StopReasonMaxTokens [StopReason](api/messages.md) = "max\_tokens"

const StopReasonStopSequence [StopReason](api/messages.md) = "stop\_sequence"

const StopReasonToolUse [StopReason](api/messages.md) = "tool\_use"

const StopReasonPauseTurn [StopReason](api/messages.md) = "pause\_turn"

const StopReasonRefusal [StopReason](api/messages.md) = "refusal"



StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



Type Message

Object type.

For Messages, this is always `"message"`.



Usage [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



CacheCreation [CacheCreation](api/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.



OutputTokensDetails [OutputTokensDetails](api/messages.md)

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



ThinkingTokens int64

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



ServerToolUse [ServerToolUsage](api/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

One of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"



type MessageCountTokensToolUnion interface{…}

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

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

type MessageDeltaUsage struct{…}

CacheCreationInputTokens int64

The cumulative number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The cumulative number of input tokens read from the cache.

InputTokens int64

The cumulative number of input tokens which were used.

OutputTokens int64

The cumulative number of output tokens which were used.



OutputTokensDetails [OutputTokensDetails](api/messages.md)

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



ThinkingTokens int64

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



ServerToolUse [ServerToolUsage](api/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



type MessageParamResp struct{…}

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

type MessageTokensCount struct{…}

InputTokens int64

The total number of tokens across the provided list of messages, system prompt, and tools.



type Metadata struct{…}



UserID stringOptional

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512

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

type Model interface{…}

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

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

type OutputConfig struct{…}

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

type OutputTokensDetails struct{…}



ThinkingTokens int64

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text



type RawContentBlockDeltaUnion interface{…}

One of the following:



type TextDelta struct{…}

Text string

Type TextDelta



type InputJSONDelta struct{…}

PartialJSON string

Type InputJSONDelta



type CitationsDelta struct{…}



Citation CitationsDeltaCitationUnion

One of the following:



type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocation struct{…}

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

FileID string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationsSearchResultLocation struct{…}

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

Type CitationsDelta



type ThinkingDelta struct{…}

Thinking string

Type ThinkingDelta



type SignatureDelta struct{…}

Signature string

Type SignatureDelta



type ContentBlockDeltaEvent struct{…}



Delta [RawContentBlockDeltaUnion](api/messages.md)

One of the following:



type TextDelta struct{…}

Text string

Type TextDelta



type InputJSONDelta struct{…}

PartialJSON string

Type InputJSONDelta



type CitationsDelta struct{…}



Citation CitationsDeltaCitationUnion

One of the following:



type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocation struct{…}

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

FileID string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationsSearchResultLocation struct{…}

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

Type CitationsDelta



type ThinkingDelta struct{…}

Thinking string

Type ThinkingDelta



type SignatureDelta struct{…}

Signature string

Type SignatureDelta

Index int64

Type ContentBlockDelta



type ContentBlockStartEvent struct{…}



ContentBlock ContentBlockStartEventContentBlockUnion

Response model for a file uploaded to the container.

One of the following:



type TextBlock struct{…}



Citations [][TextCitationUnion](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocation struct{…}

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

FileID string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationsSearchResultLocation struct{…}

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

Text string

Type Text



type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking



type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking



type ToolUseBlock struct{…}

ID string



Caller ToolUseBlockCallerUnion

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

Input map[string, any]

Name string

Type ToolUse



type ServerToolUseBlock struct{…}

ID string



Caller ServerToolUseBlockCallerUnion

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

Input map[string, any]



Name ServerToolUseBlockName

One of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web\_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web\_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code\_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash\_code\_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text\_editor\_code\_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool\_search\_tool\_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse



type WebSearchToolResultBlock struct{…}



Caller WebSearchToolResultBlockCallerUnion

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

Content [WebSearchToolResultBlockContentUnion](api/messages.md)

One of the following:



type WebSearchToolResultError struct{…}

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



type WebSearchToolResultBlockContentArray [][WebSearchResultBlock](api/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult



type WebFetchToolResultBlock struct{…}



Caller WebFetchToolResultBlockCallerUnion

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

Content WebFetchToolResultBlockContentUnion

One of the following:



type WebFetchToolResultErrorBlock struct{…}

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

type WebFetchBlock struct{…}



Content [DocumentBlock](api/messages.md)



Citations [CitationsConfig](api/messages.md)

Citation configuration for the document

Enabled bool



Source DocumentBlockSourceUnion

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

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult



type CodeExecutionToolResultBlock struct{…}



Content [CodeExecutionToolResultBlockContentUnion](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type CodeExecutionToolResultError struct{…}



ErrorCode [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type CodeExecutionResultBlock struct{…}



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



type BashCodeExecutionToolResultBlock struct{…}



Content BashCodeExecutionToolResultBlockContentUnion

One of the following:



type BashCodeExecutionToolResultError struct{…}

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

type BashCodeExecutionResultBlock struct{…}



Content [][BashCodeExecutionOutputBlock](api/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



type TextEditorCodeExecutionToolResultBlock struct{…}



Content TextEditorCodeExecutionToolResultBlockContentUnion

One of the following:



type TextEditorCodeExecutionToolResultError struct{…}



ErrorCode [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type TextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType TextEditorCodeExecutionViewResultBlockFileType

One of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult



type ToolSearchToolResultBlock struct{…}



Content ToolSearchToolResultBlockContentUnion

One of the following:



type ToolSearchToolResultError struct{…}



ErrorCode [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](api/messages.md) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type ToolSearchToolSearchResultBlock struct{…}



ToolReferences [][ToolReferenceBlock](api/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

Index int64

Type ContentBlockStart



type ContentBlockStopEvent struct{…}

Index int64

Type ContentBlockStop



type MessageDeltaEvent struct{…}



Delta MessageDeltaEventDelta



Container [Container](api/messages.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



StopDetails [RefusalStopDetails](api/messages.md)

Structured information about a refusal.



Category RefusalStopDetailsCategory

The policy category that triggered a refusal.

One of the following:

const RefusalStopDetailsCategoryCyber RefusalStopDetailsCategory = "cyber"

const RefusalStopDetailsCategoryBio RefusalStopDetailsCategory = "bio"

const RefusalStopDetailsCategoryFrontierLLM RefusalStopDetailsCategory = "frontier\_llm"

const RefusalStopDetailsCategoryReasoningExtraction RefusalStopDetailsCategory = "reasoning\_extraction"

const RefusalStopDetailsCategoryMilitaryWeapons RefusalStopDetailsCategory = "military\_weapons"



Explanation string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

Type Refusal



StopReason [StopReason](api/messages.md)

One of the following:

const StopReasonEndTurn [StopReason](api/messages.md) = "end\_turn"

const StopReasonMaxTokens [StopReason](api/messages.md) = "max\_tokens"

const StopReasonStopSequence [StopReason](api/messages.md) = "stop\_sequence"

const StopReasonToolUse [StopReason](api/messages.md) = "tool\_use"

const StopReasonPauseTurn [StopReason](api/messages.md) = "pause\_turn"

const StopReasonRefusal [StopReason](api/messages.md) = "refusal"

StopSequence string

Type MessageDelta



Usage [MessageDeltaUsage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreationInputTokens int64

The cumulative number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The cumulative number of input tokens read from the cache.

InputTokens int64

The cumulative number of input tokens which were used.

OutputTokens int64

The cumulative number of output tokens which were used.



OutputTokensDetails [OutputTokensDetails](api/messages.md)

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



ThinkingTokens int64

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



ServerToolUse [ServerToolUsage](api/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



type MessageStartEvent struct{…}



Message [Message](api/messages.md)



ID string

Unique object identifier.

The format and length of IDs may change over time.



Container [Container](api/messages.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



Content [][ContentBlockUnion](api/messages.md)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```



If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```



Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```



One of the following:



type TextBlock struct{…}



Citations [][TextCitationUnion](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocation struct{…}

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

FileID string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationsSearchResultLocation struct{…}

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

Text string

Type Text



type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking



type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking



type ToolUseBlock struct{…}

ID string



Caller ToolUseBlockCallerUnion

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

Input map[string, any]

Name string

Type ToolUse



type ServerToolUseBlock struct{…}

ID string



Caller ServerToolUseBlockCallerUnion

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

Input map[string, any]



Name ServerToolUseBlockName

One of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web\_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web\_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code\_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash\_code\_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text\_editor\_code\_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool\_search\_tool\_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse



type WebSearchToolResultBlock struct{…}



Caller WebSearchToolResultBlockCallerUnion

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

Content [WebSearchToolResultBlockContentUnion](api/messages.md)

One of the following:



type WebSearchToolResultError struct{…}

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



type WebSearchToolResultBlockContentArray [][WebSearchResultBlock](api/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult



type WebFetchToolResultBlock struct{…}



Caller WebFetchToolResultBlockCallerUnion

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

Content WebFetchToolResultBlockContentUnion

One of the following:



type WebFetchToolResultErrorBlock struct{…}

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

type WebFetchBlock struct{…}



Content [DocumentBlock](api/messages.md)



Citations [CitationsConfig](api/messages.md)

Citation configuration for the document

Enabled bool



Source DocumentBlockSourceUnion

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

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult



type CodeExecutionToolResultBlock struct{…}



Content [CodeExecutionToolResultBlockContentUnion](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type CodeExecutionToolResultError struct{…}



ErrorCode [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type CodeExecutionResultBlock struct{…}



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



type BashCodeExecutionToolResultBlock struct{…}



Content BashCodeExecutionToolResultBlockContentUnion

One of the following:



type BashCodeExecutionToolResultError struct{…}

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

type BashCodeExecutionResultBlock struct{…}



Content [][BashCodeExecutionOutputBlock](api/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



type TextEditorCodeExecutionToolResultBlock struct{…}



Content TextEditorCodeExecutionToolResultBlockContentUnion

One of the following:



type TextEditorCodeExecutionToolResultError struct{…}



ErrorCode [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type TextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType TextEditorCodeExecutionViewResultBlockFileType

One of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult



type ToolSearchToolResultBlock struct{…}



Content ToolSearchToolResultBlockContentUnion

One of the following:



type ToolSearchToolResultError struct{…}



ErrorCode [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](api/messages.md) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type ToolSearchToolSearchResultBlock struct{…}



ToolReferences [][ToolReferenceBlock](api/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

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

Role Assistant

Conversational role of the generated message.

This will always be `"assistant"`.



StopDetails [RefusalStopDetails](api/messages.md)

Structured information about a refusal.



Category RefusalStopDetailsCategory

The policy category that triggered a refusal.

One of the following:

const RefusalStopDetailsCategoryCyber RefusalStopDetailsCategory = "cyber"

const RefusalStopDetailsCategoryBio RefusalStopDetailsCategory = "bio"

const RefusalStopDetailsCategoryFrontierLLM RefusalStopDetailsCategory = "frontier\_llm"

const RefusalStopDetailsCategoryReasoningExtraction RefusalStopDetailsCategory = "reasoning\_extraction"

const RefusalStopDetailsCategoryMilitaryWeapons RefusalStopDetailsCategory = "military\_weapons"



Explanation string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

Type Refusal



StopReason [StopReason](api/messages.md)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

const StopReasonEndTurn [StopReason](api/messages.md) = "end\_turn"

const StopReasonMaxTokens [StopReason](api/messages.md) = "max\_tokens"

const StopReasonStopSequence [StopReason](api/messages.md) = "stop\_sequence"

const StopReasonToolUse [StopReason](api/messages.md) = "tool\_use"

const StopReasonPauseTurn [StopReason](api/messages.md) = "pause\_turn"

const StopReasonRefusal [StopReason](api/messages.md) = "refusal"



StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



Type Message

Object type.

For Messages, this is always `"message"`.



Usage [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



CacheCreation [CacheCreation](api/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.



OutputTokensDetails [OutputTokensDetails](api/messages.md)

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



ThinkingTokens int64

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



ServerToolUse [ServerToolUsage](api/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

One of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type MessageStart



type MessageStopEvent struct{…}

Type MessageStop



type MessageStreamEventUnion interface{…}

One of the following:



type MessageStartEvent struct{…}



Message [Message](api/messages.md)



ID string

Unique object identifier.

The format and length of IDs may change over time.



Container [Container](api/messages.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



Content [][ContentBlockUnion](api/messages.md)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```



If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```



Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```



One of the following:



type TextBlock struct{…}



Citations [][TextCitationUnion](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocation struct{…}

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

FileID string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationsSearchResultLocation struct{…}

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

Text string

Type Text



type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking



type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking



type ToolUseBlock struct{…}

ID string



Caller ToolUseBlockCallerUnion

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

Input map[string, any]

Name string

Type ToolUse



type ServerToolUseBlock struct{…}

ID string



Caller ServerToolUseBlockCallerUnion

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

Input map[string, any]



Name ServerToolUseBlockName

One of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web\_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web\_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code\_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash\_code\_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text\_editor\_code\_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool\_search\_tool\_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse



type WebSearchToolResultBlock struct{…}



Caller WebSearchToolResultBlockCallerUnion

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

Content [WebSearchToolResultBlockContentUnion](api/messages.md)

One of the following:



type WebSearchToolResultError struct{…}

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



type WebSearchToolResultBlockContentArray [][WebSearchResultBlock](api/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult



type WebFetchToolResultBlock struct{…}



Caller WebFetchToolResultBlockCallerUnion

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

Content WebFetchToolResultBlockContentUnion

One of the following:



type WebFetchToolResultErrorBlock struct{…}

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

type WebFetchBlock struct{…}



Content [DocumentBlock](api/messages.md)



Citations [CitationsConfig](api/messages.md)

Citation configuration for the document

Enabled bool



Source DocumentBlockSourceUnion

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

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult



type CodeExecutionToolResultBlock struct{…}



Content [CodeExecutionToolResultBlockContentUnion](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type CodeExecutionToolResultError struct{…}



ErrorCode [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type CodeExecutionResultBlock struct{…}



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



type BashCodeExecutionToolResultBlock struct{…}



Content BashCodeExecutionToolResultBlockContentUnion

One of the following:



type BashCodeExecutionToolResultError struct{…}

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

type BashCodeExecutionResultBlock struct{…}



Content [][BashCodeExecutionOutputBlock](api/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



type TextEditorCodeExecutionToolResultBlock struct{…}



Content TextEditorCodeExecutionToolResultBlockContentUnion

One of the following:



type TextEditorCodeExecutionToolResultError struct{…}



ErrorCode [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type TextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType TextEditorCodeExecutionViewResultBlockFileType

One of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult



type ToolSearchToolResultBlock struct{…}



Content ToolSearchToolResultBlockContentUnion

One of the following:



type ToolSearchToolResultError struct{…}



ErrorCode [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](api/messages.md) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type ToolSearchToolSearchResultBlock struct{…}



ToolReferences [][ToolReferenceBlock](api/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

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

Role Assistant

Conversational role of the generated message.

This will always be `"assistant"`.



StopDetails [RefusalStopDetails](api/messages.md)

Structured information about a refusal.



Category RefusalStopDetailsCategory

The policy category that triggered a refusal.

One of the following:

const RefusalStopDetailsCategoryCyber RefusalStopDetailsCategory = "cyber"

const RefusalStopDetailsCategoryBio RefusalStopDetailsCategory = "bio"

const RefusalStopDetailsCategoryFrontierLLM RefusalStopDetailsCategory = "frontier\_llm"

const RefusalStopDetailsCategoryReasoningExtraction RefusalStopDetailsCategory = "reasoning\_extraction"

const RefusalStopDetailsCategoryMilitaryWeapons RefusalStopDetailsCategory = "military\_weapons"



Explanation string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

Type Refusal



StopReason [StopReason](api/messages.md)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

const StopReasonEndTurn [StopReason](api/messages.md) = "end\_turn"

const StopReasonMaxTokens [StopReason](api/messages.md) = "max\_tokens"

const StopReasonStopSequence [StopReason](api/messages.md) = "stop\_sequence"

const StopReasonToolUse [StopReason](api/messages.md) = "tool\_use"

const StopReasonPauseTurn [StopReason](api/messages.md) = "pause\_turn"

const StopReasonRefusal [StopReason](api/messages.md) = "refusal"



StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



Type Message

Object type.

For Messages, this is always `"message"`.



Usage [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



CacheCreation [CacheCreation](api/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.



OutputTokensDetails [OutputTokensDetails](api/messages.md)

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



ThinkingTokens int64

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



ServerToolUse [ServerToolUsage](api/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

One of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type MessageStart



type MessageDeltaEvent struct{…}



Delta MessageDeltaEventDelta



Container [Container](api/messages.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



StopDetails [RefusalStopDetails](api/messages.md)

Structured information about a refusal.



Category RefusalStopDetailsCategory

The policy category that triggered a refusal.

One of the following:

const RefusalStopDetailsCategoryCyber RefusalStopDetailsCategory = "cyber"

const RefusalStopDetailsCategoryBio RefusalStopDetailsCategory = "bio"

const RefusalStopDetailsCategoryFrontierLLM RefusalStopDetailsCategory = "frontier\_llm"

const RefusalStopDetailsCategoryReasoningExtraction RefusalStopDetailsCategory = "reasoning\_extraction"

const RefusalStopDetailsCategoryMilitaryWeapons RefusalStopDetailsCategory = "military\_weapons"



Explanation string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

Type Refusal



StopReason [StopReason](api/messages.md)

One of the following:

const StopReasonEndTurn [StopReason](api/messages.md) = "end\_turn"

const StopReasonMaxTokens [StopReason](api/messages.md) = "max\_tokens"

const StopReasonStopSequence [StopReason](api/messages.md) = "stop\_sequence"

const StopReasonToolUse [StopReason](api/messages.md) = "tool\_use"

const StopReasonPauseTurn [StopReason](api/messages.md) = "pause\_turn"

const StopReasonRefusal [StopReason](api/messages.md) = "refusal"

StopSequence string

Type MessageDelta



Usage [MessageDeltaUsage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreationInputTokens int64

The cumulative number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The cumulative number of input tokens read from the cache.

InputTokens int64

The cumulative number of input tokens which were used.

OutputTokens int64

The cumulative number of output tokens which were used.



OutputTokensDetails [OutputTokensDetails](api/messages.md)

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



ThinkingTokens int64

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



ServerToolUse [ServerToolUsage](api/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



type MessageStopEvent struct{…}

Type MessageStop



type ContentBlockStartEvent struct{…}



ContentBlock ContentBlockStartEventContentBlockUnion

Response model for a file uploaded to the container.

One of the following:



type TextBlock struct{…}



Citations [][TextCitationUnion](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocation struct{…}

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

FileID string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationsSearchResultLocation struct{…}

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

Text string

Type Text



type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking



type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking



type ToolUseBlock struct{…}

ID string



Caller ToolUseBlockCallerUnion

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

Input map[string, any]

Name string

Type ToolUse



type ServerToolUseBlock struct{…}

ID string



Caller ServerToolUseBlockCallerUnion

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

Input map[string, any]



Name ServerToolUseBlockName

One of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web\_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web\_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code\_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash\_code\_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text\_editor\_code\_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool\_search\_tool\_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse



type WebSearchToolResultBlock struct{…}



Caller WebSearchToolResultBlockCallerUnion

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

Content [WebSearchToolResultBlockContentUnion](api/messages.md)

One of the following:



type WebSearchToolResultError struct{…}

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



type WebSearchToolResultBlockContentArray [][WebSearchResultBlock](api/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult



type WebFetchToolResultBlock struct{…}



Caller WebFetchToolResultBlockCallerUnion

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

Content WebFetchToolResultBlockContentUnion

One of the following:



type WebFetchToolResultErrorBlock struct{…}

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

type WebFetchBlock struct{…}



Content [DocumentBlock](api/messages.md)



Citations [CitationsConfig](api/messages.md)

Citation configuration for the document

Enabled bool



Source DocumentBlockSourceUnion

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

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult



type CodeExecutionToolResultBlock struct{…}



Content [CodeExecutionToolResultBlockContentUnion](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type CodeExecutionToolResultError struct{…}



ErrorCode [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type CodeExecutionResultBlock struct{…}



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



type BashCodeExecutionToolResultBlock struct{…}



Content BashCodeExecutionToolResultBlockContentUnion

One of the following:



type BashCodeExecutionToolResultError struct{…}

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

type BashCodeExecutionResultBlock struct{…}



Content [][BashCodeExecutionOutputBlock](api/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



type TextEditorCodeExecutionToolResultBlock struct{…}



Content TextEditorCodeExecutionToolResultBlockContentUnion

One of the following:



type TextEditorCodeExecutionToolResultError struct{…}



ErrorCode [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type TextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType TextEditorCodeExecutionViewResultBlockFileType

One of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult



type ToolSearchToolResultBlock struct{…}



Content ToolSearchToolResultBlockContentUnion

One of the following:



type ToolSearchToolResultError struct{…}



ErrorCode [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](api/messages.md) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type ToolSearchToolSearchResultBlock struct{…}



ToolReferences [][ToolReferenceBlock](api/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

Index int64

Type ContentBlockStart



type ContentBlockDeltaEvent struct{…}



Delta [RawContentBlockDeltaUnion](api/messages.md)

One of the following:



type TextDelta struct{…}

Text string

Type TextDelta



type InputJSONDelta struct{…}

PartialJSON string

Type InputJSONDelta



type CitationsDelta struct{…}



Citation CitationsDeltaCitationUnion

One of the following:



type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocation struct{…}

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

FileID string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationsSearchResultLocation struct{…}

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

Type CitationsDelta



type ThinkingDelta struct{…}

Thinking string

Type ThinkingDelta



type SignatureDelta struct{…}

Signature string

Type SignatureDelta

Index int64

Type ContentBlockDelta



type ContentBlockStopEvent struct{…}

Index int64

Type ContentBlockStop



type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking



type RedactedThinkingBlockParamResp struct{…}

Data string

Type RedactedThinking



type RefusalStopDetails struct{…}

Structured information about a refusal.



Category RefusalStopDetailsCategory

The policy category that triggered a refusal.

One of the following:

const RefusalStopDetailsCategoryCyber RefusalStopDetailsCategory = "cyber"

const RefusalStopDetailsCategoryBio RefusalStopDetailsCategory = "bio"

const RefusalStopDetailsCategoryFrontierLLM RefusalStopDetailsCategory = "frontier\_llm"

const RefusalStopDetailsCategoryReasoningExtraction RefusalStopDetailsCategory = "reasoning\_extraction"

const RefusalStopDetailsCategoryMilitaryWeapons RefusalStopDetailsCategory = "military\_weapons"



Explanation string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

Type Refusal

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

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type ServerToolUsage struct{…}

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



type ServerToolUseBlock struct{…}

ID string



Caller ServerToolUseBlockCallerUnion

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

Input map[string, any]



Name ServerToolUseBlockName

One of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web\_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web\_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code\_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash\_code\_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text\_editor\_code\_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool\_search\_tool\_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse

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

type SignatureDelta struct{…}

Signature string

Type SignatureDelta



type StopReason string

One of the following:

const StopReasonEndTurn [StopReason](api/messages.md) = "end\_turn"

const StopReasonMaxTokens [StopReason](api/messages.md) = "max\_tokens"

const StopReasonStopSequence [StopReason](api/messages.md) = "stop\_sequence"

const StopReasonToolUse [StopReason](api/messages.md) = "tool\_use"

const StopReasonPauseTurn [StopReason](api/messages.md) = "pause\_turn"

const StopReasonRefusal [StopReason](api/messages.md) = "refusal"



type TextBlock struct{…}



Citations [][TextCitationUnion](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocation struct{…}

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

FileID string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationsSearchResultLocation struct{…}

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

Text string

Type Text

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

type TextCitationUnion interface{…}

One of the following:



type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocation struct{…}

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

FileID string

StartBlockIndex int64

0-based index of the first cited block in the source's `content` array.

Type ContentBlockLocation



type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationsSearchResultLocation struct{…}

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

type TextCitationParamUnionResp interface{…}

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

type TextDelta struct{…}

Text string

Type TextDelta



type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type TextEditorCodeExecutionCreateResultBlockParamResp struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult



type TextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}

Type TextEditorCodeExecutionStrReplaceResult

Lines []stringOptional

NewLines int64Optional

NewStart int64Optional

OldLines int64Optional

OldStart int64Optional



type TextEditorCodeExecutionToolResultBlock struct{…}



Content TextEditorCodeExecutionToolResultBlockContentUnion

One of the following:



type TextEditorCodeExecutionToolResultError struct{…}



ErrorCode [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type TextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType TextEditorCodeExecutionViewResultBlockFileType

One of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult

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

type TextEditorCodeExecutionToolResultError struct{…}



ErrorCode [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type TextEditorCodeExecutionToolResultErrorCode string

One of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "file\_not\_found"

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

type TextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType TextEditorCodeExecutionViewResultBlockFileType

One of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

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

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking



type ThinkingBlockParamResp struct{…}

Signature string

Thinking string

Type Thinking

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

type ThinkingConfigDisabled struct{…}

Type Disabled

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

type ThinkingConfigParamUnionResp interface{…}

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

type ThinkingDelta struct{…}

Thinking string

Type ThinkingDelta

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

type ToolChoiceUnion interface{…}

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

type ToolChoiceAny struct{…}

The model will use any available tools.

Type Any



DisableParallelToolUse boolOptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



type ToolChoiceAuto struct{…}

The model will automatically decide whether to use tools.

Type Auto



DisableParallelToolUse boolOptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



type ToolChoiceNone struct{…}

The model will not be allowed to use tools.

Type None

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

type ToolReferenceBlock struct{…}

ToolName string

Type ToolReference

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

type ToolSearchToolResultBlock struct{…}



Content ToolSearchToolResultBlockContentUnion

One of the following:



type ToolSearchToolResultError struct{…}



ErrorCode [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](api/messages.md) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type ToolSearchToolSearchResultBlock struct{…}



ToolReferences [][ToolReferenceBlock](api/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

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

type ToolSearchToolResultError struct{…}



ErrorCode [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](api/messages.md) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type ToolSearchToolResultErrorCode string

One of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](api/messages.md) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

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

type ToolSearchToolSearchResultBlock struct{…}



ToolReferences [][ToolReferenceBlock](api/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

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

type ToolUnion interface{…}

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

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

type ToolUseBlock struct{…}

ID string



Caller ToolUseBlockCallerUnion

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

Input map[string, any]

Name string

Type ToolUse

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

type URLImageSource struct{…}

Type URL

URL string



type URLPDFSource struct{…}

Type URL

URL string



type Usage struct{…}



CacheCreation [CacheCreation](api/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.



OutputTokensDetails [OutputTokensDetails](api/messages.md)

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



ThinkingTokens int64

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



ServerToolUse [ServerToolUsage](api/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

One of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"



type UserLocation struct{…}

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

type WebFetchBlock struct{…}



Content [DocumentBlock](api/messages.md)



Citations [CitationsConfig](api/messages.md)

Citation configuration for the document

Enabled bool



Source DocumentBlockSourceUnion

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

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

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

type WebFetchToolResultBlock struct{…}



Caller WebFetchToolResultBlockCallerUnion

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

Content WebFetchToolResultBlockContentUnion

One of the following:



type WebFetchToolResultErrorBlock struct{…}

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

type WebFetchBlock struct{…}



Content [DocumentBlock](api/messages.md)



Citations [CitationsConfig](api/messages.md)

Citation configuration for the document

Enabled bool



Source DocumentBlockSourceUnion

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

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

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

type WebFetchToolResultErrorBlock struct{…}

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

type WebFetchToolResultErrorCode string

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



type WebSearchResultBlock struct{…}

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string



type WebSearchResultBlockParamResp struct{…}

EncryptedContent string

Title string

Type WebSearchResult

URL string

PageAge stringOptional

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



type WebSearchToolResultBlock struct{…}



Caller WebSearchToolResultBlockCallerUnion

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

Content [WebSearchToolResultBlockContentUnion](api/messages.md)

One of the following:



type WebSearchToolResultError struct{…}

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



type WebSearchToolResultBlockContentArray [][WebSearchResultBlock](api/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult



type WebSearchToolResultBlockContentUnion interface{…}

One of the following:



type WebSearchToolResultError struct{…}

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



type WebSearchToolResultBlockContentArray [][WebSearchResultBlock](api/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

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

type WebSearchToolResultBlockParamContentUnionResp interface{…}

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



type WebSearchToolResultError struct{…}

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



type WebSearchToolResultErrorCode string

One of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](api/messages.md) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](api/messages.md) = "max\_uses\_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](api/messages.md) = "query\_too\_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](api/messages.md) = "request\_too\_large"

#### MessagesBatches

##### [Create a Message Batch](api/messages/batches/create.md)

client.Messages.Batches.New(ctx, params) (\*[MessageBatch](api/messages/batches.md), error)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/messages/batches/retrieve.md)

client.Messages.Batches.Get(ctx, messageBatchID) (\*[MessageBatch](api/messages/batches.md), error)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/messages/batches/list.md)

client.Messages.Batches.List(ctx, query) (\*Page[[MessageBatch](api/messages/batches.md)], error)

GET/v1/messages/batches

##### [Cancel a Message Batch](api/messages/batches/cancel.md)

client.Messages.Batches.Cancel(ctx, messageBatchID) (\*[MessageBatch](api/messages/batches.md), error)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/messages/batches/delete.md)

client.Messages.Batches.Delete(ctx, messageBatchID) (\*[DeletedMessageBatch](api/messages/batches.md), error)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/messages/batches/results.md)

client.Messages.Batches.Results(ctx, messageBatchID) (\*[MessageBatchIndividualResponse](api/messages/batches.md), error)

GET/v1/messages/batches/{message\_batch\_id}/results

---

*Copyright © Anthropic. All rights reserved.*
