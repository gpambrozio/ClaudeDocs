# Messages

Copy page



Go

# Messages

##### [Create a Message](api/beta/messages/create.md)

client.Beta.Messages.New(ctx, params) (\*[BetaMessage](api/beta/messages.md), error)

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

client.Beta.Messages.CountTokens(ctx, params) (\*[BetaMessageTokensCount](api/beta/messages.md), error)

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse



type BetaAdvisorMessageIterationUsage struct{…}

Token usage for an advisor sub-inference iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type AdvisorMessage

Usage for an advisor sub-inference iteration



type BetaAdvisorRedactedResultBlock struct{…}

EncryptedContent string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

StopReason string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

Type AdvisorRedactedResult



type BetaAdvisorRedactedResultBlockParamResp struct{…}

EncryptedContent string

Opaque blob produced by a prior response; must be round-tripped verbatim.

Type AdvisorRedactedResult

StopReason stringOptional



type BetaAdvisorResultBlock struct{…}

StopReason string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

Text string

Type AdvisorResult



type BetaAdvisorResultBlockParamResp struct{…}

Text string

Type AdvisorResult

StopReason stringOptional



type BetaAdvisorTool20260301 struct{…}

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

Name Advisor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Advisor20260301



AllowedCallers []stringOptional

One of the following:

const BetaAdvisorTool20260301AllowedCallerDirect BetaAdvisorTool20260301AllowedCaller = "direct"

const BetaAdvisorTool20260301AllowedCallerCodeExecution20250825 BetaAdvisorTool20260301AllowedCaller = "code\_execution\_20250825"

const BetaAdvisorTool20260301AllowedCallerCodeExecution20260120 BetaAdvisorTool20260301AllowedCaller = "code\_execution\_20260120"

