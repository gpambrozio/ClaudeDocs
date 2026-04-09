# Beta

Copy page

C#

# Beta

##### ModelsExpand Collapse

class BetaApiError:

required string Message

JsonElement Type "api\_error"constant

class BetaAuthenticationError:

required string Message

JsonElement Type "authentication\_error"constant

class BetaBillingError:

required string Message

JsonElement Type "billing\_error"constant

class BetaError: A class that can be one of several variants.union

class BetaInvalidRequestError:

required string Message

JsonElement Type "invalid\_request\_error"constant

class BetaAuthenticationError:

required string Message

JsonElement Type "authentication\_error"constant

class BetaBillingError:

required string Message

JsonElement Type "billing\_error"constant

class BetaPermissionError:

required string Message

JsonElement Type "permission\_error"constant

class BetaNotFoundError:

required string Message

JsonElement Type "not\_found\_error"constant

class BetaRateLimitError:

required string Message

JsonElement Type "rate\_limit\_error"constant

class BetaGatewayTimeoutError:

required string Message

JsonElement Type "timeout\_error"constant

class BetaApiError:

required string Message

JsonElement Type "api\_error"constant

class BetaOverloadedError:

required string Message

JsonElement Type "overloaded\_error"constant

class BetaErrorResponse:

required [BetaError](api/beta.md) Error

Accepts one of the following:

class BetaInvalidRequestError:

required string Message

JsonElement Type "invalid\_request\_error"constant

class BetaAuthenticationError:

required string Message

JsonElement Type "authentication\_error"constant

class BetaBillingError:

required string Message

JsonElement Type "billing\_error"constant

class BetaPermissionError:

required string Message

JsonElement Type "permission\_error"constant

class BetaNotFoundError:

required string Message

JsonElement Type "not\_found\_error"constant

class BetaRateLimitError:

required string Message

JsonElement Type "rate\_limit\_error"constant

class BetaGatewayTimeoutError:

required string Message

JsonElement Type "timeout\_error"constant

class BetaApiError:

required string Message

JsonElement Type "api\_error"constant

class BetaOverloadedError:

required string Message

JsonElement Type "overloaded\_error"constant

required string? RequestID

JsonElement Type "error"constant

class BetaGatewayTimeoutError:

required string Message

JsonElement Type "timeout\_error"constant

class BetaInvalidRequestError:

required string Message

JsonElement Type "invalid\_request\_error"constant

class BetaNotFoundError:

required string Message

JsonElement Type "not\_found\_error"constant

class BetaOverloadedError:

required string Message

JsonElement Type "overloaded\_error"constant

class BetaPermissionError:

required string Message

JsonElement Type "permission\_error"constant

class BetaRateLimitError:

required string Message

JsonElement Type "rate\_limit\_error"constant

#### BetaModels

##### [List Models](api/beta/models/list.md)

[ModelListPageResponse](api/beta.md) Beta.Models.List(ModelListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

[BetaModelInfo](api/beta.md) Beta.Models.Retrieve(ModelRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/models/{model\_id}

##### ModelsExpand Collapse

class BetaCapabilitySupport:

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

class BetaContextManagementCapability:

Context management capability details.

required [BetaCapabilitySupport](api/beta.md)? ClearThinking20251015

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md)? ClearToolUses20250919

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md)? Compact20260112

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

class BetaEffortCapability:

Effort (reasoning\_effort) capability details.

required [BetaCapabilitySupport](api/beta.md) High

Whether the model supports high effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) Low

Whether the model supports low effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) Max

Whether the model supports max effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) Medium

Whether the model supports medium effort level.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

class BetaModelCapabilities:

Model capability information.

required [BetaCapabilitySupport](api/beta.md) Batch

Whether the model supports the Batch API.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) Citations

Whether the model supports citation generation.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) CodeExecution

Whether the model supports code execution tools.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaContextManagementCapability](api/beta.md) ContextManagement

Context management support and available strategies.

required [BetaCapabilitySupport](api/beta.md)? ClearThinking20251015

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md)? ClearToolUses20250919

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md)? Compact20260112

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaEffortCapability](api/beta.md) Effort

Effort (reasoning\_effort) support and available levels.

required [BetaCapabilitySupport](api/beta.md) High

Whether the model supports high effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) Low

Whether the model supports low effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) Max

Whether the model supports max effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) Medium

Whether the model supports medium effort level.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) ImageInput

Whether the model accepts image content blocks.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) PdfInput

Whether the model accepts PDF content blocks.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) StructuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaThinkingCapability](api/beta.md) Thinking

Thinking capability and supported type configurations.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaThinkingTypes](api/beta.md) Types

Supported thinking type configurations.

required [BetaCapabilitySupport](api/beta.md) Adaptive

Whether the model supports thinking with type 'adaptive' (auto).

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) Enabled

Whether the model supports thinking with type 'enabled'.

required Boolean Supported

Whether this capability is supported by the model.

class BetaModelInfo:

required string ID

Unique model identifier.

required [BetaModelCapabilities](api/beta.md)? Capabilities

Model capability information.

required [BetaCapabilitySupport](api/beta.md) Batch

Whether the model supports the Batch API.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) Citations

Whether the model supports citation generation.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) CodeExecution

Whether the model supports code execution tools.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaContextManagementCapability](api/beta.md) ContextManagement

Context management support and available strategies.

required [BetaCapabilitySupport](api/beta.md)? ClearThinking20251015

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md)? ClearToolUses20250919

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md)? Compact20260112

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaEffortCapability](api/beta.md) Effort

Effort (reasoning\_effort) support and available levels.

required [BetaCapabilitySupport](api/beta.md) High

Whether the model supports high effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) Low

Whether the model supports low effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) Max

Whether the model supports max effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) Medium

Whether the model supports medium effort level.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) ImageInput

Whether the model accepts image content blocks.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) PdfInput

Whether the model accepts PDF content blocks.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) StructuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaThinkingCapability](api/beta.md) Thinking

Thinking capability and supported type configurations.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaThinkingTypes](api/beta.md) Types

Supported thinking type configurations.

required [BetaCapabilitySupport](api/beta.md) Adaptive

Whether the model supports thinking with type 'adaptive' (auto).

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) Enabled

Whether the model supports thinking with type 'enabled'.

required Boolean Supported

Whether this capability is supported by the model.

required DateTimeOffset CreatedAt

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

required string DisplayName

A human-readable name for the model.

required Long? MaxInputTokens

Maximum input context window size in tokens for this model.

required Long? MaxTokens

Maximum value for the `max_tokens` parameter when using this model.

JsonElement Type "model"constant

Object type.

For Models, this is always `"model"`.

class BetaThinkingCapability:

Thinking capability details.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaThinkingTypes](api/beta.md) Types

Supported thinking type configurations.

required [BetaCapabilitySupport](api/beta.md) Adaptive

Whether the model supports thinking with type 'adaptive' (auto).

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) Enabled

Whether the model supports thinking with type 'enabled'.

required Boolean Supported

Whether this capability is supported by the model.

class BetaThinkingTypes:

Supported thinking type configurations.

required [BetaCapabilitySupport](api/beta.md) Adaptive

Whether the model supports thinking with type 'adaptive' (auto).

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](api/beta.md) Enabled

Whether the model supports thinking with type 'enabled'.

required Boolean Supported

Whether this capability is supported by the model.

#### BetaMessages

##### [Create a Message](api/beta/messages/create.md)