const BetaAdvisorTool20260301AllowedCallerCodeExecution20260521 BetaAdvisorTool20260301AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Caching [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxTokens int64Optional

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaAdvisorToolResultBlock struct{…}



Content BetaAdvisorToolResultBlockContentUnion

One of the following:



type BetaAdvisorToolResultError struct{…}



ErrorCode BetaAdvisorToolResultErrorErrorCode

One of the following:

const BetaAdvisorToolResultErrorErrorCodeMaxUsesExceeded BetaAdvisorToolResultErrorErrorCode = "max\_uses\_exceeded"

const BetaAdvisorToolResultErrorErrorCodePromptTooLong BetaAdvisorToolResultErrorErrorCode = "prompt\_too\_long"

const BetaAdvisorToolResultErrorErrorCodeTooManyRequests BetaAdvisorToolResultErrorErrorCode = "too\_many\_requests"

const BetaAdvisorToolResultErrorErrorCodeOverloaded BetaAdvisorToolResultErrorErrorCode = "overloaded"

const BetaAdvisorToolResultErrorErrorCodeUnavailable BetaAdvisorToolResultErrorErrorCode = "unavailable"

const BetaAdvisorToolResultErrorErrorCodeExecutionTimeExceeded BetaAdvisorToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaAdvisorToolResultErrorErrorCodeModelNotFound BetaAdvisorToolResultErrorErrorCode = "model\_not\_found"

Type AdvisorToolResultError



type BetaAdvisorResultBlock struct{…}

StopReason string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

Text string

Type AdvisorResult



type BetaAdvisorRedactedResultBlock struct{…}

EncryptedContent string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

StopReason string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

Type AdvisorRedactedResult

ToolUseID string

Type AdvisorToolResult



type BetaAdvisorToolResultBlockParamResp struct{…}



Content BetaAdvisorToolResultBlockParamContentUnionResp

One of the following:



type BetaAdvisorToolResultErrorParamResp struct{…}



ErrorCode BetaAdvisorToolResultErrorParamErrorCode

One of the following:

const BetaAdvisorToolResultErrorParamErrorCodeMaxUsesExceeded BetaAdvisorToolResultErrorParamErrorCode = "max\_uses\_exceeded"

const BetaAdvisorToolResultErrorParamErrorCodePromptTooLong BetaAdvisorToolResultErrorParamErrorCode = "prompt\_too\_long"

const BetaAdvisorToolResultErrorParamErrorCodeTooManyRequests BetaAdvisorToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaAdvisorToolResultErrorParamErrorCodeOverloaded BetaAdvisorToolResultErrorParamErrorCode = "overloaded"

const BetaAdvisorToolResultErrorParamErrorCodeUnavailable BetaAdvisorToolResultErrorParamErrorCode = "unavailable"

const BetaAdvisorToolResultErrorParamErrorCodeExecutionTimeExceeded BetaAdvisorToolResultErrorParamErrorCode = "execution\_time\_exceeded"

const BetaAdvisorToolResultErrorParamErrorCodeModelNotFound BetaAdvisorToolResultErrorParamErrorCode = "model\_not\_found"

Type AdvisorToolResultError



type BetaAdvisorResultBlockParamResp struct{…}

Text string

Type AdvisorResult

StopReason stringOptional



type BetaAdvisorRedactedResultBlockParamResp struct{…}

EncryptedContent string

Opaque blob produced by a prior response; must be round-tripped verbatim.

Type AdvisorRedactedResult

StopReason stringOptional

ToolUseID string

Type AdvisorToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaAdvisorToolResultError struct{…}



ErrorCode BetaAdvisorToolResultErrorErrorCode

One of the following:

const BetaAdvisorToolResultErrorErrorCodeMaxUsesExceeded BetaAdvisorToolResultErrorErrorCode = "max\_uses\_exceeded"

const BetaAdvisorToolResultErrorErrorCodePromptTooLong BetaAdvisorToolResultErrorErrorCode = "prompt\_too\_long"

const BetaAdvisorToolResultErrorErrorCodeTooManyRequests BetaAdvisorToolResultErrorErrorCode = "too\_many\_requests"

const BetaAdvisorToolResultErrorErrorCodeOverloaded BetaAdvisorToolResultErrorErrorCode = "overloaded"

const BetaAdvisorToolResultErrorErrorCodeUnavailable BetaAdvisorToolResultErrorErrorCode = "unavailable"

const BetaAdvisorToolResultErrorErrorCodeExecutionTimeExceeded BetaAdvisorToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaAdvisorToolResultErrorErrorCodeModelNotFound BetaAdvisorToolResultErrorErrorCode = "model\_not\_found"

Type AdvisorToolResultError



type BetaAdvisorToolResultErrorParamResp struct{…}



ErrorCode BetaAdvisorToolResultErrorParamErrorCode

One of the following:

const BetaAdvisorToolResultErrorParamErrorCodeMaxUsesExceeded BetaAdvisorToolResultErrorParamErrorCode = "max\_uses\_exceeded"

const BetaAdvisorToolResultErrorParamErrorCodePromptTooLong BetaAdvisorToolResultErrorParamErrorCode = "prompt\_too\_long"

const BetaAdvisorToolResultErrorParamErrorCodeTooManyRequests BetaAdvisorToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaAdvisorToolResultErrorParamErrorCodeOverloaded BetaAdvisorToolResultErrorParamErrorCode = "overloaded"

const BetaAdvisorToolResultErrorParamErrorCodeUnavailable BetaAdvisorToolResultErrorParamErrorCode = "unavailable"

const BetaAdvisorToolResultErrorParamErrorCodeExecutionTimeExceeded BetaAdvisorToolResultErrorParamErrorCode = "execution\_time\_exceeded"

const BetaAdvisorToolResultErrorParamErrorCodeModelNotFound BetaAdvisorToolResultErrorParamErrorCode = "model\_not\_found"

Type AdvisorToolResultError



type BetaAllThinkingTurns struct{…}

Type All



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaBashCodeExecutionOutputBlock struct{…}

FileID string

Type BashCodeExecutionOutput



type BetaBashCodeExecutionOutputBlockParamResp struct{…}

FileID string

Type BashCodeExecutionOutput



type BetaBashCodeExecutionResultBlock struct{…}



Content [][BetaBashCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult



type BetaBashCodeExecutionResultBlockParamResp struct{…}



Content [][BetaBashCodeExecutionOutputBlockParamResp](api/beta/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult



type BetaBashCodeExecutionToolResultBlock struct{…}



Content BetaBashCodeExecutionToolResultBlockContentUnion

One of the following:



type BetaBashCodeExecutionToolResultError struct{…}



ErrorCode BetaBashCodeExecutionToolResultErrorErrorCode

One of the following:

const BetaBashCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaBashCodeExecutionToolResultErrorErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaBashCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaBashCodeExecutionToolResultErrorErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorErrorCode = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError



type BetaBashCodeExecutionResultBlock struct{…}



Content [][BetaBashCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



type BetaBashCodeExecutionToolResultBlockParamResp struct{…}



Content BetaBashCodeExecutionToolResultBlockParamContentUnionResp

One of the following:



type BetaBashCodeExecutionToolResultErrorParamResp struct{…}



ErrorCode BetaBashCodeExecutionToolResultErrorParamErrorCode

One of the following:

const BetaBashCodeExecutionToolResultErrorParamErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorParamErrorCode = "invalid\_tool\_input"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorParamErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorParamErrorCode = "execution\_time\_exceeded"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorParamErrorCode = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError



type BetaBashCodeExecutionResultBlockParamResp struct{…}



Content [][BetaBashCodeExecutionOutputBlockParamResp](api/beta/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaBashCodeExecutionToolResultError struct{…}



ErrorCode BetaBashCodeExecutionToolResultErrorErrorCode

One of the following:

const BetaBashCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaBashCodeExecutionToolResultErrorErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaBashCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaBashCodeExecutionToolResultErrorErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorErrorCode = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError



type BetaBashCodeExecutionToolResultErrorParamResp struct{…}



ErrorCode BetaBashCodeExecutionToolResultErrorParamErrorCode

One of the following:

const BetaBashCodeExecutionToolResultErrorParamErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorParamErrorCode = "invalid\_tool\_input"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorParamErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorParamErrorCode = "execution\_time\_exceeded"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorParamErrorCode = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError



type BetaCacheControlEphemeral struct{…}

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaCacheCreation struct{…}

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.



type BetaCacheMissMessagesChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type MessagesChanged



type BetaCacheMissModelChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type ModelChanged



type BetaCacheMissPreviousMessageNotFound struct{…}

Type PreviousMessageNotFound



type BetaCacheMissSystemChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type SystemChanged



type BetaCacheMissToolsChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type ToolsChanged



type BetaCacheMissUnavailable struct{…}

Type Unavailable



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationConfig struct{…}

Enabled bool



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationSearchResultLocation struct{…}

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

type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationsConfigParamResp struct{…}

Enabled boolOptional



type BetaCitationsDelta struct{…}



Citation BetaCitationsDeltaCitationUnion

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaClearThinking20251015Edit struct{…}

Type ClearThinking20251015



Keep BetaClearThinking20251015EditKeepUnionOptional

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

One of the following:



type BetaThinkingTurns struct{…}

Type ThinkingTurns

Value int64



type BetaAllThinkingTurns struct{…}

Type All

All



type BetaClearThinking20251015EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

ClearedThinkingTurns int64

Number of thinking turns that were cleared.

Type ClearThinking20251015

The type of context management edit applied.



type BetaClearToolUses20250919Edit struct{…}

Type ClearToolUses20250919



ClearAtLeast [BetaInputTokensClearAtLeast](api/beta/messages.md)Optional

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

Type InputTokens

Value int64



ClearToolInputs BetaClearToolUses20250919EditClearToolInputsUnionOptional

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

One of the following:

bool

[]string

ExcludeTools []stringOptional

Tool names whose uses are preserved from clearing



Keep [BetaToolUsesKeep](api/beta/messages.md)Optional

Number of tool uses to retain in the conversation

Type ToolUses

Value int64



Trigger BetaClearToolUses20250919EditTriggerUnionOptional

Condition that triggers the context management strategy

One of the following:



type BetaInputTokensTrigger struct{…}

Type InputTokens

Value int64



type BetaToolUsesTrigger struct{…}

Type ToolUses

Value int64



type BetaClearToolUses20250919EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

ClearedToolUses int64

Number of tool uses that were cleared.

Type ClearToolUses20250919

The type of context management edit applied.



type BetaCodeExecutionOutputBlock struct{…}

FileID string

Type CodeExecutionOutput



type BetaCodeExecutionOutputBlockParamResp struct{…}

FileID string

Type CodeExecutionOutput



type BetaCodeExecutionResultBlock struct{…}



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type BetaCodeExecutionResultBlockParamResp struct{…}



Content [][BetaCodeExecutionOutputBlockParamResp](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type BetaCodeExecutionTool20250522 struct{…}



Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250522



AllowedCallers []stringOptional

One of the following:

const BetaCodeExecutionTool20250522AllowedCallerDirect BetaCodeExecutionTool20250522AllowedCaller = "direct"

const BetaCodeExecutionTool20250522AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20250522AllowedCaller = "code\_execution\_20250825"

const BetaCodeExecutionTool20250522AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20250522AllowedCaller = "code\_execution\_20260120"

const BetaCodeExecutionTool20250522AllowedCallerCodeExecution20260521 BetaCodeExecutionTool20250522AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaCodeExecutionTool20250825 struct{…}



Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250825



AllowedCallers []stringOptional

One of the following:

const BetaCodeExecutionTool20250825AllowedCallerDirect BetaCodeExecutionTool20250825AllowedCaller = "direct"

const BetaCodeExecutionTool20250825AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20250825AllowedCaller = "code\_execution\_20250825"

const BetaCodeExecutionTool20250825AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20250825AllowedCaller = "code\_execution\_20260120"

const BetaCodeExecutionTool20250825AllowedCallerCodeExecution20260521 BetaCodeExecutionTool20250825AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaCodeExecutionTool20260120 struct{…}

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20260120



AllowedCallers []stringOptional

One of the following:

const BetaCodeExecutionTool20260120AllowedCallerDirect BetaCodeExecutionTool20260120AllowedCaller = "direct"

const BetaCodeExecutionTool20260120AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20260120AllowedCaller = "code\_execution\_20250825"

const BetaCodeExecutionTool20260120AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20260120AllowedCaller = "code\_execution\_20260120"

const BetaCodeExecutionTool20260120AllowedCallerCodeExecution20260521 BetaCodeExecutionTool20260120AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaCodeExecutionTool20260521 struct{…}

Code execution tool with REPL state persistence.



Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20260521



AllowedCallers []stringOptional

One of the following:

const BetaCodeExecutionTool20260521AllowedCallerDirect BetaCodeExecutionTool20260521AllowedCaller = "direct"

const BetaCodeExecutionTool20260521AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20260521AllowedCaller = "code\_execution\_20250825"

const BetaCodeExecutionTool20260521AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20260521AllowedCaller = "code\_execution\_20260120"

const BetaCodeExecutionTool20260521AllowedCallerCodeExecution20260521 BetaCodeExecutionTool20260521AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaCodeExecutionToolResultBlock struct{…}



Content [BetaCodeExecutionToolResultBlockContentUnion](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type BetaCodeExecutionToolResultError struct{…}



ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type BetaCodeExecutionResultBlock struct{…}



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type BetaEncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



type BetaCodeExecutionToolResultBlockContentUnion interface{…}

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type BetaCodeExecutionToolResultError struct{…}



ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type BetaCodeExecutionResultBlock struct{…}



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type BetaEncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult



type BetaCodeExecutionToolResultBlockParamResp struct{…}



Content [BetaCodeExecutionToolResultBlockParamContentUnionResp](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type BetaCodeExecutionToolResultErrorParamResp struct{…}



ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type BetaCodeExecutionResultBlockParamResp struct{…}



Content [][BetaCodeExecutionOutputBlockParamResp](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type BetaEncryptedCodeExecutionResultBlockParamResp struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][BetaCodeExecutionOutputBlockParamResp](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaCodeExecutionToolResultBlockParamContentUnionResp interface{…}

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type BetaCodeExecutionToolResultErrorParamResp struct{…}



ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type BetaCodeExecutionResultBlockParamResp struct{…}



Content [][BetaCodeExecutionOutputBlockParamResp](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type BetaEncryptedCodeExecutionResultBlockParamResp struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][BetaCodeExecutionOutputBlockParamResp](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult



type BetaCodeExecutionToolResultError struct{…}



ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type BetaCodeExecutionToolResultErrorCode string

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "execution\_time\_exceeded"



type BetaCodeExecutionToolResultErrorParamResp struct{…}



ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type BetaCompact20260112Edit struct{…}

Automatically compact older context when reaching the configured trigger threshold.

Type Compact20260112

Instructions stringOptional

Additional instructions for summarization.

PauseAfterCompaction boolOptional

Whether to pause after compaction and return the compaction block to the user.



Trigger [BetaInputTokensTrigger](api/beta/messages.md)Optional

When to trigger compaction. Defaults to 150000 input tokens.

Type InputTokens

Value int64



type BetaCompactionBlock struct{…}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Content string

Summary of compacted content, or null if compaction failed

EncryptedContent string

Opaque metadata from prior compaction, to be round-tripped verbatim

Type Compaction



type BetaCompactionBlockParamResp struct{…}

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

Type Compaction



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Content stringOptional

Summary of previously compacted content, or null if compaction failed

EncryptedContent stringOptional

Opaque metadata from prior compaction, to be round-tripped verbatim



type BetaCompactionContentBlockDelta struct{…}

Content string

EncryptedContent string

Opaque metadata from prior compaction, to be round-tripped verbatim

Type CompactionDelta



type BetaCompactionIterationUsage struct{…}

Token usage for a compaction iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

Type Compaction

Usage for a compaction iteration



type BetaContainer struct{…}

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



Skills [][BetaSkill](api/beta/messages.md)

Skills loaded in the container

SkillID string

Skill ID



Type BetaSkillType

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

const BetaSkillTypeAnthropic BetaSkillType = "anthropic"

const BetaSkillTypeCustom BetaSkillType = "custom"

Version string

Skill version or 'latest' for most recent version



type BetaContainerParamsResp struct{…}

Container parameters with skills to be loaded.

ID stringOptional

Container id



Skills [][BetaSkillParamsResp](api/beta/messages.md)Optional

List of skills to load in the container

SkillID string

Skill ID



Type BetaSkillParamsType

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

const BetaSkillParamsTypeAnthropic BetaSkillParamsType = "anthropic"

const BetaSkillParamsTypeCustom BetaSkillParamsType = "custom"

Version stringOptional

Skill version or 'latest' for most recent version



type BetaContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload



type BetaContainerUploadBlockParamResp struct{…}

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

FileID string

Type ContainerUpload



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaContentBlockUnion interface{…}

Response model for a file uploaded to the container.

One of the following:



type BetaTextBlock struct{…}



Citations [][BetaTextCitationUnion](api/beta/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

type BetaThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking



type BetaRedactedThinkingBlock struct{…}

Data string

Type RedactedThinking



type BetaToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse



Caller BetaToolUseBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaServerToolUseBlock struct{…}

ID string

Input map[string, any]



Name BetaServerToolUseBlockName

One of the following:

const BetaServerToolUseBlockNameAdvisor BetaServerToolUseBlockName = "advisor"

const BetaServerToolUseBlockNameWebSearch BetaServerToolUseBlockName = "web\_search"

const BetaServerToolUseBlockNameWebFetch BetaServerToolUseBlockName = "web\_fetch"

const BetaServerToolUseBlockNameCodeExecution BetaServerToolUseBlockName = "code\_execution"

const BetaServerToolUseBlockNameBashCodeExecution BetaServerToolUseBlockName = "bash\_code\_execution"

const BetaServerToolUseBlockNameTextEditorCodeExecution BetaServerToolUseBlockName = "text\_editor\_code\_execution"

const BetaServerToolUseBlockNameToolSearchToolRegex BetaServerToolUseBlockName = "tool\_search\_tool\_regex"

const BetaServerToolUseBlockNameToolSearchToolBm25 BetaServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse



Caller BetaServerToolUseBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebSearchToolResultBlock struct{…}



Content [BetaWebSearchToolResultBlockContentUnion](api/beta/messages.md)

One of the following:



type BetaWebSearchToolResultError struct{…}



ErrorCode [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "request\_too\_large"

Type WebSearchToolResultError



type BetaWebSearchToolResultBlockContentArray [][BetaWebSearchResultBlock](api/beta/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult



Caller BetaWebSearchToolResultBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebFetchToolResultBlock struct{…}



Content BetaWebFetchToolResultBlockContentUnion

One of the following:



type BetaWebFetchToolResultErrorBlock struct{…}



ErrorCode [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotInPriorContext [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_in\_prior\_context"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unavailable"

Type WebFetchToolResultError



type BetaWebFetchBlock struct{…}



Content [BetaDocumentBlock](api/beta/messages.md)



Citations [BetaCitationConfig](api/beta/messages.md)

Citation configuration for the document

Enabled bool



Source BetaDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

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

Caller BetaWebFetchToolResultBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaAdvisorToolResultBlock struct{…}



Content BetaAdvisorToolResultBlockContentUnion

One of the following:



type BetaAdvisorToolResultError struct{…}



ErrorCode BetaAdvisorToolResultErrorErrorCode

One of the following:

const BetaAdvisorToolResultErrorErrorCodeMaxUsesExceeded BetaAdvisorToolResultErrorErrorCode = "max\_uses\_exceeded"

const BetaAdvisorToolResultErrorErrorCodePromptTooLong BetaAdvisorToolResultErrorErrorCode = "prompt\_too\_long"

const BetaAdvisorToolResultErrorErrorCodeTooManyRequests BetaAdvisorToolResultErrorErrorCode = "too\_many\_requests"

const BetaAdvisorToolResultErrorErrorCodeOverloaded BetaAdvisorToolResultErrorErrorCode = "overloaded"

const BetaAdvisorToolResultErrorErrorCodeUnavailable BetaAdvisorToolResultErrorErrorCode = "unavailable"

const BetaAdvisorToolResultErrorErrorCodeExecutionTimeExceeded BetaAdvisorToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaAdvisorToolResultErrorErrorCodeModelNotFound BetaAdvisorToolResultErrorErrorCode = "model\_not\_found"

Type AdvisorToolResultError



type BetaAdvisorResultBlock struct{…}

StopReason string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

Text string

Type AdvisorResult



type BetaAdvisorRedactedResultBlock struct{…}

EncryptedContent string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

StopReason string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

Type AdvisorRedactedResult

ToolUseID string

Type AdvisorToolResult



type BetaCodeExecutionToolResultBlock struct{…}



Content [BetaCodeExecutionToolResultBlockContentUnion](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type BetaCodeExecutionToolResultError struct{…}



ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type BetaCodeExecutionResultBlock struct{…}



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type BetaEncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



type BetaBashCodeExecutionToolResultBlock struct{…}



Content BetaBashCodeExecutionToolResultBlockContentUnion

One of the following:



type BetaBashCodeExecutionToolResultError struct{…}



ErrorCode BetaBashCodeExecutionToolResultErrorErrorCode

One of the following:

const BetaBashCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaBashCodeExecutionToolResultErrorErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaBashCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaBashCodeExecutionToolResultErrorErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorErrorCode = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError



type BetaBashCodeExecutionResultBlock struct{…}



Content [][BetaBashCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



type BetaTextEditorCodeExecutionToolResultBlock struct{…}



Content BetaTextEditorCodeExecutionToolResultBlockContentUnion

One of the following:



type BetaTextEditorCodeExecutionToolResultError struct{…}



ErrorCode BetaTextEditorCodeExecutionToolResultErrorErrorCode

One of the following:

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorErrorCode = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type BetaTextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType BetaTextEditorCodeExecutionViewResultBlockFileType

One of the following:

const BetaTextEditorCodeExecutionViewResultBlockFileTypeText BetaTextEditorCodeExecutionViewResultBlockFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockFileTypeImage BetaTextEditorCodeExecutionViewResultBlockFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockFileTypePDF BetaTextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type BetaTextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type BetaTextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult



type BetaToolSearchToolResultBlock struct{…}



Content BetaToolSearchToolResultBlockContentUnion

One of the following:



type BetaToolSearchToolResultError struct{…}



ErrorCode BetaToolSearchToolResultErrorErrorCode

One of the following:

const BetaToolSearchToolResultErrorErrorCodeInvalidToolInput BetaToolSearchToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaToolSearchToolResultErrorErrorCodeUnavailable BetaToolSearchToolResultErrorErrorCode = "unavailable"

const BetaToolSearchToolResultErrorErrorCodeTooManyRequests BetaToolSearchToolResultErrorErrorCode = "too\_many\_requests"

const BetaToolSearchToolResultErrorErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorErrorCode = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type BetaToolSearchToolSearchResultBlock struct{…}



ToolReferences [][BetaToolReferenceBlock](api/beta/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



type BetaMCPToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

The name of the MCP tool

ServerName string

The name of the MCP server

Type MCPToolUse



type BetaMCPToolResultBlock struct{…}



Content BetaMCPToolResultBlockContentUnion

One of the following:

string



type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent [][BetaTextBlock](api/beta/messages.md)



Citations [][BetaTextCitationUnion](api/beta/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

IsError bool

ToolUseID string

Type MCPToolResult



type BetaContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload



type BetaCompactionBlock struct{…}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Content string

Summary of compacted content, or null if compaction failed

EncryptedContent string

Opaque metadata from prior compaction, to be round-tripped verbatim

Type Compaction



type BetaFallbackBlock struct{…}

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



From [BetaFallbackInfo](api/beta/messages.md)

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

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

To [BetaFallbackInfo](api/beta/messages.md)

The fallback model producing the content that follows this block. Its `model` is always the canonical id.

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

Trigger [BetaFallbackRefusalTrigger](api/beta/messages.md)

What caused the `from` model to hand over at this hop.



Category BetaFallbackRefusalTriggerCategory

The policy category that triggered a refusal.

One of the following:

const BetaFallbackRefusalTriggerCategoryCyber BetaFallbackRefusalTriggerCategory = "cyber"

const BetaFallbackRefusalTriggerCategoryBio BetaFallbackRefusalTriggerCategory = "bio"

const BetaFallbackRefusalTriggerCategoryFrontierLLM BetaFallbackRefusalTriggerCategory = "frontier\_llm"

const BetaFallbackRefusalTriggerCategoryReasoningExtraction BetaFallbackRefusalTriggerCategory = "reasoning\_extraction"

const BetaFallbackRefusalTriggerCategoryMilitaryWeapons BetaFallbackRefusalTriggerCategory = "military\_weapons"

Type Refusal

Type Fallback



type BetaContentBlockParamUnionResp interface{…}

Regular text content.

One of the following:



type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaRequestDocumentBlock struct{…}



Source BetaRequestDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text



type BetaContentBlockSource struct{…}



Content BetaContentBlockSourceContentUnion

One of the following:

string



[][BetaContentBlockSourceContentUnion](api/beta/messages.md)

One of the following:



type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type Content



type BetaURLPDFSource struct{…}

Type URL

URL string



type BetaFileDocumentSource struct{…}

FileID string

Type File

Type Document



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

Enabled boolOptional

Context stringOptional

Title stringOptional



type BetaSearchResultBlockParamResp struct{…}



Content [][BetaTextBlockParamResp](api/beta/messages.md)

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

Enabled boolOptional



type BetaThinkingBlockParamResp struct{…}

Signature string

Thinking string

Type Thinking



type BetaRedactedThinkingBlockParamResp struct{…}

Data string

Type RedactedThinking



type BetaToolUseBlockParamResp struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Caller BetaToolUseBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaToolResultBlockParamResp struct{…}

ToolUseID string

Type ToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Content []BetaToolResultBlockParamContentUnionRespOptional

One of the following:



[]BetaToolResultBlockParamContentUnionResp

One of the following:



type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaSearchResultBlockParamResp struct{…}



Content [][BetaTextBlockParamResp](api/beta/messages.md)

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

Enabled boolOptional



type BetaRequestDocumentBlock struct{…}



Source BetaRequestDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text



type BetaContentBlockSource struct{…}



Content BetaContentBlockSourceContentUnion

One of the following:

string



[][BetaContentBlockSourceContentUnion](api/beta/messages.md)

One of the following:



type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type Content



type BetaURLPDFSource struct{…}

Type URL

URL string



type BetaFileDocumentSource struct{…}

FileID string

Type File

Type Document



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

Enabled boolOptional

Context stringOptional

Title stringOptional



type BetaToolReferenceBlockParamResp struct{…}

Tool reference block that can be included in tool\_result content.

ToolName string

Type ToolReference



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

IsError boolOptional



type BetaServerToolUseBlockParamResp struct{…}

ID string

Input map[string, any]



Name BetaServerToolUseBlockParamName

One of the following:

const BetaServerToolUseBlockParamNameAdvisor BetaServerToolUseBlockParamName = "advisor"

const BetaServerToolUseBlockParamNameWebSearch BetaServerToolUseBlockParamName = "web\_search"

const BetaServerToolUseBlockParamNameWebFetch BetaServerToolUseBlockParamName = "web\_fetch"

const BetaServerToolUseBlockParamNameCodeExecution BetaServerToolUseBlockParamName = "code\_execution"

const BetaServerToolUseBlockParamNameBashCodeExecution BetaServerToolUseBlockParamName = "bash\_code\_execution"

const BetaServerToolUseBlockParamNameTextEditorCodeExecution BetaServerToolUseBlockParamName = "text\_editor\_code\_execution"

const BetaServerToolUseBlockParamNameToolSearchToolRegex BetaServerToolUseBlockParamName = "tool\_search\_tool\_regex"

const BetaServerToolUseBlockParamNameToolSearchToolBm25 BetaServerToolUseBlockParamName = "tool\_search\_tool\_bm25"

Type ServerToolUse



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Caller BetaServerToolUseBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebSearchToolResultBlockParamResp struct{…}



Content [BetaWebSearchToolResultBlockParamContentUnionResp](api/beta/messages.md)

One of the following:



[][BetaWebSearchResultBlockParamResp](api/beta/messages.md)

EncryptedContent string

Title string

Type WebSearchResult

URL string

PageAge stringOptional



type BetaWebSearchToolRequestError struct{…}



ErrorCode [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "request\_too\_large"

Type WebSearchToolResultError

ToolUseID string

Type WebSearchToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Caller BetaWebSearchToolResultBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebFetchToolResultBlockParamResp struct{…}



Content BetaWebFetchToolResultBlockParamContentUnionResp

One of the following:



type BetaWebFetchToolResultErrorBlockParamResp struct{…}



ErrorCode [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotInPriorContext [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_in\_prior\_context"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unavailable"

Type WebFetchToolResultError



type BetaWebFetchBlockParamResp struct{…}



Content [BetaRequestDocumentBlock](api/beta/messages.md)



Source BetaRequestDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text



type BetaContentBlockSource struct{…}



Content BetaContentBlockSourceContentUnion

One of the following:

string



[][BetaContentBlockSourceContentUnion](api/beta/messages.md)

One of the following:



type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type Content



type BetaURLPDFSource struct{…}

Type URL

URL string



type BetaFileDocumentSource struct{…}

FileID string

Type File

Type Document



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

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

CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Caller BetaWebFetchToolResultBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaAdvisorToolResultBlockParamResp struct{…}



Content BetaAdvisorToolResultBlockParamContentUnionResp

One of the following:



type BetaAdvisorToolResultErrorParamResp struct{…}



ErrorCode BetaAdvisorToolResultErrorParamErrorCode

One of the following:

const BetaAdvisorToolResultErrorParamErrorCodeMaxUsesExceeded BetaAdvisorToolResultErrorParamErrorCode = "max\_uses\_exceeded"

const BetaAdvisorToolResultErrorParamErrorCodePromptTooLong BetaAdvisorToolResultErrorParamErrorCode = "prompt\_too\_long"

const BetaAdvisorToolResultErrorParamErrorCodeTooManyRequests BetaAdvisorToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaAdvisorToolResultErrorParamErrorCodeOverloaded BetaAdvisorToolResultErrorParamErrorCode = "overloaded"

const BetaAdvisorToolResultErrorParamErrorCodeUnavailable BetaAdvisorToolResultErrorParamErrorCode = "unavailable"

const BetaAdvisorToolResultErrorParamErrorCodeExecutionTimeExceeded BetaAdvisorToolResultErrorParamErrorCode = "execution\_time\_exceeded"

const BetaAdvisorToolResultErrorParamErrorCodeModelNotFound BetaAdvisorToolResultErrorParamErrorCode = "model\_not\_found"

Type AdvisorToolResultError



type BetaAdvisorResultBlockParamResp struct{…}

Text string

Type AdvisorResult

StopReason stringOptional



type BetaAdvisorRedactedResultBlockParamResp struct{…}

EncryptedContent string

Opaque blob produced by a prior response; must be round-tripped verbatim.

Type AdvisorRedactedResult

StopReason stringOptional

ToolUseID string

Type AdvisorToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaCodeExecutionToolResultBlockParamResp struct{…}



Content [BetaCodeExecutionToolResultBlockParamContentUnionResp](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type BetaCodeExecutionToolResultErrorParamResp struct{…}



ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type BetaCodeExecutionResultBlockParamResp struct{…}



Content [][BetaCodeExecutionOutputBlockParamResp](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type BetaEncryptedCodeExecutionResultBlockParamResp struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][BetaCodeExecutionOutputBlockParamResp](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaBashCodeExecutionToolResultBlockParamResp struct{…}



Content BetaBashCodeExecutionToolResultBlockParamContentUnionResp

One of the following:



type BetaBashCodeExecutionToolResultErrorParamResp struct{…}



ErrorCode BetaBashCodeExecutionToolResultErrorParamErrorCode

One of the following:

const BetaBashCodeExecutionToolResultErrorParamErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorParamErrorCode = "invalid\_tool\_input"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorParamErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorParamErrorCode = "execution\_time\_exceeded"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorParamErrorCode = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError



type BetaBashCodeExecutionResultBlockParamResp struct{…}



Content [][BetaBashCodeExecutionOutputBlockParamResp](api/beta/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaTextEditorCodeExecutionToolResultBlockParamResp struct{…}



Content BetaTextEditorCodeExecutionToolResultBlockParamContentUnionResp

One of the following:



type BetaTextEditorCodeExecutionToolResultErrorParamResp struct{…}



ErrorCode BetaTextEditorCodeExecutionToolResultErrorParamErrorCode

One of the following:

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "invalid\_tool\_input"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "execution\_time\_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "file\_not\_found"

Type TextEditorCodeExecutionToolResultError

ErrorMessage stringOptional



type BetaTextEditorCodeExecutionViewResultBlockParamResp struct{…}

Content string



FileType BetaTextEditorCodeExecutionViewResultBlockParamFileType

One of the following:

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypeText BetaTextEditorCodeExecutionViewResultBlockParamFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypeImage BetaTextEditorCodeExecutionViewResultBlockParamFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypePDF BetaTextEditorCodeExecutionViewResultBlockParamFileType = "pdf"

Type TextEditorCodeExecutionViewResult

NumLines int64Optional

StartLine int64Optional

TotalLines int64Optional



type BetaTextEditorCodeExecutionCreateResultBlockParamResp struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type BetaTextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}

Type TextEditorCodeExecutionStrReplaceResult

Lines []stringOptional

NewLines int64Optional

NewStart int64Optional

OldLines int64Optional

OldStart int64Optional

ToolUseID string

Type TextEditorCodeExecutionToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaToolSearchToolResultBlockParamResp struct{…}



Content BetaToolSearchToolResultBlockParamContentUnionResp

One of the following:



type BetaToolSearchToolResultErrorParamResp struct{…}



ErrorCode BetaToolSearchToolResultErrorParamErrorCode

One of the following:

const BetaToolSearchToolResultErrorParamErrorCodeInvalidToolInput BetaToolSearchToolResultErrorParamErrorCode = "invalid\_tool\_input"

const BetaToolSearchToolResultErrorParamErrorCodeUnavailable BetaToolSearchToolResultErrorParamErrorCode = "unavailable"

const BetaToolSearchToolResultErrorParamErrorCodeTooManyRequests BetaToolSearchToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaToolSearchToolResultErrorParamErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorParamErrorCode = "execution\_time\_exceeded"

Type ToolSearchToolResultError

ErrorMessage stringOptional



type BetaToolSearchToolSearchResultBlockParamResp struct{…}



ToolReferences [][BetaToolReferenceBlockParamResp](api/beta/messages.md)

ToolName string

Type ToolReference



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaMCPToolUseBlockParamResp struct{…}

ID string

Input map[string, any]

Name string

ServerName string

The name of the MCP server

Type MCPToolUse



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaRequestMCPToolResultBlockParamResp struct{…}

ToolUseID string

Type MCPToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Content BetaRequestMCPToolResultBlockParamContentUnionRespOptional

One of the following:

string



[][BetaTextBlockParamResp](api/beta/messages.md)

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

IsError boolOptional



type BetaContainerUploadBlockParamResp struct{…}

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

FileID string

Type ContainerUpload



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaCompactionBlockParamResp struct{…}

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

Type Compaction



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Content stringOptional

Summary of previously compacted content, or null if compaction failed

EncryptedContent stringOptional

Opaque metadata from prior compaction, to be round-tripped verbatim



type BetaMidConversationSystemBlockParamResp struct{…}

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



Content [][BetaTextBlockParamResp](api/beta/messages.md)

System instruction text blocks.

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaFallbackBlockParamResp struct{…}

A `fallback` block echoed back from a prior response.

Accepted in `messages[].content` and not rendered into the prompt; not
validated against the request's `fallbacks` chain or top-level `model`.

Echo the assistant turn back verbatim, including this block in its
original position. The block marks the boundary between content produced
before and after a fallback hop, and the server relies on that boundary
to validate the turn: when thinking runs flank the boundary, omitting
the block merges them into one span the server cannot validate (the
request is rejected), and moving it into the middle of a single run is
likewise rejected; between non-thinking blocks the block's placement has
no validation effect.



From [BetaFallbackInfoParamResp](api/beta/messages.md)

Identifies one hop of a fallback transition.

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

To [BetaFallbackInfoParamResp](api/beta/messages.md)

Identifies one hop of a fallback transition.

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

Type Fallback

Trigger anyOptional

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



type BetaContentBlockSource struct{…}



Content BetaContentBlockSourceContentUnion

One of the following:

string



[][BetaContentBlockSourceContentUnion](api/beta/messages.md)

One of the following:



type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type Content



type BetaContentBlockSourceContentUnion interface{…}

One of the following:



type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaContextManagementConfig struct{…}



Edits []BetaContextManagementConfigEditUnionOptional

List of context management edits to apply

One of the following:



type BetaClearToolUses20250919Edit struct{…}

Type ClearToolUses20250919



ClearAtLeast [BetaInputTokensClearAtLeast](api/beta/messages.md)Optional

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

Type InputTokens

Value int64



ClearToolInputs BetaClearToolUses20250919EditClearToolInputsUnionOptional

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

One of the following:

bool

[]string

ExcludeTools []stringOptional

Tool names whose uses are preserved from clearing



Keep [BetaToolUsesKeep](api/beta/messages.md)Optional

Number of tool uses to retain in the conversation

Type ToolUses

Value int64



Trigger BetaClearToolUses20250919EditTriggerUnionOptional

Condition that triggers the context management strategy

One of the following:



type BetaInputTokensTrigger struct{…}

Type InputTokens

Value int64



type BetaToolUsesTrigger struct{…}

Type ToolUses

Value int64



type BetaClearThinking20251015Edit struct{…}

Type ClearThinking20251015



Keep BetaClearThinking20251015EditKeepUnionOptional

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

One of the following:



type BetaThinkingTurns struct{…}

Type ThinkingTurns

Value int64



type BetaAllThinkingTurns struct{…}

Type All

All



type BetaCompact20260112Edit struct{…}

Automatically compact older context when reaching the configured trigger threshold.

Type Compact20260112

Instructions stringOptional

Additional instructions for summarization.

PauseAfterCompaction boolOptional

Whether to pause after compaction and return the compaction block to the user.



Trigger [BetaInputTokensTrigger](api/beta/messages.md)Optional

When to trigger compaction. Defaults to 150000 input tokens.

Type InputTokens

Value int64



type BetaContextManagementResponse struct{…}



AppliedEdits []BetaContextManagementResponseAppliedEditUnion

List of context management edits that were applied.

One of the following:



type BetaClearToolUses20250919EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

ClearedToolUses int64

Number of tool uses that were cleared.

Type ClearToolUses20250919

The type of context management edit applied.



type BetaClearThinking20251015EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

ClearedThinkingTurns int64

Number of thinking turns that were cleared.

Type ClearThinking20251015

The type of context management edit applied.



type BetaCountTokensContextManagementResponse struct{…}

OriginalInputTokens int64

The original token count before context management was applied



type BetaDiagnostics struct{…}

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



CacheMissReason BetaDiagnosticsCacheMissReasonUnion

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



type BetaCacheMissModelChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type ModelChanged



type BetaCacheMissSystemChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type SystemChanged



type BetaCacheMissToolsChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type ToolsChanged



type BetaCacheMissMessagesChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type MessagesChanged



type BetaCacheMissPreviousMessageNotFound struct{…}

Type PreviousMessageNotFound



type BetaCacheMissUnavailable struct{…}

Type Unavailable



type BetaDiagnosticsParamResp struct{…}

Request-level diagnostics. Currently carries the previous response
id for prompt-cache divergence reporting.

PreviousMessageID stringOptional

The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaDocumentBlock struct{…}



Citations [BetaCitationConfig](api/beta/messages.md)

Citation configuration for the document

Enabled bool



Source BetaDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

Title string

The title of the document

Type Document



type BetaEncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult



type BetaEncryptedCodeExecutionResultBlockParamResp struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][BetaCodeExecutionOutputBlockParamResp](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult



type BetaFallbackBlock struct{…}

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



From [BetaFallbackInfo](api/beta/messages.md)

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

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

To [BetaFallbackInfo](api/beta/messages.md)

The fallback model producing the content that follows this block. Its `model` is always the canonical id.

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

Trigger [BetaFallbackRefusalTrigger](api/beta/messages.md)

What caused the `from` model to hand over at this hop.



Category BetaFallbackRefusalTriggerCategory

The policy category that triggered a refusal.

One of the following:

const BetaFallbackRefusalTriggerCategoryCyber BetaFallbackRefusalTriggerCategory = "cyber"

const BetaFallbackRefusalTriggerCategoryBio BetaFallbackRefusalTriggerCategory = "bio"

const BetaFallbackRefusalTriggerCategoryFrontierLLM BetaFallbackRefusalTriggerCategory = "frontier\_llm"

const BetaFallbackRefusalTriggerCategoryReasoningExtraction BetaFallbackRefusalTriggerCategory = "reasoning\_extraction"

const BetaFallbackRefusalTriggerCategoryMilitaryWeapons BetaFallbackRefusalTriggerCategory = "military\_weapons"

Type Refusal

Type Fallback



type BetaFallbackBlockParamResp struct{…}

A `fallback` block echoed back from a prior response.

Accepted in `messages[].content` and not rendered into the prompt; not
validated against the request's `fallbacks` chain or top-level `model`.

Echo the assistant turn back verbatim, including this block in its
original position. The block marks the boundary between content produced
before and after a fallback hop, and the server relies on that boundary
to validate the turn: when thinking runs flank the boundary, omitting
the block merges them into one span the server cannot validate (the
request is rejected), and moving it into the middle of a single run is
likewise rejected; between non-thinking blocks the block's placement has
no validation effect.



From [BetaFallbackInfoParamResp](api/beta/messages.md)

Identifies one hop of a fallback transition.

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

To [BetaFallbackInfoParamResp](api/beta/messages.md)

Identifies one hop of a fallback transition.

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

Type Fallback

Trigger anyOptional

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



type BetaFallbackInfo struct{…}

Identifies one hop of a fallback transition.

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

type BetaFallbackInfoParamResp struct{…}

Identifies one hop of a fallback transition.

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

type BetaFallbackMessageIterationUsage struct{…}

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type FallbackMessage

Usage for the fallback-model attempt that served the response



type BetaFallbackParamResp struct{…}

One entry in the `fallbacks` chain on a `/v1/messages` request.

`model` is required. The four override fields (`max_tokens`, `thinking`,
`output_config`, and `speed`) replace the corresponding top-level field
for this attempt only and are validated as if the request were made to
`model`. Any other key is rejected at parse time.

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

MaxTokens int64Optional



OutputConfig [BetaOutputConfig](api/beta/messages.md)Optional



Effort BetaOutputConfigEffortOptional

All possible effort levels.

One of the following:

const BetaOutputConfigEffortLow BetaOutputConfigEffort = "low"

const BetaOutputConfigEffortMedium BetaOutputConfigEffort = "medium"

const BetaOutputConfigEffortHigh BetaOutputConfigEffort = "high"

const BetaOutputConfigEffortXhigh BetaOutputConfigEffort = "xhigh"

const BetaOutputConfigEffortMax BetaOutputConfigEffort = "max"



Format [BetaJSONOutputFormat](api/beta/messages.md)Optional

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

Schema map[string, any]

The JSON schema of the format

Type JSONSchema



TaskBudget [BetaTokenTaskBudget](api/beta/messages.md)Optional

User-configurable total token budget across contexts.

Total int64

Total token budget across all contexts in the session.

Type Tokens

The budget type. Currently only 'tokens' is supported.

Remaining int64Optional

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



Speed BetaFallbackParamSpeedOptional

One of the following:

const BetaFallbackParamSpeedStandard BetaFallbackParamSpeed = "standard"

const BetaFallbackParamSpeedFast BetaFallbackParamSpeed = "fast"



Thinking BetaFallbackParamThinkingUnionRespOptional

One of the following:



type BetaThinkingConfigEnabled struct{…}



BudgetTokens int64

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

Type Enabled



Display BetaThinkingConfigEnabledDisplayOptional

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

const BetaThinkingConfigEnabledDisplaySummarized BetaThinkingConfigEnabledDisplay = "summarized"

const BetaThinkingConfigEnabledDisplayOmitted BetaThinkingConfigEnabledDisplay = "omitted"



type BetaThinkingConfigDisabled struct{…}

Type Disabled



type BetaThinkingConfigAdaptive struct{…}

Type Adaptive



Display BetaThinkingConfigAdaptiveDisplayOptional

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

const BetaThinkingConfigAdaptiveDisplaySummarized BetaThinkingConfigAdaptiveDisplay = "summarized"

const BetaThinkingConfigAdaptiveDisplayOmitted BetaThinkingConfigAdaptiveDisplay = "omitted"



type BetaFallbackRefusalTrigger struct{…}

The `from` model declined for policy reasons.



Category BetaFallbackRefusalTriggerCategory

The policy category that triggered a refusal.

One of the following:

const BetaFallbackRefusalTriggerCategoryCyber BetaFallbackRefusalTriggerCategory = "cyber"

const BetaFallbackRefusalTriggerCategoryBio BetaFallbackRefusalTriggerCategory = "bio"

const BetaFallbackRefusalTriggerCategoryFrontierLLM BetaFallbackRefusalTriggerCategory = "frontier\_llm"

const BetaFallbackRefusalTriggerCategoryReasoningExtraction BetaFallbackRefusalTriggerCategory = "reasoning\_extraction"

const BetaFallbackRefusalTriggerCategoryMilitaryWeapons BetaFallbackRefusalTriggerCategory = "military\_weapons"

Type Refusal



type BetaFileDocumentSource struct{…}

FileID string

Type File



type BetaFileImageSource struct{…}

FileID string

Type File



type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaInputJSONDelta struct{…}

PartialJSON string

Type InputJSONDelta



type BetaInputTokensClearAtLeast struct{…}

Type InputTokens

Value int64



type BetaInputTokensTrigger struct{…}

Type InputTokens

Value int64



type BetaIterationsUsage []BetaIterationsUsageItemUnion

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



type BetaMessageIterationUsage struct{…}

Token usage for a sampling iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type Message

Usage for a sampling iteration



type BetaCompactionIterationUsage struct{…}

Token usage for a compaction iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

Type Compaction

Usage for a compaction iteration



type BetaAdvisorMessageIterationUsage struct{…}

Token usage for an advisor sub-inference iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type AdvisorMessage

Usage for an advisor sub-inference iteration



type BetaFallbackMessageIterationUsage struct{…}

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type FallbackMessage

Usage for the fallback-model attempt that served the response



type BetaJSONOutputFormat struct{…}

Schema map[string, any]

The JSON schema of the format

Type JSONSchema



type BetaMCPToolConfig struct{…}

Configuration for a specific tool in an MCP toolset.

DeferLoading boolOptional

Enabled boolOptional



type BetaMCPToolDefaultConfig struct{…}

Default configuration for tools in an MCP toolset.

DeferLoading boolOptional

Enabled boolOptional



type BetaMCPToolResultBlock struct{…}



Content BetaMCPToolResultBlockContentUnion

One of the following:

string



type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent [][BetaTextBlock](api/beta/messages.md)



Citations [][BetaTextCitationUnion](api/beta/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

IsError bool

ToolUseID string

Type MCPToolResult



type BetaMCPToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

The name of the MCP tool

ServerName string

The name of the MCP server

Type MCPToolUse



type BetaMCPToolUseBlockParamResp struct{…}

ID string

Input map[string, any]

Name string

ServerName string

The name of the MCP server

Type MCPToolUse



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaMCPToolset struct{…}

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

MCPServerName string

Name of the MCP server to configure tools for

Type MCPToolset



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Configs map[string, [BetaMCPToolConfig](api/beta/messages.md)]Optional

Configuration overrides for specific tools, keyed by tool name

DeferLoading boolOptional

Enabled boolOptional



DefaultConfig [BetaMCPToolDefaultConfig](api/beta/messages.md)Optional

Default configuration applied to all tools from this server

DeferLoading boolOptional

Enabled boolOptional



type BetaMemoryTool20250818 struct{…}



Name Memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Memory20250818



AllowedCallers []stringOptional

One of the following:

const BetaMemoryTool20250818AllowedCallerDirect BetaMemoryTool20250818AllowedCaller = "direct"

const BetaMemoryTool20250818AllowedCallerCodeExecution20250825 BetaMemoryTool20250818AllowedCaller = "code\_execution\_20250825"

const BetaMemoryTool20250818AllowedCallerCodeExecution20260120 BetaMemoryTool20250818AllowedCaller = "code\_execution\_20260120"

const BetaMemoryTool20250818AllowedCallerCodeExecution20260521 BetaMemoryTool20250818AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaMemoryTool20250818CommandUnion interface{…}

One of the following:



type BetaMemoryTool20250818ViewCommand struct{…}

Command View

Command type identifier

Path string

Path to directory or file to view

ViewRange []int64Optional

Optional line range for viewing specific lines



type BetaMemoryTool20250818CreateCommand struct{…}

Command Create

Command type identifier

FileText string

Content to write to the file

Path string

Path where the file should be created



type BetaMemoryTool20250818StrReplaceCommand struct{…}

Command StrReplace

Command type identifier

NewStr string

Text to replace with

OldStr string

Text to search for and replace

Path string

Path to the file where text should be replaced



type BetaMemoryTool20250818InsertCommand struct{…}

Command Insert

Command type identifier

InsertLine int64

Line number where text should be inserted

InsertText string

Text to insert at the specified line

Path string

Path to the file where text should be inserted



type BetaMemoryTool20250818DeleteCommand struct{…}

Command Delete

Command type identifier

Path string

Path to the file or directory to delete



type BetaMemoryTool20250818RenameCommand struct{…}

Command Rename

Command type identifier

NewPath string

New path for the file or directory

OldPath string

Current path of the file or directory



type BetaMemoryTool20250818CreateCommand struct{…}

Command Create

Command type identifier

FileText string

Content to write to the file

Path string

Path where the file should be created



type BetaMemoryTool20250818DeleteCommand struct{…}

Command Delete

Command type identifier

Path string

Path to the file or directory to delete



type BetaMemoryTool20250818InsertCommand struct{…}

Command Insert

Command type identifier

InsertLine int64

Line number where text should be inserted

InsertText string

Text to insert at the specified line

Path string

Path to the file where text should be inserted



type BetaMemoryTool20250818RenameCommand struct{…}

Command Rename

Command type identifier

NewPath string

New path for the file or directory

OldPath string

Current path of the file or directory



type BetaMemoryTool20250818StrReplaceCommand struct{…}

Command StrReplace

Command type identifier

NewStr string

Text to replace with

OldStr string

Text to search for and replace

Path string

Path to the file where text should be replaced



type BetaMemoryTool20250818ViewCommand struct{…}

Command View

Command type identifier

Path string

Path to directory or file to view

ViewRange []int64Optional

Optional line range for viewing specific lines



type BetaMessage struct{…}



ID string

Unique object identifier.

The format and length of IDs may change over time.



Container [BetaContainer](api/beta/messages.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



Skills [][BetaSkill](api/beta/messages.md)

Skills loaded in the container

SkillID string

Skill ID



Type BetaSkillType

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

const BetaSkillTypeAnthropic BetaSkillType = "anthropic"

const BetaSkillTypeCustom BetaSkillType = "custom"

Version string

Skill version or 'latest' for most recent version



Content [][BetaContentBlockUnion](api/beta/messages.md)

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

type BetaTextBlock struct{…}



Citations [][BetaTextCitationUnion](api/beta/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

type BetaThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking



type BetaRedactedThinkingBlock struct{…}

Data string

Type RedactedThinking



type BetaToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse



Caller BetaToolUseBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaServerToolUseBlock struct{…}

ID string

Input map[string, any]



Name BetaServerToolUseBlockName

One of the following:

const BetaServerToolUseBlockNameAdvisor BetaServerToolUseBlockName = "advisor"

const BetaServerToolUseBlockNameWebSearch BetaServerToolUseBlockName = "web\_search"

const BetaServerToolUseBlockNameWebFetch BetaServerToolUseBlockName = "web\_fetch"

const BetaServerToolUseBlockNameCodeExecution BetaServerToolUseBlockName = "code\_execution"

const BetaServerToolUseBlockNameBashCodeExecution BetaServerToolUseBlockName = "bash\_code\_execution"

const BetaServerToolUseBlockNameTextEditorCodeExecution BetaServerToolUseBlockName = "text\_editor\_code\_execution"

const BetaServerToolUseBlockNameToolSearchToolRegex BetaServerToolUseBlockName = "tool\_search\_tool\_regex"

const BetaServerToolUseBlockNameToolSearchToolBm25 BetaServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse



Caller BetaServerToolUseBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebSearchToolResultBlock struct{…}



Content [BetaWebSearchToolResultBlockContentUnion](api/beta/messages.md)

One of the following:



type BetaWebSearchToolResultError struct{…}



ErrorCode [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "request\_too\_large"

Type WebSearchToolResultError



type BetaWebSearchToolResultBlockContentArray [][BetaWebSearchResultBlock](api/beta/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult



Caller BetaWebSearchToolResultBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebFetchToolResultBlock struct{…}



Content BetaWebFetchToolResultBlockContentUnion

One of the following:



type BetaWebFetchToolResultErrorBlock struct{…}



ErrorCode [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotInPriorContext [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_in\_prior\_context"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unavailable"

Type WebFetchToolResultError



type BetaWebFetchBlock struct{…}



Content [BetaDocumentBlock](api/beta/messages.md)



Citations [BetaCitationConfig](api/beta/messages.md)

Citation configuration for the document

Enabled bool



Source BetaDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

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

Caller BetaWebFetchToolResultBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaAdvisorToolResultBlock struct{…}



Content BetaAdvisorToolResultBlockContentUnion

One of the following:



type BetaAdvisorToolResultError struct{…}



ErrorCode BetaAdvisorToolResultErrorErrorCode

One of the following:

const BetaAdvisorToolResultErrorErrorCodeMaxUsesExceeded BetaAdvisorToolResultErrorErrorCode = "max\_uses\_exceeded"

const BetaAdvisorToolResultErrorErrorCodePromptTooLong BetaAdvisorToolResultErrorErrorCode = "prompt\_too\_long"

const BetaAdvisorToolResultErrorErrorCodeTooManyRequests BetaAdvisorToolResultErrorErrorCode = "too\_many\_requests"

const BetaAdvisorToolResultErrorErrorCodeOverloaded BetaAdvisorToolResultErrorErrorCode = "overloaded"

const BetaAdvisorToolResultErrorErrorCodeUnavailable BetaAdvisorToolResultErrorErrorCode = "unavailable"

const BetaAdvisorToolResultErrorErrorCodeExecutionTimeExceeded BetaAdvisorToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaAdvisorToolResultErrorErrorCodeModelNotFound BetaAdvisorToolResultErrorErrorCode = "model\_not\_found"

Type AdvisorToolResultError



type BetaAdvisorResultBlock struct{…}

StopReason string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

Text string

Type AdvisorResult



type BetaAdvisorRedactedResultBlock struct{…}

EncryptedContent string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

StopReason string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

Type AdvisorRedactedResult

ToolUseID string

Type AdvisorToolResult



type BetaCodeExecutionToolResultBlock struct{…}



Content [BetaCodeExecutionToolResultBlockContentUnion](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type BetaCodeExecutionToolResultError struct{…}



ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type BetaCodeExecutionResultBlock struct{…}



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type BetaEncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



type BetaBashCodeExecutionToolResultBlock struct{…}



Content BetaBashCodeExecutionToolResultBlockContentUnion

One of the following:



type BetaBashCodeExecutionToolResultError struct{…}



ErrorCode BetaBashCodeExecutionToolResultErrorErrorCode

One of the following:

const BetaBashCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaBashCodeExecutionToolResultErrorErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaBashCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaBashCodeExecutionToolResultErrorErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorErrorCode = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError



type BetaBashCodeExecutionResultBlock struct{…}



Content [][BetaBashCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



type BetaTextEditorCodeExecutionToolResultBlock struct{…}



Content BetaTextEditorCodeExecutionToolResultBlockContentUnion

One of the following:



type BetaTextEditorCodeExecutionToolResultError struct{…}



ErrorCode BetaTextEditorCodeExecutionToolResultErrorErrorCode

One of the following:

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorErrorCode = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type BetaTextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType BetaTextEditorCodeExecutionViewResultBlockFileType

One of the following:

const BetaTextEditorCodeExecutionViewResultBlockFileTypeText BetaTextEditorCodeExecutionViewResultBlockFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockFileTypeImage BetaTextEditorCodeExecutionViewResultBlockFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockFileTypePDF BetaTextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type BetaTextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type BetaTextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult



type BetaToolSearchToolResultBlock struct{…}



Content BetaToolSearchToolResultBlockContentUnion

One of the following:



type BetaToolSearchToolResultError struct{…}



ErrorCode BetaToolSearchToolResultErrorErrorCode

One of the following:

const BetaToolSearchToolResultErrorErrorCodeInvalidToolInput BetaToolSearchToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaToolSearchToolResultErrorErrorCodeUnavailable BetaToolSearchToolResultErrorErrorCode = "unavailable"

const BetaToolSearchToolResultErrorErrorCodeTooManyRequests BetaToolSearchToolResultErrorErrorCode = "too\_many\_requests"

const BetaToolSearchToolResultErrorErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorErrorCode = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type BetaToolSearchToolSearchResultBlock struct{…}



ToolReferences [][BetaToolReferenceBlock](api/beta/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



type BetaMCPToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

The name of the MCP tool

ServerName string

The name of the MCP server

Type MCPToolUse



type BetaMCPToolResultBlock struct{…}



Content BetaMCPToolResultBlockContentUnion

One of the following:

string



type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent [][BetaTextBlock](api/beta/messages.md)



Citations [][BetaTextCitationUnion](api/beta/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

IsError bool

ToolUseID string

Type MCPToolResult



type BetaContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload



type BetaCompactionBlock struct{…}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Content string

Summary of compacted content, or null if compaction failed

EncryptedContent string

Opaque metadata from prior compaction, to be round-tripped verbatim

Type Compaction



type BetaFallbackBlock struct{…}

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



From [BetaFallbackInfo](api/beta/messages.md)

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

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

To [BetaFallbackInfo](api/beta/messages.md)

The fallback model producing the content that follows this block. Its `model` is always the canonical id.

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

Trigger [BetaFallbackRefusalTrigger](api/beta/messages.md)

What caused the `from` model to hand over at this hop.



Category BetaFallbackRefusalTriggerCategory

The policy category that triggered a refusal.

One of the following:

const BetaFallbackRefusalTriggerCategoryCyber BetaFallbackRefusalTriggerCategory = "cyber"

const BetaFallbackRefusalTriggerCategoryBio BetaFallbackRefusalTriggerCategory = "bio"

const BetaFallbackRefusalTriggerCategoryFrontierLLM BetaFallbackRefusalTriggerCategory = "frontier\_llm"

const BetaFallbackRefusalTriggerCategoryReasoningExtraction BetaFallbackRefusalTriggerCategory = "reasoning\_extraction"

const BetaFallbackRefusalTriggerCategoryMilitaryWeapons BetaFallbackRefusalTriggerCategory = "military\_weapons"

Type Refusal

Type Fallback



ContextManagement [BetaContextManagementResponse](api/beta/messages.md)

Context management response.

Information about context management strategies applied during the request.



AppliedEdits []BetaContextManagementResponseAppliedEditUnion

List of context management edits that were applied.

One of the following:



type BetaClearToolUses20250919EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

ClearedToolUses int64

Number of tool uses that were cleared.

Type ClearToolUses20250919

The type of context management edit applied.



type BetaClearThinking20251015EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

ClearedThinkingTurns int64

Number of thinking turns that were cleared.

Type ClearThinking20251015

The type of context management edit applied.



Diagnostics [BetaDiagnostics](api/beta/messages.md)

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



CacheMissReason BetaDiagnosticsCacheMissReasonUnion

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



type BetaCacheMissModelChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type ModelChanged



type BetaCacheMissSystemChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type SystemChanged



type BetaCacheMissToolsChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type ToolsChanged



type BetaCacheMissMessagesChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type MessagesChanged



type BetaCacheMissPreviousMessageNotFound struct{…}

Type PreviousMessageNotFound



type BetaCacheMissUnavailable struct{…}

Type Unavailable

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

StopDetails [BetaRefusalStopDetails](api/beta/messages.md)

Structured information about a refusal.



Category BetaRefusalStopDetailsCategory

The policy category that triggered a refusal.

One of the following:

const BetaRefusalStopDetailsCategoryCyber BetaRefusalStopDetailsCategory = "cyber"

const BetaRefusalStopDetailsCategoryBio BetaRefusalStopDetailsCategory = "bio"

const BetaRefusalStopDetailsCategoryFrontierLLM BetaRefusalStopDetailsCategory = "frontier\_llm"

const BetaRefusalStopDetailsCategoryReasoningExtraction BetaRefusalStopDetailsCategory = "reasoning\_extraction"

const BetaRefusalStopDetailsCategoryMilitaryWeapons BetaRefusalStopDetailsCategory = "military\_weapons"



Explanation string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



FallbackCreditToken string

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



FallbackHasPrefillClaim bool

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

RecommendedModel string

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

Type Refusal



StopReason [BetaStopReason](api/beta/messages.md)

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

const BetaStopReasonEndTurn [BetaStopReason](api/beta/messages.md) = "end\_turn"

const BetaStopReasonMaxTokens [BetaStopReason](api/beta/messages.md) = "max\_tokens"

const BetaStopReasonStopSequence [BetaStopReason](api/beta/messages.md) = "stop\_sequence"

const BetaStopReasonToolUse [BetaStopReason](api/beta/messages.md) = "tool\_use"

const BetaStopReasonPauseTurn [BetaStopReason](api/beta/messages.md) = "pause\_turn"

const BetaStopReasonCompaction [BetaStopReason](api/beta/messages.md) = "compaction"

const BetaStopReasonRefusal [BetaStopReason](api/beta/messages.md) = "refusal"

const BetaStopReasonModelContextWindowExceeded [BetaStopReason](api/beta/messages.md) = "model\_context\_window\_exceeded"



StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



Type Message

Object type.

For Messages, this is always `"message"`.



Usage [BetaUsage](api/beta/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

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



Iterations [BetaIterationsUsage](api/beta/messages.md)

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



type BetaMessageIterationUsage struct{…}

Token usage for a sampling iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type Message

Usage for a sampling iteration



type BetaCompactionIterationUsage struct{…}

Token usage for a compaction iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

Type Compaction

Usage for a compaction iteration



type BetaAdvisorMessageIterationUsage struct{…}

Token usage for an advisor sub-inference iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type AdvisorMessage

Usage for an advisor sub-inference iteration



type BetaFallbackMessageIterationUsage struct{…}

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type FallbackMessage

Usage for the fallback-model attempt that served the response

OutputTokens int64

The number of output tokens which were used.



OutputTokensDetails [BetaOutputTokensDetails](api/beta/messages.md)

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

ServerToolUse [BetaServerToolUsage](api/beta/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



ServiceTier BetaUsageServiceTier

If the request used the priority, standard, or batch tier.

One of the following:

const BetaUsageServiceTierStandard BetaUsageServiceTier = "standard"

const BetaUsageServiceTierPriority BetaUsageServiceTier = "priority"

const BetaUsageServiceTierBatch BetaUsageServiceTier = "batch"



Speed BetaUsageSpeed

The inference speed mode used for this request.

One of the following:

const BetaUsageSpeedStandard BetaUsageSpeed = "standard"

const BetaUsageSpeedFast BetaUsageSpeed = "fast"



type BetaMessageDeltaUsage struct{…}

CacheCreationInputTokens int64

The cumulative number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The cumulative number of input tokens read from the cache.

InputTokens int64

The cumulative number of input tokens which were used.



Iterations [BetaIterationsUsage](api/beta/messages.md)

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



type BetaMessageIterationUsage struct{…}

Token usage for a sampling iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type Message

Usage for a sampling iteration



type BetaCompactionIterationUsage struct{…}

Token usage for a compaction iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

Type Compaction

Usage for a compaction iteration



type BetaAdvisorMessageIterationUsage struct{…}

Token usage for an advisor sub-inference iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type AdvisorMessage

Usage for an advisor sub-inference iteration



type BetaFallbackMessageIterationUsage struct{…}

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type FallbackMessage

Usage for the fallback-model attempt that served the response

OutputTokens int64

The cumulative number of output tokens which were used.



OutputTokensDetails [BetaOutputTokensDetails](api/beta/messages.md)

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

ServerToolUse [BetaServerToolUsage](api/beta/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



type BetaMessageIterationUsage struct{…}

Token usage for a sampling iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type Message

Usage for a sampling iteration



type BetaMessageParamResp struct{…}



Content [][BetaContentBlockParamUnionResp](api/beta/messages.md)

One of the following:



[][BetaContentBlockParamUnionResp](api/beta/messages.md)

One of the following:



type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaRequestDocumentBlock struct{…}



Source BetaRequestDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text



type BetaContentBlockSource struct{…}



Content BetaContentBlockSourceContentUnion

One of the following:

string



[][BetaContentBlockSourceContentUnion](api/beta/messages.md)

One of the following:



type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type Content



type BetaURLPDFSource struct{…}

Type URL

URL string



type BetaFileDocumentSource struct{…}

FileID string

Type File

Type Document



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

Enabled boolOptional

Context stringOptional

Title stringOptional



type BetaSearchResultBlockParamResp struct{…}



Content [][BetaTextBlockParamResp](api/beta/messages.md)

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

Enabled boolOptional



type BetaThinkingBlockParamResp struct{…}

Signature string

Thinking string

Type Thinking



type BetaRedactedThinkingBlockParamResp struct{…}

Data string

Type RedactedThinking



type BetaToolUseBlockParamResp struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Caller BetaToolUseBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaToolResultBlockParamResp struct{…}

ToolUseID string

Type ToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Content []BetaToolResultBlockParamContentUnionRespOptional

One of the following:



[]BetaToolResultBlockParamContentUnionResp

One of the following:



type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaSearchResultBlockParamResp struct{…}



Content [][BetaTextBlockParamResp](api/beta/messages.md)

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

Enabled boolOptional



type BetaRequestDocumentBlock struct{…}



Source BetaRequestDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text



type BetaContentBlockSource struct{…}



Content BetaContentBlockSourceContentUnion

One of the following:

string



[][BetaContentBlockSourceContentUnion](api/beta/messages.md)

One of the following:



type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type Content



type BetaURLPDFSource struct{…}

Type URL

URL string



type BetaFileDocumentSource struct{…}

FileID string

Type File

Type Document



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

Enabled boolOptional

Context stringOptional

Title stringOptional



type BetaToolReferenceBlockParamResp struct{…}

Tool reference block that can be included in tool\_result content.

ToolName string

Type ToolReference



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

IsError boolOptional



type BetaServerToolUseBlockParamResp struct{…}

ID string

Input map[string, any]



Name BetaServerToolUseBlockParamName

One of the following:

const BetaServerToolUseBlockParamNameAdvisor BetaServerToolUseBlockParamName = "advisor"

const BetaServerToolUseBlockParamNameWebSearch BetaServerToolUseBlockParamName = "web\_search"

const BetaServerToolUseBlockParamNameWebFetch BetaServerToolUseBlockParamName = "web\_fetch"

const BetaServerToolUseBlockParamNameCodeExecution BetaServerToolUseBlockParamName = "code\_execution"

const BetaServerToolUseBlockParamNameBashCodeExecution BetaServerToolUseBlockParamName = "bash\_code\_execution"

const BetaServerToolUseBlockParamNameTextEditorCodeExecution BetaServerToolUseBlockParamName = "text\_editor\_code\_execution"

const BetaServerToolUseBlockParamNameToolSearchToolRegex BetaServerToolUseBlockParamName = "tool\_search\_tool\_regex"

const BetaServerToolUseBlockParamNameToolSearchToolBm25 BetaServerToolUseBlockParamName = "tool\_search\_tool\_bm25"

Type ServerToolUse



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Caller BetaServerToolUseBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebSearchToolResultBlockParamResp struct{…}



Content [BetaWebSearchToolResultBlockParamContentUnionResp](api/beta/messages.md)

One of the following:



[][BetaWebSearchResultBlockParamResp](api/beta/messages.md)

EncryptedContent string

Title string

Type WebSearchResult

URL string

PageAge stringOptional



type BetaWebSearchToolRequestError struct{…}



ErrorCode [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "request\_too\_large"

Type WebSearchToolResultError

ToolUseID string

Type WebSearchToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Caller BetaWebSearchToolResultBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebFetchToolResultBlockParamResp struct{…}



Content BetaWebFetchToolResultBlockParamContentUnionResp

One of the following:



type BetaWebFetchToolResultErrorBlockParamResp struct{…}



ErrorCode [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotInPriorContext [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_in\_prior\_context"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unavailable"

Type WebFetchToolResultError



type BetaWebFetchBlockParamResp struct{…}



Content [BetaRequestDocumentBlock](api/beta/messages.md)



Source BetaRequestDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text



type BetaContentBlockSource struct{…}



Content BetaContentBlockSourceContentUnion

One of the following:

string



[][BetaContentBlockSourceContentUnion](api/beta/messages.md)

One of the following:



type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type Content



type BetaURLPDFSource struct{…}

Type URL

URL string



type BetaFileDocumentSource struct{…}

FileID string

Type File

Type Document



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

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

CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Caller BetaWebFetchToolResultBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaAdvisorToolResultBlockParamResp struct{…}



Content BetaAdvisorToolResultBlockParamContentUnionResp

One of the following:



type BetaAdvisorToolResultErrorParamResp struct{…}



ErrorCode BetaAdvisorToolResultErrorParamErrorCode

One of the following:

const BetaAdvisorToolResultErrorParamErrorCodeMaxUsesExceeded BetaAdvisorToolResultErrorParamErrorCode = "max\_uses\_exceeded"

const BetaAdvisorToolResultErrorParamErrorCodePromptTooLong BetaAdvisorToolResultErrorParamErrorCode = "prompt\_too\_long"

const BetaAdvisorToolResultErrorParamErrorCodeTooManyRequests BetaAdvisorToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaAdvisorToolResultErrorParamErrorCodeOverloaded BetaAdvisorToolResultErrorParamErrorCode = "overloaded"

const BetaAdvisorToolResultErrorParamErrorCodeUnavailable BetaAdvisorToolResultErrorParamErrorCode = "unavailable"

const BetaAdvisorToolResultErrorParamErrorCodeExecutionTimeExceeded BetaAdvisorToolResultErrorParamErrorCode = "execution\_time\_exceeded"

const BetaAdvisorToolResultErrorParamErrorCodeModelNotFound BetaAdvisorToolResultErrorParamErrorCode = "model\_not\_found"

Type AdvisorToolResultError



type BetaAdvisorResultBlockParamResp struct{…}

Text string

Type AdvisorResult

StopReason stringOptional



type BetaAdvisorRedactedResultBlockParamResp struct{…}

EncryptedContent string

Opaque blob produced by a prior response; must be round-tripped verbatim.

Type AdvisorRedactedResult

StopReason stringOptional

ToolUseID string

Type AdvisorToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaCodeExecutionToolResultBlockParamResp struct{…}



Content [BetaCodeExecutionToolResultBlockParamContentUnionResp](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type BetaCodeExecutionToolResultErrorParamResp struct{…}



ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type BetaCodeExecutionResultBlockParamResp struct{…}



Content [][BetaCodeExecutionOutputBlockParamResp](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type BetaEncryptedCodeExecutionResultBlockParamResp struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][BetaCodeExecutionOutputBlockParamResp](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaBashCodeExecutionToolResultBlockParamResp struct{…}



Content BetaBashCodeExecutionToolResultBlockParamContentUnionResp

One of the following:



type BetaBashCodeExecutionToolResultErrorParamResp struct{…}



ErrorCode BetaBashCodeExecutionToolResultErrorParamErrorCode

One of the following:

const BetaBashCodeExecutionToolResultErrorParamErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorParamErrorCode = "invalid\_tool\_input"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorParamErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorParamErrorCode = "execution\_time\_exceeded"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorParamErrorCode = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError



type BetaBashCodeExecutionResultBlockParamResp struct{…}



Content [][BetaBashCodeExecutionOutputBlockParamResp](api/beta/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaTextEditorCodeExecutionToolResultBlockParamResp struct{…}



Content BetaTextEditorCodeExecutionToolResultBlockParamContentUnionResp

One of the following:



type BetaTextEditorCodeExecutionToolResultErrorParamResp struct{…}



ErrorCode BetaTextEditorCodeExecutionToolResultErrorParamErrorCode

One of the following:

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "invalid\_tool\_input"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "execution\_time\_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "file\_not\_found"

Type TextEditorCodeExecutionToolResultError

ErrorMessage stringOptional



type BetaTextEditorCodeExecutionViewResultBlockParamResp struct{…}

Content string



FileType BetaTextEditorCodeExecutionViewResultBlockParamFileType

One of the following:

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypeText BetaTextEditorCodeExecutionViewResultBlockParamFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypeImage BetaTextEditorCodeExecutionViewResultBlockParamFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypePDF BetaTextEditorCodeExecutionViewResultBlockParamFileType = "pdf"

Type TextEditorCodeExecutionViewResult

NumLines int64Optional

StartLine int64Optional

TotalLines int64Optional



type BetaTextEditorCodeExecutionCreateResultBlockParamResp struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type BetaTextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}

Type TextEditorCodeExecutionStrReplaceResult

Lines []stringOptional

NewLines int64Optional

NewStart int64Optional

OldLines int64Optional

OldStart int64Optional

ToolUseID string

Type TextEditorCodeExecutionToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaToolSearchToolResultBlockParamResp struct{…}



Content BetaToolSearchToolResultBlockParamContentUnionResp

One of the following:



type BetaToolSearchToolResultErrorParamResp struct{…}



ErrorCode BetaToolSearchToolResultErrorParamErrorCode

One of the following:

const BetaToolSearchToolResultErrorParamErrorCodeInvalidToolInput BetaToolSearchToolResultErrorParamErrorCode = "invalid\_tool\_input"

const BetaToolSearchToolResultErrorParamErrorCodeUnavailable BetaToolSearchToolResultErrorParamErrorCode = "unavailable"

const BetaToolSearchToolResultErrorParamErrorCodeTooManyRequests BetaToolSearchToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaToolSearchToolResultErrorParamErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorParamErrorCode = "execution\_time\_exceeded"

Type ToolSearchToolResultError

ErrorMessage stringOptional



type BetaToolSearchToolSearchResultBlockParamResp struct{…}



ToolReferences [][BetaToolReferenceBlockParamResp](api/beta/messages.md)

ToolName string

Type ToolReference



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaMCPToolUseBlockParamResp struct{…}

ID string

Input map[string, any]

Name string

ServerName string

The name of the MCP server

Type MCPToolUse



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaRequestMCPToolResultBlockParamResp struct{…}

ToolUseID string

Type MCPToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Content BetaRequestMCPToolResultBlockParamContentUnionRespOptional

One of the following:

string



[][BetaTextBlockParamResp](api/beta/messages.md)

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

IsError boolOptional



type BetaContainerUploadBlockParamResp struct{…}

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

FileID string

Type ContainerUpload



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaCompactionBlockParamResp struct{…}

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

Type Compaction



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Content stringOptional

Summary of previously compacted content, or null if compaction failed

EncryptedContent stringOptional

Opaque metadata from prior compaction, to be round-tripped verbatim



type BetaMidConversationSystemBlockParamResp struct{…}

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



Content [][BetaTextBlockParamResp](api/beta/messages.md)

System instruction text blocks.

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaFallbackBlockParamResp struct{…}

A `fallback` block echoed back from a prior response.

Accepted in `messages[].content` and not rendered into the prompt; not
validated against the request's `fallbacks` chain or top-level `model`.

Echo the assistant turn back verbatim, including this block in its
original position. The block marks the boundary between content produced
before and after a fallback hop, and the server relies on that boundary
to validate the turn: when thinking runs flank the boundary, omitting
the block merges them into one span the server cannot validate (the
request is rejected), and moving it into the middle of a single run is
likewise rejected; between non-thinking blocks the block's placement has
no validation effect.



From [BetaFallbackInfoParamResp](api/beta/messages.md)

Identifies one hop of a fallback transition.

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

To [BetaFallbackInfoParamResp](api/beta/messages.md)

Identifies one hop of a fallback transition.

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

Type Fallback

Trigger anyOptional

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



Role BetaMessageParamRole

One of the following:

const BetaMessageParamRoleUser BetaMessageParamRole = "user"

const BetaMessageParamRoleAssistant BetaMessageParamRole = "assistant"

const BetaMessageParamRoleSystem BetaMessageParamRole = "system"



type BetaMessageTokensCount struct{…}



ContextManagement [BetaCountTokensContextManagementResponse](api/beta/messages.md)

Information about context management applied to the message.

OriginalInputTokens int64

The original token count before context management was applied

InputTokens int64

The total number of tokens across the provided list of messages, system prompt, and tools.



type BetaMetadata struct{…}



UserID stringOptional

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



type BetaMidConversationSystemBlockParamResp struct{…}

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



Content [][BetaTextBlockParamResp](api/beta/messages.md)

System instruction text blocks.

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaOutputConfig struct{…}



Effort BetaOutputConfigEffortOptional

All possible effort levels.

One of the following:

const BetaOutputConfigEffortLow BetaOutputConfigEffort = "low"

const BetaOutputConfigEffortMedium BetaOutputConfigEffort = "medium"

const BetaOutputConfigEffortHigh BetaOutputConfigEffort = "high"

const BetaOutputConfigEffortXhigh BetaOutputConfigEffort = "xhigh"

const BetaOutputConfigEffortMax BetaOutputConfigEffort = "max"



Format [BetaJSONOutputFormat](api/beta/messages.md)Optional

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

Schema map[string, any]

The JSON schema of the format

Type JSONSchema



TaskBudget [BetaTokenTaskBudget](api/beta/messages.md)Optional

User-configurable total token budget across contexts.

Total int64

Total token budget across all contexts in the session.

Type Tokens

The budget type. Currently only 'tokens' is supported.

Remaining int64Optional

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



type BetaOutputTokensDetails struct{…}

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

type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text



type BetaRawContentBlockDeltaUnion interface{…}

One of the following:



type BetaTextDelta struct{…}

Text string

Type TextDelta



type BetaInputJSONDelta struct{…}

PartialJSON string

Type InputJSONDelta



type BetaCitationsDelta struct{…}



Citation BetaCitationsDeltaCitationUnion

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

type BetaThinkingDelta struct{…}

EstimatedTokens int64

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

Thinking string

Type ThinkingDelta



type BetaSignatureDelta struct{…}

Signature string

Type SignatureDelta



type BetaCompactionContentBlockDelta struct{…}

Content string

EncryptedContent string

Opaque metadata from prior compaction, to be round-tripped verbatim

Type CompactionDelta



type BetaRawContentBlockDeltaEvent struct{…}



Delta [BetaRawContentBlockDeltaUnion](api/beta/messages.md)

One of the following:



type BetaTextDelta struct{…}

Text string

Type TextDelta



type BetaInputJSONDelta struct{…}

PartialJSON string

Type InputJSONDelta



type BetaCitationsDelta struct{…}



Citation BetaCitationsDeltaCitationUnion

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

type BetaThinkingDelta struct{…}

EstimatedTokens int64

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

Thinking string

Type ThinkingDelta



type BetaSignatureDelta struct{…}

Signature string

Type SignatureDelta



type BetaCompactionContentBlockDelta struct{…}

Content string

EncryptedContent string

Opaque metadata from prior compaction, to be round-tripped verbatim

Type CompactionDelta

Index int64

Type ContentBlockDelta



type BetaRawContentBlockStartEvent struct{…}



ContentBlock BetaRawContentBlockStartEventContentBlockUnion

Response model for a file uploaded to the container.

One of the following:



type BetaTextBlock struct{…}



Citations [][BetaTextCitationUnion](api/beta/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

type BetaThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking



type BetaRedactedThinkingBlock struct{…}

Data string

Type RedactedThinking



type BetaToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse



Caller BetaToolUseBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaServerToolUseBlock struct{…}

ID string

Input map[string, any]



Name BetaServerToolUseBlockName

One of the following:

const BetaServerToolUseBlockNameAdvisor BetaServerToolUseBlockName = "advisor"

const BetaServerToolUseBlockNameWebSearch BetaServerToolUseBlockName = "web\_search"

const BetaServerToolUseBlockNameWebFetch BetaServerToolUseBlockName = "web\_fetch"

const BetaServerToolUseBlockNameCodeExecution BetaServerToolUseBlockName = "code\_execution"

const BetaServerToolUseBlockNameBashCodeExecution BetaServerToolUseBlockName = "bash\_code\_execution"

const BetaServerToolUseBlockNameTextEditorCodeExecution BetaServerToolUseBlockName = "text\_editor\_code\_execution"

const BetaServerToolUseBlockNameToolSearchToolRegex BetaServerToolUseBlockName = "tool\_search\_tool\_regex"

const BetaServerToolUseBlockNameToolSearchToolBm25 BetaServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse



Caller BetaServerToolUseBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebSearchToolResultBlock struct{…}



Content [BetaWebSearchToolResultBlockContentUnion](api/beta/messages.md)

One of the following:



type BetaWebSearchToolResultError struct{…}



ErrorCode [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "request\_too\_large"

Type WebSearchToolResultError



type BetaWebSearchToolResultBlockContentArray [][BetaWebSearchResultBlock](api/beta/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult



Caller BetaWebSearchToolResultBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebFetchToolResultBlock struct{…}



Content BetaWebFetchToolResultBlockContentUnion

One of the following:



type BetaWebFetchToolResultErrorBlock struct{…}



ErrorCode [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotInPriorContext [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_in\_prior\_context"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unavailable"

Type WebFetchToolResultError



type BetaWebFetchBlock struct{…}



Content [BetaDocumentBlock](api/beta/messages.md)



Citations [BetaCitationConfig](api/beta/messages.md)

Citation configuration for the document

Enabled bool



Source BetaDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

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

Caller BetaWebFetchToolResultBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaAdvisorToolResultBlock struct{…}



Content BetaAdvisorToolResultBlockContentUnion

One of the following:



type BetaAdvisorToolResultError struct{…}



ErrorCode BetaAdvisorToolResultErrorErrorCode

One of the following:

const BetaAdvisorToolResultErrorErrorCodeMaxUsesExceeded BetaAdvisorToolResultErrorErrorCode = "max\_uses\_exceeded"

const BetaAdvisorToolResultErrorErrorCodePromptTooLong BetaAdvisorToolResultErrorErrorCode = "prompt\_too\_long"

const BetaAdvisorToolResultErrorErrorCodeTooManyRequests BetaAdvisorToolResultErrorErrorCode = "too\_many\_requests"

const BetaAdvisorToolResultErrorErrorCodeOverloaded BetaAdvisorToolResultErrorErrorCode = "overloaded"

const BetaAdvisorToolResultErrorErrorCodeUnavailable BetaAdvisorToolResultErrorErrorCode = "unavailable"

const BetaAdvisorToolResultErrorErrorCodeExecutionTimeExceeded BetaAdvisorToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaAdvisorToolResultErrorErrorCodeModelNotFound BetaAdvisorToolResultErrorErrorCode = "model\_not\_found"

Type AdvisorToolResultError



type BetaAdvisorResultBlock struct{…}

StopReason string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

Text string

Type AdvisorResult



type BetaAdvisorRedactedResultBlock struct{…}

EncryptedContent string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

StopReason string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

Type AdvisorRedactedResult

ToolUseID string

Type AdvisorToolResult



type BetaCodeExecutionToolResultBlock struct{…}



Content [BetaCodeExecutionToolResultBlockContentUnion](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type BetaCodeExecutionToolResultError struct{…}



ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type BetaCodeExecutionResultBlock struct{…}



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type BetaEncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



type BetaBashCodeExecutionToolResultBlock struct{…}



Content BetaBashCodeExecutionToolResultBlockContentUnion

One of the following:



type BetaBashCodeExecutionToolResultError struct{…}



ErrorCode BetaBashCodeExecutionToolResultErrorErrorCode

One of the following:

const BetaBashCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaBashCodeExecutionToolResultErrorErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaBashCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaBashCodeExecutionToolResultErrorErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorErrorCode = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError



type BetaBashCodeExecutionResultBlock struct{…}



Content [][BetaBashCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



type BetaTextEditorCodeExecutionToolResultBlock struct{…}



Content BetaTextEditorCodeExecutionToolResultBlockContentUnion

One of the following:



type BetaTextEditorCodeExecutionToolResultError struct{…}



ErrorCode BetaTextEditorCodeExecutionToolResultErrorErrorCode

One of the following:

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorErrorCode = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type BetaTextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType BetaTextEditorCodeExecutionViewResultBlockFileType

One of the following:

const BetaTextEditorCodeExecutionViewResultBlockFileTypeText BetaTextEditorCodeExecutionViewResultBlockFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockFileTypeImage BetaTextEditorCodeExecutionViewResultBlockFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockFileTypePDF BetaTextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type BetaTextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type BetaTextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult



type BetaToolSearchToolResultBlock struct{…}



Content BetaToolSearchToolResultBlockContentUnion

One of the following:



type BetaToolSearchToolResultError struct{…}



ErrorCode BetaToolSearchToolResultErrorErrorCode

One of the following:

const BetaToolSearchToolResultErrorErrorCodeInvalidToolInput BetaToolSearchToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaToolSearchToolResultErrorErrorCodeUnavailable BetaToolSearchToolResultErrorErrorCode = "unavailable"

const BetaToolSearchToolResultErrorErrorCodeTooManyRequests BetaToolSearchToolResultErrorErrorCode = "too\_many\_requests"

const BetaToolSearchToolResultErrorErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorErrorCode = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type BetaToolSearchToolSearchResultBlock struct{…}



ToolReferences [][BetaToolReferenceBlock](api/beta/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



type BetaMCPToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

The name of the MCP tool

ServerName string

The name of the MCP server

Type MCPToolUse



type BetaMCPToolResultBlock struct{…}



Content BetaMCPToolResultBlockContentUnion

One of the following:

string



type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent [][BetaTextBlock](api/beta/messages.md)



Citations [][BetaTextCitationUnion](api/beta/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

IsError bool

ToolUseID string

Type MCPToolResult



type BetaContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload



type BetaCompactionBlock struct{…}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Content string

Summary of compacted content, or null if compaction failed

EncryptedContent string

Opaque metadata from prior compaction, to be round-tripped verbatim

Type Compaction



type BetaFallbackBlock struct{…}

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



From [BetaFallbackInfo](api/beta/messages.md)

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

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

To [BetaFallbackInfo](api/beta/messages.md)

The fallback model producing the content that follows this block. Its `model` is always the canonical id.

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

Trigger [BetaFallbackRefusalTrigger](api/beta/messages.md)

What caused the `from` model to hand over at this hop.



Category BetaFallbackRefusalTriggerCategory

The policy category that triggered a refusal.

One of the following:

const BetaFallbackRefusalTriggerCategoryCyber BetaFallbackRefusalTriggerCategory = "cyber"

const BetaFallbackRefusalTriggerCategoryBio BetaFallbackRefusalTriggerCategory = "bio"

const BetaFallbackRefusalTriggerCategoryFrontierLLM BetaFallbackRefusalTriggerCategory = "frontier\_llm"

const BetaFallbackRefusalTriggerCategoryReasoningExtraction BetaFallbackRefusalTriggerCategory = "reasoning\_extraction"

const BetaFallbackRefusalTriggerCategoryMilitaryWeapons BetaFallbackRefusalTriggerCategory = "military\_weapons"

Type Refusal

Type Fallback

Index int64

Type ContentBlockStart



type BetaRawContentBlockStopEvent struct{…}

Index int64

Type ContentBlockStop



type BetaRawMessageDeltaEvent struct{…}



ContextManagement [BetaContextManagementResponse](api/beta/messages.md)

Information about context management strategies applied during the request



AppliedEdits []BetaContextManagementResponseAppliedEditUnion

List of context management edits that were applied.

One of the following:



type BetaClearToolUses20250919EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

ClearedToolUses int64

Number of tool uses that were cleared.

Type ClearToolUses20250919

The type of context management edit applied.



type BetaClearThinking20251015EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

ClearedThinkingTurns int64

Number of thinking turns that were cleared.

Type ClearThinking20251015

The type of context management edit applied.



Delta BetaRawMessageDeltaEventDelta



Container [BetaContainer](api/beta/messages.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



Skills [][BetaSkill](api/beta/messages.md)

Skills loaded in the container

SkillID string

Skill ID



Type BetaSkillType

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

const BetaSkillTypeAnthropic BetaSkillType = "anthropic"

const BetaSkillTypeCustom BetaSkillType = "custom"

Version string

Skill version or 'latest' for most recent version



StopDetails [BetaRefusalStopDetails](api/beta/messages.md)

Structured information about a refusal.



Category BetaRefusalStopDetailsCategory

The policy category that triggered a refusal.

One of the following:

const BetaRefusalStopDetailsCategoryCyber BetaRefusalStopDetailsCategory = "cyber"

const BetaRefusalStopDetailsCategoryBio BetaRefusalStopDetailsCategory = "bio"

const BetaRefusalStopDetailsCategoryFrontierLLM BetaRefusalStopDetailsCategory = "frontier\_llm"

const BetaRefusalStopDetailsCategoryReasoningExtraction BetaRefusalStopDetailsCategory = "reasoning\_extraction"

const BetaRefusalStopDetailsCategoryMilitaryWeapons BetaRefusalStopDetailsCategory = "military\_weapons"



Explanation string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



FallbackCreditToken string

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



FallbackHasPrefillClaim bool

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

RecommendedModel string

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

Type Refusal



StopReason [BetaStopReason](api/beta/messages.md)

One of the following:

const BetaStopReasonEndTurn [BetaStopReason](api/beta/messages.md) = "end\_turn"

const BetaStopReasonMaxTokens [BetaStopReason](api/beta/messages.md) = "max\_tokens"

const BetaStopReasonStopSequence [BetaStopReason](api/beta/messages.md) = "stop\_sequence"

const BetaStopReasonToolUse [BetaStopReason](api/beta/messages.md) = "tool\_use"

const BetaStopReasonPauseTurn [BetaStopReason](api/beta/messages.md) = "pause\_turn"

const BetaStopReasonCompaction [BetaStopReason](api/beta/messages.md) = "compaction"

const BetaStopReasonRefusal [BetaStopReason](api/beta/messages.md) = "refusal"

const BetaStopReasonModelContextWindowExceeded [BetaStopReason](api/beta/messages.md) = "model\_context\_window\_exceeded"

StopSequence string

Type MessageDelta



Usage [BetaMessageDeltaUsage](api/beta/messages.md)

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



Iterations [BetaIterationsUsage](api/beta/messages.md)

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



type BetaMessageIterationUsage struct{…}

Token usage for a sampling iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type Message

Usage for a sampling iteration



type BetaCompactionIterationUsage struct{…}

Token usage for a compaction iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

Type Compaction

Usage for a compaction iteration



type BetaAdvisorMessageIterationUsage struct{…}

Token usage for an advisor sub-inference iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type AdvisorMessage

Usage for an advisor sub-inference iteration



type BetaFallbackMessageIterationUsage struct{…}

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type FallbackMessage

Usage for the fallback-model attempt that served the response

OutputTokens int64

The cumulative number of output tokens which were used.



OutputTokensDetails [BetaOutputTokensDetails](api/beta/messages.md)

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

ServerToolUse [BetaServerToolUsage](api/beta/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



type BetaRawMessageStartEvent struct{…}



Message [BetaMessage](api/beta/messages.md)



ID string

Unique object identifier.

The format and length of IDs may change over time.



Container [BetaContainer](api/beta/messages.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



Skills [][BetaSkill](api/beta/messages.md)

Skills loaded in the container

SkillID string

Skill ID



Type BetaSkillType

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

const BetaSkillTypeAnthropic BetaSkillType = "anthropic"

const BetaSkillTypeCustom BetaSkillType = "custom"

Version string

Skill version or 'latest' for most recent version



Content [][BetaContentBlockUnion](api/beta/messages.md)

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

type BetaTextBlock struct{…}



Citations [][BetaTextCitationUnion](api/beta/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

type BetaThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking



type BetaRedactedThinkingBlock struct{…}

Data string

Type RedactedThinking



type BetaToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse



Caller BetaToolUseBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaServerToolUseBlock struct{…}

ID string

Input map[string, any]



Name BetaServerToolUseBlockName

One of the following:

const BetaServerToolUseBlockNameAdvisor BetaServerToolUseBlockName = "advisor"

const BetaServerToolUseBlockNameWebSearch BetaServerToolUseBlockName = "web\_search"

const BetaServerToolUseBlockNameWebFetch BetaServerToolUseBlockName = "web\_fetch"

const BetaServerToolUseBlockNameCodeExecution BetaServerToolUseBlockName = "code\_execution"

const BetaServerToolUseBlockNameBashCodeExecution BetaServerToolUseBlockName = "bash\_code\_execution"

const BetaServerToolUseBlockNameTextEditorCodeExecution BetaServerToolUseBlockName = "text\_editor\_code\_execution"

const BetaServerToolUseBlockNameToolSearchToolRegex BetaServerToolUseBlockName = "tool\_search\_tool\_regex"

const BetaServerToolUseBlockNameToolSearchToolBm25 BetaServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse



Caller BetaServerToolUseBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebSearchToolResultBlock struct{…}



Content [BetaWebSearchToolResultBlockContentUnion](api/beta/messages.md)

One of the following:



type BetaWebSearchToolResultError struct{…}



ErrorCode [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "request\_too\_large"

Type WebSearchToolResultError



type BetaWebSearchToolResultBlockContentArray [][BetaWebSearchResultBlock](api/beta/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult



Caller BetaWebSearchToolResultBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebFetchToolResultBlock struct{…}



Content BetaWebFetchToolResultBlockContentUnion

One of the following:



type BetaWebFetchToolResultErrorBlock struct{…}



ErrorCode [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotInPriorContext [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_in\_prior\_context"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unavailable"

Type WebFetchToolResultError



type BetaWebFetchBlock struct{…}



Content [BetaDocumentBlock](api/beta/messages.md)



Citations [BetaCitationConfig](api/beta/messages.md)

Citation configuration for the document

Enabled bool



Source BetaDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

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

Caller BetaWebFetchToolResultBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaAdvisorToolResultBlock struct{…}



Content BetaAdvisorToolResultBlockContentUnion

One of the following:



type BetaAdvisorToolResultError struct{…}



ErrorCode BetaAdvisorToolResultErrorErrorCode

One of the following:

const BetaAdvisorToolResultErrorErrorCodeMaxUsesExceeded BetaAdvisorToolResultErrorErrorCode = "max\_uses\_exceeded"

const BetaAdvisorToolResultErrorErrorCodePromptTooLong BetaAdvisorToolResultErrorErrorCode = "prompt\_too\_long"

const BetaAdvisorToolResultErrorErrorCodeTooManyRequests BetaAdvisorToolResultErrorErrorCode = "too\_many\_requests"

const BetaAdvisorToolResultErrorErrorCodeOverloaded BetaAdvisorToolResultErrorErrorCode = "overloaded"

const BetaAdvisorToolResultErrorErrorCodeUnavailable BetaAdvisorToolResultErrorErrorCode = "unavailable"

const BetaAdvisorToolResultErrorErrorCodeExecutionTimeExceeded BetaAdvisorToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaAdvisorToolResultErrorErrorCodeModelNotFound BetaAdvisorToolResultErrorErrorCode = "model\_not\_found"

Type AdvisorToolResultError



type BetaAdvisorResultBlock struct{…}

StopReason string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

Text string

Type AdvisorResult



type BetaAdvisorRedactedResultBlock struct{…}

EncryptedContent string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

StopReason string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

Type AdvisorRedactedResult

ToolUseID string

Type AdvisorToolResult



type BetaCodeExecutionToolResultBlock struct{…}



Content [BetaCodeExecutionToolResultBlockContentUnion](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type BetaCodeExecutionToolResultError struct{…}



ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type BetaCodeExecutionResultBlock struct{…}



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type BetaEncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



type BetaBashCodeExecutionToolResultBlock struct{…}



Content BetaBashCodeExecutionToolResultBlockContentUnion

One of the following:



type BetaBashCodeExecutionToolResultError struct{…}



ErrorCode BetaBashCodeExecutionToolResultErrorErrorCode

One of the following:

const BetaBashCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaBashCodeExecutionToolResultErrorErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaBashCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaBashCodeExecutionToolResultErrorErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorErrorCode = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError



type BetaBashCodeExecutionResultBlock struct{…}



Content [][BetaBashCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



type BetaTextEditorCodeExecutionToolResultBlock struct{…}



Content BetaTextEditorCodeExecutionToolResultBlockContentUnion

One of the following:



type BetaTextEditorCodeExecutionToolResultError struct{…}



ErrorCode BetaTextEditorCodeExecutionToolResultErrorErrorCode

One of the following:

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorErrorCode = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type BetaTextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType BetaTextEditorCodeExecutionViewResultBlockFileType

One of the following:

const BetaTextEditorCodeExecutionViewResultBlockFileTypeText BetaTextEditorCodeExecutionViewResultBlockFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockFileTypeImage BetaTextEditorCodeExecutionViewResultBlockFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockFileTypePDF BetaTextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type BetaTextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type BetaTextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult



type BetaToolSearchToolResultBlock struct{…}



Content BetaToolSearchToolResultBlockContentUnion

One of the following:



type BetaToolSearchToolResultError struct{…}



ErrorCode BetaToolSearchToolResultErrorErrorCode

One of the following:

const BetaToolSearchToolResultErrorErrorCodeInvalidToolInput BetaToolSearchToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaToolSearchToolResultErrorErrorCodeUnavailable BetaToolSearchToolResultErrorErrorCode = "unavailable"

const BetaToolSearchToolResultErrorErrorCodeTooManyRequests BetaToolSearchToolResultErrorErrorCode = "too\_many\_requests"

const BetaToolSearchToolResultErrorErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorErrorCode = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type BetaToolSearchToolSearchResultBlock struct{…}



ToolReferences [][BetaToolReferenceBlock](api/beta/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



type BetaMCPToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

The name of the MCP tool

ServerName string

The name of the MCP server

Type MCPToolUse



type BetaMCPToolResultBlock struct{…}



Content BetaMCPToolResultBlockContentUnion

One of the following:

string



type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent [][BetaTextBlock](api/beta/messages.md)



Citations [][BetaTextCitationUnion](api/beta/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

IsError bool

ToolUseID string

Type MCPToolResult



type BetaContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload



type BetaCompactionBlock struct{…}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Content string

Summary of compacted content, or null if compaction failed

EncryptedContent string

Opaque metadata from prior compaction, to be round-tripped verbatim

Type Compaction



type BetaFallbackBlock struct{…}

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



From [BetaFallbackInfo](api/beta/messages.md)

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

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

To [BetaFallbackInfo](api/beta/messages.md)

The fallback model producing the content that follows this block. Its `model` is always the canonical id.

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

Trigger [BetaFallbackRefusalTrigger](api/beta/messages.md)

What caused the `from` model to hand over at this hop.



Category BetaFallbackRefusalTriggerCategory

The policy category that triggered a refusal.

One of the following:

const BetaFallbackRefusalTriggerCategoryCyber BetaFallbackRefusalTriggerCategory = "cyber"

const BetaFallbackRefusalTriggerCategoryBio BetaFallbackRefusalTriggerCategory = "bio"

const BetaFallbackRefusalTriggerCategoryFrontierLLM BetaFallbackRefusalTriggerCategory = "frontier\_llm"

const BetaFallbackRefusalTriggerCategoryReasoningExtraction BetaFallbackRefusalTriggerCategory = "reasoning\_extraction"

const BetaFallbackRefusalTriggerCategoryMilitaryWeapons BetaFallbackRefusalTriggerCategory = "military\_weapons"

Type Refusal

Type Fallback



ContextManagement [BetaContextManagementResponse](api/beta/messages.md)

Context management response.

Information about context management strategies applied during the request.



AppliedEdits []BetaContextManagementResponseAppliedEditUnion

List of context management edits that were applied.

One of the following:



type BetaClearToolUses20250919EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

ClearedToolUses int64

Number of tool uses that were cleared.

Type ClearToolUses20250919

The type of context management edit applied.



type BetaClearThinking20251015EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

ClearedThinkingTurns int64

Number of thinking turns that were cleared.

Type ClearThinking20251015

The type of context management edit applied.



Diagnostics [BetaDiagnostics](api/beta/messages.md)

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



CacheMissReason BetaDiagnosticsCacheMissReasonUnion

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



type BetaCacheMissModelChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type ModelChanged



type BetaCacheMissSystemChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type SystemChanged



type BetaCacheMissToolsChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type ToolsChanged



type BetaCacheMissMessagesChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type MessagesChanged



type BetaCacheMissPreviousMessageNotFound struct{…}

Type PreviousMessageNotFound



type BetaCacheMissUnavailable struct{…}

Type Unavailable

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

StopDetails [BetaRefusalStopDetails](api/beta/messages.md)

Structured information about a refusal.



Category BetaRefusalStopDetailsCategory

The policy category that triggered a refusal.

One of the following:

const BetaRefusalStopDetailsCategoryCyber BetaRefusalStopDetailsCategory = "cyber"

const BetaRefusalStopDetailsCategoryBio BetaRefusalStopDetailsCategory = "bio"

const BetaRefusalStopDetailsCategoryFrontierLLM BetaRefusalStopDetailsCategory = "frontier\_llm"

const BetaRefusalStopDetailsCategoryReasoningExtraction BetaRefusalStopDetailsCategory = "reasoning\_extraction"

const BetaRefusalStopDetailsCategoryMilitaryWeapons BetaRefusalStopDetailsCategory = "military\_weapons"



Explanation string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



FallbackCreditToken string

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



FallbackHasPrefillClaim bool

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

RecommendedModel string

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

Type Refusal



StopReason [BetaStopReason](api/beta/messages.md)

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

const BetaStopReasonEndTurn [BetaStopReason](api/beta/messages.md) = "end\_turn"

const BetaStopReasonMaxTokens [BetaStopReason](api/beta/messages.md) = "max\_tokens"

const BetaStopReasonStopSequence [BetaStopReason](api/beta/messages.md) = "stop\_sequence"

const BetaStopReasonToolUse [BetaStopReason](api/beta/messages.md) = "tool\_use"

const BetaStopReasonPauseTurn [BetaStopReason](api/beta/messages.md) = "pause\_turn"

const BetaStopReasonCompaction [BetaStopReason](api/beta/messages.md) = "compaction"

const BetaStopReasonRefusal [BetaStopReason](api/beta/messages.md) = "refusal"

const BetaStopReasonModelContextWindowExceeded [BetaStopReason](api/beta/messages.md) = "model\_context\_window\_exceeded"



StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



Type Message

Object type.

For Messages, this is always `"message"`.



Usage [BetaUsage](api/beta/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

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



Iterations [BetaIterationsUsage](api/beta/messages.md)

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



type BetaMessageIterationUsage struct{…}

Token usage for a sampling iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type Message

Usage for a sampling iteration



type BetaCompactionIterationUsage struct{…}

Token usage for a compaction iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

Type Compaction

Usage for a compaction iteration



type BetaAdvisorMessageIterationUsage struct{…}

Token usage for an advisor sub-inference iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type AdvisorMessage

Usage for an advisor sub-inference iteration



type BetaFallbackMessageIterationUsage struct{…}

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type FallbackMessage

Usage for the fallback-model attempt that served the response

OutputTokens int64

The number of output tokens which were used.



OutputTokensDetails [BetaOutputTokensDetails](api/beta/messages.md)

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

ServerToolUse [BetaServerToolUsage](api/beta/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



ServiceTier BetaUsageServiceTier

If the request used the priority, standard, or batch tier.

One of the following:

const BetaUsageServiceTierStandard BetaUsageServiceTier = "standard"

const BetaUsageServiceTierPriority BetaUsageServiceTier = "priority"

const BetaUsageServiceTierBatch BetaUsageServiceTier = "batch"



Speed BetaUsageSpeed

The inference speed mode used for this request.

One of the following:

const BetaUsageSpeedStandard BetaUsageSpeed = "standard"

const BetaUsageSpeedFast BetaUsageSpeed = "fast"

Type MessageStart



type BetaRawMessageStopEvent struct{…}

Type MessageStop



type BetaRawMessageStreamEventUnion interface{…}

One of the following:



type BetaRawMessageStartEvent struct{…}



Message [BetaMessage](api/beta/messages.md)



ID string

Unique object identifier.

The format and length of IDs may change over time.



Container [BetaContainer](api/beta/messages.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



Skills [][BetaSkill](api/beta/messages.md)

Skills loaded in the container

SkillID string

Skill ID



Type BetaSkillType

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

const BetaSkillTypeAnthropic BetaSkillType = "anthropic"

const BetaSkillTypeCustom BetaSkillType = "custom"

Version string

Skill version or 'latest' for most recent version



Content [][BetaContentBlockUnion](api/beta/messages.md)

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

type BetaTextBlock struct{…}



Citations [][BetaTextCitationUnion](api/beta/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

type BetaThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking



type BetaRedactedThinkingBlock struct{…}

Data string

Type RedactedThinking



type BetaToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse



Caller BetaToolUseBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaServerToolUseBlock struct{…}

ID string

Input map[string, any]



Name BetaServerToolUseBlockName

One of the following:

const BetaServerToolUseBlockNameAdvisor BetaServerToolUseBlockName = "advisor"

const BetaServerToolUseBlockNameWebSearch BetaServerToolUseBlockName = "web\_search"

const BetaServerToolUseBlockNameWebFetch BetaServerToolUseBlockName = "web\_fetch"

const BetaServerToolUseBlockNameCodeExecution BetaServerToolUseBlockName = "code\_execution"

const BetaServerToolUseBlockNameBashCodeExecution BetaServerToolUseBlockName = "bash\_code\_execution"

const BetaServerToolUseBlockNameTextEditorCodeExecution BetaServerToolUseBlockName = "text\_editor\_code\_execution"

const BetaServerToolUseBlockNameToolSearchToolRegex BetaServerToolUseBlockName = "tool\_search\_tool\_regex"

const BetaServerToolUseBlockNameToolSearchToolBm25 BetaServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse



Caller BetaServerToolUseBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebSearchToolResultBlock struct{…}



Content [BetaWebSearchToolResultBlockContentUnion](api/beta/messages.md)

One of the following:



type BetaWebSearchToolResultError struct{…}



ErrorCode [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "request\_too\_large"

Type WebSearchToolResultError



type BetaWebSearchToolResultBlockContentArray [][BetaWebSearchResultBlock](api/beta/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult



Caller BetaWebSearchToolResultBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebFetchToolResultBlock struct{…}



Content BetaWebFetchToolResultBlockContentUnion

One of the following:



type BetaWebFetchToolResultErrorBlock struct{…}



ErrorCode [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotInPriorContext [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_in\_prior\_context"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unavailable"

Type WebFetchToolResultError



type BetaWebFetchBlock struct{…}



Content [BetaDocumentBlock](api/beta/messages.md)



Citations [BetaCitationConfig](api/beta/messages.md)

Citation configuration for the document

Enabled bool



Source BetaDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

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

Caller BetaWebFetchToolResultBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaAdvisorToolResultBlock struct{…}



Content BetaAdvisorToolResultBlockContentUnion

One of the following:



type BetaAdvisorToolResultError struct{…}



ErrorCode BetaAdvisorToolResultErrorErrorCode

One of the following:

const BetaAdvisorToolResultErrorErrorCodeMaxUsesExceeded BetaAdvisorToolResultErrorErrorCode = "max\_uses\_exceeded"

const BetaAdvisorToolResultErrorErrorCodePromptTooLong BetaAdvisorToolResultErrorErrorCode = "prompt\_too\_long"

const BetaAdvisorToolResultErrorErrorCodeTooManyRequests BetaAdvisorToolResultErrorErrorCode = "too\_many\_requests"

const BetaAdvisorToolResultErrorErrorCodeOverloaded BetaAdvisorToolResultErrorErrorCode = "overloaded"

const BetaAdvisorToolResultErrorErrorCodeUnavailable BetaAdvisorToolResultErrorErrorCode = "unavailable"

const BetaAdvisorToolResultErrorErrorCodeExecutionTimeExceeded BetaAdvisorToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaAdvisorToolResultErrorErrorCodeModelNotFound BetaAdvisorToolResultErrorErrorCode = "model\_not\_found"

Type AdvisorToolResultError



type BetaAdvisorResultBlock struct{…}

StopReason string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

Text string

Type AdvisorResult



type BetaAdvisorRedactedResultBlock struct{…}

EncryptedContent string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

StopReason string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

Type AdvisorRedactedResult

ToolUseID string

Type AdvisorToolResult



type BetaCodeExecutionToolResultBlock struct{…}



Content [BetaCodeExecutionToolResultBlockContentUnion](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type BetaCodeExecutionToolResultError struct{…}



ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type BetaCodeExecutionResultBlock struct{…}



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type BetaEncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



type BetaBashCodeExecutionToolResultBlock struct{…}



Content BetaBashCodeExecutionToolResultBlockContentUnion

One of the following:



type BetaBashCodeExecutionToolResultError struct{…}



ErrorCode BetaBashCodeExecutionToolResultErrorErrorCode

One of the following:

const BetaBashCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaBashCodeExecutionToolResultErrorErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaBashCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaBashCodeExecutionToolResultErrorErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorErrorCode = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError



type BetaBashCodeExecutionResultBlock struct{…}



Content [][BetaBashCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



type BetaTextEditorCodeExecutionToolResultBlock struct{…}



Content BetaTextEditorCodeExecutionToolResultBlockContentUnion

One of the following:



type BetaTextEditorCodeExecutionToolResultError struct{…}



ErrorCode BetaTextEditorCodeExecutionToolResultErrorErrorCode

One of the following:

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorErrorCode = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type BetaTextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType BetaTextEditorCodeExecutionViewResultBlockFileType

One of the following:

const BetaTextEditorCodeExecutionViewResultBlockFileTypeText BetaTextEditorCodeExecutionViewResultBlockFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockFileTypeImage BetaTextEditorCodeExecutionViewResultBlockFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockFileTypePDF BetaTextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type BetaTextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type BetaTextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult



type BetaToolSearchToolResultBlock struct{…}



Content BetaToolSearchToolResultBlockContentUnion

One of the following:



type BetaToolSearchToolResultError struct{…}



ErrorCode BetaToolSearchToolResultErrorErrorCode

One of the following:

const BetaToolSearchToolResultErrorErrorCodeInvalidToolInput BetaToolSearchToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaToolSearchToolResultErrorErrorCodeUnavailable BetaToolSearchToolResultErrorErrorCode = "unavailable"

const BetaToolSearchToolResultErrorErrorCodeTooManyRequests BetaToolSearchToolResultErrorErrorCode = "too\_many\_requests"

const BetaToolSearchToolResultErrorErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorErrorCode = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type BetaToolSearchToolSearchResultBlock struct{…}



ToolReferences [][BetaToolReferenceBlock](api/beta/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



type BetaMCPToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

The name of the MCP tool

ServerName string

The name of the MCP server

Type MCPToolUse



type BetaMCPToolResultBlock struct{…}



Content BetaMCPToolResultBlockContentUnion

One of the following:

string



type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent [][BetaTextBlock](api/beta/messages.md)



Citations [][BetaTextCitationUnion](api/beta/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

IsError bool

ToolUseID string

Type MCPToolResult



type BetaContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload



type BetaCompactionBlock struct{…}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Content string

Summary of compacted content, or null if compaction failed

EncryptedContent string

Opaque metadata from prior compaction, to be round-tripped verbatim

Type Compaction



type BetaFallbackBlock struct{…}

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



From [BetaFallbackInfo](api/beta/messages.md)

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

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

To [BetaFallbackInfo](api/beta/messages.md)

The fallback model producing the content that follows this block. Its `model` is always the canonical id.

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

Trigger [BetaFallbackRefusalTrigger](api/beta/messages.md)

What caused the `from` model to hand over at this hop.



Category BetaFallbackRefusalTriggerCategory

The policy category that triggered a refusal.

One of the following:

const BetaFallbackRefusalTriggerCategoryCyber BetaFallbackRefusalTriggerCategory = "cyber"

const BetaFallbackRefusalTriggerCategoryBio BetaFallbackRefusalTriggerCategory = "bio"

const BetaFallbackRefusalTriggerCategoryFrontierLLM BetaFallbackRefusalTriggerCategory = "frontier\_llm"

const BetaFallbackRefusalTriggerCategoryReasoningExtraction BetaFallbackRefusalTriggerCategory = "reasoning\_extraction"

const BetaFallbackRefusalTriggerCategoryMilitaryWeapons BetaFallbackRefusalTriggerCategory = "military\_weapons"

Type Refusal

Type Fallback



ContextManagement [BetaContextManagementResponse](api/beta/messages.md)

Context management response.

Information about context management strategies applied during the request.



AppliedEdits []BetaContextManagementResponseAppliedEditUnion

List of context management edits that were applied.

One of the following:



type BetaClearToolUses20250919EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

ClearedToolUses int64

Number of tool uses that were cleared.

Type ClearToolUses20250919

The type of context management edit applied.



type BetaClearThinking20251015EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

ClearedThinkingTurns int64

Number of thinking turns that were cleared.

Type ClearThinking20251015

The type of context management edit applied.



Diagnostics [BetaDiagnostics](api/beta/messages.md)

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



CacheMissReason BetaDiagnosticsCacheMissReasonUnion

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



type BetaCacheMissModelChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type ModelChanged



type BetaCacheMissSystemChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type SystemChanged



type BetaCacheMissToolsChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type ToolsChanged



type BetaCacheMissMessagesChanged struct{…}

CacheMissedInputTokens int64

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

Type MessagesChanged



type BetaCacheMissPreviousMessageNotFound struct{…}

Type PreviousMessageNotFound



type BetaCacheMissUnavailable struct{…}

Type Unavailable

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

StopDetails [BetaRefusalStopDetails](api/beta/messages.md)

Structured information about a refusal.



Category BetaRefusalStopDetailsCategory

The policy category that triggered a refusal.

One of the following:

const BetaRefusalStopDetailsCategoryCyber BetaRefusalStopDetailsCategory = "cyber"

const BetaRefusalStopDetailsCategoryBio BetaRefusalStopDetailsCategory = "bio"

const BetaRefusalStopDetailsCategoryFrontierLLM BetaRefusalStopDetailsCategory = "frontier\_llm"

const BetaRefusalStopDetailsCategoryReasoningExtraction BetaRefusalStopDetailsCategory = "reasoning\_extraction"

const BetaRefusalStopDetailsCategoryMilitaryWeapons BetaRefusalStopDetailsCategory = "military\_weapons"



Explanation string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



FallbackCreditToken string

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



FallbackHasPrefillClaim bool

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

RecommendedModel string

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

Type Refusal



StopReason [BetaStopReason](api/beta/messages.md)

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

const BetaStopReasonEndTurn [BetaStopReason](api/beta/messages.md) = "end\_turn"

const BetaStopReasonMaxTokens [BetaStopReason](api/beta/messages.md) = "max\_tokens"

const BetaStopReasonStopSequence [BetaStopReason](api/beta/messages.md) = "stop\_sequence"

const BetaStopReasonToolUse [BetaStopReason](api/beta/messages.md) = "tool\_use"

const BetaStopReasonPauseTurn [BetaStopReason](api/beta/messages.md) = "pause\_turn"

const BetaStopReasonCompaction [BetaStopReason](api/beta/messages.md) = "compaction"

const BetaStopReasonRefusal [BetaStopReason](api/beta/messages.md) = "refusal"

const BetaStopReasonModelContextWindowExceeded [BetaStopReason](api/beta/messages.md) = "model\_context\_window\_exceeded"



StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



Type Message

Object type.

For Messages, this is always `"message"`.



Usage [BetaUsage](api/beta/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

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



Iterations [BetaIterationsUsage](api/beta/messages.md)

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



type BetaMessageIterationUsage struct{…}

Token usage for a sampling iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type Message

Usage for a sampling iteration



type BetaCompactionIterationUsage struct{…}

Token usage for a compaction iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

Type Compaction

Usage for a compaction iteration



type BetaAdvisorMessageIterationUsage struct{…}

Token usage for an advisor sub-inference iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type AdvisorMessage

Usage for an advisor sub-inference iteration



type BetaFallbackMessageIterationUsage struct{…}

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type FallbackMessage

Usage for the fallback-model attempt that served the response

OutputTokens int64

The number of output tokens which were used.



OutputTokensDetails [BetaOutputTokensDetails](api/beta/messages.md)

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

ServerToolUse [BetaServerToolUsage](api/beta/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



ServiceTier BetaUsageServiceTier

If the request used the priority, standard, or batch tier.

One of the following:

const BetaUsageServiceTierStandard BetaUsageServiceTier = "standard"

const BetaUsageServiceTierPriority BetaUsageServiceTier = "priority"

const BetaUsageServiceTierBatch BetaUsageServiceTier = "batch"



Speed BetaUsageSpeed

The inference speed mode used for this request.

One of the following:

const BetaUsageSpeedStandard BetaUsageSpeed = "standard"

const BetaUsageSpeedFast BetaUsageSpeed = "fast"

Type MessageStart



type BetaRawMessageDeltaEvent struct{…}



ContextManagement [BetaContextManagementResponse](api/beta/messages.md)

Information about context management strategies applied during the request



AppliedEdits []BetaContextManagementResponseAppliedEditUnion

List of context management edits that were applied.

One of the following:



type BetaClearToolUses20250919EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

ClearedToolUses int64

Number of tool uses that were cleared.

Type ClearToolUses20250919

The type of context management edit applied.



type BetaClearThinking20251015EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

ClearedThinkingTurns int64

Number of thinking turns that were cleared.

Type ClearThinking20251015

The type of context management edit applied.



Delta BetaRawMessageDeltaEventDelta



Container [BetaContainer](api/beta/messages.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



Skills [][BetaSkill](api/beta/messages.md)

Skills loaded in the container

SkillID string

Skill ID



Type BetaSkillType

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

const BetaSkillTypeAnthropic BetaSkillType = "anthropic"

const BetaSkillTypeCustom BetaSkillType = "custom"

Version string

Skill version or 'latest' for most recent version



StopDetails [BetaRefusalStopDetails](api/beta/messages.md)

Structured information about a refusal.



Category BetaRefusalStopDetailsCategory

The policy category that triggered a refusal.

One of the following:

const BetaRefusalStopDetailsCategoryCyber BetaRefusalStopDetailsCategory = "cyber"

const BetaRefusalStopDetailsCategoryBio BetaRefusalStopDetailsCategory = "bio"

const BetaRefusalStopDetailsCategoryFrontierLLM BetaRefusalStopDetailsCategory = "frontier\_llm"

const BetaRefusalStopDetailsCategoryReasoningExtraction BetaRefusalStopDetailsCategory = "reasoning\_extraction"

const BetaRefusalStopDetailsCategoryMilitaryWeapons BetaRefusalStopDetailsCategory = "military\_weapons"



Explanation string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



FallbackCreditToken string

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



FallbackHasPrefillClaim bool

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

RecommendedModel string

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

Type Refusal



StopReason [BetaStopReason](api/beta/messages.md)

One of the following:

const BetaStopReasonEndTurn [BetaStopReason](api/beta/messages.md) = "end\_turn"

const BetaStopReasonMaxTokens [BetaStopReason](api/beta/messages.md) = "max\_tokens"

const BetaStopReasonStopSequence [BetaStopReason](api/beta/messages.md) = "stop\_sequence"

const BetaStopReasonToolUse [BetaStopReason](api/beta/messages.md) = "tool\_use"

const BetaStopReasonPauseTurn [BetaStopReason](api/beta/messages.md) = "pause\_turn"

const BetaStopReasonCompaction [BetaStopReason](api/beta/messages.md) = "compaction"

const BetaStopReasonRefusal [BetaStopReason](api/beta/messages.md) = "refusal"

const BetaStopReasonModelContextWindowExceeded [BetaStopReason](api/beta/messages.md) = "model\_context\_window\_exceeded"

StopSequence string

Type MessageDelta



Usage [BetaMessageDeltaUsage](api/beta/messages.md)

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



Iterations [BetaIterationsUsage](api/beta/messages.md)

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



type BetaMessageIterationUsage struct{…}

Token usage for a sampling iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type Message

Usage for a sampling iteration



type BetaCompactionIterationUsage struct{…}

Token usage for a compaction iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

Type Compaction

Usage for a compaction iteration



type BetaAdvisorMessageIterationUsage struct{…}

Token usage for an advisor sub-inference iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type AdvisorMessage

Usage for an advisor sub-inference iteration



type BetaFallbackMessageIterationUsage struct{…}

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type FallbackMessage

Usage for the fallback-model attempt that served the response

OutputTokens int64

The cumulative number of output tokens which were used.



OutputTokensDetails [BetaOutputTokensDetails](api/beta/messages.md)

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

ServerToolUse [BetaServerToolUsage](api/beta/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



type BetaRawMessageStopEvent struct{…}

Type MessageStop



type BetaRawContentBlockStartEvent struct{…}



ContentBlock BetaRawContentBlockStartEventContentBlockUnion

Response model for a file uploaded to the container.

One of the following:



type BetaTextBlock struct{…}



Citations [][BetaTextCitationUnion](api/beta/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

type BetaThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking



type BetaRedactedThinkingBlock struct{…}

Data string

Type RedactedThinking



type BetaToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse



Caller BetaToolUseBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaServerToolUseBlock struct{…}

ID string

Input map[string, any]



Name BetaServerToolUseBlockName

One of the following:

const BetaServerToolUseBlockNameAdvisor BetaServerToolUseBlockName = "advisor"

const BetaServerToolUseBlockNameWebSearch BetaServerToolUseBlockName = "web\_search"

const BetaServerToolUseBlockNameWebFetch BetaServerToolUseBlockName = "web\_fetch"

const BetaServerToolUseBlockNameCodeExecution BetaServerToolUseBlockName = "code\_execution"

const BetaServerToolUseBlockNameBashCodeExecution BetaServerToolUseBlockName = "bash\_code\_execution"

const BetaServerToolUseBlockNameTextEditorCodeExecution BetaServerToolUseBlockName = "text\_editor\_code\_execution"

const BetaServerToolUseBlockNameToolSearchToolRegex BetaServerToolUseBlockName = "tool\_search\_tool\_regex"

const BetaServerToolUseBlockNameToolSearchToolBm25 BetaServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse



Caller BetaServerToolUseBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebSearchToolResultBlock struct{…}



Content [BetaWebSearchToolResultBlockContentUnion](api/beta/messages.md)

One of the following:



type BetaWebSearchToolResultError struct{…}



ErrorCode [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "request\_too\_large"

Type WebSearchToolResultError



type BetaWebSearchToolResultBlockContentArray [][BetaWebSearchResultBlock](api/beta/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult



Caller BetaWebSearchToolResultBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebFetchToolResultBlock struct{…}



Content BetaWebFetchToolResultBlockContentUnion

One of the following:



type BetaWebFetchToolResultErrorBlock struct{…}



ErrorCode [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotInPriorContext [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_in\_prior\_context"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unavailable"

Type WebFetchToolResultError



type BetaWebFetchBlock struct{…}



Content [BetaDocumentBlock](api/beta/messages.md)



Citations [BetaCitationConfig](api/beta/messages.md)

Citation configuration for the document

Enabled bool



Source BetaDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

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

Caller BetaWebFetchToolResultBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaAdvisorToolResultBlock struct{…}



Content BetaAdvisorToolResultBlockContentUnion

One of the following:



type BetaAdvisorToolResultError struct{…}



ErrorCode BetaAdvisorToolResultErrorErrorCode

One of the following:

const BetaAdvisorToolResultErrorErrorCodeMaxUsesExceeded BetaAdvisorToolResultErrorErrorCode = "max\_uses\_exceeded"

const BetaAdvisorToolResultErrorErrorCodePromptTooLong BetaAdvisorToolResultErrorErrorCode = "prompt\_too\_long"

const BetaAdvisorToolResultErrorErrorCodeTooManyRequests BetaAdvisorToolResultErrorErrorCode = "too\_many\_requests"

const BetaAdvisorToolResultErrorErrorCodeOverloaded BetaAdvisorToolResultErrorErrorCode = "overloaded"

const BetaAdvisorToolResultErrorErrorCodeUnavailable BetaAdvisorToolResultErrorErrorCode = "unavailable"

const BetaAdvisorToolResultErrorErrorCodeExecutionTimeExceeded BetaAdvisorToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaAdvisorToolResultErrorErrorCodeModelNotFound BetaAdvisorToolResultErrorErrorCode = "model\_not\_found"

Type AdvisorToolResultError



type BetaAdvisorResultBlock struct{…}

StopReason string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

Text string

Type AdvisorResult



type BetaAdvisorRedactedResultBlock struct{…}

EncryptedContent string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

StopReason string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

Type AdvisorRedactedResult

ToolUseID string

Type AdvisorToolResult



type BetaCodeExecutionToolResultBlock struct{…}



Content [BetaCodeExecutionToolResultBlockContentUnion](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type BetaCodeExecutionToolResultError struct{…}



ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type BetaCodeExecutionResultBlock struct{…}



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type BetaEncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][BetaCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



type BetaBashCodeExecutionToolResultBlock struct{…}



Content BetaBashCodeExecutionToolResultBlockContentUnion

One of the following:



type BetaBashCodeExecutionToolResultError struct{…}



ErrorCode BetaBashCodeExecutionToolResultErrorErrorCode

One of the following:

const BetaBashCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaBashCodeExecutionToolResultErrorErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaBashCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaBashCodeExecutionToolResultErrorErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorErrorCode = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError



type BetaBashCodeExecutionResultBlock struct{…}



Content [][BetaBashCodeExecutionOutputBlock](api/beta/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



type BetaTextEditorCodeExecutionToolResultBlock struct{…}



Content BetaTextEditorCodeExecutionToolResultBlockContentUnion

One of the following:



type BetaTextEditorCodeExecutionToolResultError struct{…}



ErrorCode BetaTextEditorCodeExecutionToolResultErrorErrorCode

One of the following:

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorErrorCode = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type BetaTextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType BetaTextEditorCodeExecutionViewResultBlockFileType

One of the following:

const BetaTextEditorCodeExecutionViewResultBlockFileTypeText BetaTextEditorCodeExecutionViewResultBlockFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockFileTypeImage BetaTextEditorCodeExecutionViewResultBlockFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockFileTypePDF BetaTextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type BetaTextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type BetaTextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult



type BetaToolSearchToolResultBlock struct{…}



Content BetaToolSearchToolResultBlockContentUnion

One of the following:



type BetaToolSearchToolResultError struct{…}



ErrorCode BetaToolSearchToolResultErrorErrorCode

One of the following:

const BetaToolSearchToolResultErrorErrorCodeInvalidToolInput BetaToolSearchToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaToolSearchToolResultErrorErrorCodeUnavailable BetaToolSearchToolResultErrorErrorCode = "unavailable"

const BetaToolSearchToolResultErrorErrorCodeTooManyRequests BetaToolSearchToolResultErrorErrorCode = "too\_many\_requests"

const BetaToolSearchToolResultErrorErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorErrorCode = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type BetaToolSearchToolSearchResultBlock struct{…}



ToolReferences [][BetaToolReferenceBlock](api/beta/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



type BetaMCPToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

The name of the MCP tool

ServerName string

The name of the MCP server

Type MCPToolUse



type BetaMCPToolResultBlock struct{…}



Content BetaMCPToolResultBlockContentUnion

One of the following:

string



type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent [][BetaTextBlock](api/beta/messages.md)



Citations [][BetaTextCitationUnion](api/beta/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

IsError bool

ToolUseID string

Type MCPToolResult



type BetaContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload



type BetaCompactionBlock struct{…}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Content string

Summary of compacted content, or null if compaction failed

EncryptedContent string

Opaque metadata from prior compaction, to be round-tripped verbatim

Type Compaction



type BetaFallbackBlock struct{…}

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



From [BetaFallbackInfo](api/beta/messages.md)

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

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

To [BetaFallbackInfo](api/beta/messages.md)

The fallback model producing the content that follows this block. Its `model` is always the canonical id.

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

Trigger [BetaFallbackRefusalTrigger](api/beta/messages.md)

What caused the `from` model to hand over at this hop.



Category BetaFallbackRefusalTriggerCategory

The policy category that triggered a refusal.

One of the following:

const BetaFallbackRefusalTriggerCategoryCyber BetaFallbackRefusalTriggerCategory = "cyber"

const BetaFallbackRefusalTriggerCategoryBio BetaFallbackRefusalTriggerCategory = "bio"

const BetaFallbackRefusalTriggerCategoryFrontierLLM BetaFallbackRefusalTriggerCategory = "frontier\_llm"

const BetaFallbackRefusalTriggerCategoryReasoningExtraction BetaFallbackRefusalTriggerCategory = "reasoning\_extraction"

const BetaFallbackRefusalTriggerCategoryMilitaryWeapons BetaFallbackRefusalTriggerCategory = "military\_weapons"

Type Refusal

Type Fallback

Index int64

Type ContentBlockStart



type BetaRawContentBlockDeltaEvent struct{…}



Delta [BetaRawContentBlockDeltaUnion](api/beta/messages.md)

One of the following:



type BetaTextDelta struct{…}

Text string

Type TextDelta



type BetaInputJSONDelta struct{…}

PartialJSON string

Type InputJSONDelta



type BetaCitationsDelta struct{…}



Citation BetaCitationsDeltaCitationUnion

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

type BetaThinkingDelta struct{…}

EstimatedTokens int64

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

Thinking string

Type ThinkingDelta



type BetaSignatureDelta struct{…}

Signature string

Type SignatureDelta



type BetaCompactionContentBlockDelta struct{…}

Content string

EncryptedContent string

Opaque metadata from prior compaction, to be round-tripped verbatim

Type CompactionDelta

Index int64

Type ContentBlockDelta



type BetaRawContentBlockStopEvent struct{…}

Index int64

Type ContentBlockStop



type BetaRedactedThinkingBlock struct{…}

Data string

Type RedactedThinking



type BetaRedactedThinkingBlockParamResp struct{…}

Data string

Type RedactedThinking



type BetaRefusalStopDetails struct{…}

Structured information about a refusal.



Category BetaRefusalStopDetailsCategory

The policy category that triggered a refusal.

One of the following:

const BetaRefusalStopDetailsCategoryCyber BetaRefusalStopDetailsCategory = "cyber"

const BetaRefusalStopDetailsCategoryBio BetaRefusalStopDetailsCategory = "bio"

const BetaRefusalStopDetailsCategoryFrontierLLM BetaRefusalStopDetailsCategory = "frontier\_llm"

const BetaRefusalStopDetailsCategoryReasoningExtraction BetaRefusalStopDetailsCategory = "reasoning\_extraction"

const BetaRefusalStopDetailsCategoryMilitaryWeapons BetaRefusalStopDetailsCategory = "military\_weapons"



Explanation string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



FallbackCreditToken string

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



FallbackHasPrefillClaim bool

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

RecommendedModel string

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

Type Refusal



type BetaRequestDocumentBlock struct{…}



Source BetaRequestDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text



type BetaContentBlockSource struct{…}



Content BetaContentBlockSourceContentUnion

One of the following:

string



[][BetaContentBlockSourceContentUnion](api/beta/messages.md)

One of the following:



type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type Content



type BetaURLPDFSource struct{…}

Type URL

URL string



type BetaFileDocumentSource struct{…}

FileID string

Type File

Type Document



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

Enabled boolOptional

Context stringOptional

Title stringOptional



type BetaRequestMCPServerToolConfiguration struct{…}

AllowedTools []stringOptional

Enabled boolOptional



type BetaRequestMCPServerURLDefinition struct{…}

Name string

Type URL

URL string

AuthorizationToken stringOptional



ToolConfiguration [BetaRequestMCPServerToolConfiguration](api/beta/messages.md)Optional

AllowedTools []stringOptional

Enabled boolOptional



type BetaRequestMCPToolResultBlockParamResp struct{…}

ToolUseID string

Type MCPToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Content BetaRequestMCPToolResultBlockParamContentUnionRespOptional

One of the following:

string



[][BetaTextBlockParamResp](api/beta/messages.md)

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

IsError boolOptional



type BetaSearchResultBlockParamResp struct{…}



Content [][BetaTextBlockParamResp](api/beta/messages.md)

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

Enabled boolOptional



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaServerToolUsage struct{…}

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



type BetaServerToolUseBlock struct{…}

ID string

Input map[string, any]



Name BetaServerToolUseBlockName

One of the following:

const BetaServerToolUseBlockNameAdvisor BetaServerToolUseBlockName = "advisor"

const BetaServerToolUseBlockNameWebSearch BetaServerToolUseBlockName = "web\_search"

const BetaServerToolUseBlockNameWebFetch BetaServerToolUseBlockName = "web\_fetch"

const BetaServerToolUseBlockNameCodeExecution BetaServerToolUseBlockName = "code\_execution"

const BetaServerToolUseBlockNameBashCodeExecution BetaServerToolUseBlockName = "bash\_code\_execution"

const BetaServerToolUseBlockNameTextEditorCodeExecution BetaServerToolUseBlockName = "text\_editor\_code\_execution"

const BetaServerToolUseBlockNameToolSearchToolRegex BetaServerToolUseBlockName = "tool\_search\_tool\_regex"

const BetaServerToolUseBlockNameToolSearchToolBm25 BetaServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse



Caller BetaServerToolUseBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaServerToolUseBlockParamResp struct{…}

ID string

Input map[string, any]



Name BetaServerToolUseBlockParamName

One of the following:

const BetaServerToolUseBlockParamNameAdvisor BetaServerToolUseBlockParamName = "advisor"

const BetaServerToolUseBlockParamNameWebSearch BetaServerToolUseBlockParamName = "web\_search"

const BetaServerToolUseBlockParamNameWebFetch BetaServerToolUseBlockParamName = "web\_fetch"

const BetaServerToolUseBlockParamNameCodeExecution BetaServerToolUseBlockParamName = "code\_execution"

const BetaServerToolUseBlockParamNameBashCodeExecution BetaServerToolUseBlockParamName = "bash\_code\_execution"

const BetaServerToolUseBlockParamNameTextEditorCodeExecution BetaServerToolUseBlockParamName = "text\_editor\_code\_execution"

const BetaServerToolUseBlockParamNameToolSearchToolRegex BetaServerToolUseBlockParamName = "tool\_search\_tool\_regex"

const BetaServerToolUseBlockParamNameToolSearchToolBm25 BetaServerToolUseBlockParamName = "tool\_search\_tool\_bm25"

Type ServerToolUse



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Caller BetaServerToolUseBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaSignatureDelta struct{…}

Signature string

Type SignatureDelta



type BetaSkill struct{…}

A skill that was loaded in a container (response model).

SkillID string

Skill ID



Type BetaSkillType

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

const BetaSkillTypeAnthropic BetaSkillType = "anthropic"

const BetaSkillTypeCustom BetaSkillType = "custom"

Version string

Skill version or 'latest' for most recent version



type BetaSkillParamsResp struct{…}

Specification for a skill to be loaded in a container (request model).

SkillID string

Skill ID



Type BetaSkillParamsType

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

const BetaSkillParamsTypeAnthropic BetaSkillParamsType = "anthropic"

const BetaSkillParamsTypeCustom BetaSkillParamsType = "custom"

Version stringOptional

Skill version or 'latest' for most recent version



type BetaStopReason string

One of the following:

const BetaStopReasonEndTurn [BetaStopReason](api/beta/messages.md) = "end\_turn"

const BetaStopReasonMaxTokens [BetaStopReason](api/beta/messages.md) = "max\_tokens"

const BetaStopReasonStopSequence [BetaStopReason](api/beta/messages.md) = "stop\_sequence"

const BetaStopReasonToolUse [BetaStopReason](api/beta/messages.md) = "tool\_use"

const BetaStopReasonPauseTurn [BetaStopReason](api/beta/messages.md) = "pause\_turn"

const BetaStopReasonCompaction [BetaStopReason](api/beta/messages.md) = "compaction"

const BetaStopReasonRefusal [BetaStopReason](api/beta/messages.md) = "refusal"

const BetaStopReasonModelContextWindowExceeded [BetaStopReason](api/beta/messages.md) = "model\_context\_window\_exceeded"



type BetaTextBlock struct{…}



Citations [][BetaTextCitationUnion](api/beta/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaTextCitationUnion interface{…}

One of the following:



type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocation struct{…}

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

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocation struct{…}

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

type BetaTextCitationParamUnionResp interface{…}

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaTextDelta struct{…}

Text string

Type TextDelta



type BetaTextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type BetaTextEditorCodeExecutionCreateResultBlockParamResp struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type BetaTextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult



type BetaTextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}

Type TextEditorCodeExecutionStrReplaceResult

Lines []stringOptional

NewLines int64Optional

NewStart int64Optional

OldLines int64Optional

OldStart int64Optional



type BetaTextEditorCodeExecutionToolResultBlock struct{…}



Content BetaTextEditorCodeExecutionToolResultBlockContentUnion

One of the following:



type BetaTextEditorCodeExecutionToolResultError struct{…}



ErrorCode BetaTextEditorCodeExecutionToolResultErrorErrorCode

One of the following:

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorErrorCode = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type BetaTextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType BetaTextEditorCodeExecutionViewResultBlockFileType

One of the following:

const BetaTextEditorCodeExecutionViewResultBlockFileTypeText BetaTextEditorCodeExecutionViewResultBlockFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockFileTypeImage BetaTextEditorCodeExecutionViewResultBlockFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockFileTypePDF BetaTextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type BetaTextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type BetaTextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult



type BetaTextEditorCodeExecutionToolResultBlockParamResp struct{…}



Content BetaTextEditorCodeExecutionToolResultBlockParamContentUnionResp

One of the following:



type BetaTextEditorCodeExecutionToolResultErrorParamResp struct{…}



ErrorCode BetaTextEditorCodeExecutionToolResultErrorParamErrorCode

One of the following:

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "invalid\_tool\_input"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "execution\_time\_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "file\_not\_found"

Type TextEditorCodeExecutionToolResultError

ErrorMessage stringOptional



type BetaTextEditorCodeExecutionViewResultBlockParamResp struct{…}

Content string



FileType BetaTextEditorCodeExecutionViewResultBlockParamFileType

One of the following:

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypeText BetaTextEditorCodeExecutionViewResultBlockParamFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypeImage BetaTextEditorCodeExecutionViewResultBlockParamFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypePDF BetaTextEditorCodeExecutionViewResultBlockParamFileType = "pdf"

Type TextEditorCodeExecutionViewResult

NumLines int64Optional

StartLine int64Optional

TotalLines int64Optional



type BetaTextEditorCodeExecutionCreateResultBlockParamResp struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type BetaTextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}

Type TextEditorCodeExecutionStrReplaceResult

Lines []stringOptional

NewLines int64Optional

NewStart int64Optional

OldLines int64Optional

OldStart int64Optional

ToolUseID string

Type TextEditorCodeExecutionToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaTextEditorCodeExecutionToolResultError struct{…}



ErrorCode BetaTextEditorCodeExecutionToolResultErrorErrorCode

One of the following:

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorErrorCode = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type BetaTextEditorCodeExecutionToolResultErrorParamResp struct{…}



ErrorCode BetaTextEditorCodeExecutionToolResultErrorParamErrorCode

One of the following:

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "invalid\_tool\_input"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "execution\_time\_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "file\_not\_found"

Type TextEditorCodeExecutionToolResultError

ErrorMessage stringOptional



type BetaTextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType BetaTextEditorCodeExecutionViewResultBlockFileType

One of the following:

const BetaTextEditorCodeExecutionViewResultBlockFileTypeText BetaTextEditorCodeExecutionViewResultBlockFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockFileTypeImage BetaTextEditorCodeExecutionViewResultBlockFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockFileTypePDF BetaTextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type BetaTextEditorCodeExecutionViewResultBlockParamResp struct{…}

Content string



FileType BetaTextEditorCodeExecutionViewResultBlockParamFileType

One of the following:

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypeText BetaTextEditorCodeExecutionViewResultBlockParamFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypeImage BetaTextEditorCodeExecutionViewResultBlockParamFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypePDF BetaTextEditorCodeExecutionViewResultBlockParamFileType = "pdf"

Type TextEditorCodeExecutionViewResult

NumLines int64Optional

StartLine int64Optional

TotalLines int64Optional



type BetaThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking



type BetaThinkingBlockParamResp struct{…}

Signature string

Thinking string

Type Thinking



type BetaThinkingConfigAdaptive struct{…}

Type Adaptive



Display BetaThinkingConfigAdaptiveDisplayOptional

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

const BetaThinkingConfigAdaptiveDisplaySummarized BetaThinkingConfigAdaptiveDisplay = "summarized"

const BetaThinkingConfigAdaptiveDisplayOmitted BetaThinkingConfigAdaptiveDisplay = "omitted"



type BetaThinkingConfigDisabled struct{…}

Type Disabled



type BetaThinkingConfigEnabled struct{…}



BudgetTokens int64

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

Type Enabled



Display BetaThinkingConfigEnabledDisplayOptional

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

const BetaThinkingConfigEnabledDisplaySummarized BetaThinkingConfigEnabledDisplay = "summarized"

const BetaThinkingConfigEnabledDisplayOmitted BetaThinkingConfigEnabledDisplay = "omitted"



type BetaThinkingConfigParamUnionResp interface{…}

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

One of the following:



type BetaThinkingConfigEnabled struct{…}



BudgetTokens int64

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

Type Enabled



Display BetaThinkingConfigEnabledDisplayOptional

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

const BetaThinkingConfigEnabledDisplaySummarized BetaThinkingConfigEnabledDisplay = "summarized"

const BetaThinkingConfigEnabledDisplayOmitted BetaThinkingConfigEnabledDisplay = "omitted"



type BetaThinkingConfigDisabled struct{…}

Type Disabled



type BetaThinkingConfigAdaptive struct{…}

Type Adaptive



Display BetaThinkingConfigAdaptiveDisplayOptional

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

const BetaThinkingConfigAdaptiveDisplaySummarized BetaThinkingConfigAdaptiveDisplay = "summarized"

const BetaThinkingConfigAdaptiveDisplayOmitted BetaThinkingConfigAdaptiveDisplay = "omitted"



type BetaThinkingDelta struct{…}

EstimatedTokens int64

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

Thinking string

Type ThinkingDelta



type BetaThinkingTurns struct{…}

Type ThinkingTurns

Value int64



type BetaTokenTaskBudget struct{…}

User-configurable total token budget across contexts.

Total int64

Total token budget across all contexts in the session.

Type Tokens

The budget type. Currently only 'tokens' is supported.

Remaining int64Optional

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



type BetaTool struct{…}



InputSchema BetaToolInputSchema

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

const BetaToolAllowedCallerDirect BetaToolAllowedCaller = "direct"

const BetaToolAllowedCallerCodeExecution20250825 BetaToolAllowedCaller = "code\_execution\_20250825"

const BetaToolAllowedCallerCodeExecution20260120 BetaToolAllowedCaller = "code\_execution\_20260120"

const BetaToolAllowedCallerCodeExecution20260521 BetaToolAllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

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

Type BetaToolTypeOptional



type BetaToolBash20241022 struct{…}



Name Bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Bash20241022



AllowedCallers []stringOptional

One of the following:

const BetaToolBash20241022AllowedCallerDirect BetaToolBash20241022AllowedCaller = "direct"

const BetaToolBash20241022AllowedCallerCodeExecution20250825 BetaToolBash20241022AllowedCaller = "code\_execution\_20250825"

const BetaToolBash20241022AllowedCallerCodeExecution20260120 BetaToolBash20241022AllowedCaller = "code\_execution\_20260120"

const BetaToolBash20241022AllowedCallerCodeExecution20260521 BetaToolBash20241022AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolBash20250124 struct{…}



Name Bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Bash20250124



AllowedCallers []stringOptional

One of the following:

const BetaToolBash20250124AllowedCallerDirect BetaToolBash20250124AllowedCaller = "direct"

const BetaToolBash20250124AllowedCallerCodeExecution20250825 BetaToolBash20250124AllowedCaller = "code\_execution\_20250825"

const BetaToolBash20250124AllowedCallerCodeExecution20260120 BetaToolBash20250124AllowedCaller = "code\_execution\_20260120"

const BetaToolBash20250124AllowedCallerCodeExecution20260521 BetaToolBash20250124AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolChoiceUnion interface{…}

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



type BetaToolChoiceAuto struct{…}

The model will automatically decide whether to use tools.

Type Auto



DisableParallelToolUse boolOptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



type BetaToolChoiceAny struct{…}

The model will use any available tools.

Type Any



DisableParallelToolUse boolOptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



type BetaToolChoiceTool struct{…}

The model will use the specified tool with `tool_choice.name`.

Name string

The name of the tool to use.

Type Tool



DisableParallelToolUse boolOptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



type BetaToolChoiceNone struct{…}

The model will not be allowed to use tools.

Type None



type BetaToolChoiceAny struct{…}

The model will use any available tools.

Type Any



DisableParallelToolUse boolOptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



type BetaToolChoiceAuto struct{…}

The model will automatically decide whether to use tools.

Type Auto



DisableParallelToolUse boolOptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



type BetaToolChoiceNone struct{…}

The model will not be allowed to use tools.

Type None



type BetaToolChoiceTool struct{…}

The model will use the specified tool with `tool_choice.name`.

Name string

The name of the tool to use.

Type Tool



DisableParallelToolUse boolOptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



type BetaToolComputerUse20241022 struct{…}

DisplayHeightPx int64

The height of the display in pixels.

DisplayWidthPx int64

The width of the display in pixels.



Name Computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Computer20241022



AllowedCallers []stringOptional

One of the following:

const BetaToolComputerUse20241022AllowedCallerDirect BetaToolComputerUse20241022AllowedCaller = "direct"

const BetaToolComputerUse20241022AllowedCallerCodeExecution20250825 BetaToolComputerUse20241022AllowedCaller = "code\_execution\_20250825"

const BetaToolComputerUse20241022AllowedCallerCodeExecution20260120 BetaToolComputerUse20241022AllowedCaller = "code\_execution\_20260120"

const BetaToolComputerUse20241022AllowedCallerCodeExecution20260521 BetaToolComputerUse20241022AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

DisplayNumber int64Optional

The X11 display number (e.g. 0, 1) for the display.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolComputerUse20250124 struct{…}

DisplayHeightPx int64

The height of the display in pixels.

DisplayWidthPx int64

The width of the display in pixels.



Name Computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Computer20250124



AllowedCallers []stringOptional

One of the following:

const BetaToolComputerUse20250124AllowedCallerDirect BetaToolComputerUse20250124AllowedCaller = "direct"

const BetaToolComputerUse20250124AllowedCallerCodeExecution20250825 BetaToolComputerUse20250124AllowedCaller = "code\_execution\_20250825"

const BetaToolComputerUse20250124AllowedCallerCodeExecution20260120 BetaToolComputerUse20250124AllowedCaller = "code\_execution\_20260120"

const BetaToolComputerUse20250124AllowedCallerCodeExecution20260521 BetaToolComputerUse20250124AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

DisplayNumber int64Optional

The X11 display number (e.g. 0, 1) for the display.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolComputerUse20251124 struct{…}

DisplayHeightPx int64

The height of the display in pixels.

DisplayWidthPx int64

The width of the display in pixels.



Name Computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Computer20251124



AllowedCallers []stringOptional

One of the following:

const BetaToolComputerUse20251124AllowedCallerDirect BetaToolComputerUse20251124AllowedCaller = "direct"

const BetaToolComputerUse20251124AllowedCallerCodeExecution20250825 BetaToolComputerUse20251124AllowedCaller = "code\_execution\_20250825"

const BetaToolComputerUse20251124AllowedCallerCodeExecution20260120 BetaToolComputerUse20251124AllowedCaller = "code\_execution\_20260120"

const BetaToolComputerUse20251124AllowedCallerCodeExecution20260521 BetaToolComputerUse20251124AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

DisplayNumber int64Optional

The X11 display number (e.g. 0, 1) for the display.

EnableZoom boolOptional

Whether to enable an action to take a zoomed-in screenshot of the screen.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolReferenceBlock struct{…}

ToolName string

Type ToolReference



type BetaToolReferenceBlockParamResp struct{…}

Tool reference block that can be included in tool\_result content.

ToolName string

Type ToolReference



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaToolResultBlockParamResp struct{…}

ToolUseID string

Type ToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Content []BetaToolResultBlockParamContentUnionRespOptional

One of the following:



[]BetaToolResultBlockParamContentUnionResp

One of the following:



type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaSearchResultBlockParamResp struct{…}



Content [][BetaTextBlockParamResp](api/beta/messages.md)

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

Enabled boolOptional



type BetaRequestDocumentBlock struct{…}



Source BetaRequestDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text



type BetaContentBlockSource struct{…}



Content BetaContentBlockSourceContentUnion

One of the following:

string



[][BetaContentBlockSourceContentUnion](api/beta/messages.md)

One of the following:



type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type Content



type BetaURLPDFSource struct{…}

Type URL

URL string



type BetaFileDocumentSource struct{…}

FileID string

Type File

Type Document



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

Enabled boolOptional

Context stringOptional

Title stringOptional



type BetaToolReferenceBlockParamResp struct{…}

Tool reference block that can be included in tool\_result content.

ToolName string

Type ToolReference



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

IsError boolOptional



type BetaToolSearchToolBm25\_20251119 struct{…}



Name ToolSearchToolBm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



Type BetaToolSearchToolBm25\_20251119Type

One of the following:

const BetaToolSearchToolBm25\_20251119TypeToolSearchToolBm25\_20251119 BetaToolSearchToolBm25\_20251119Type = "tool\_search\_tool\_bm25\_20251119"

const BetaToolSearchToolBm25\_20251119TypeToolSearchToolBm25 BetaToolSearchToolBm25\_20251119Type = "tool\_search\_tool\_bm25"



AllowedCallers []stringOptional

One of the following:

const BetaToolSearchToolBm25\_20251119AllowedCallerDirect BetaToolSearchToolBm25\_20251119AllowedCaller = "direct"

const BetaToolSearchToolBm25\_20251119AllowedCallerCodeExecution20250825 BetaToolSearchToolBm25\_20251119AllowedCaller = "code\_execution\_20250825"

const BetaToolSearchToolBm25\_20251119AllowedCallerCodeExecution20260120 BetaToolSearchToolBm25\_20251119AllowedCaller = "code\_execution\_20260120"

const BetaToolSearchToolBm25\_20251119AllowedCallerCodeExecution20260521 BetaToolSearchToolBm25\_20251119AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolSearchToolRegex20251119 struct{…}



Name ToolSearchToolRegex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



Type BetaToolSearchToolRegex20251119Type

One of the following:

const BetaToolSearchToolRegex20251119TypeToolSearchToolRegex20251119 BetaToolSearchToolRegex20251119Type = "tool\_search\_tool\_regex\_20251119"

const BetaToolSearchToolRegex20251119TypeToolSearchToolRegex BetaToolSearchToolRegex20251119Type = "tool\_search\_tool\_regex"



AllowedCallers []stringOptional

One of the following:

const BetaToolSearchToolRegex20251119AllowedCallerDirect BetaToolSearchToolRegex20251119AllowedCaller = "direct"

const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20250825 BetaToolSearchToolRegex20251119AllowedCaller = "code\_execution\_20250825"

const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20260120 BetaToolSearchToolRegex20251119AllowedCaller = "code\_execution\_20260120"

const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20260521 BetaToolSearchToolRegex20251119AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolSearchToolResultBlock struct{…}



Content BetaToolSearchToolResultBlockContentUnion

One of the following:



type BetaToolSearchToolResultError struct{…}



ErrorCode BetaToolSearchToolResultErrorErrorCode

One of the following:

const BetaToolSearchToolResultErrorErrorCodeInvalidToolInput BetaToolSearchToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaToolSearchToolResultErrorErrorCodeUnavailable BetaToolSearchToolResultErrorErrorCode = "unavailable"

const BetaToolSearchToolResultErrorErrorCodeTooManyRequests BetaToolSearchToolResultErrorErrorCode = "too\_many\_requests"

const BetaToolSearchToolResultErrorErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorErrorCode = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type BetaToolSearchToolSearchResultBlock struct{…}



ToolReferences [][BetaToolReferenceBlock](api/beta/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



type BetaToolSearchToolResultBlockParamResp struct{…}



Content BetaToolSearchToolResultBlockParamContentUnionResp

One of the following:



type BetaToolSearchToolResultErrorParamResp struct{…}



ErrorCode BetaToolSearchToolResultErrorParamErrorCode

One of the following:

const BetaToolSearchToolResultErrorParamErrorCodeInvalidToolInput BetaToolSearchToolResultErrorParamErrorCode = "invalid\_tool\_input"

const BetaToolSearchToolResultErrorParamErrorCodeUnavailable BetaToolSearchToolResultErrorParamErrorCode = "unavailable"

const BetaToolSearchToolResultErrorParamErrorCodeTooManyRequests BetaToolSearchToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaToolSearchToolResultErrorParamErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorParamErrorCode = "execution\_time\_exceeded"

Type ToolSearchToolResultError

ErrorMessage stringOptional



type BetaToolSearchToolSearchResultBlockParamResp struct{…}



ToolReferences [][BetaToolReferenceBlockParamResp](api/beta/messages.md)

ToolName string

Type ToolReference



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



type BetaToolSearchToolResultError struct{…}



ErrorCode BetaToolSearchToolResultErrorErrorCode

One of the following:

const BetaToolSearchToolResultErrorErrorCodeInvalidToolInput BetaToolSearchToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaToolSearchToolResultErrorErrorCodeUnavailable BetaToolSearchToolResultErrorErrorCode = "unavailable"

const BetaToolSearchToolResultErrorErrorCodeTooManyRequests BetaToolSearchToolResultErrorErrorCode = "too\_many\_requests"

const BetaToolSearchToolResultErrorErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorErrorCode = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type BetaToolSearchToolResultErrorParamResp struct{…}



ErrorCode BetaToolSearchToolResultErrorParamErrorCode

One of the following:

const BetaToolSearchToolResultErrorParamErrorCodeInvalidToolInput BetaToolSearchToolResultErrorParamErrorCode = "invalid\_tool\_input"

const BetaToolSearchToolResultErrorParamErrorCodeUnavailable BetaToolSearchToolResultErrorParamErrorCode = "unavailable"

const BetaToolSearchToolResultErrorParamErrorCodeTooManyRequests BetaToolSearchToolResultErrorParamErrorCode = "too\_many\_requests"

const BetaToolSearchToolResultErrorParamErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorParamErrorCode = "execution\_time\_exceeded"

Type ToolSearchToolResultError

ErrorMessage stringOptional



type BetaToolSearchToolSearchResultBlock struct{…}



ToolReferences [][BetaToolReferenceBlock](api/beta/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult



type BetaToolSearchToolSearchResultBlockParamResp struct{…}



ToolReferences [][BetaToolReferenceBlockParamResp](api/beta/messages.md)

ToolName string

Type ToolReference



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type ToolSearchToolSearchResult



type BetaToolTextEditor20241022 struct{…}



Name StrReplaceEditor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20241022



AllowedCallers []stringOptional

One of the following:

const BetaToolTextEditor20241022AllowedCallerDirect BetaToolTextEditor20241022AllowedCaller = "direct"

const BetaToolTextEditor20241022AllowedCallerCodeExecution20250825 BetaToolTextEditor20241022AllowedCaller = "code\_execution\_20250825"

const BetaToolTextEditor20241022AllowedCallerCodeExecution20260120 BetaToolTextEditor20241022AllowedCaller = "code\_execution\_20260120"

const BetaToolTextEditor20241022AllowedCallerCodeExecution20260521 BetaToolTextEditor20241022AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolTextEditor20250124 struct{…}



Name StrReplaceEditor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250124



AllowedCallers []stringOptional

One of the following:

const BetaToolTextEditor20250124AllowedCallerDirect BetaToolTextEditor20250124AllowedCaller = "direct"

const BetaToolTextEditor20250124AllowedCallerCodeExecution20250825 BetaToolTextEditor20250124AllowedCaller = "code\_execution\_20250825"

const BetaToolTextEditor20250124AllowedCallerCodeExecution20260120 BetaToolTextEditor20250124AllowedCaller = "code\_execution\_20260120"

const BetaToolTextEditor20250124AllowedCallerCodeExecution20260521 BetaToolTextEditor20250124AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolTextEditor20250429 struct{…}



Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250429



AllowedCallers []stringOptional

One of the following:

const BetaToolTextEditor20250429AllowedCallerDirect BetaToolTextEditor20250429AllowedCaller = "direct"

const BetaToolTextEditor20250429AllowedCallerCodeExecution20250825 BetaToolTextEditor20250429AllowedCaller = "code\_execution\_20250825"

const BetaToolTextEditor20250429AllowedCallerCodeExecution20260120 BetaToolTextEditor20250429AllowedCaller = "code\_execution\_20260120"

const BetaToolTextEditor20250429AllowedCallerCodeExecution20260521 BetaToolTextEditor20250429AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolTextEditor20250728 struct{…}



Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250728



AllowedCallers []stringOptional

One of the following:

const BetaToolTextEditor20250728AllowedCallerDirect BetaToolTextEditor20250728AllowedCaller = "direct"

const BetaToolTextEditor20250728AllowedCallerCodeExecution20250825 BetaToolTextEditor20250728AllowedCaller = "code\_execution\_20250825"

const BetaToolTextEditor20250728AllowedCallerCodeExecution20260120 BetaToolTextEditor20250728AllowedCaller = "code\_execution\_20260120"

const BetaToolTextEditor20250728AllowedCallerCodeExecution20260521 BetaToolTextEditor20250728AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

MaxCharacters int64Optional

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolUnion interface{…}

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

One of the following:



type BetaTool struct{…}



InputSchema BetaToolInputSchema

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

const BetaToolAllowedCallerDirect BetaToolAllowedCaller = "direct"

const BetaToolAllowedCallerCodeExecution20250825 BetaToolAllowedCaller = "code\_execution\_20250825"

const BetaToolAllowedCallerCodeExecution20260120 BetaToolAllowedCaller = "code\_execution\_20260120"

const BetaToolAllowedCallerCodeExecution20260521 BetaToolAllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

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

Type BetaToolTypeOptional



type BetaToolBash20241022 struct{…}



Name Bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Bash20241022



AllowedCallers []stringOptional

One of the following:

const BetaToolBash20241022AllowedCallerDirect BetaToolBash20241022AllowedCaller = "direct"

const BetaToolBash20241022AllowedCallerCodeExecution20250825 BetaToolBash20241022AllowedCaller = "code\_execution\_20250825"

const BetaToolBash20241022AllowedCallerCodeExecution20260120 BetaToolBash20241022AllowedCaller = "code\_execution\_20260120"

const BetaToolBash20241022AllowedCallerCodeExecution20260521 BetaToolBash20241022AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolBash20250124 struct{…}



Name Bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Bash20250124



AllowedCallers []stringOptional

One of the following:

const BetaToolBash20250124AllowedCallerDirect BetaToolBash20250124AllowedCaller = "direct"

const BetaToolBash20250124AllowedCallerCodeExecution20250825 BetaToolBash20250124AllowedCaller = "code\_execution\_20250825"

const BetaToolBash20250124AllowedCallerCodeExecution20260120 BetaToolBash20250124AllowedCaller = "code\_execution\_20260120"

const BetaToolBash20250124AllowedCallerCodeExecution20260521 BetaToolBash20250124AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaCodeExecutionTool20250522 struct{…}



Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250522



AllowedCallers []stringOptional

One of the following:

const BetaCodeExecutionTool20250522AllowedCallerDirect BetaCodeExecutionTool20250522AllowedCaller = "direct"

const BetaCodeExecutionTool20250522AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20250522AllowedCaller = "code\_execution\_20250825"

const BetaCodeExecutionTool20250522AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20250522AllowedCaller = "code\_execution\_20260120"

const BetaCodeExecutionTool20250522AllowedCallerCodeExecution20260521 BetaCodeExecutionTool20250522AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaCodeExecutionTool20250825 struct{…}



Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250825



AllowedCallers []stringOptional

One of the following:

const BetaCodeExecutionTool20250825AllowedCallerDirect BetaCodeExecutionTool20250825AllowedCaller = "direct"

const BetaCodeExecutionTool20250825AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20250825AllowedCaller = "code\_execution\_20250825"

const BetaCodeExecutionTool20250825AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20250825AllowedCaller = "code\_execution\_20260120"

const BetaCodeExecutionTool20250825AllowedCallerCodeExecution20260521 BetaCodeExecutionTool20250825AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaCodeExecutionTool20260120 struct{…}

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20260120



AllowedCallers []stringOptional

One of the following:

const BetaCodeExecutionTool20260120AllowedCallerDirect BetaCodeExecutionTool20260120AllowedCaller = "direct"

const BetaCodeExecutionTool20260120AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20260120AllowedCaller = "code\_execution\_20250825"

const BetaCodeExecutionTool20260120AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20260120AllowedCaller = "code\_execution\_20260120"

const BetaCodeExecutionTool20260120AllowedCallerCodeExecution20260521 BetaCodeExecutionTool20260120AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaCodeExecutionTool20260521 struct{…}

Code execution tool with REPL state persistence.



Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20260521



AllowedCallers []stringOptional

One of the following:

const BetaCodeExecutionTool20260521AllowedCallerDirect BetaCodeExecutionTool20260521AllowedCaller = "direct"

const BetaCodeExecutionTool20260521AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20260521AllowedCaller = "code\_execution\_20250825"

const BetaCodeExecutionTool20260521AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20260521AllowedCaller = "code\_execution\_20260120"

const BetaCodeExecutionTool20260521AllowedCallerCodeExecution20260521 BetaCodeExecutionTool20260521AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolComputerUse20241022 struct{…}

DisplayHeightPx int64

The height of the display in pixels.

DisplayWidthPx int64

The width of the display in pixels.



Name Computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Computer20241022



AllowedCallers []stringOptional

One of the following:

const BetaToolComputerUse20241022AllowedCallerDirect BetaToolComputerUse20241022AllowedCaller = "direct"

const BetaToolComputerUse20241022AllowedCallerCodeExecution20250825 BetaToolComputerUse20241022AllowedCaller = "code\_execution\_20250825"

const BetaToolComputerUse20241022AllowedCallerCodeExecution20260120 BetaToolComputerUse20241022AllowedCaller = "code\_execution\_20260120"

const BetaToolComputerUse20241022AllowedCallerCodeExecution20260521 BetaToolComputerUse20241022AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

DisplayNumber int64Optional

The X11 display number (e.g. 0, 1) for the display.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaMemoryTool20250818 struct{…}



Name Memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Memory20250818



AllowedCallers []stringOptional

One of the following:

const BetaMemoryTool20250818AllowedCallerDirect BetaMemoryTool20250818AllowedCaller = "direct"

const BetaMemoryTool20250818AllowedCallerCodeExecution20250825 BetaMemoryTool20250818AllowedCaller = "code\_execution\_20250825"

const BetaMemoryTool20250818AllowedCallerCodeExecution20260120 BetaMemoryTool20250818AllowedCaller = "code\_execution\_20260120"

const BetaMemoryTool20250818AllowedCallerCodeExecution20260521 BetaMemoryTool20250818AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolComputerUse20250124 struct{…}

DisplayHeightPx int64

The height of the display in pixels.

DisplayWidthPx int64

The width of the display in pixels.



Name Computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Computer20250124



AllowedCallers []stringOptional

One of the following:

const BetaToolComputerUse20250124AllowedCallerDirect BetaToolComputerUse20250124AllowedCaller = "direct"

const BetaToolComputerUse20250124AllowedCallerCodeExecution20250825 BetaToolComputerUse20250124AllowedCaller = "code\_execution\_20250825"

const BetaToolComputerUse20250124AllowedCallerCodeExecution20260120 BetaToolComputerUse20250124AllowedCaller = "code\_execution\_20260120"

const BetaToolComputerUse20250124AllowedCallerCodeExecution20260521 BetaToolComputerUse20250124AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

DisplayNumber int64Optional

The X11 display number (e.g. 0, 1) for the display.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolTextEditor20241022 struct{…}



Name StrReplaceEditor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20241022



AllowedCallers []stringOptional

One of the following:

const BetaToolTextEditor20241022AllowedCallerDirect BetaToolTextEditor20241022AllowedCaller = "direct"

const BetaToolTextEditor20241022AllowedCallerCodeExecution20250825 BetaToolTextEditor20241022AllowedCaller = "code\_execution\_20250825"

const BetaToolTextEditor20241022AllowedCallerCodeExecution20260120 BetaToolTextEditor20241022AllowedCaller = "code\_execution\_20260120"

const BetaToolTextEditor20241022AllowedCallerCodeExecution20260521 BetaToolTextEditor20241022AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolComputerUse20251124 struct{…}

DisplayHeightPx int64

The height of the display in pixels.

DisplayWidthPx int64

The width of the display in pixels.



Name Computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Computer20251124



AllowedCallers []stringOptional

One of the following:

const BetaToolComputerUse20251124AllowedCallerDirect BetaToolComputerUse20251124AllowedCaller = "direct"

const BetaToolComputerUse20251124AllowedCallerCodeExecution20250825 BetaToolComputerUse20251124AllowedCaller = "code\_execution\_20250825"

const BetaToolComputerUse20251124AllowedCallerCodeExecution20260120 BetaToolComputerUse20251124AllowedCaller = "code\_execution\_20260120"

const BetaToolComputerUse20251124AllowedCallerCodeExecution20260521 BetaToolComputerUse20251124AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

DisplayNumber int64Optional

The X11 display number (e.g. 0, 1) for the display.

EnableZoom boolOptional

Whether to enable an action to take a zoomed-in screenshot of the screen.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolTextEditor20250124 struct{…}



Name StrReplaceEditor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250124



AllowedCallers []stringOptional

One of the following:

const BetaToolTextEditor20250124AllowedCallerDirect BetaToolTextEditor20250124AllowedCaller = "direct"

const BetaToolTextEditor20250124AllowedCallerCodeExecution20250825 BetaToolTextEditor20250124AllowedCaller = "code\_execution\_20250825"

const BetaToolTextEditor20250124AllowedCallerCodeExecution20260120 BetaToolTextEditor20250124AllowedCaller = "code\_execution\_20260120"

const BetaToolTextEditor20250124AllowedCallerCodeExecution20260521 BetaToolTextEditor20250124AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolTextEditor20250429 struct{…}



Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250429



AllowedCallers []stringOptional

One of the following:

const BetaToolTextEditor20250429AllowedCallerDirect BetaToolTextEditor20250429AllowedCaller = "direct"

const BetaToolTextEditor20250429AllowedCallerCodeExecution20250825 BetaToolTextEditor20250429AllowedCaller = "code\_execution\_20250825"

const BetaToolTextEditor20250429AllowedCallerCodeExecution20260120 BetaToolTextEditor20250429AllowedCaller = "code\_execution\_20260120"

const BetaToolTextEditor20250429AllowedCallerCodeExecution20260521 BetaToolTextEditor20250429AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolTextEditor20250728 struct{…}



Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250728



AllowedCallers []stringOptional

One of the following:

const BetaToolTextEditor20250728AllowedCallerDirect BetaToolTextEditor20250728AllowedCaller = "direct"

const BetaToolTextEditor20250728AllowedCallerCodeExecution20250825 BetaToolTextEditor20250728AllowedCaller = "code\_execution\_20250825"

const BetaToolTextEditor20250728AllowedCallerCodeExecution20260120 BetaToolTextEditor20250728AllowedCaller = "code\_execution\_20260120"

const BetaToolTextEditor20250728AllowedCallerCodeExecution20260521 BetaToolTextEditor20250728AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

InputExamples []map[string, any]Optional

MaxCharacters int64Optional

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaWebSearchTool20250305 struct{…}



Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20250305



AllowedCallers []stringOptional

One of the following:

const BetaWebSearchTool20250305AllowedCallerDirect BetaWebSearchTool20250305AllowedCaller = "direct"

const BetaWebSearchTool20250305AllowedCallerCodeExecution20250825 BetaWebSearchTool20250305AllowedCaller = "code\_execution\_20250825"

const BetaWebSearchTool20250305AllowedCallerCodeExecution20260120 BetaWebSearchTool20250305AllowedCaller = "code\_execution\_20260120"

const BetaWebSearchTool20250305AllowedCallerCodeExecution20260521 BetaWebSearchTool20250305AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains []stringOptional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



UserLocation [BetaUserLocation](api/beta/messages.md)Optional

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

type BetaWebFetchTool20250910 struct{…}



Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20250910



AllowedCallers []stringOptional

One of the following:

const BetaWebFetchTool20250910AllowedCallerDirect BetaWebFetchTool20250910AllowedCaller = "direct"

const BetaWebFetchTool20250910AllowedCallerCodeExecution20250825 BetaWebFetchTool20250910AllowedCaller = "code\_execution\_20250825"

const BetaWebFetchTool20250910AllowedCallerCodeExecution20260120 BetaWebFetchTool20250910AllowedCaller = "code\_execution\_20260120"

const BetaWebFetchTool20250910AllowedCallerCodeExecution20260521 BetaWebFetchTool20250910AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

List of domains to allow fetching from

BlockedDomains []stringOptional

List of domains to block fetching from



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

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

type BetaWebSearchTool20260209 struct{…}



Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20260209



AllowedCallers []stringOptional

One of the following:

const BetaWebSearchTool20260209AllowedCallerDirect BetaWebSearchTool20260209AllowedCaller = "direct"

const BetaWebSearchTool20260209AllowedCallerCodeExecution20250825 BetaWebSearchTool20260209AllowedCaller = "code\_execution\_20250825"

const BetaWebSearchTool20260209AllowedCallerCodeExecution20260120 BetaWebSearchTool20260209AllowedCaller = "code\_execution\_20260120"

const BetaWebSearchTool20260209AllowedCallerCodeExecution20260521 BetaWebSearchTool20260209AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains []stringOptional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



UserLocation [BetaUserLocation](api/beta/messages.md)Optional

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

type BetaWebFetchTool20260209 struct{…}



Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20260209



AllowedCallers []stringOptional

One of the following:

const BetaWebFetchTool20260209AllowedCallerDirect BetaWebFetchTool20260209AllowedCaller = "direct"

const BetaWebFetchTool20260209AllowedCallerCodeExecution20250825 BetaWebFetchTool20260209AllowedCaller = "code\_execution\_20250825"

const BetaWebFetchTool20260209AllowedCallerCodeExecution20260120 BetaWebFetchTool20260209AllowedCaller = "code\_execution\_20260120"

const BetaWebFetchTool20260209AllowedCallerCodeExecution20260521 BetaWebFetchTool20260209AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

List of domains to allow fetching from

BlockedDomains []stringOptional

List of domains to block fetching from



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

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

type BetaWebFetchTool20260309 struct{…}

Web fetch tool with use\_cache parameter for bypassing cached content.



Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20260309



AllowedCallers []stringOptional

One of the following:

const BetaWebFetchTool20260309AllowedCallerDirect BetaWebFetchTool20260309AllowedCaller = "direct"

const BetaWebFetchTool20260309AllowedCallerCodeExecution20250825 BetaWebFetchTool20260309AllowedCaller = "code\_execution\_20250825"

const BetaWebFetchTool20260309AllowedCallerCodeExecution20260120 BetaWebFetchTool20260309AllowedCaller = "code\_execution\_20260120"

const BetaWebFetchTool20260309AllowedCallerCodeExecution20260521 BetaWebFetchTool20260309AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

List of domains to allow fetching from

BlockedDomains []stringOptional

List of domains to block fetching from



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

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

type BetaWebSearchTool20260318 struct{…}



Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20260318



AllowedCallers []stringOptional

One of the following:

const BetaWebSearchTool20260318AllowedCallerDirect BetaWebSearchTool20260318AllowedCaller = "direct"

const BetaWebSearchTool20260318AllowedCallerCodeExecution20250825 BetaWebSearchTool20260318AllowedCaller = "code\_execution\_20250825"

const BetaWebSearchTool20260318AllowedCallerCodeExecution20260120 BetaWebSearchTool20260318AllowedCaller = "code\_execution\_20260120"

const BetaWebSearchTool20260318AllowedCallerCodeExecution20260521 BetaWebSearchTool20260318AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains []stringOptional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.



ResponseInclusion BetaWebSearchTool20260318ResponseInclusionOptional

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

const BetaWebSearchTool20260318ResponseInclusionFull BetaWebSearchTool20260318ResponseInclusion = "full"

const BetaWebSearchTool20260318ResponseInclusionExcluded BetaWebSearchTool20260318ResponseInclusion = "excluded"

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



UserLocation [BetaUserLocation](api/beta/messages.md)Optional

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

type BetaWebFetchTool20260318 struct{…}



Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20260318



AllowedCallers []stringOptional

One of the following:

const BetaWebFetchTool20260318AllowedCallerDirect BetaWebFetchTool20260318AllowedCaller = "direct"

const BetaWebFetchTool20260318AllowedCallerCodeExecution20250825 BetaWebFetchTool20260318AllowedCaller = "code\_execution\_20250825"

const BetaWebFetchTool20260318AllowedCallerCodeExecution20260120 BetaWebFetchTool20260318AllowedCaller = "code\_execution\_20260120"

const BetaWebFetchTool20260318AllowedCallerCodeExecution20260521 BetaWebFetchTool20260318AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

List of domains to allow fetching from

BlockedDomains []stringOptional

List of domains to block fetching from



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled boolOptional

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxContentTokens int64Optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.



ResponseInclusion BetaWebFetchTool20260318ResponseInclusionOptional

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

const BetaWebFetchTool20260318ResponseInclusionFull BetaWebFetchTool20260318ResponseInclusion = "full"

const BetaWebFetchTool20260318ResponseInclusionExcluded BetaWebFetchTool20260318ResponseInclusion = "excluded"

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

UseCache boolOptional

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



type BetaAdvisorTool20260301 struct{…}

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

Name Advisor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Advisor20260301



AllowedCallers []stringOptional

One of the following:

const BetaAdvisorTool20260301AllowedCallerDirect BetaAdvisorTool20260301AllowedCaller = "direct"

const BetaAdvisorTool20260301AllowedCallerCodeExecution20250825 BetaAdvisorTool20260301AllowedCaller = "code\_execution\_20250825"

const BetaAdvisorTool20260301AllowedCallerCodeExecution20260120 BetaAdvisorTool20260301AllowedCaller = "code\_execution\_20260120"

const BetaAdvisorTool20260301AllowedCallerCodeExecution20260521 BetaAdvisorTool20260301AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Caching [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxTokens int64Optional

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolSearchToolBm25\_20251119 struct{…}



Name ToolSearchToolBm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



Type BetaToolSearchToolBm25\_20251119Type

One of the following:

const BetaToolSearchToolBm25\_20251119TypeToolSearchToolBm25\_20251119 BetaToolSearchToolBm25\_20251119Type = "tool\_search\_tool\_bm25\_20251119"

const BetaToolSearchToolBm25\_20251119TypeToolSearchToolBm25 BetaToolSearchToolBm25\_20251119Type = "tool\_search\_tool\_bm25"



AllowedCallers []stringOptional

One of the following:

const BetaToolSearchToolBm25\_20251119AllowedCallerDirect BetaToolSearchToolBm25\_20251119AllowedCaller = "direct"

const BetaToolSearchToolBm25\_20251119AllowedCallerCodeExecution20250825 BetaToolSearchToolBm25\_20251119AllowedCaller = "code\_execution\_20250825"

const BetaToolSearchToolBm25\_20251119AllowedCallerCodeExecution20260120 BetaToolSearchToolBm25\_20251119AllowedCaller = "code\_execution\_20260120"

const BetaToolSearchToolBm25\_20251119AllowedCallerCodeExecution20260521 BetaToolSearchToolBm25\_20251119AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaToolSearchToolRegex20251119 struct{…}



Name ToolSearchToolRegex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



Type BetaToolSearchToolRegex20251119Type

One of the following:

const BetaToolSearchToolRegex20251119TypeToolSearchToolRegex20251119 BetaToolSearchToolRegex20251119Type = "tool\_search\_tool\_regex\_20251119"

const BetaToolSearchToolRegex20251119TypeToolSearchToolRegex BetaToolSearchToolRegex20251119Type = "tool\_search\_tool\_regex"



AllowedCallers []stringOptional

One of the following:

const BetaToolSearchToolRegex20251119AllowedCallerDirect BetaToolSearchToolRegex20251119AllowedCaller = "direct"

const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20250825 BetaToolSearchToolRegex20251119AllowedCaller = "code\_execution\_20250825"

const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20260120 BetaToolSearchToolRegex20251119AllowedCaller = "code\_execution\_20260120"

const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20260521 BetaToolSearchToolRegex20251119AllowedCaller = "code\_execution\_20260521"



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



type BetaMCPToolset struct{…}

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

MCPServerName string

Name of the MCP server to configure tools for

Type MCPToolset



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Configs map[string, [BetaMCPToolConfig](api/beta/messages.md)]Optional

Configuration overrides for specific tools, keyed by tool name

DeferLoading boolOptional

Enabled boolOptional



DefaultConfig [BetaMCPToolDefaultConfig](api/beta/messages.md)Optional

Default configuration applied to all tools from this server

DeferLoading boolOptional

Enabled boolOptional



type BetaToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse



Caller BetaToolUseBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaToolUseBlockParamResp struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Caller BetaToolUseBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaToolUsesKeep struct{…}

Type ToolUses

Value int64



type BetaToolUsesTrigger struct{…}

Type ToolUses

Value int64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaURLPDFSource struct{…}

Type URL

URL string



type BetaUsage struct{…}



CacheCreation [BetaCacheCreation](api/beta/messages.md)

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



Iterations [BetaIterationsUsage](api/beta/messages.md)

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



type BetaMessageIterationUsage struct{…}

Token usage for a sampling iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type Message

Usage for a sampling iteration



type BetaCompactionIterationUsage struct{…}

Token usage for a compaction iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

Type Compaction

Usage for a compaction iteration



type BetaAdvisorMessageIterationUsage struct{…}

Token usage for an advisor sub-inference iteration.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type AdvisorMessage

Usage for an advisor sub-inference iteration



type BetaFallbackMessageIterationUsage struct{…}

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



CacheCreation [BetaCacheCreation](api/beta/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InputTokens int64

The number of input tokens which were used.

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

OutputTokens int64

The number of output tokens which were used.

Type FallbackMessage

Usage for the fallback-model attempt that served the response

OutputTokens int64

The number of output tokens which were used.



OutputTokensDetails [BetaOutputTokensDetails](api/beta/messages.md)

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

ServerToolUse [BetaServerToolUsage](api/beta/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



ServiceTier BetaUsageServiceTier

If the request used the priority, standard, or batch tier.

One of the following:

const BetaUsageServiceTierStandard BetaUsageServiceTier = "standard"

const BetaUsageServiceTierPriority BetaUsageServiceTier = "priority"

const BetaUsageServiceTierBatch BetaUsageServiceTier = "batch"



Speed BetaUsageSpeed

The inference speed mode used for this request.

One of the following:

const BetaUsageSpeedStandard BetaUsageSpeed = "standard"

const BetaUsageSpeedFast BetaUsageSpeed = "fast"



type BetaUserLocation struct{…}

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

type BetaWebFetchBlock struct{…}



Content [BetaDocumentBlock](api/beta/messages.md)



Citations [BetaCitationConfig](api/beta/messages.md)

Citation configuration for the document

Enabled bool



Source BetaDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

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

type BetaWebFetchBlockParamResp struct{…}



Content [BetaRequestDocumentBlock](api/beta/messages.md)



Source BetaRequestDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text



type BetaContentBlockSource struct{…}



Content BetaContentBlockSourceContentUnion

One of the following:

string



[][BetaContentBlockSourceContentUnion](api/beta/messages.md)

One of the following:



type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type Content



type BetaURLPDFSource struct{…}

Type URL

URL string



type BetaFileDocumentSource struct{…}

FileID string

Type File

Type Document



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

Enabled boolOptional

Context stringOptional

Title stringOptional

Type WebFetchResult

URL string

Fetched content URL

RetrievedAt stringOptional

ISO 8601 timestamp when the content was retrieved



type BetaWebFetchTool20250910 struct{…}



Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20250910



AllowedCallers []stringOptional

One of the following:

const BetaWebFetchTool20250910AllowedCallerDirect BetaWebFetchTool20250910AllowedCaller = "direct"

const BetaWebFetchTool20250910AllowedCallerCodeExecution20250825 BetaWebFetchTool20250910AllowedCaller = "code\_execution\_20250825"

const BetaWebFetchTool20250910AllowedCallerCodeExecution20260120 BetaWebFetchTool20250910AllowedCaller = "code\_execution\_20260120"

const BetaWebFetchTool20250910AllowedCallerCodeExecution20260521 BetaWebFetchTool20250910AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

List of domains to allow fetching from

BlockedDomains []stringOptional

List of domains to block fetching from



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

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

type BetaWebFetchTool20260209 struct{…}



Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20260209



AllowedCallers []stringOptional

One of the following:

const BetaWebFetchTool20260209AllowedCallerDirect BetaWebFetchTool20260209AllowedCaller = "direct"

const BetaWebFetchTool20260209AllowedCallerCodeExecution20250825 BetaWebFetchTool20260209AllowedCaller = "code\_execution\_20250825"

const BetaWebFetchTool20260209AllowedCallerCodeExecution20260120 BetaWebFetchTool20260209AllowedCaller = "code\_execution\_20260120"

const BetaWebFetchTool20260209AllowedCallerCodeExecution20260521 BetaWebFetchTool20260209AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

List of domains to allow fetching from

BlockedDomains []stringOptional

List of domains to block fetching from



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

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

type BetaWebFetchTool20260309 struct{…}

Web fetch tool with use\_cache parameter for bypassing cached content.



Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20260309



AllowedCallers []stringOptional

One of the following:

const BetaWebFetchTool20260309AllowedCallerDirect BetaWebFetchTool20260309AllowedCaller = "direct"

const BetaWebFetchTool20260309AllowedCallerCodeExecution20250825 BetaWebFetchTool20260309AllowedCaller = "code\_execution\_20250825"

const BetaWebFetchTool20260309AllowedCallerCodeExecution20260120 BetaWebFetchTool20260309AllowedCaller = "code\_execution\_20260120"

const BetaWebFetchTool20260309AllowedCallerCodeExecution20260521 BetaWebFetchTool20260309AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

List of domains to allow fetching from

BlockedDomains []stringOptional

List of domains to block fetching from



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

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

type BetaWebFetchTool20260318 struct{…}



Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20260318



AllowedCallers []stringOptional

One of the following:

const BetaWebFetchTool20260318AllowedCallerDirect BetaWebFetchTool20260318AllowedCaller = "direct"

const BetaWebFetchTool20260318AllowedCallerCodeExecution20250825 BetaWebFetchTool20260318AllowedCaller = "code\_execution\_20250825"

const BetaWebFetchTool20260318AllowedCallerCodeExecution20260120 BetaWebFetchTool20260318AllowedCaller = "code\_execution\_20260120"

const BetaWebFetchTool20260318AllowedCallerCodeExecution20260521 BetaWebFetchTool20260318AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

List of domains to allow fetching from

BlockedDomains []stringOptional

List of domains to block fetching from



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled boolOptional

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxContentTokens int64Optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.



ResponseInclusion BetaWebFetchTool20260318ResponseInclusionOptional

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

const BetaWebFetchTool20260318ResponseInclusionFull BetaWebFetchTool20260318ResponseInclusion = "full"

const BetaWebFetchTool20260318ResponseInclusionExcluded BetaWebFetchTool20260318ResponseInclusion = "excluded"

Strict boolOptional

When true, guarantees schema validation on tool names and inputs

UseCache boolOptional

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



type BetaWebFetchToolResultBlock struct{…}



Content BetaWebFetchToolResultBlockContentUnion

One of the following:



type BetaWebFetchToolResultErrorBlock struct{…}



ErrorCode [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotInPriorContext [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_in\_prior\_context"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unavailable"

Type WebFetchToolResultError



type BetaWebFetchBlock struct{…}



Content [BetaDocumentBlock](api/beta/messages.md)



Citations [BetaCitationConfig](api/beta/messages.md)

Citation configuration for the document

Enabled bool



Source BetaDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

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

Caller BetaWebFetchToolResultBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebFetchToolResultBlockParamResp struct{…}



Content BetaWebFetchToolResultBlockParamContentUnionResp

One of the following:



type BetaWebFetchToolResultErrorBlockParamResp struct{…}



ErrorCode [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotInPriorContext [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_in\_prior\_context"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unavailable"

Type WebFetchToolResultError



type BetaWebFetchBlockParamResp struct{…}



Content [BetaRequestDocumentBlock](api/beta/messages.md)



Source BetaRequestDocumentBlockSourceUnion

One of the following:



type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text



type BetaContentBlockSource struct{…}



Content BetaContentBlockSourceContentUnion

One of the following:

string



[][BetaContentBlockSourceContentUnion](api/beta/messages.md)

One of the following:



type BetaTextBlockParamResp struct{…}

Text string

Type Text



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [][BetaTextCitationParamUnionResp](api/beta/messages.md)Optional

One of the following:



type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation



type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation



type BetaCitationContentBlockLocationParamResp struct{…}

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

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type BetaCitationSearchResultLocationParamResp struct{…}

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

type BetaImageBlockParamResp struct{…}



Source BetaImageBlockParamSourceUnionResp

One of the following:



type BetaBase64ImageSource struct{…}

Data string



MediaType BetaBase64ImageSourceMediaType

One of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64



type BetaURLImageSource struct{…}

Type URL

URL string



type BetaFileImageSource struct{…}

FileID string

Type File

Type Image



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type Content



type BetaURLPDFSource struct{…}

Type URL

URL string



type BetaFileDocumentSource struct{…}

FileID string

Type File

Type Document



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Citations [BetaCitationsConfigParamResp](api/beta/messages.md)Optional

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

CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Caller BetaWebFetchToolResultBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebFetchToolResultErrorBlock struct{…}



ErrorCode [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotInPriorContext [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_in\_prior\_context"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unavailable"

Type WebFetchToolResultError



type BetaWebFetchToolResultErrorBlockParamResp struct{…}



ErrorCode [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotInPriorContext [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_in\_prior\_context"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unavailable"

Type WebFetchToolResultError



type BetaWebFetchToolResultErrorCode string

One of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotInPriorContext [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_in\_prior\_context"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta/messages.md) = "unavailable"



type BetaWebSearchResultBlock struct{…}

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string



type BetaWebSearchResultBlockParamResp struct{…}

EncryptedContent string

Title string

Type WebSearchResult

URL string

PageAge stringOptional



type BetaWebSearchTool20250305 struct{…}



Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20250305



AllowedCallers []stringOptional

One of the following:

const BetaWebSearchTool20250305AllowedCallerDirect BetaWebSearchTool20250305AllowedCaller = "direct"

const BetaWebSearchTool20250305AllowedCallerCodeExecution20250825 BetaWebSearchTool20250305AllowedCaller = "code\_execution\_20250825"

const BetaWebSearchTool20250305AllowedCallerCodeExecution20260120 BetaWebSearchTool20250305AllowedCaller = "code\_execution\_20260120"

const BetaWebSearchTool20250305AllowedCallerCodeExecution20260521 BetaWebSearchTool20250305AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains []stringOptional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



UserLocation [BetaUserLocation](api/beta/messages.md)Optional

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

type BetaWebSearchTool20260209 struct{…}



Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20260209



AllowedCallers []stringOptional

One of the following:

const BetaWebSearchTool20260209AllowedCallerDirect BetaWebSearchTool20260209AllowedCaller = "direct"

const BetaWebSearchTool20260209AllowedCallerCodeExecution20250825 BetaWebSearchTool20260209AllowedCaller = "code\_execution\_20250825"

const BetaWebSearchTool20260209AllowedCallerCodeExecution20260120 BetaWebSearchTool20260209AllowedCaller = "code\_execution\_20260120"

const BetaWebSearchTool20260209AllowedCallerCodeExecution20260521 BetaWebSearchTool20260209AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains []stringOptional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



UserLocation [BetaUserLocation](api/beta/messages.md)Optional

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

type BetaWebSearchTool20260318 struct{…}



Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20260318



AllowedCallers []stringOptional

One of the following:

const BetaWebSearchTool20260318AllowedCallerDirect BetaWebSearchTool20260318AllowedCaller = "direct"

const BetaWebSearchTool20260318AllowedCallerCodeExecution20250825 BetaWebSearchTool20260318AllowedCaller = "code\_execution\_20250825"

const BetaWebSearchTool20260318AllowedCallerCodeExecution20260120 BetaWebSearchTool20260318AllowedCaller = "code\_execution\_20260120"

const BetaWebSearchTool20260318AllowedCallerCodeExecution20260521 BetaWebSearchTool20260318AllowedCaller = "code\_execution\_20260521"

AllowedDomains []stringOptional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains []stringOptional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading boolOptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

MaxUses int64Optional

Maximum number of times the tool can be used in the API request.



ResponseInclusion BetaWebSearchTool20260318ResponseInclusionOptional

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

const BetaWebSearchTool20260318ResponseInclusionFull BetaWebSearchTool20260318ResponseInclusion = "full"

const BetaWebSearchTool20260318ResponseInclusionExcluded BetaWebSearchTool20260318ResponseInclusion = "excluded"

Strict boolOptional

When true, guarantees schema validation on tool names and inputs



UserLocation [BetaUserLocation](api/beta/messages.md)Optional

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

type BetaWebSearchToolRequestError struct{…}



ErrorCode [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "request\_too\_large"

Type WebSearchToolResultError



type BetaWebSearchToolResultBlock struct{…}



Content [BetaWebSearchToolResultBlockContentUnion](api/beta/messages.md)

One of the following:



type BetaWebSearchToolResultError struct{…}



ErrorCode [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "request\_too\_large"

Type WebSearchToolResultError



type BetaWebSearchToolResultBlockContentArray [][BetaWebSearchResultBlock](api/beta/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult



Caller BetaWebSearchToolResultBlockCallerUnionOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebSearchToolResultBlockContentUnion interface{…}

One of the following:



type BetaWebSearchToolResultError struct{…}



ErrorCode [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "request\_too\_large"

Type WebSearchToolResultError



type BetaWebSearchToolResultBlockContentArray [][BetaWebSearchResultBlock](api/beta/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string



type BetaWebSearchToolResultBlockParamResp struct{…}



Content [BetaWebSearchToolResultBlockParamContentUnionResp](api/beta/messages.md)

One of the following:



[][BetaWebSearchResultBlockParamResp](api/beta/messages.md)

EncryptedContent string

Title string

Type WebSearchResult

URL string

PageAge stringOptional



type BetaWebSearchToolRequestError struct{…}



ErrorCode [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "request\_too\_large"

Type WebSearchToolResultError

ToolUseID string

Type WebSearchToolResult



CacheControl [BetaCacheControlEphemeral](api/beta/messages.md)Optional

Create a cache control breakpoint at this content block.

Type Ephemeral



TTL BetaCacheControlEphemeralTTLOptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"



Caller BetaWebSearchToolResultBlockParamCallerUnionRespOptional

Tool invocation directly from the model.

One of the following:



type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type BetaServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



type BetaWebSearchToolResultBlockParamContentUnionResp interface{…}

One of the following:



[][BetaWebSearchResultBlockParamResp](api/beta/messages.md)

EncryptedContent string

Title string

Type WebSearchResult

URL string

PageAge stringOptional



type BetaWebSearchToolRequestError struct{…}



ErrorCode [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "request\_too\_large"

Type WebSearchToolResultError



type BetaWebSearchToolResultError struct{…}



ErrorCode [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "request\_too\_large"

Type WebSearchToolResultError



type BetaWebSearchToolResultErrorCode string

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta/messages.md) = "request\_too\_large"

#### MessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

client.Beta.Messages.Batches.New(ctx, params) (\*[BetaMessageBatch](api/beta/messages/batches.md), error)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

client.Beta.Messages.Batches.Get(ctx, messageBatchID, query) (\*[BetaMessageBatch](api/beta/messages/batches.md), error)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

client.Beta.Messages.Batches.List(ctx, params) (\*Page[[BetaMessageBatch](api/beta/messages/batches.md)], error)

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

client.Beta.Messages.Batches.Cancel(ctx, messageBatchID, body) (\*[BetaMessageBatch](api/beta/messages/batches.md), error)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

client.Beta.Messages.Batches.Delete(ctx, messageBatchID, body) (\*[BetaDeletedMessageBatch](api/beta/messages/batches.md), error)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

client.Beta.Messages.Batches.Results(ctx, messageBatchID, query) (\*[BetaMessageBatchIndividualResponse](api/beta/messages/batches.md), error)

GET/v1/messages/batches/{message\_batch\_id}/results

---

*Copyright © Anthropic. All rights reserved.*