[BetaMessage](api/beta.md) Beta.Messages.Create(MessageCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

[BetaMessageTokensCount](api/beta.md) Beta.Messages.CountTokens(MessageCountTokensParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse

class BetaAllThinkingTurns:

JsonElement Type "all"constant

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaBashCodeExecutionOutputBlock:

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

class BetaBashCodeExecutionOutputBlockParam:

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList<[BetaBashCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

class BetaBashCodeExecutionResultBlockParam:

required IReadOnlyList<[BetaBashCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList<[BetaBashCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlockParam:

required IReadOnlyList<[BetaBashCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant

class BetaCacheControlEphemeral:

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

class BetaCacheCreation:

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationConfig:

required Boolean Enabled

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationsConfigParam:

Boolean Enabled

class BetaCitationsDelta:

required Citation Citation

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

JsonElement Type "citations\_delta"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaClearThinking20251015Edit:

JsonElement Type "clear\_thinking\_20251015"constant

Keep Keep

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns:

JsonElement Type "thinking\_turns"constant

required Long Value

class BetaAllThinkingTurns:

JsonElement Type "all"constant

class All:

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear\_thinking\_20251015"constant

The type of context management edit applied.

class BetaClearToolUses20250919Edit:

JsonElement Type "clear\_tool\_uses\_20250919"constant

[BetaInputTokensClearAtLeast](api/beta.md)? ClearAtLeast

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

JsonElement Type "input\_tokens"constant

required Long Value

ClearToolInputs? ClearToolInputs

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

Boolean

IReadOnlyList<string>

IReadOnlyList<string>? ExcludeTools

Tool names whose uses are preserved from clearing

[BetaToolUsesKeep](api/beta.md) Keep

Number of tool uses to retain in the conversation

JsonElement Type "tool\_uses"constant

required Long Value

Trigger Trigger

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger:

JsonElement Type "input\_tokens"constant

required Long Value

class BetaToolUsesTrigger:

JsonElement Type "tool\_uses"constant

required Long Value

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaCodeExecutionOutputBlock:

required string FileID

JsonElement Type "code\_execution\_output"constant

class BetaCodeExecutionOutputBlockParam:

required string FileID

JsonElement Type "code\_execution\_output"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

class BetaCodeExecutionResultBlockParam:

required IReadOnlyList<[BetaCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

class BetaCodeExecutionTool20250522:

JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20250522"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250825:

JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20250825"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20260120:

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20260120"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant

class BetaCodeExecutionToolResultBlockContent: A class that can be one of several variants.union

Code execution result with encrypted stdout for PFC + web\_search results.

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

class BetaCodeExecutionToolResultBlockParam:

required [BetaCodeExecutionToolResultBlockParamContent](api/beta.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlockParam:

required IReadOnlyList<[BetaCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.

required IReadOnlyList<[BetaCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaCodeExecutionToolResultBlockParamContent: A class that can be one of several variants.union

Code execution result with encrypted stdout for PFC + web\_search results.

class BetaCodeExecutionToolResultErrorParam:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlockParam:

required IReadOnlyList<[BetaCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.

required IReadOnlyList<[BetaCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

enum BetaCodeExecutionToolResultErrorCode:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

class BetaCodeExecutionToolResultErrorParam:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

class BetaCompact20260112Edit:

Automatically compact older context when reaching the configured trigger threshold.

JsonElement Type "compact\_20260112"constant

string? Instructions

Additional instructions for summarization.

Boolean PauseAfterCompaction

Whether to pause after compaction and return the compaction block to the user.

[BetaInputTokensTrigger](api/beta.md)? Trigger

When to trigger compaction. Defaults to 150000 input tokens.

JsonElement Type "input\_tokens"constant

required Long Value

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

required string? Content

Summary of previously compacted content, or null if compaction failed

JsonElement Type "compaction"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaCompactionContentBlockDelta:

required string? Content

JsonElement Type "compaction\_delta"constant

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

class BetaContainer:

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList<[BetaSkill](api/beta.md)>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

class BetaContainerParams:

Container parameters with skills to be loaded.

string? ID

Container id

IReadOnlyList<[BetaSkillParams](api/beta.md)>? Skills

List of skills to load in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

string Version

Skill version or 'latest' for most recent version

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container\_upload"constant

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

required string FileID

JsonElement Type "container\_upload"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaContentBlock: A class that can be one of several variants.union

Response model for a file uploaded to the container.

class BetaTextBlock:

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required Name Name

Accepts one of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](api/beta.md) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[BetaWebSearchResultBlock](api/beta.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](api/beta.md) Content

required [BetaCitationConfig](api/beta.md)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList<[BetaBashCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList<[BetaToolReferenceBlock](api/beta.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaTextBlock](api/beta.md)>

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

class BetaContentBlockParam: A class that can be one of several variants.union

Regular text content.

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaRequestDocumentBlock:

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Boolean Enabled

string? Context

string? Title

class BetaSearchResultBlockParam:

required IReadOnlyList<[BetaTextBlockParam](api/beta.md)> Content

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

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

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md) Citations

Boolean Enabled

class BetaThinkingBlockParam:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlockParam:

required string Data

JsonElement Type "redacted\_thinking"constant

class BetaToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaToolResultBlockParam:

required string ToolUseID

JsonElement Type "tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaSearchResultBlockParam:

required IReadOnlyList<[BetaTextBlockParam](api/beta.md)> Content

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

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

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md) Citations

Boolean Enabled

class BetaRequestDocumentBlock:

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Boolean Enabled

string? Context

string? Title

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

required string ToolName

JsonElement Type "tool\_reference"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean IsError

class BetaServerToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required Name Name

Accepts one of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebSearchToolResultBlockParam:

required [BetaWebSearchToolResultBlockParamContent](api/beta.md) Content

Accepts one of the following:

IReadOnlyList<[BetaWebSearchResultBlockParam](api/beta.md)>

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge

class BetaWebSearchToolRequestError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

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

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebFetchToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam:

required [BetaWebFetchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlockParam:

required [BetaRequestDocumentBlock](api/beta.md) Content

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Boolean Enabled

string? Context

string? Title

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaCodeExecutionToolResultBlockParam:

required [BetaCodeExecutionToolResultBlockParamContent](api/beta.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlockParam:

required IReadOnlyList<[BetaCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.

required IReadOnlyList<[BetaCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaBashCodeExecutionToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlockParam:

required IReadOnlyList<[BetaBashCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaTextEditorCodeExecutionToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

string? ErrorMessage

class BetaTextEditorCodeExecutionViewResultBlockParam:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

Long? NumLines

Long? StartLine

Long? TotalLines

class BetaTextEditorCodeExecutionCreateResultBlockParam:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

IReadOnlyList<string>? Lines

Long? NewLines

Long? NewStart

Long? OldLines

Long? OldStart

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaToolSearchToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlockParam:

required IReadOnlyList<[BetaToolReferenceBlockParam](api/beta.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaMcpToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

required string ServerName

The name of the MCP server

JsonElement Type "mcp\_tool\_use"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaRequestMcpToolResultBlockParam:

required string ToolUseID

JsonElement Type "mcp\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextBlockParam](api/beta.md)>

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

Boolean IsError

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

required string FileID

JsonElement Type "container\_upload"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

required string? Content

Summary of previously compacted content, or null if compaction failed

JsonElement Type "compaction"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaContentBlockSourceContent: A class that can be one of several variants.union

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaContextManagementConfig:

IReadOnlyList<Edit> Edits

List of context management edits to apply

Accepts one of the following:

class BetaClearToolUses20250919Edit:

JsonElement Type "clear\_tool\_uses\_20250919"constant

[BetaInputTokensClearAtLeast](api/beta.md)? ClearAtLeast

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

JsonElement Type "input\_tokens"constant

required Long Value

ClearToolInputs? ClearToolInputs

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

Boolean

IReadOnlyList<string>

IReadOnlyList<string>? ExcludeTools

Tool names whose uses are preserved from clearing

[BetaToolUsesKeep](api/beta.md) Keep

Number of tool uses to retain in the conversation

JsonElement Type "tool\_uses"constant

required Long Value

Trigger Trigger

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger:

JsonElement Type "input\_tokens"constant

required Long Value

class BetaToolUsesTrigger:

JsonElement Type "tool\_uses"constant

required Long Value

class BetaClearThinking20251015Edit:

JsonElement Type "clear\_thinking\_20251015"constant

Keep Keep

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns:

JsonElement Type "thinking\_turns"constant

required Long Value

class BetaAllThinkingTurns:

JsonElement Type "all"constant

class All:

class BetaCompact20260112Edit:

Automatically compact older context when reaching the configured trigger threshold.

JsonElement Type "compact\_20260112"constant

string? Instructions

Additional instructions for summarization.

Boolean PauseAfterCompaction

Whether to pause after compaction and return the compaction block to the user.

[BetaInputTokensTrigger](api/beta.md)? Trigger

When to trigger compaction. Defaults to 150000 input tokens.

JsonElement Type "input\_tokens"constant

required Long Value

class BetaContextManagementResponse:

required IReadOnlyList<AppliedEdit> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear\_thinking\_20251015"constant

The type of context management edit applied.

class BetaCountTokensContextManagementResponse:

required Long OriginalInputTokens

The original token count before context management was applied

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaDocumentBlock:

required [BetaCitationConfig](api/beta.md)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.

required IReadOnlyList<[BetaCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaInputJsonDelta:

required string PartialJson

JsonElement Type "input\_json\_delta"constant

class BetaInputTokensClearAtLeast:

JsonElement Type "input\_tokens"constant

required Long Value

class BetaInputTokensTrigger:

JsonElement Type "input\_tokens"constant

required Long Value

class BetaJsonOutputFormat:

required IReadOnlyDictionary<string, JsonElement> Schema

The JSON schema of the format

JsonElement Type "json\_schema"constant

class BetaMcpToolConfig:

Configuration for a specific tool in an MCP toolset.

Boolean DeferLoading

Boolean Enabled

class BetaMcpToolDefaultConfig:

Default configuration for tools in an MCP toolset.

Boolean DeferLoading

Boolean Enabled

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaTextBlock](api/beta.md)>

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp\_tool\_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp\_tool\_use"constant

class BetaMcpToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

required string ServerName

The name of the MCP server

JsonElement Type "mcp\_tool\_use"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaMcpToolset:

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

required string McpServerName

Name of the MCP server to configure tools for

JsonElement Type "mcp\_toolset"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyDictionary<string, [BetaMcpToolConfig](api/beta.md)>? Configs

Configuration overrides for specific tools, keyed by tool name

Boolean DeferLoading

Boolean Enabled

[BetaMcpToolDefaultConfig](api/beta.md) DefaultConfig

Default configuration applied to all tools from this server

Boolean DeferLoading

Boolean Enabled

class BetaMemoryTool20250818:

JsonElement Name "memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "memory\_20250818"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaMemoryTool20250818Command: A class that can be one of several variants.union

class BetaMemoryTool20250818ViewCommand:

JsonElement Command "view"constant

Command type identifier

required string Path

Path to directory or file to view

IReadOnlyList<Long> ViewRange

Optional line range for viewing specific lines

class BetaMemoryTool20250818CreateCommand:

JsonElement Command "create"constant

Command type identifier

required string FileText

Content to write to the file

required string Path

Path where the file should be created

class BetaMemoryTool20250818StrReplaceCommand:

JsonElement Command "str\_replace"constant

Command type identifier

required string NewStr

Text to replace with

required string OldStr

Text to search for and replace

required string Path

Path to the file where text should be replaced

class BetaMemoryTool20250818InsertCommand:

JsonElement Command "insert"constant

Command type identifier

required Long InsertLine

Line number where text should be inserted

required string InsertText

Text to insert at the specified line

required string Path

Path to the file where text should be inserted

class BetaMemoryTool20250818DeleteCommand:

JsonElement Command "delete"constant

Command type identifier

required string Path

Path to the file or directory to delete

class BetaMemoryTool20250818RenameCommand:

JsonElement Command "rename"constant

Command type identifier

required string NewPath

New path for the file or directory

required string OldPath

Current path of the file or directory

class BetaMemoryTool20250818CreateCommand:

JsonElement Command "create"constant

Command type identifier

required string FileText

Content to write to the file

required string Path

Path where the file should be created

class BetaMemoryTool20250818DeleteCommand:

JsonElement Command "delete"constant

Command type identifier

required string Path

Path to the file or directory to delete

class BetaMemoryTool20250818InsertCommand:

JsonElement Command "insert"constant

Command type identifier

required Long InsertLine

Line number where text should be inserted

required string InsertText

Text to insert at the specified line

required string Path

Path to the file where text should be inserted

class BetaMemoryTool20250818RenameCommand:

JsonElement Command "rename"constant

Command type identifier

required string NewPath

New path for the file or directory

required string OldPath

Current path of the file or directory

class BetaMemoryTool20250818StrReplaceCommand:

JsonElement Command "str\_replace"constant

Command type identifier

required string NewStr

Text to replace with

required string OldStr

Text to search for and replace

required string Path

Path to the file where text should be replaced

class BetaMemoryTool20250818ViewCommand:

JsonElement Command "view"constant

Command type identifier

required string Path

Path to directory or file to view

IReadOnlyList<Long> ViewRange

Optional line range for viewing specific lines

class BetaMessage:

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required [BetaContainer](api/beta.md)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList<[BetaSkill](api/beta.md)>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

required IReadOnlyList<[BetaContentBlock](api/beta.md)> Content

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

class BetaTextBlock:

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required Name Name

Accepts one of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](api/beta.md) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[BetaWebSearchResultBlock](api/beta.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](api/beta.md) Content

required [BetaCitationConfig](api/beta.md)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList<[BetaBashCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList<[BetaToolReferenceBlock](api/beta.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaTextBlock](api/beta.md)>

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

required [BetaContextManagementResponse](api/beta.md)? ContextManagement

Context management response.

Information about context management strategies applied during the request.

required IReadOnlyList<AppliedEdit> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear\_thinking\_20251015"constant

The type of context management edit applied.

required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-mythos-preview"ClaudeMythosPreview

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"ClaudeOpus4\_6

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

"claude-opus-4-1"ClaudeOpus4\_1

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Exceptional model for specialized complex tasks

"claude-opus-4-0"ClaudeOpus4\_0

Powerful model for complex tasks

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Powerful model for complex tasks

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Fast and cost-effective model

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [BetaRefusalStopDetails](api/beta.md)? StopDetails

Structured information about a refusal.

required Category? Category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"Cyber

"bio"Bio

required string? Explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonElement Type "refusal"constant

required [BetaStopReason](api/beta.md)? StopReason

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

"compaction"Compaction

"refusal"Refusal

"model\_context\_window\_exceeded"ModelContextWindowExceeded

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [BetaUsage](api/beta.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [BetaCacheCreation](api/beta.md)? CacheCreation

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

required IReadOnlyList<BetaIterationsUsageItems>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The number of output tokens which were used.

required [BetaServerToolUsage](api/beta.md)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

required Speed? Speed

The inference speed mode used for this request.

Accepts one of the following:

"standard"Standard

"fast"Fast

class BetaMessageDeltaUsage:

required Long? CacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The cumulative number of input tokens read from the cache.

required Long? InputTokens

The cumulative number of input tokens which were used.

required IReadOnlyList<BetaIterationsUsageItems>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The cumulative number of output tokens which were used.

required [BetaServerToolUsage](api/beta.md)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaMessageParam:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaContentBlockParam](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaRequestDocumentBlock:

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Boolean Enabled

string? Context

string? Title

class BetaSearchResultBlockParam:

required IReadOnlyList<[BetaTextBlockParam](api/beta.md)> Content

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

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

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md) Citations

Boolean Enabled

class BetaThinkingBlockParam:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlockParam:

required string Data

JsonElement Type "redacted\_thinking"constant

class BetaToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaToolResultBlockParam:

required string ToolUseID

JsonElement Type "tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaSearchResultBlockParam:

required IReadOnlyList<[BetaTextBlockParam](api/beta.md)> Content

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

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

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md) Citations

Boolean Enabled

class BetaRequestDocumentBlock:

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Boolean Enabled

string? Context

string? Title

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

required string ToolName

JsonElement Type "tool\_reference"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean IsError

class BetaServerToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required Name Name

Accepts one of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebSearchToolResultBlockParam:

required [BetaWebSearchToolResultBlockParamContent](api/beta.md) Content

Accepts one of the following:

IReadOnlyList<[BetaWebSearchResultBlockParam](api/beta.md)>

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge

class BetaWebSearchToolRequestError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

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

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebFetchToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam:

required [BetaWebFetchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlockParam:

required [BetaRequestDocumentBlock](api/beta.md) Content

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Boolean Enabled

string? Context

string? Title

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaCodeExecutionToolResultBlockParam:

required [BetaCodeExecutionToolResultBlockParamContent](api/beta.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlockParam:

required IReadOnlyList<[BetaCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.

required IReadOnlyList<[BetaCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaBashCodeExecutionToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlockParam:

required IReadOnlyList<[BetaBashCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaTextEditorCodeExecutionToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

string? ErrorMessage

class BetaTextEditorCodeExecutionViewResultBlockParam:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

Long? NumLines

Long? StartLine

Long? TotalLines

class BetaTextEditorCodeExecutionCreateResultBlockParam:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

IReadOnlyList<string>? Lines

Long? NewLines

Long? NewStart

Long? OldLines

Long? OldStart

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaToolSearchToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlockParam:

required IReadOnlyList<[BetaToolReferenceBlockParam](api/beta.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaMcpToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

required string ServerName

The name of the MCP server

JsonElement Type "mcp\_tool\_use"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaRequestMcpToolResultBlockParam:

required string ToolUseID

JsonElement Type "mcp\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextBlockParam](api/beta.md)>

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

Boolean IsError

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

required string FileID

JsonElement Type "container\_upload"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

required string? Content

Summary of previously compacted content, or null if compaction failed

JsonElement Type "compaction"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaMessageTokensCount:

required [BetaCountTokensContextManagementResponse](api/beta.md)? ContextManagement

Information about context management applied to the message.

required Long OriginalInputTokens

The original token count before context management was applied

required Long InputTokens

The total number of tokens across the provided list of messages, system prompt, and tools.

class BetaMetadata:

string? UserID

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512

class BetaOutputConfig:

Effort? Effort

All possible effort levels.

Accepts one of the following:

"low"Low

"medium"Medium

"high"High

"max"Max

[BetaJsonOutputFormat](api/beta.md)? Format

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

required IReadOnlyDictionary<string, JsonElement> Schema

The JSON schema of the format

JsonElement Type "json\_schema"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaRawContentBlockDelta: A class that can be one of several variants.union

class BetaTextDelta:

required string Text

JsonElement Type "text\_delta"constant

class BetaInputJsonDelta:

required string PartialJson

JsonElement Type "input\_json\_delta"constant

class BetaCitationsDelta:

required Citation Citation

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

JsonElement Type "citations\_delta"constant

class BetaThinkingDelta:

required string Thinking

JsonElement Type "thinking\_delta"constant

class BetaSignatureDelta:

required string Signature

JsonElement Type "signature\_delta"constant

class BetaCompactionContentBlockDelta:

required string? Content

JsonElement Type "compaction\_delta"constant

class BetaRawContentBlockDeltaEvent:

required [BetaRawContentBlockDelta](api/beta.md) Delta

Accepts one of the following:

class BetaTextDelta:

required string Text

JsonElement Type "text\_delta"constant

class BetaInputJsonDelta:

required string PartialJson

JsonElement Type "input\_json\_delta"constant

class BetaCitationsDelta:

required Citation Citation

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

JsonElement Type "citations\_delta"constant

class BetaThinkingDelta:

required string Thinking

JsonElement Type "thinking\_delta"constant

class BetaSignatureDelta:

required string Signature

JsonElement Type "signature\_delta"constant

class BetaCompactionContentBlockDelta:

required string? Content

JsonElement Type "compaction\_delta"constant

required Long Index

JsonElement Type "content\_block\_delta"constant

class BetaRawContentBlockStartEvent:

required ContentBlock ContentBlock

Response model for a file uploaded to the container.

Accepts one of the following:

class BetaTextBlock:

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required Name Name

Accepts one of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](api/beta.md) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[BetaWebSearchResultBlock](api/beta.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](api/beta.md) Content

required [BetaCitationConfig](api/beta.md)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList<[BetaBashCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList<[BetaToolReferenceBlock](api/beta.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaTextBlock](api/beta.md)>

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

required Long Index

JsonElement Type "content\_block\_start"constant

class BetaRawContentBlockStopEvent:

required Long Index

JsonElement Type "content\_block\_stop"constant

class BetaRawMessageDeltaEvent:

required [BetaContextManagementResponse](api/beta.md)? ContextManagement

Information about context management strategies applied during the request

required IReadOnlyList<AppliedEdit> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear\_thinking\_20251015"constant

The type of context management edit applied.

required Delta Delta

required [BetaContainer](api/beta.md)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList<[BetaSkill](api/beta.md)>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

required [BetaRefusalStopDetails](api/beta.md)? StopDetails

Structured information about a refusal.

required Category? Category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"Cyber

"bio"Bio

required string? Explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonElement Type "refusal"constant

required [BetaStopReason](api/beta.md)? StopReason

Accepts one of the following:

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"compaction"Compaction

"refusal"Refusal

"model\_context\_window\_exceeded"ModelContextWindowExceeded

required string? StopSequence

JsonElement Type "message\_delta"constant

required [BetaMessageDeltaUsage](api/beta.md) Usage

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

required IReadOnlyList<BetaIterationsUsageItems>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The cumulative number of output tokens which were used.

required [BetaServerToolUsage](api/beta.md)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

class BetaRawMessageStartEvent:

required [BetaMessage](api/beta.md) Message

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required [BetaContainer](api/beta.md)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList<[BetaSkill](api/beta.md)>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

required IReadOnlyList<[BetaContentBlock](api/beta.md)> Content

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

class BetaTextBlock:

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required Name Name

Accepts one of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](api/beta.md) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[BetaWebSearchResultBlock](api/beta.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](api/beta.md) Content

required [BetaCitationConfig](api/beta.md)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList<[BetaBashCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList<[BetaToolReferenceBlock](api/beta.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaTextBlock](api/beta.md)>

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

required [BetaContextManagementResponse](api/beta.md)? ContextManagement

Context management response.

Information about context management strategies applied during the request.

required IReadOnlyList<AppliedEdit> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear\_thinking\_20251015"constant

The type of context management edit applied.

required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-mythos-preview"ClaudeMythosPreview

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"ClaudeOpus4\_6

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

"claude-opus-4-1"ClaudeOpus4\_1

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Exceptional model for specialized complex tasks

"claude-opus-4-0"ClaudeOpus4\_0

Powerful model for complex tasks

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Powerful model for complex tasks

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Fast and cost-effective model

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [BetaRefusalStopDetails](api/beta.md)? StopDetails

Structured information about a refusal.

required Category? Category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"Cyber

"bio"Bio

required string? Explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonElement Type "refusal"constant

required [BetaStopReason](api/beta.md)? StopReason

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

"compaction"Compaction

"refusal"Refusal

"model\_context\_window\_exceeded"ModelContextWindowExceeded

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [BetaUsage](api/beta.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [BetaCacheCreation](api/beta.md)? CacheCreation

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

required IReadOnlyList<BetaIterationsUsageItems>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The number of output tokens which were used.

required [BetaServerToolUsage](api/beta.md)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

required Speed? Speed

The inference speed mode used for this request.

Accepts one of the following:

"standard"Standard

"fast"Fast

JsonElement Type "message\_start"constant

class BetaRawMessageStopEvent:

JsonElement Type "message\_stop"constant

class BetaRawMessageStreamEvent: A class that can be one of several variants.union

class BetaRawMessageStartEvent:

required [BetaMessage](api/beta.md) Message

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required [BetaContainer](api/beta.md)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList<[BetaSkill](api/beta.md)>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

required IReadOnlyList<[BetaContentBlock](api/beta.md)> Content

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

class BetaTextBlock:

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required Name Name

Accepts one of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](api/beta.md) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[BetaWebSearchResultBlock](api/beta.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](api/beta.md) Content

required [BetaCitationConfig](api/beta.md)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList<[BetaBashCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList<[BetaToolReferenceBlock](api/beta.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaTextBlock](api/beta.md)>

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

required [BetaContextManagementResponse](api/beta.md)? ContextManagement

Context management response.

Information about context management strategies applied during the request.

required IReadOnlyList<AppliedEdit> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear\_thinking\_20251015"constant

The type of context management edit applied.

required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-mythos-preview"ClaudeMythosPreview

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"ClaudeOpus4\_6

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

"claude-opus-4-1"ClaudeOpus4\_1

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Exceptional model for specialized complex tasks

"claude-opus-4-0"ClaudeOpus4\_0

Powerful model for complex tasks

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Powerful model for complex tasks

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Fast and cost-effective model

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [BetaRefusalStopDetails](api/beta.md)? StopDetails

Structured information about a refusal.

required Category? Category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"Cyber

"bio"Bio

required string? Explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonElement Type "refusal"constant

required [BetaStopReason](api/beta.md)? StopReason

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

"compaction"Compaction

"refusal"Refusal

"model\_context\_window\_exceeded"ModelContextWindowExceeded

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [BetaUsage](api/beta.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [BetaCacheCreation](api/beta.md)? CacheCreation

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

required IReadOnlyList<BetaIterationsUsageItems>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The number of output tokens which were used.

required [BetaServerToolUsage](api/beta.md)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

required Speed? Speed

The inference speed mode used for this request.

Accepts one of the following:

"standard"Standard

"fast"Fast

JsonElement Type "message\_start"constant

class BetaRawMessageDeltaEvent:

required [BetaContextManagementResponse](api/beta.md)? ContextManagement

Information about context management strategies applied during the request

required IReadOnlyList<AppliedEdit> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear\_thinking\_20251015"constant

The type of context management edit applied.

required Delta Delta

required [BetaContainer](api/beta.md)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList<[BetaSkill](api/beta.md)>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

required [BetaRefusalStopDetails](api/beta.md)? StopDetails

Structured information about a refusal.

required Category? Category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"Cyber

"bio"Bio

required string? Explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonElement Type "refusal"constant

required [BetaStopReason](api/beta.md)? StopReason

Accepts one of the following:

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"compaction"Compaction

"refusal"Refusal

"model\_context\_window\_exceeded"ModelContextWindowExceeded

required string? StopSequence

JsonElement Type "message\_delta"constant

required [BetaMessageDeltaUsage](api/beta.md) Usage

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

required IReadOnlyList<BetaIterationsUsageItems>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The cumulative number of output tokens which were used.

required [BetaServerToolUsage](api/beta.md)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

class BetaRawMessageStopEvent:

JsonElement Type "message\_stop"constant

class BetaRawContentBlockStartEvent:

required ContentBlock ContentBlock

Response model for a file uploaded to the container.

Accepts one of the following:

class BetaTextBlock:

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required Name Name

Accepts one of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](api/beta.md) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[BetaWebSearchResultBlock](api/beta.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](api/beta.md) Content

required [BetaCitationConfig](api/beta.md)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList<[BetaBashCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList<[BetaToolReferenceBlock](api/beta.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaTextBlock](api/beta.md)>

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

required Long Index

JsonElement Type "content\_block\_start"constant

class BetaRawContentBlockDeltaEvent:

required [BetaRawContentBlockDelta](api/beta.md) Delta

Accepts one of the following:

class BetaTextDelta:

required string Text

JsonElement Type "text\_delta"constant

class BetaInputJsonDelta:

required string PartialJson

JsonElement Type "input\_json\_delta"constant

class BetaCitationsDelta:

required Citation Citation

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

JsonElement Type "citations\_delta"constant

class BetaThinkingDelta:

required string Thinking

JsonElement Type "thinking\_delta"constant

class BetaSignatureDelta:

required string Signature

JsonElement Type "signature\_delta"constant

class BetaCompactionContentBlockDelta:

required string? Content

JsonElement Type "compaction\_delta"constant

required Long Index

JsonElement Type "content\_block\_delta"constant

class BetaRawContentBlockStopEvent:

required Long Index

JsonElement Type "content\_block\_stop"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class BetaRedactedThinkingBlockParam:

required string Data

JsonElement Type "redacted\_thinking"constant

class BetaRefusalStopDetails:

Structured information about a refusal.

required Category? Category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"Cyber

"bio"Bio

required string? Explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonElement Type "refusal"constant

class BetaRequestDocumentBlock:

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Boolean Enabled

string? Context

string? Title

class BetaRequestMcpServerToolConfiguration:

IReadOnlyList<string>? AllowedTools

Boolean? Enabled

class BetaRequestMcpServerUrlDefinition:

required string Name

JsonElement Type "url"constant

required string Url

string? AuthorizationToken

[BetaRequestMcpServerToolConfiguration](api/beta.md)? ToolConfiguration

IReadOnlyList<string>? AllowedTools

Boolean? Enabled

class BetaRequestMcpToolResultBlockParam:

required string ToolUseID

JsonElement Type "mcp\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextBlockParam](api/beta.md)>

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

Boolean IsError

class BetaSearchResultBlockParam:

required IReadOnlyList<[BetaTextBlockParam](api/beta.md)> Content

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

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

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md) Citations

Boolean Enabled

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaServerToolUsage:

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required Name Name

Accepts one of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaServerToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required Name Name

Accepts one of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaSignatureDelta:

required string Signature

JsonElement Type "signature\_delta"constant

class BetaSkill:

A skill that was loaded in a container (response model).

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

class BetaSkillParams:

Specification for a skill to be loaded in a container (request model).

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

string Version

Skill version or 'latest' for most recent version

enum BetaStopReason:

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"compaction"Compaction

"refusal"Refusal

"model\_context\_window\_exceeded"ModelContextWindowExceeded

class BetaTextBlock:

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaTextCitation: A class that can be one of several variants.union

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaTextCitationParam: A class that can be one of several variants.union

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaTextDelta:

required string Text

JsonElement Type "text\_delta"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlockParam:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

IReadOnlyList<string>? Lines

Long? NewLines

Long? NewStart

Long? OldLines

Long? OldStart

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

string? ErrorMessage

class BetaTextEditorCodeExecutionViewResultBlockParam:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

Long? NumLines

Long? StartLine

Long? TotalLines

class BetaTextEditorCodeExecutionCreateResultBlockParam:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

IReadOnlyList<string>? Lines

Long? NewLines

Long? NewStart

Long? OldLines

Long? OldStart

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

string? ErrorMessage

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionViewResultBlockParam:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

Long? NumLines

Long? StartLine

Long? TotalLines

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaThinkingBlockParam:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaThinkingConfigAdaptive:

JsonElement Type "adaptive"constant

Display? Display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

"summarized"Summarized

"omitted"Omitted

class BetaThinkingConfigDisabled:

JsonElement Type "disabled"constant

class BetaThinkingConfigEnabled:

required Long BudgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

JsonElement Type "enabled"constant

Display? Display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

"summarized"Summarized

"omitted"Omitted

class BetaThinkingConfigParam: A class that can be one of several variants.union

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

class BetaThinkingConfigEnabled:

required Long BudgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

JsonElement Type "enabled"constant

Display? Display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

"summarized"Summarized

"omitted"Omitted

class BetaThinkingConfigDisabled:

JsonElement Type "disabled"constant

class BetaThinkingConfigAdaptive:

JsonElement Type "adaptive"constant

Display? Display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

"summarized"Summarized

"omitted"Omitted

class BetaThinkingDelta:

required string Thinking

JsonElement Type "thinking\_delta"constant

class BetaThinkingTurns:

JsonElement Type "thinking\_turns"constant

required Long Value

class BetaTool:

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

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

string Description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Boolean? EagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Type? Type

class BetaToolBash20241022:

JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash\_20241022"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolBash20250124:

JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash\_20250124"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolChoice: A class that can be one of several variants.union

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

class BetaToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonElement Type "auto"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceAny:

The model will use any available tools.

JsonElement Type "any"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

required string Name

The name of the tool to use.

JsonElement Type "tool"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceNone:

The model will not be allowed to use tools.

JsonElement Type "none"constant

class BetaToolChoiceAny:

The model will use any available tools.

JsonElement Type "any"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonElement Type "auto"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceNone:

The model will not be allowed to use tools.

JsonElement Type "none"constant

class BetaToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

required string Name

The name of the tool to use.

JsonElement Type "tool"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolComputerUse20241022:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.

JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer\_20241022"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20250124:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.

JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer\_20250124"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20251124:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.

JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer\_20251124"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

Boolean EnableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolReferenceBlock:

required string ToolName

JsonElement Type "tool\_reference"constant

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

required string ToolName

JsonElement Type "tool\_reference"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaToolResultBlockParam:

required string ToolUseID

JsonElement Type "tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaSearchResultBlockParam:

required IReadOnlyList<[BetaTextBlockParam](api/beta.md)> Content

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

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

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md) Citations

Boolean Enabled

class BetaRequestDocumentBlock:

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Boolean Enabled

string? Context

string? Title

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

required string ToolName

JsonElement Type "tool\_reference"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean IsError

class BetaToolSearchToolBm25\_20251119:

JsonElement Name "tool\_search\_tool\_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

required Type Type

Accepts one of the following:

"tool\_search\_tool\_bm25\_20251119"ToolSearchToolBm25\_20251119

"tool\_search\_tool\_bm25"ToolSearchToolBm25

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolRegex20251119:

JsonElement Name "tool\_search\_tool\_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

required Type Type

Accepts one of the following:

"tool\_search\_tool\_regex\_20251119"ToolSearchToolRegex20251119

"tool\_search\_tool\_regex"ToolSearchToolRegex

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList<[BetaToolReferenceBlock](api/beta.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant

class BetaToolSearchToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlockParam:

required IReadOnlyList<[BetaToolReferenceBlockParam](api/beta.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList<[BetaToolReferenceBlock](api/beta.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

class BetaToolSearchToolSearchResultBlockParam:

required IReadOnlyList<[BetaToolReferenceBlockParam](api/beta.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

JsonElement Type "tool\_search\_tool\_search\_result"constant

class BetaToolTextEditor20241022:

JsonElement Name "str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20241022"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250124:

JsonElement Name "str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250124"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250429:

JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250429"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250728:

JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250728"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Long? MaxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolUnion: A class that can be one of several variants.union

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

class BetaTool:

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

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

string Description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Boolean? EagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Type? Type

class BetaToolBash20241022:

JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash\_20241022"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolBash20250124:

JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash\_20250124"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250522:

JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20250522"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250825:

JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20250825"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20260120:

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20260120"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20241022:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.

JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer\_20241022"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaMemoryTool20250818:

JsonElement Name "memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "memory\_20250818"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20250124:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.

JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer\_20250124"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20241022:

JsonElement Name "str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20241022"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20251124:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.

JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer\_20251124"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

Boolean EnableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250124:

JsonElement Name "str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250124"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250429:

JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250429"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250728:

JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250728"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Long? MaxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaWebSearchTool20250305:

JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20250305"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

[BetaUserLocation](api/beta.md)? UserLocation

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

class BetaWebFetchTool20250910:

JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20250910"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaWebSearchTool20260209:

JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20260209"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

[BetaUserLocation](api/beta.md)? UserLocation

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

class BetaWebFetchTool20260209:

JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20260209"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaWebFetchTool20260309:

Web fetch tool with use\_cache parameter for bypassing cached content.

JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20260309"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Boolean UseCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

class BetaToolSearchToolBm25\_20251119:

JsonElement Name "tool\_search\_tool\_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

required Type Type

Accepts one of the following:

"tool\_search\_tool\_bm25\_20251119"ToolSearchToolBm25\_20251119

"tool\_search\_tool\_bm25"ToolSearchToolBm25

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolRegex20251119:

JsonElement Name "tool\_search\_tool\_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

required Type Type

Accepts one of the following:

"tool\_search\_tool\_regex\_20251119"ToolSearchToolRegex20251119

"tool\_search\_tool\_regex"ToolSearchToolRegex

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaMcpToolset:

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

required string McpServerName

Name of the MCP server to configure tools for

JsonElement Type "mcp\_toolset"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyDictionary<string, [BetaMcpToolConfig](api/beta.md)>? Configs

Configuration overrides for specific tools, keyed by tool name

Boolean DeferLoading

Boolean Enabled

[BetaMcpToolDefaultConfig](api/beta.md) DefaultConfig

Default configuration applied to all tools from this server

Boolean DeferLoading

Boolean Enabled

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaToolUsesKeep:

JsonElement Type "tool\_uses"constant

required Long Value

class BetaToolUsesTrigger:

JsonElement Type "tool\_uses"constant

required Long Value

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaUsage:

required [BetaCacheCreation](api/beta.md)? CacheCreation

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

required IReadOnlyList<BetaIterationsUsageItems>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The number of output tokens which were used.

required [BetaServerToolUsage](api/beta.md)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

required Speed? Speed

The inference speed mode used for this request.

Accepts one of the following:

"standard"Standard

"fast"Fast

class BetaUserLocation:

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class BetaWebFetchBlock:

required [BetaDocumentBlock](api/beta.md) Content

required [BetaCitationConfig](api/beta.md)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

class BetaWebFetchBlockParam:

required [BetaRequestDocumentBlock](api/beta.md) Content

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Boolean Enabled

string? Context

string? Title

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

class BetaWebFetchTool20250910:

JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20250910"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaWebFetchTool20260209:

JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20260209"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaWebFetchTool20260309:

Web fetch tool with use\_cache parameter for bypassing cached content.

JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20260309"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Boolean UseCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](api/beta.md) Content

required [BetaCitationConfig](api/beta.md)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebFetchToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam:

required [BetaWebFetchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlockParam:

required [BetaRequestDocumentBlock](api/beta.md) Content

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Boolean Enabled

string? Context

string? Title

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant

class BetaWebFetchToolResultErrorBlockParam:

required [BetaWebFetchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant

enum BetaWebFetchToolResultErrorCode:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

class BetaWebSearchResultBlock:

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

class BetaWebSearchResultBlockParam:

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge

class BetaWebSearchTool20250305:

JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20250305"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

[BetaUserLocation](api/beta.md)? UserLocation

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

class BetaWebSearchTool20260209:

JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20260209"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

[BetaUserLocation](api/beta.md)? UserLocation

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

class BetaWebSearchToolRequestError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](api/beta.md) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[BetaWebSearchResultBlock](api/beta.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebSearchToolResultBlockContent: A class that can be one of several variants.union

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[BetaWebSearchResultBlock](api/beta.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

class BetaWebSearchToolResultBlockParam:

required [BetaWebSearchToolResultBlockParamContent](api/beta.md) Content

Accepts one of the following:

IReadOnlyList<[BetaWebSearchResultBlockParam](api/beta.md)>

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge

class BetaWebSearchToolRequestError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

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

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebSearchToolResultBlockParamContent: A class that can be one of several variants.union

IReadOnlyList<[BetaWebSearchResultBlockParam](api/beta.md)>

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge

class BetaWebSearchToolRequestError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

enum BetaWebSearchToolResultErrorCode:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

#### BetaMessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

[BetaMessageBatch](api/beta.md) Beta.Messages.Batches.Create(BatchCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

[BetaMessageBatch](api/beta.md) Beta.Messages.Batches.Retrieve(BatchRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

[BatchListPageResponse](api/beta.md) Beta.Messages.Batches.List(BatchListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

[BetaMessageBatch](api/beta.md) Beta.Messages.Batches.Cancel(BatchCancelParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

[BetaDeletedMessageBatch](api/beta.md) Beta.Messages.Batches.Delete(BatchDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

[BetaMessageBatchIndividualResponse](api/beta.md) Beta.Messages.Batches.ResultsStreaming(BatchResultsParamsparameters, CancellationTokencancellationToken = default)

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

class BetaDeletedMessageBatch:

required string ID

ID of the Message Batch.

JsonElement Type "message\_batch\_deleted"constant

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

class BetaMessageBatch:

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

required [BetaMessageBatchRequestCounts](api/beta.md) RequestCounts

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

class BetaMessageBatchCanceledResult:

JsonElement Type "canceled"constant

class BetaMessageBatchErroredResult:

required [BetaErrorResponse](api/beta.md) Error

required [BetaError](api/beta.md) Error

Accepts one of the following:

class BetaInvalidRequestError:

required string Message

JsonElement Type "invalid\_request\_error"constant

class BetaAuthenticationError:

required string Message

JsonElement Type "authentication\_error"constant

class BetaBillingError:

required string Message

JsonElement Type "billing\_error"constant

class BetaPermissionError:

required string Message

JsonElement Type "permission\_error"constant

class BetaNotFoundError:

required string Message

JsonElement Type "not\_found\_error"constant

class BetaRateLimitError:

required string Message

JsonElement Type "rate\_limit\_error"constant

class BetaGatewayTimeoutError:

required string Message

JsonElement Type "timeout\_error"constant

class BetaApiError:

required string Message

JsonElement Type "api\_error"constant

class BetaOverloadedError:

required string Message

JsonElement Type "overloaded\_error"constant

required string? RequestID

JsonElement Type "error"constant

JsonElement Type "errored"constant

class BetaMessageBatchExpiredResult:

JsonElement Type "expired"constant

class BetaMessageBatchIndividualResponse:

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

required string CustomID

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

required [BetaMessageBatchResult](api/beta.md) Result

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class BetaMessageBatchSucceededResult:

required [BetaMessage](api/beta.md) Message

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required [BetaContainer](api/beta.md)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList<[BetaSkill](api/beta.md)>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

required IReadOnlyList<[BetaContentBlock](api/beta.md)> Content

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

class BetaTextBlock:

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required Name Name

Accepts one of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](api/beta.md) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[BetaWebSearchResultBlock](api/beta.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](api/beta.md) Content

required [BetaCitationConfig](api/beta.md)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList<[BetaBashCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList<[BetaToolReferenceBlock](api/beta.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaTextBlock](api/beta.md)>

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

required [BetaContextManagementResponse](api/beta.md)? ContextManagement

Context management response.

Information about context management strategies applied during the request.

required IReadOnlyList<AppliedEdit> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear\_thinking\_20251015"constant

The type of context management edit applied.

required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-mythos-preview"ClaudeMythosPreview

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"ClaudeOpus4\_6

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

"claude-opus-4-1"ClaudeOpus4\_1

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Exceptional model for specialized complex tasks

"claude-opus-4-0"ClaudeOpus4\_0

Powerful model for complex tasks

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Powerful model for complex tasks

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Fast and cost-effective model

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [BetaRefusalStopDetails](api/beta.md)? StopDetails

Structured information about a refusal.

required Category? Category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"Cyber

"bio"Bio

required string? Explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonElement Type "refusal"constant

required [BetaStopReason](api/beta.md)? StopReason

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

"compaction"Compaction

"refusal"Refusal

"model\_context\_window\_exceeded"ModelContextWindowExceeded

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [BetaUsage](api/beta.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [BetaCacheCreation](api/beta.md)? CacheCreation

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

required IReadOnlyList<BetaIterationsUsageItems>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The number of output tokens which were used.

required [BetaServerToolUsage](api/beta.md)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

required Speed? Speed

The inference speed mode used for this request.

Accepts one of the following:

"standard"Standard

"fast"Fast

JsonElement Type "succeeded"constant

class BetaMessageBatchErroredResult:

required [BetaErrorResponse](api/beta.md) Error

required [BetaError](api/beta.md) Error

Accepts one of the following:

class BetaInvalidRequestError:

required string Message

JsonElement Type "invalid\_request\_error"constant

class BetaAuthenticationError:

required string Message

JsonElement Type "authentication\_error"constant

class BetaBillingError:

required string Message

JsonElement Type "billing\_error"constant

class BetaPermissionError:

required string Message

JsonElement Type "permission\_error"constant

class BetaNotFoundError:

required string Message

JsonElement Type "not\_found\_error"constant

class BetaRateLimitError:

required string Message

JsonElement Type "rate\_limit\_error"constant

class BetaGatewayTimeoutError:

required string Message

JsonElement Type "timeout\_error"constant

class BetaApiError:

required string Message

JsonElement Type "api\_error"constant

class BetaOverloadedError:

required string Message

JsonElement Type "overloaded\_error"constant

required string? RequestID

JsonElement Type "error"constant

JsonElement Type "errored"constant

class BetaMessageBatchCanceledResult:

JsonElement Type "canceled"constant

class BetaMessageBatchExpiredResult:

JsonElement Type "expired"constant

class BetaMessageBatchRequestCounts:

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

class BetaMessageBatchResult: A class that can be one of several variants.union

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

class BetaMessageBatchSucceededResult:

required [BetaMessage](api/beta.md) Message

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required [BetaContainer](api/beta.md)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList<[BetaSkill](api/beta.md)>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

required IReadOnlyList<[BetaContentBlock](api/beta.md)> Content

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

class BetaTextBlock:

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required Name Name

Accepts one of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](api/beta.md) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[BetaWebSearchResultBlock](api/beta.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](api/beta.md) Content

required [BetaCitationConfig](api/beta.md)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList<[BetaBashCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList<[BetaToolReferenceBlock](api/beta.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaTextBlock](api/beta.md)>

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

required [BetaContextManagementResponse](api/beta.md)? ContextManagement

Context management response.

Information about context management strategies applied during the request.

required IReadOnlyList<AppliedEdit> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear\_thinking\_20251015"constant

The type of context management edit applied.

required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-mythos-preview"ClaudeMythosPreview

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"ClaudeOpus4\_6

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

"claude-opus-4-1"ClaudeOpus4\_1

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Exceptional model for specialized complex tasks

"claude-opus-4-0"ClaudeOpus4\_0

Powerful model for complex tasks

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Powerful model for complex tasks

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Fast and cost-effective model

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [BetaRefusalStopDetails](api/beta.md)? StopDetails

Structured information about a refusal.

required Category? Category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"Cyber

"bio"Bio

required string? Explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonElement Type "refusal"constant

required [BetaStopReason](api/beta.md)? StopReason

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

"compaction"Compaction

"refusal"Refusal

"model\_context\_window\_exceeded"ModelContextWindowExceeded

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [BetaUsage](api/beta.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [BetaCacheCreation](api/beta.md)? CacheCreation

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

required IReadOnlyList<BetaIterationsUsageItems>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The number of output tokens which were used.

required [BetaServerToolUsage](api/beta.md)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

required Speed? Speed

The inference speed mode used for this request.

Accepts one of the following:

"standard"Standard

"fast"Fast

JsonElement Type "succeeded"constant

class BetaMessageBatchErroredResult:

required [BetaErrorResponse](api/beta.md) Error

required [BetaError](api/beta.md) Error

Accepts one of the following:

class BetaInvalidRequestError:

required string Message

JsonElement Type "invalid\_request\_error"constant

class BetaAuthenticationError:

required string Message

JsonElement Type "authentication\_error"constant

class BetaBillingError:

required string Message

JsonElement Type "billing\_error"constant

class BetaPermissionError:

required string Message

JsonElement Type "permission\_error"constant

class BetaNotFoundError:

required string Message

JsonElement Type "not\_found\_error"constant

class BetaRateLimitError:

required string Message

JsonElement Type "rate\_limit\_error"constant

class BetaGatewayTimeoutError:

required string Message

JsonElement Type "timeout\_error"constant

class BetaApiError:

required string Message

JsonElement Type "api\_error"constant

class BetaOverloadedError:

required string Message

JsonElement Type "overloaded\_error"constant

required string? RequestID

JsonElement Type "error"constant

JsonElement Type "errored"constant

class BetaMessageBatchCanceledResult:

JsonElement Type "canceled"constant

class BetaMessageBatchExpiredResult:

JsonElement Type "expired"constant

class BetaMessageBatchSucceededResult:

required [BetaMessage](api/beta.md) Message

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required [BetaContainer](api/beta.md)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList<[BetaSkill](api/beta.md)>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

required IReadOnlyList<[BetaContentBlock](api/beta.md)> Content

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

class BetaTextBlock:

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required Name Name

Accepts one of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](api/beta.md) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

IReadOnlyList<[BetaWebSearchResultBlock](api/beta.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](api/beta.md) Content

required [BetaCitationConfig](api/beta.md)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

required IReadOnlyList<[BetaCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList<[BetaBashCodeExecutionOutputBlock](api/beta.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList<[BetaToolReferenceBlock](api/beta.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaTextBlock](api/beta.md)>

required IReadOnlyList<[BetaTextCitation](api/beta.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

required [BetaContextManagementResponse](api/beta.md)? ContextManagement

Context management response.

Information about context management strategies applied during the request.

required IReadOnlyList<AppliedEdit> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear\_thinking\_20251015"constant

The type of context management edit applied.

required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-mythos-preview"ClaudeMythosPreview

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"ClaudeOpus4\_6

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

"claude-opus-4-1"ClaudeOpus4\_1

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Exceptional model for specialized complex tasks

"claude-opus-4-0"ClaudeOpus4\_0

Powerful model for complex tasks

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Powerful model for complex tasks

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Fast and cost-effective model

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [BetaRefusalStopDetails](api/beta.md)? StopDetails

Structured information about a refusal.

required Category? Category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"Cyber

"bio"Bio

required string? Explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonElement Type "refusal"constant

required [BetaStopReason](api/beta.md)? StopReason

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

"compaction"Compaction

"refusal"Refusal

"model\_context\_window\_exceeded"ModelContextWindowExceeded

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [BetaUsage](api/beta.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [BetaCacheCreation](api/beta.md)? CacheCreation

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

required IReadOnlyList<BetaIterationsUsageItems>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](api/beta.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The number of output tokens which were used.

required [BetaServerToolUsage](api/beta.md)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

required Speed? Speed

The inference speed mode used for this request.

Accepts one of the following:

"standard"Standard

"fast"Fast

JsonElement Type "succeeded"constant

#### BetaAgents

##### [Create Agent](api/beta/agents/create.md)

[BetaManagedAgentsAgent](api/beta.md) Beta.Agents.Create(AgentCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

[AgentListPageResponse](api/beta.md) Beta.Agents.List(AgentListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

[BetaManagedAgentsAgent](api/beta.md) Beta.Agents.Retrieve(AgentRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

[BetaManagedAgentsAgent](api/beta.md) Beta.Agents.Update(AgentUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

[BetaManagedAgentsAgent](api/beta.md) Beta.Agents.Archive(AgentArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/agents/{agent\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsAgent:

A Managed Agents `agent`.

required string ID

required DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string? Description

required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> McpServers

required string Name

required Type Type

required string Url

required IReadOnlyDictionary<string, string> Metadata

required [BetaManagedAgentsModelConfig](api/beta.md) Model

Model identifier and configuration.

required [BetaManagedAgentsModel](api/beta.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

required string Name

required IReadOnlyList<Skill> Skills

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version

class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System

required IReadOnlyList<Tool> Tools

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401:

required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta.md)> Configs

required Boolean Enabled

required Name Name

Built-in agent tool identifier.

Accepts one of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type

class BetaManagedAgentsMcpToolset:

required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta.md)> Configs

required Boolean Enabled

required string Name

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type

class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description

required [BetaManagedAgentsCustomToolInputSchema](api/beta.md) InputSchema

JSON Schema for custom tool input parameters.

IReadOnlyDictionary<string, JsonElement>? Properties

JSON Schema properties defining the tool's input parameters.

IReadOnlyList<string> Required

List of required property names.

Type Type

Must be 'object' for tool input schemas.

required string Name

required Type Type

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required Int Version

The agent's current version. Starts at 1 and increments when the agent is modified.

class BetaManagedAgentsAgentToolConfig:

Configuration for a specific agent tool.

required Boolean Enabled

required Name Name

Built-in agent tool identifier.

Accepts one of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

class BetaManagedAgentsAgentToolConfigParams:

Configuration override for a specific tool within a toolset.

required Name Name

Built-in agent tool identifier.

Accepts one of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch

Boolean? Enabled

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

PermissionPolicy? PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

class BetaManagedAgentsAgentToolsetDefaultConfig:

Resolved default configuration for agent tools.

required Boolean Enabled

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

class BetaManagedAgentsAgentToolsetDefaultConfigParams:

Default configuration for all tools in a toolset.

Boolean? Enabled

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

PermissionPolicy? PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

class BetaManagedAgentsAgentToolset20260401:

required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta.md)> Configs

required Boolean Enabled

required Name Name

Built-in agent tool identifier.

Accepts one of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type

class BetaManagedAgentsAgentToolset20260401Params:

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

required Type Type

IReadOnlyList<[BetaManagedAgentsAgentToolConfigParams](api/beta.md)> Configs

Per-tool configuration overrides.

required Name Name

Built-in agent tool identifier.

Accepts one of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch

Boolean? Enabled

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

PermissionPolicy? PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

[BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta.md)? DefaultConfig

Default configuration for all tools in a toolset.

Boolean? Enabled

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

PermissionPolicy? PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version

class BetaManagedAgentsAnthropicSkillParams:

An Anthropic-managed skill.

required string SkillID

Identifier of the Anthropic skill (e.g., "xlsx").

required Type Type

string? Version

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

class BetaManagedAgentsCustomSkillParams:

A user-created custom skill.

required string SkillID

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

required Type Type

string? Version

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description

required [BetaManagedAgentsCustomToolInputSchema](api/beta.md) InputSchema

JSON Schema for custom tool input parameters.

IReadOnlyDictionary<string, JsonElement>? Properties

JSON Schema properties defining the tool's input parameters.

IReadOnlyList<string> Required

List of required property names.

Type Type

Must be 'object' for tool input schemas.

required string Name

required Type Type

class BetaManagedAgentsCustomToolInputSchema:

JSON Schema for custom tool input parameters.

IReadOnlyDictionary<string, JsonElement>? Properties

JSON Schema properties defining the tool's input parameters.

IReadOnlyList<string> Required

List of required property names.

Type Type

Must be 'object' for tool input schemas.

class BetaManagedAgentsCustomToolParams:

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

required string Description

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

required [BetaManagedAgentsCustomToolInputSchema](api/beta.md) InputSchema

JSON Schema for custom tool input parameters.

IReadOnlyDictionary<string, JsonElement>? Properties

JSON Schema properties defining the tool's input parameters.

IReadOnlyList<string> Required

List of required property names.

Type Type

Must be 'object' for tool input schemas.

required string Name

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

required Type Type

class BetaManagedAgentsMcpServerUrlDefinition:

URL-based MCP server connection as returned in API responses.

required string Name

required Type Type

required string Url

class BetaManagedAgentsMcpToolConfig:

Resolved configuration for a specific MCP tool.

required Boolean Enabled

required string Name

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

class BetaManagedAgentsMcpToolConfigParams:

Configuration override for a specific MCP tool.

required string Name

Name of the MCP tool to configure. 1-128 characters.

Boolean? Enabled

Whether this tool is enabled. Overrides the `default_config` setting.

PermissionPolicy? PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

class BetaManagedAgentsMcpToolset:

required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta.md)> Configs

required Boolean Enabled

required string Name

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type

class BetaManagedAgentsMcpToolsetDefaultConfig:

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

class BetaManagedAgentsMcpToolsetDefaultConfigParams:

Default configuration for all tools from an MCP server.

Boolean? Enabled

Whether tools are enabled by default. Defaults to true if not specified.

PermissionPolicy? PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

class BetaManagedAgentsMcpToolsetParams:

Configuration for tools from an MCP server defined in `mcp_servers`.

required string McpServerName

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

required Type Type

IReadOnlyList<[BetaManagedAgentsMcpToolConfigParams](api/beta.md)> Configs

Per-tool configuration overrides.

required string Name

Name of the MCP tool to configure. 1-128 characters.

Boolean? Enabled

Whether this tool is enabled. Overrides the `default_config` setting.

PermissionPolicy? PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

[BetaManagedAgentsMcpToolsetDefaultConfigParams](api/beta.md)? DefaultConfig

Default configuration for all tools from an MCP server.

Boolean? Enabled

Whether tools are enabled by default. Defaults to true if not specified.

PermissionPolicy? PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

class BetaManagedAgentsModelConfig:

Model identifier and configuration.

required [BetaManagedAgentsModel](api/beta.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

class BetaManagedAgentsModelConfigParams:

An object that defines additional configuration control over model use

required [BetaManagedAgentsModel](api/beta.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

class BetaManagedAgentsSkillParams: A class that can be one of several variants.union

Skill to load in the session container.

class BetaManagedAgentsAnthropicSkillParams:

An Anthropic-managed skill.

required string SkillID

Identifier of the Anthropic skill (e.g., "xlsx").

required Type Type

string? Version

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomSkillParams:

A user-created custom skill.

required string SkillID

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

required Type Type

string? Version

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsUrlMcpServerParams:

URL-based MCP server connection.

required string Name

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

required Type Type

required string Url

Endpoint URL for the MCP server.

#### BetaAgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

[VersionListPageResponse](api/beta.md) Beta.Agents.Versions.List(VersionListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/agents/{agent\_id}/versions

#### BetaEnvironments

##### [Create Environment](api/beta/environments/create.md)

[BetaEnvironment](api/beta.md) Beta.Environments.Create(EnvironmentCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

[EnvironmentListPageResponse](api/beta.md) Beta.Environments.List(EnvironmentListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

[BetaEnvironment](api/beta.md) Beta.Environments.Retrieve(EnvironmentRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

[BetaEnvironment](api/beta.md) Beta.Environments.Update(EnvironmentUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

[BetaEnvironmentDeleteResponse](api/beta.md) Beta.Environments.Delete(EnvironmentDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

[BetaEnvironment](api/beta.md) Beta.Environments.Archive(EnvironmentArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}/archive

##### ModelsExpand Collapse

class BetaCloudConfig:

`cloud` environment configuration.

required Networking Networking

Network configuration policy.

Accepts one of the following:

class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonElement Type "unrestricted"constant

Network policy type

class BetaLimitedNetwork:

Limited network access.

required Boolean AllowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

required Boolean AllowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

required IReadOnlyList<string> AllowedHosts

Specifies domains the container can reach.

JsonElement Type "limited"constant

Network policy type

required [BetaPackages](api/beta.md) Packages

Package manager configuration.

required IReadOnlyList<string> Apt

Ubuntu/Debian packages to install

required IReadOnlyList<string> Cargo

Rust packages to install

required IReadOnlyList<string> Gem

Ruby packages to install

required IReadOnlyList<string> Go

Go packages to install

required IReadOnlyList<string> Npm

Node.js packages to install

required IReadOnlyList<string> Pip

Python packages to install

Type Type

Package configuration type

JsonElement Type "cloud"constant

Environment type

class BetaCloudConfigParams:

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

JsonElement Type "cloud"constant

Environment type

Networking? Networking

Network configuration policy. Omit on update to preserve the existing value.

Accepts one of the following:

class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonElement Type "unrestricted"constant

Network policy type

class BetaLimitedNetworkParams:

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

JsonElement Type "limited"constant

Network policy type

Boolean? AllowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Boolean? AllowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

IReadOnlyList<string>? AllowedHosts

Specifies domains the container can reach.

[BetaPackagesParams](api/beta.md)? Packages

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

IReadOnlyList<string>? Apt

Ubuntu/Debian packages to install

IReadOnlyList<string>? Cargo

Rust packages to install

IReadOnlyList<string>? Gem

Ruby packages to install

IReadOnlyList<string>? Go

Go packages to install

IReadOnlyList<string>? Npm

Node.js packages to install

IReadOnlyList<string>? Pip

Python packages to install

Type Type

Package configuration type

class BetaEnvironment:

Unified Environment resource for both cloud and BYOC environments.

required string ID

Environment identifier (e.g., 'env\_...')

required string? ArchivedAt

RFC 3339 timestamp when environment was archived, or null if not archived

required [BetaCloudConfig](api/beta.md) Config

`cloud` environment configuration.

required Networking Networking

Network configuration policy.

Accepts one of the following:

class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonElement Type "unrestricted"constant

Network policy type

class BetaLimitedNetwork:

Limited network access.

required Boolean AllowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

required Boolean AllowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

required IReadOnlyList<string> AllowedHosts

Specifies domains the container can reach.

JsonElement Type "limited"constant

Network policy type

required [BetaPackages](api/beta.md) Packages

Package manager configuration.

required IReadOnlyList<string> Apt

Ubuntu/Debian packages to install

required IReadOnlyList<string> Cargo

Rust packages to install

required IReadOnlyList<string> Gem

Ruby packages to install

required IReadOnlyList<string> Go

Go packages to install

required IReadOnlyList<string> Npm

Node.js packages to install

required IReadOnlyList<string> Pip

Python packages to install

Type Type

Package configuration type

JsonElement Type "cloud"constant

Environment type

required string CreatedAt

RFC 3339 timestamp when environment was created

required string Description

User-provided description for the environment

required IReadOnlyDictionary<string, string> Metadata

User-provided metadata key-value pairs

required string Name

Human-readable name for the environment

JsonElement Type "environment"constant

The type of object (always 'environment')

required string UpdatedAt

RFC 3339 timestamp when environment was last updated

class BetaEnvironmentDeleteResponse:

Response after deleting an environment.

required string ID

Environment identifier

JsonElement Type "environment\_deleted"constant

The type of response

class BetaLimitedNetwork:

Limited network access.

required Boolean AllowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

required Boolean AllowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

required IReadOnlyList<string> AllowedHosts

Specifies domains the container can reach.

JsonElement Type "limited"constant

Network policy type

class BetaLimitedNetworkParams:

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

JsonElement Type "limited"constant

Network policy type

Boolean? AllowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Boolean? AllowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

IReadOnlyList<string>? AllowedHosts

Specifies domains the container can reach.

class BetaPackages:

Packages (and their versions) available in this environment.

required IReadOnlyList<string> Apt

Ubuntu/Debian packages to install

required IReadOnlyList<string> Cargo

Rust packages to install

required IReadOnlyList<string> Gem

Ruby packages to install

required IReadOnlyList<string> Go

Go packages to install

required IReadOnlyList<string> Npm

Node.js packages to install

required IReadOnlyList<string> Pip

Python packages to install

Type Type

Package configuration type

class BetaPackagesParams:

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

IReadOnlyList<string>? Apt

Ubuntu/Debian packages to install

IReadOnlyList<string>? Cargo

Rust packages to install

IReadOnlyList<string>? Gem

Ruby packages to install

IReadOnlyList<string>? Go

Go packages to install

IReadOnlyList<string>? Npm

Node.js packages to install

IReadOnlyList<string>? Pip

Python packages to install

Type Type

Package configuration type

class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonElement Type "unrestricted"constant

Network policy type

#### BetaSessions

##### [Create Session](api/beta/sessions/create.md)

[BetaManagedAgentsSession](api/beta.md) Beta.Sessions.Create(SessionCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

[SessionListPageResponse](api/beta.md) Beta.Sessions.List(SessionListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

[BetaManagedAgentsSession](api/beta.md) Beta.Sessions.Retrieve(SessionRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

[BetaManagedAgentsSession](api/beta.md) Beta.Sessions.Update(SessionUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

[BetaManagedAgentsDeletedSession](api/beta.md) Beta.Sessions.Delete(SessionDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

[BetaManagedAgentsSession](api/beta.md) Beta.Sessions.Archive(SessionArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsAgentParams:

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

required string ID

The `agent` ID.

required Type Type

Int Version

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type

class BetaManagedAgentsCacheCreationUsage:

Prompt-cache creation token usage broken down by cache lifetime.

Int Ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Int Ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type

class BetaManagedAgentsDeletedSession:

Confirmation that a `session` has been permanently deleted.

required string ID

required Type Type

class BetaManagedAgentsFileResourceParams:

Mount a file uploaded via the Files API into the session.

required string FileID

ID of a previously uploaded file.

required Type Type

string? MountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

class BetaManagedAgentsGitHubRepositoryResourceParams:

Mount a GitHub repository into the session's container.

required string AuthorizationToken

GitHub authorization token used to clone the repository.

required Type Type

required string Url

Github URL of the repository

Checkout? Checkout

Branch or commit to check out. Defaults to the repository's default branch.

Accepts one of the following:

class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type

class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type

string? MountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.

class BetaManagedAgentsSession:

A Managed Agents `session`.

required string ID

required [BetaManagedAgentsSessionAgent](api/beta.md) Agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

required string ID

required string? Description

required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> McpServers

required string Name

required Type Type

required string Url

required [BetaManagedAgentsModelConfig](api/beta.md) Model

Model identifier and configuration.

required [BetaManagedAgentsModel](api/beta.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

required string Name

required IReadOnlyList<Skill> Skills

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version

class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System

required IReadOnlyList<Tool> Tools

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401:

required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta.md)> Configs

required Boolean Enabled

required Name Name

Built-in agent tool identifier.

Accepts one of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type

class BetaManagedAgentsMcpToolset:

required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta.md)> Configs

required Boolean Enabled

required string Name

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type

class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description

required [BetaManagedAgentsCustomToolInputSchema](api/beta.md) InputSchema

JSON Schema for custom tool input parameters.

IReadOnlyDictionary<string, JsonElement>? Properties

JSON Schema properties defining the tool's input parameters.

IReadOnlyList<string> Required

List of required property names.

Type Type

Must be 'object' for tool input schemas.

required string Name

required Type Type

required Type Type

required Int Version

required DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string EnvironmentID

required IReadOnlyDictionary<string, string> Metadata

required IReadOnlyList<[BetaManagedAgentsSessionResource](api/beta.md)> Resources

Accepts one of the following:

class BetaManagedAgentsGitHubRepositoryResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required string Url

Checkout? Checkout

Accepts one of the following:

class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type

class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type

class BetaManagedAgentsFileResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string FileID

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required [BetaManagedAgentsSessionStats](api/beta.md) Stats

Timing statistics for a session.

Double ActiveSeconds

Cumulative time in seconds the session spent in running status. Excludes idle time.

Double DurationSeconds

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

required Status Status

SessionStatus enum

Accepts one of the following:

"rescheduling"Rescheduling

"running"Running

"idle"Idle

"terminated"Terminated

required string? Title

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required [BetaManagedAgentsSessionUsage](api/beta.md) Usage

Cumulative token usage for a session across all turns.

[BetaManagedAgentsCacheCreationUsage](api/beta.md) CacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

Int Ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Int Ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

Int CacheReadInputTokens

Total tokens read from prompt cache.

Int InputTokens

Total input tokens consumed across all turns.

Int OutputTokens

Total output tokens generated across all turns.

required IReadOnlyList<string> VaultIds

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

class BetaManagedAgentsSessionAgent:

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

required string ID

required string? Description

required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> McpServers

required string Name

required Type Type

required string Url

required [BetaManagedAgentsModelConfig](api/beta.md) Model

Model identifier and configuration.

required [BetaManagedAgentsModel](api/beta.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

required string Name

required IReadOnlyList<Skill> Skills

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version

class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System

required IReadOnlyList<Tool> Tools

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401:

required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta.md)> Configs

required Boolean Enabled

required Name Name

Built-in agent tool identifier.

Accepts one of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type

class BetaManagedAgentsMcpToolset:

required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta.md)> Configs

required Boolean Enabled

required string Name

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type

class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description

required [BetaManagedAgentsCustomToolInputSchema](api/beta.md) InputSchema

JSON Schema for custom tool input parameters.

IReadOnlyDictionary<string, JsonElement>? Properties

JSON Schema properties defining the tool's input parameters.

IReadOnlyList<string> Required

List of required property names.

Type Type

Must be 'object' for tool input schemas.

required string Name

required Type Type

required Type Type

required Int Version

class BetaManagedAgentsSessionStats:

Timing statistics for a session.

Double ActiveSeconds

Cumulative time in seconds the session spent in running status. Excludes idle time.

Double DurationSeconds

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

class BetaManagedAgentsSessionUsage:

Cumulative token usage for a session across all turns.

[BetaManagedAgentsCacheCreationUsage](api/beta.md) CacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

Int Ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Int Ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

Int CacheReadInputTokens

Total tokens read from prompt cache.

Int InputTokens

Total input tokens consumed across all turns.

Int OutputTokens

Total output tokens generated across all turns.

#### BetaSessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

[EventListPageResponse](api/beta.md) Beta.Sessions.Events.List(EventListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

[BetaManagedAgentsSendSessionEvents](api/beta.md) Beta.Sessions.Events.Send(EventSendParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

[BetaManagedAgentsStreamSessionEvents](api/beta.md) Beta.Sessions.Events.StreamStreaming(EventStreamParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/events/stream

##### ModelsExpand Collapse

class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the custom tool being called.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

required string ID

Unique identifier for this event.

required string McpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string McpServerName

Name of the MCP server providing the tool.

required string Name

Name of the MCP tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<[BetaManagedAgentsTextBlock](api/beta.md)> Content

Array of text blocks comprising the agent response.

required string Text

The text content.

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string ToolUseID

The id of the `agent.tool_use` event this result corresponds to.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the agent tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

class BetaManagedAgentsEventParams: A class that can be one of several variants.union

Union type for event parameters that can be sent to a session.

class BetaManagedAgentsUserMessageEventParams:

Parameters for sending a user message to the session.

required IReadOnlyList<Content> Content

Array of content blocks for the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

class BetaManagedAgentsUserInterruptEventParams:

Parameters for sending an interrupt to pause the agent.

required Type Type

class BetaManagedAgentsUserToolConfirmationEventParams:

Parameters for confirming or denying a tool execution request.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

class BetaManagedAgentsUserCustomToolResultEventParams:

Parameters for providing the result of a custom tool execution.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

required string McpServerName

Name of the MCP server that failed authentication.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

required string McpServerName

Name of the MCP server that failed to connect.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

class BetaManagedAgentsSendSessionEvents:

Events that were successfully sent to the session.

IReadOnlyList<Data> Data

Sent events

Accepts one of the following:

class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

required string ID

Unique identifier for this event.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

required string ID

Unique identifier for this event.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

required string ID

Unique identifier for this event.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type

class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

required string ID

Unique identifier for this event.

required Error Error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

required string McpServerName

Name of the MCP server that failed to connect.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

required string McpServerName

Name of the MCP server that failed authentication.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionEvent: A class that can be one of several variants.union

Union type for all event types in a session.

class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

required string ID

Unique identifier for this event.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

required string ID

Unique identifier for this event.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

required string ID

Unique identifier for this event.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the custom tool being called.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<[BetaManagedAgentsTextBlock](api/beta.md)> Content

Array of text blocks comprising the agent response.

required string Text

The text content.

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string McpServerName

Name of the MCP server providing the tool.

required string Name

Name of the MCP tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

required string ID

Unique identifier for this event.

required string McpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the agent tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string ToolUseID

The id of the `agent.tool_use` event this result corresponds to.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

required string ID

Unique identifier for this event.

required Error Error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

required string McpServerName

Name of the MCP server that failed to connect.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

required string McpServerName

Name of the MCP server that failed authentication.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required StopReason StopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

required Type Type

class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

required string ID

Unique identifier for this event.

required Boolean? IsError

Whether the model request resulted in an error.

required string ModelRequestStartID

The id of the corresponding `span.model_request_start` event.

required [BetaManagedAgentsSpanModelUsage](api/beta.md) ModelUsage

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.

Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required StopReason StopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

required Type Type

class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

required string ID

Unique identifier for this event.

required Boolean? IsError

Whether the model request resulted in an error.

required string ModelRequestStartID

The id of the corresponding `span.model_request_start` event.

required [BetaManagedAgentsSpanModelUsage](api/beta.md) ModelUsage

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.

Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelUsage:

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.

Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

class BetaManagedAgentsStreamSessionEvents: A class that can be one of several variants.union

Server-sent event in the session stream.

class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

required string ID

Unique identifier for this event.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

required string ID

Unique identifier for this event.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

required string ID

Unique identifier for this event.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the custom tool being called.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<[BetaManagedAgentsTextBlock](api/beta.md)> Content

Array of text blocks comprising the agent response.

required string Text

The text content.

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string McpServerName

Name of the MCP server providing the tool.

required string Name

Name of the MCP tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

required string ID

Unique identifier for this event.

required string McpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the agent tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string ToolUseID

The id of the `agent.tool_use` event this result corresponds to.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

required string ID

Unique identifier for this event.

required Error Error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

required string McpServerName

Name of the MCP server that failed to connect.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

required string McpServerName

Name of the MCP server that failed authentication.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required StopReason StopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

required Type Type

class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

required string ID

Unique identifier for this event.

required Boolean? IsError

Whether the model request resulted in an error.

required string ModelRequestStartID

The id of the corresponding `span.model_request_start` event.

required [BetaManagedAgentsSpanModelUsage](api/beta.md) ModelUsage

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.

Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

required string ID

Unique identifier for this event.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEventParams:

Parameters for providing the result of a custom tool execution.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

required string ID

Unique identifier for this event.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEventParams:

Parameters for sending an interrupt to pause the agent.

required Type Type

class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserMessageEventParams:

Parameters for sending a user message to the session.

required IReadOnlyList<Content> Content

Array of content blocks for the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

required string ID

Unique identifier for this event.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEventParams:

Parameters for confirming or denying a tool execution request.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

#### BetaSessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

[BetaManagedAgentsFileResource](api/beta.md) Beta.Sessions.Resources.Add(ResourceAddParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

[ResourceListPageResponse](api/beta.md) Beta.Sessions.Resources.List(ResourceListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

[ResourceRetrieveResponse](api/beta.md) Beta.Sessions.Resources.Retrieve(ResourceRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

[ResourceUpdateResponse](api/beta.md) Beta.Sessions.Resources.Update(ResourceUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

[BetaManagedAgentsDeleteSessionResource](api/beta.md) Beta.Sessions.Resources.Delete(ResourceDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsDeleteSessionResource:

Confirmation of resource deletion.

required string ID

required Type Type

class BetaManagedAgentsFileResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string FileID

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsGitHubRepositoryResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required string Url

Checkout? Checkout

Accepts one of the following:

class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type

class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type

class BetaManagedAgentsSessionResource: A class that can be one of several variants.union

class BetaManagedAgentsGitHubRepositoryResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required string Url

Checkout? Checkout

Accepts one of the following:

class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type

class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type

class BetaManagedAgentsFileResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string FileID

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

#### BetaVaults

##### [Create Vault](api/beta/vaults/create.md)

[BetaManagedAgentsVault](api/beta.md) Beta.Vaults.Create(VaultCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

[VaultListPageResponse](api/beta.md) Beta.Vaults.List(VaultListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

[BetaManagedAgentsVault](api/beta.md) Beta.Vaults.Retrieve(VaultRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

[BetaManagedAgentsVault](api/beta.md) Beta.Vaults.Update(VaultUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

[BetaManagedAgentsDeletedVault](api/beta.md) Beta.Vaults.Delete(VaultDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

[BetaManagedAgentsVault](api/beta.md) Beta.Vaults.Archive(VaultArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsDeletedVault:

Confirmation of a deleted vault.

required string ID

Unique identifier of the deleted vault.

required Type Type

class BetaManagedAgentsVault:

A vault that stores credentials for use by agents during sessions.

required string ID

Unique identifier for the vault.

required DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string DisplayName

Human-readable name for the vault.

required IReadOnlyDictionary<string, string> Metadata

Arbitrary key-value metadata attached to the vault.

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

#### BetaVaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

[BetaManagedAgentsCredential](api/beta.md) Beta.Vaults.Credentials.Create(CredentialCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

[CredentialListPageResponse](api/beta.md) Beta.Vaults.Credentials.List(CredentialListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

[BetaManagedAgentsCredential](api/beta.md) Beta.Vaults.Credentials.Retrieve(CredentialRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

[BetaManagedAgentsCredential](api/beta.md) Beta.Vaults.Credentials.Update(CredentialUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

[BetaManagedAgentsDeletedCredential](api/beta.md) Beta.Vaults.Credentials.Delete(CredentialDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

[BetaManagedAgentsCredential](api/beta.md) Beta.Vaults.Credentials.Archive(CredentialArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsCredential:

A credential stored in a vault. Sensitive fields are never returned in responses.

required string ID

Unique identifier for the credential.

required DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

required Auth Auth

Authentication details for a credential.

Accepts one of the following:

class BetaManagedAgentsMcpOAuthAuthResponse:

OAuth credential details for an MCP server.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type

DateTimeOffset? ExpiresAt

A timestamp in RFC 3339 format

[BetaManagedAgentsMcpOAuthRefreshResponse](api/beta.md)? Refresh

OAuth refresh token configuration returned in credential responses.

required string ClientID

OAuth client ID.

required string TokenEndpoint

Token endpoint URL used to refresh the access token.

required TokenEndpointAuth TokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

required Type Type

class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

required Type Type

class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

required Type Type

string? Resource

OAuth resource indicator.

string? Scope

OAuth scope for the refresh request.

class BetaManagedAgentsStaticBearerAuthResponse:

Static bearer token credential details for an MCP server.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required IReadOnlyDictionary<string, string> Metadata

Arbitrary key-value metadata attached to the credential.

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required string VaultID

Identifier of the vault this credential belongs to.

string? DisplayName

Human-readable name for the credential.

class BetaManagedAgentsDeletedCredential:

Confirmation of a deleted credential.

required string ID

Unique identifier of the deleted credential.

required Type Type

class BetaManagedAgentsMcpOAuthAuthResponse:

OAuth credential details for an MCP server.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type

DateTimeOffset? ExpiresAt

A timestamp in RFC 3339 format

[BetaManagedAgentsMcpOAuthRefreshResponse](api/beta.md)? Refresh

OAuth refresh token configuration returned in credential responses.

required string ClientID

OAuth client ID.

required string TokenEndpoint

Token endpoint URL used to refresh the access token.

required TokenEndpointAuth TokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

required Type Type

class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

required Type Type

class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

required Type Type

string? Resource

OAuth resource indicator.

string? Scope

OAuth scope for the refresh request.

class BetaManagedAgentsMcpOAuthCreateParams:

Parameters for creating an MCP OAuth credential.

required string AccessToken

OAuth access token.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type

DateTimeOffset? ExpiresAt

A timestamp in RFC 3339 format

[BetaManagedAgentsMcpOAuthRefreshParams](api/beta.md)? Refresh

OAuth refresh token parameters for creating a credential with refresh support.

required string ClientID

OAuth client ID.

required string RefreshToken

OAuth refresh token.

required string TokenEndpoint

Token endpoint URL used to refresh the access token.

required TokenEndpointAuth TokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

required Type Type

class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type

class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type

string? Resource

OAuth resource indicator.

string? Scope

OAuth scope for the refresh request.

class BetaManagedAgentsMcpOAuthRefreshParams:

OAuth refresh token parameters for creating a credential with refresh support.

required string ClientID

OAuth client ID.

required string RefreshToken

OAuth refresh token.

required string TokenEndpoint

Token endpoint URL used to refresh the access token.

required TokenEndpointAuth TokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

required Type Type

class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type

class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type

string? Resource

OAuth resource indicator.

string? Scope

OAuth scope for the refresh request.

class BetaManagedAgentsMcpOAuthRefreshResponse:

OAuth refresh token configuration returned in credential responses.

required string ClientID

OAuth client ID.

required string TokenEndpoint

Token endpoint URL used to refresh the access token.

required TokenEndpointAuth TokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

required Type Type

class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

required Type Type

class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

required Type Type

string? Resource

OAuth resource indicator.

string? Scope

OAuth scope for the refresh request.

class BetaManagedAgentsMcpOAuthRefreshUpdateParams:

Parameters for updating OAuth refresh token configuration.

string? RefreshToken

Updated OAuth refresh token.

string? Scope

Updated OAuth scope for the refresh request.

TokenEndpointAuth TokenEndpointAuth

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.

class BetaManagedAgentsMcpOAuthUpdateParams:

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

required Type Type

string? AccessToken

Updated OAuth access token.

DateTimeOffset? ExpiresAt

A timestamp in RFC 3339 format

[BetaManagedAgentsMcpOAuthRefreshUpdateParams](api/beta.md)? Refresh

Parameters for updating OAuth refresh token configuration.

string? RefreshToken

Updated OAuth refresh token.

string? Scope

Updated OAuth scope for the refresh request.

TokenEndpointAuth TokenEndpointAuth

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.

class BetaManagedAgentsStaticBearerAuthResponse:

Static bearer token credential details for an MCP server.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type

class BetaManagedAgentsStaticBearerCreateParams:

Parameters for creating a static bearer token credential.

required string Token

Static bearer token value.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type

class BetaManagedAgentsStaticBearerUpdateParams:

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

required Type Type

string? Token

Updated static bearer token value.

class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type

class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

required Type Type

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

required Type Type

class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

required Type Type

class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type

class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

required Type Type

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.

#### BetaFiles

##### [Upload File](api/beta/files/upload.md)

[FileMetadata](api/beta.md) Beta.Files.Upload(FileUploadParamsparameters, CancellationTokencancellationToken = default)

POST/v1/files

##### [List Files](api/beta/files/list.md)

[FileListPageResponse](api/beta.md) Beta.Files.List(FileListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/files

##### [Download File](api/beta/files/download.md)

HttpResponse Beta.Files.Download(FileDownloadParamsparameters, CancellationTokencancellationToken = default)

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

[FileMetadata](api/beta.md) Beta.Files.RetrieveMetadata(FileRetrieveMetadataParamsparameters, CancellationTokencancellationToken = default)

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

[DeletedFile](api/beta.md) Beta.Files.Delete(FileDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/files/{file\_id}

##### ModelsExpand Collapse

class BetaFileScope:

required string ID

The ID of the scoping resource (e.g., the session ID).

JsonElement Type "session"constant

The type of scope (e.g., `"session"`).

class DeletedFile:

required string ID

ID of the deleted file.

Type Type

Deleted object type.

For file deletion, this is always `"file_deleted"`.

class FileMetadata:

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required DateTimeOffset CreatedAt

RFC 3339 datetime string representing when the file was created.

required string Filename

Original filename of the uploaded file.

required string MimeType

MIME type of the file.

required Long SizeBytes

Size of the file in bytes.

JsonElement Type "file"constant

Object type.

For files, this is always `"file"`.

Boolean Downloadable

Whether the file can be downloaded.

[BetaFileScope](api/beta.md)? Scope

The scope of this file, indicating the context in which it was created (e.g., a session).

required string ID

The ID of the scoping resource (e.g., the session ID).

JsonElement Type "session"constant

The type of scope (e.g., `"session"`).

#### BetaSkills

##### [Create Skill](api/beta/skills/create.md)

[SkillCreateResponse](api/beta.md) Beta.Skills.Create(SkillCreateParams?parameters, CancellationTokencancellationToken = default)

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

[SkillListPageResponse](api/beta.md) Beta.Skills.List(SkillListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

[SkillRetrieveResponse](api/beta.md) Beta.Skills.Retrieve(SkillRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

[SkillDeleteResponse](api/beta.md) Beta.Skills.Delete(SkillDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/skills/{skill\_id}

#### BetaSkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

[VersionCreateResponse](api/beta.md) Beta.Skills.Versions.Create(VersionCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

[VersionListPageResponse](api/beta.md) Beta.Skills.Versions.List(VersionListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill\_id}/versions

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

[VersionRetrieveResponse](api/beta.md) Beta.Skills.Versions.Retrieve(VersionRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

[VersionDeleteResponse](api/beta.md) Beta.Skills.Versions.Delete(VersionDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/skills/{skill\_id}/versions/{version}

---

*Copyright © Anthropic. All rights reserved.*
