# Beta

Copy page

SDK language

PHP

# Beta

##### ModelsExpand Collapse

AnthropicBeta

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

[BetaAPIError](api/beta.md)

string message

"api\_error" type

[BetaAuthenticationError](api/beta.md)

string message

"authentication\_error" type

[BetaBillingError](api/beta.md)

string message

"billing\_error" type

[BetaError](api/beta.md)

One of the following:

[BetaInvalidRequestError](api/beta.md)

string message

"invalid\_request\_error" type

[BetaAuthenticationError](api/beta.md)

string message

"authentication\_error" type

[BetaBillingError](api/beta.md)

string message

"billing\_error" type

[BetaPermissionError](api/beta.md)

string message

"permission\_error" type

[BetaNotFoundError](api/beta.md)

string message

"not\_found\_error" type

[BetaRateLimitError](api/beta.md)

string message

"rate\_limit\_error" type

[BetaGatewayTimeoutError](api/beta.md)

string message

"timeout\_error" type

[BetaAPIError](api/beta.md)

string message

"api\_error" type

[BetaOverloadedError](api/beta.md)

string message

"overloaded\_error" type

[BetaErrorResponse](api/beta.md)

[BetaError](api/beta.md) error

?string requestID

"error" type

[BetaGatewayTimeoutError](api/beta.md)

string message

"timeout\_error" type

[BetaInvalidRequestError](api/beta.md)

string message

"invalid\_request\_error" type

[BetaNotFoundError](api/beta.md)

string message

"not\_found\_error" type

[BetaOverloadedError](api/beta.md)

string message

"overloaded\_error" type

[BetaPermissionError](api/beta.md)

string message

"permission\_error" type

[BetaRateLimitError](api/beta.md)

string message

"rate\_limit\_error" type

#### BetaModels

##### [List Models](api/beta/models/list.md)

$client->beta->models->list(?string afterID, ?string beforeID, ?int limit, ?list<AnthropicBeta> betas): Page<[BetaModelInfo](api/beta.md)>

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

$client->beta->models->retrieve(string modelID, ?list<AnthropicBeta> betas): [BetaModelInfo](api/beta.md)

GET/v1/models/{model\_id}

##### ModelsExpand Collapse

[BetaCapabilitySupport](api/beta.md)

bool supported

Whether this capability is supported by the model.

[BetaContextManagementCapability](api/beta.md)

?[BetaCapabilitySupport](api/beta.md) clearThinking20251015

Indicates whether a capability is supported.

?[BetaCapabilitySupport](api/beta.md) clearToolUses20250919

Indicates whether a capability is supported.

?[BetaCapabilitySupport](api/beta.md) compact20260112

Indicates whether a capability is supported.

bool supported

Whether this capability is supported by the model.

[BetaEffortCapability](api/beta.md)

[BetaCapabilitySupport](api/beta.md) high

Whether the model supports high effort level.

[BetaCapabilitySupport](api/beta.md) low

Whether the model supports low effort level.

[BetaCapabilitySupport](api/beta.md) max

Whether the model supports max effort level.

[BetaCapabilitySupport](api/beta.md) medium

Whether the model supports medium effort level.

bool supported

Whether this capability is supported by the model.

?[BetaCapabilitySupport](api/beta.md) xhigh

Indicates whether a capability is supported.

[BetaModelCapabilities](api/beta.md)

[BetaCapabilitySupport](api/beta.md) batch

Whether the model supports the Batch API.

[BetaCapabilitySupport](api/beta.md) citations

Whether the model supports citation generation.

[BetaCapabilitySupport](api/beta.md) codeExecution

Whether the model supports code execution tools.

[BetaContextManagementCapability](api/beta.md) contextManagement

Context management support and available strategies.

[BetaEffortCapability](api/beta.md) effort

Effort (reasoning\_effort) support and available levels.

[BetaCapabilitySupport](api/beta.md) imageInput

Whether the model accepts image content blocks.

[BetaCapabilitySupport](api/beta.md) pdfInput

Whether the model accepts PDF content blocks.

[BetaCapabilitySupport](api/beta.md) structuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

[BetaThinkingCapability](api/beta.md) thinking

Thinking capability and supported type configurations.

[BetaModelInfo](api/beta.md)

string id

Unique model identifier.

?list<string> allowedFallbackModels

Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.

?[BetaModelCapabilities](api/beta.md) capabilities

Model capability information.

\Datetime createdAt

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

string displayName

A human-readable name for the model.

?int maxInputTokens

Maximum input context window size in tokens for this model.

?int maxTokens

Maximum value for the `max_tokens` parameter when using this model.

"model" type

Object type.

For Models, this is always `"model"`.

[BetaThinkingCapability](api/beta.md)

bool supported

Whether this capability is supported by the model.

[BetaThinkingTypes](api/beta.md) types

Supported thinking type configurations.

[BetaThinkingTypes](api/beta.md)

[BetaCapabilitySupport](api/beta.md) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

[BetaCapabilitySupport](api/beta.md) enabled

Whether the model supports thinking with type 'enabled'.

#### BetaMessages

##### [Create a Message](api/beta/messages/create.md)

$client->beta->messages->create(int maxTokens, list<[BetaMessageParam](api/beta.md)> messages, Model model, ?[BetaCacheControlEphemeral](api/beta.md) cacheControl, ?[Container](api/beta/messages/create.md) container, ?[BetaContextManagementConfig](api/beta.md) contextManagement, ?[BetaDiagnosticsParam](api/beta.md) diagnostics, ?string fallbackCreditToken, ?list<[BetaFallbackParam](api/beta.md)> fallbacks, ?string inferenceGeo, ?list<[BetaRequestMCPServerURLDefinition](api/beta.md)> mcpServers, ?[BetaMetadata](api/beta.md) metadata, ?[BetaOutputConfig](api/beta.md) outputConfig, ?[BetaJSONOutputFormat](api/beta.md) outputFormat, ?[ServiceTier](api/beta/messages/create.md) serviceTier, ?[Speed](api/beta/messages/create.md) speed, ?list<string> stopSequences, ?[System](api/beta/messages/create.md) system, ?float temperature, ?[BetaThinkingConfigParam](api/beta.md) thinking, ?[BetaToolChoice](api/beta.md) toolChoice, ?list<[BetaToolUnion](api/beta.md)> tools, ?int topK, ?float topP, ?string userProfileID, ?list<AnthropicBeta> betas): [BetaMessage](api/beta.md)

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

$client->beta->messages->countTokens(list<[BetaMessageParam](api/beta.md)> messages, Model model, ?[BetaCacheControlEphemeral](api/beta.md) cacheControl, ?[BetaContextManagementConfig](api/beta.md) contextManagement, ?list<[BetaRequestMCPServerURLDefinition](api/beta.md)> mcpServers, ?[BetaOutputConfig](api/beta.md) outputConfig, ?[BetaJSONOutputFormat](api/beta.md) outputFormat, ?[Speed](api/beta/messages/count_tokens.md) speed, ?[System](api/beta/messages/count_tokens.md) system, ?[BetaThinkingConfigParam](api/beta.md) thinking, ?[BetaToolChoice](api/beta.md) toolChoice, ?list<Tool> tools, ?list<AnthropicBeta> betas): [BetaMessageTokensCount](api/beta.md)

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse

[BetaAdvisorMessageIterationUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

int cacheReadInputTokens

The number of input tokens read from the cache.

int inputTokens

The number of input tokens which were used.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

int outputTokens

The number of output tokens which were used.

"advisor\_message" type

Usage for an advisor sub-inference iteration

[BetaAdvisorRedactedResultBlock](api/beta.md)

string encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

?string stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

"advisor\_redacted\_result" type

[BetaAdvisorRedactedResultBlockParam](api/beta.md)

string encryptedContent

Opaque blob produced by a prior response; must be round-tripped verbatim.

"advisor\_redacted\_result" type

?string stopReason

[BetaAdvisorResultBlock](api/beta.md)

?string stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

string text

"advisor\_result" type

[BetaAdvisorResultBlockParam](api/beta.md)

string text

"advisor\_result" type

?string stopReason

[BetaAdvisorTool20260301](api/beta.md)

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"advisor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"advisor\_20260301" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCacheControlEphemeral](api/beta.md) caching

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxTokens

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaAdvisorToolResultBlock](api/beta.md)

Content content

string toolUseID

"advisor\_tool\_result" type

[BetaAdvisorToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"advisor\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaAdvisorToolResultError](api/beta.md)

ErrorCode errorCode

"advisor\_tool\_result\_error" type

[BetaAdvisorToolResultErrorParam](api/beta.md)

ErrorCode errorCode

"advisor\_tool\_result\_error" type

[BetaAllThinkingTurns](api/beta.md)

"all" type

[BetaBase64ImageSource](api/beta.md)

string data

MediaType mediaType

"base64" type

[BetaBase64PDFSource](api/beta.md)

string data

"application/pdf" mediaType

"base64" type

[BetaBashCodeExecutionOutputBlock](api/beta.md)

string fileID

"bash\_code\_execution\_output" type

[BetaBashCodeExecutionOutputBlockParam](api/beta.md)

string fileID

"bash\_code\_execution\_output" type

[BetaBashCodeExecutionResultBlock](api/beta.md)

list<[BetaBashCodeExecutionOutputBlock](api/beta.md)> content

int returnCode

string stderr

string stdout

"bash\_code\_execution\_result" type

[BetaBashCodeExecutionResultBlockParam](api/beta.md)

list<[BetaBashCodeExecutionOutputBlockParam](api/beta.md)> content

int returnCode

string stderr

string stdout

"bash\_code\_execution\_result" type

[BetaBashCodeExecutionToolResultBlock](api/beta.md)

Content content

string toolUseID

"bash\_code\_execution\_tool\_result" type

[BetaBashCodeExecutionToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"bash\_code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaBashCodeExecutionToolResultError](api/beta.md)

ErrorCode errorCode

"bash\_code\_execution\_tool\_result\_error" type

[BetaBashCodeExecutionToolResultErrorParam](api/beta.md)

ErrorCode errorCode

"bash\_code\_execution\_tool\_result\_error" type

[BetaCacheControlEphemeral](api/beta.md)

"ephemeral" type

?TTL ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

[BetaCacheCreation](api/beta.md)

int ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

int ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

[BetaCacheMissMessagesChanged](api/beta.md)

int cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

"messages\_changed" type

[BetaCacheMissModelChanged](api/beta.md)

int cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

"model\_changed" type

[BetaCacheMissPreviousMessageNotFound](api/beta.md)

"previous\_message\_not\_found" type

[BetaCacheMissSystemChanged](api/beta.md)

int cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

"system\_changed" type

[BetaCacheMissToolsChanged](api/beta.md)

int cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

"tools\_changed" type

[BetaCacheMissUnavailable](api/beta.md)

"unavailable" type

[BetaCitationCharLocation](api/beta.md)

string citedText

int documentIndex

?string documentTitle

int endCharIndex

?string fileID

int startCharIndex

"char\_location" type

[BetaCitationCharLocationParam](api/beta.md)

string citedText

int documentIndex

?string documentTitle

int endCharIndex

int startCharIndex

"char\_location" type

[BetaCitationConfig](api/beta.md)

bool enabled

[BetaCitationContentBlockLocation](api/beta.md)

string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int documentIndex

?string documentTitle

int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

?string fileID

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

"content\_block\_location" type

[BetaCitationContentBlockLocationParam](api/beta.md)

string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int documentIndex

?string documentTitle

int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

"content\_block\_location" type

[BetaCitationPageLocation](api/beta.md)

string citedText

int documentIndex

?string documentTitle

int endPageNumber

?string fileID

int startPageNumber

"page\_location" type

[BetaCitationPageLocationParam](api/beta.md)

string citedText

int documentIndex

?string documentTitle

int endPageNumber

int startPageNumber

"page\_location" type

[BetaCitationSearchResultLocation](api/beta.md)

string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

int searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

string source

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

?string title

"search\_result\_location" type

[BetaCitationSearchResultLocationParam](api/beta.md)

string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

int searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

string source

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

?string title

"search\_result\_location" type

[BetaCitationWebSearchResultLocationParam](api/beta.md)

string citedText

string encryptedIndex

?string title

"web\_search\_result\_location" type

string url

[BetaCitationsConfigParam](api/beta.md)

?bool enabled

[BetaCitationsDelta](api/beta.md)

Citation citation

"citations\_delta" type

[BetaCitationsWebSearchResultLocation](api/beta.md)

string citedText

string encryptedIndex

?string title

"web\_search\_result\_location" type

string url

[BetaClearThinking20251015Edit](api/beta.md)

"clear\_thinking\_20251015" type

?Keep keep

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

[BetaClearThinking20251015EditResponse](api/beta.md)

int clearedInputTokens

Number of input tokens cleared by this edit.

int clearedThinkingTurns

Number of thinking turns that were cleared.

"clear\_thinking\_20251015" type

The type of context management edit applied.

[BetaClearToolUses20250919Edit](api/beta.md)

"clear\_tool\_uses\_20250919" type

?[BetaInputTokensClearAtLeast](api/beta.md) clearAtLeast

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

?ClearToolInputs clearToolInputs

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

?list<string> excludeTools

Tool names whose uses are preserved from clearing

?[BetaToolUsesKeep](api/beta.md) keep

Number of tool uses to retain in the conversation

?Trigger trigger

Condition that triggers the context management strategy

[BetaClearToolUses20250919EditResponse](api/beta.md)

int clearedInputTokens

Number of input tokens cleared by this edit.

int clearedToolUses

Number of tool uses that were cleared.

"clear\_tool\_uses\_20250919" type

The type of context management edit applied.

[BetaCodeExecutionOutputBlock](api/beta.md)

string fileID

"code\_execution\_output" type

[BetaCodeExecutionOutputBlockParam](api/beta.md)

string fileID

"code\_execution\_output" type

[BetaCodeExecutionResultBlock](api/beta.md)

list<[BetaCodeExecutionOutputBlock](api/beta.md)> content

int returnCode

string stderr

string stdout

"code\_execution\_result" type

[BetaCodeExecutionResultBlockParam](api/beta.md)

list<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

int returnCode

string stderr

string stdout

"code\_execution\_result" type

[BetaCodeExecutionTool20250522](api/beta.md)

"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250522" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaCodeExecutionTool20250825](api/beta.md)

"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250825" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaCodeExecutionTool20260120](api/beta.md)

"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20260120" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaCodeExecutionToolResultBlock](api/beta.md)

[BetaCodeExecutionToolResultBlockContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

string toolUseID

"code\_execution\_tool\_result" type

[BetaCodeExecutionToolResultBlockContent](api/beta.md)

One of the following:

[BetaCodeExecutionToolResultError](api/beta.md)

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

"code\_execution\_tool\_result\_error" type

[BetaCodeExecutionResultBlock](api/beta.md)

list<[BetaCodeExecutionOutputBlock](api/beta.md)> content

int returnCode

string stderr

string stdout

"code\_execution\_result" type

[BetaEncryptedCodeExecutionResultBlock](api/beta.md)

list<[BetaCodeExecutionOutputBlock](api/beta.md)> content

string encryptedStdout

int returnCode

string stderr

"encrypted\_code\_execution\_result" type

[BetaCodeExecutionToolResultBlockParam](api/beta.md)

[BetaCodeExecutionToolResultBlockParamContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

string toolUseID

"code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaCodeExecutionToolResultBlockParamContent](api/beta.md)

One of the following:

[BetaCodeExecutionToolResultErrorParam](api/beta.md)

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

"code\_execution\_tool\_result\_error" type

[BetaCodeExecutionResultBlockParam](api/beta.md)

list<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

int returnCode

string stderr

string stdout

"code\_execution\_result" type

[BetaEncryptedCodeExecutionResultBlockParam](api/beta.md)

list<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

string encryptedStdout

int returnCode

string stderr

"encrypted\_code\_execution\_result" type

[BetaCodeExecutionToolResultError](api/beta.md)

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

"code\_execution\_tool\_result\_error" type

[BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

[BetaCodeExecutionToolResultErrorParam](api/beta.md)

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

"code\_execution\_tool\_result\_error" type

[BetaCompact20260112Edit](api/beta.md)

"compact\_20260112" type

?string instructions

Additional instructions for summarization.

?bool pauseAfterCompaction

Whether to pause after compaction and return the compaction block to the user.

?[BetaInputTokensTrigger](api/beta.md) trigger

When to trigger compaction. Defaults to 150000 input tokens.

[BetaCompactionBlock](api/beta.md)

?string content

Summary of compacted content, or null if compaction failed

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

"compaction" type

[BetaCompactionBlockParam](api/beta.md)

"compaction" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?string content

Summary of previously compacted content, or null if compaction failed

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

[BetaCompactionContentBlockDelta](api/beta.md)

?string content

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

"compaction\_delta" type

[BetaCompactionIterationUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

int cacheReadInputTokens

The number of input tokens read from the cache.

int inputTokens

The number of input tokens which were used.

int outputTokens

The number of output tokens which were used.

"compaction" type

Usage for a compaction iteration

[BetaContainer](api/beta.md)

string id

Identifier for the container used in this request

\Datetime expiresAt

The time at which the container will expire.

?list<[BetaSkill](api/beta.md)> skills

Skills loaded in the container

[BetaContainerParams](api/beta.md)

?string id

Container id

?list<[BetaSkillParams](api/beta.md)> skills

List of skills to load in the container

[BetaContainerUploadBlock](api/beta.md)

string fileID

"container\_upload" type

[BetaContainerUploadBlockParam](api/beta.md)

string fileID

"container\_upload" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaContentBlock](api/beta.md)

One of the following:

[BetaTextBlock](api/beta.md)

?list<[BetaTextCitation](api/beta.md)> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

string text

"text" type

[BetaThinkingBlock](api/beta.md)

string signature

string thinking

"thinking" type

[BetaRedactedThinkingBlock](api/beta.md)

string data

"redacted\_thinking" type

[BetaToolUseBlock](api/beta.md)

string id

array<string,mixed> input

string name

"tool\_use" type

?Caller caller

Tool invocation directly from the model.

[BetaServerToolUseBlock](api/beta.md)

string id

array<string,mixed> input

Name name

"server\_tool\_use" type

?Caller caller

Tool invocation directly from the model.

[BetaWebSearchToolResultBlock](api/beta.md)

[BetaWebSearchToolResultBlockContent](api/beta.md) content

string toolUseID

"web\_search\_tool\_result" type

?Caller caller

Tool invocation directly from the model.

[BetaWebFetchToolResultBlock](api/beta.md)

Content content

string toolUseID

"web\_fetch\_tool\_result" type

?Caller caller

Tool invocation directly from the model.

[BetaAdvisorToolResultBlock](api/beta.md)

Content content

string toolUseID

"advisor\_tool\_result" type

[BetaCodeExecutionToolResultBlock](api/beta.md)

[BetaCodeExecutionToolResultBlockContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

string toolUseID

"code\_execution\_tool\_result" type

[BetaBashCodeExecutionToolResultBlock](api/beta.md)

Content content

string toolUseID

"bash\_code\_execution\_tool\_result" type

[BetaTextEditorCodeExecutionToolResultBlock](api/beta.md)

Content content

string toolUseID

"text\_editor\_code\_execution\_tool\_result" type

[BetaToolSearchToolResultBlock](api/beta.md)

Content content

string toolUseID

"tool\_search\_tool\_result" type

[BetaMCPToolUseBlock](api/beta.md)

string id

array<string,mixed> input

string name

The name of the MCP tool

string serverName

The name of the MCP server

"mcp\_tool\_use" type

[BetaMCPToolResultBlock](api/beta.md)

Content content

bool isError

string toolUseID

"mcp\_tool\_result" type

[BetaContainerUploadBlock](api/beta.md)

string fileID

"container\_upload" type

[BetaCompactionBlock](api/beta.md)

?string content

Summary of compacted content, or null if compaction failed

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

"compaction" type

[BetaFallbackBlock](api/beta.md)

[BetaFallbackInfo](api/beta.md) from

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

[BetaFallbackInfo](api/beta.md) to

The fallback model producing the content that follows this block. Its `model` is always the canonical id.

"fallback" type

[BetaContentBlockParam](api/beta.md)

One of the following:

[BetaTextBlockParam](api/beta.md)

string text

"text" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?list<[BetaTextCitationParam](api/beta.md)> citations

[BetaImageBlockParam](api/beta.md)

Source source

"image" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaRequestDocumentBlock](api/beta.md)

Source source

"document" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

?string context

?string title

[BetaSearchResultBlockParam](api/beta.md)

list<[BetaTextBlockParam](api/beta.md)> content

string source

string title

"search\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

[BetaThinkingBlockParam](api/beta.md)

string signature

string thinking

"thinking" type

[BetaRedactedThinkingBlockParam](api/beta.md)

string data

"redacted\_thinking" type

[BetaToolUseBlockParam](api/beta.md)

string id

array<string,mixed> input

string name

"tool\_use" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.

[BetaToolResultBlockParam](api/beta.md)

string toolUseID

"tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Content content

?bool isError

[BetaServerToolUseBlockParam](api/beta.md)

string id

array<string,mixed> input

Name name

"server\_tool\_use" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.

[BetaWebSearchToolResultBlockParam](api/beta.md)

[BetaWebSearchToolResultBlockParamContent](api/beta.md) content

string toolUseID

"web\_search\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.

[BetaWebFetchToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"web\_fetch\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.

[BetaAdvisorToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"advisor\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaCodeExecutionToolResultBlockParam](api/beta.md)

[BetaCodeExecutionToolResultBlockParamContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

string toolUseID

"code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaBashCodeExecutionToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"bash\_code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaTextEditorCodeExecutionToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"text\_editor\_code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaToolSearchToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"tool\_search\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaMCPToolUseBlockParam](api/beta.md)

string id

array<string,mixed> input

string name

string serverName

The name of the MCP server

"mcp\_tool\_use" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaRequestMCPToolResultBlockParam](api/beta.md)

string toolUseID

"mcp\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Content content

?bool isError

[BetaContainerUploadBlockParam](api/beta.md)

string fileID

"container\_upload" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaCompactionBlockParam](api/beta.md)

"compaction" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?string content

Summary of previously compacted content, or null if compaction failed

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

[BetaMidConversationSystemBlockParam](api/beta.md)

list<[BetaTextBlockParam](api/beta.md)> content

System instruction text blocks.

"mid\_conv\_system" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaFallbackBlockParam](api/beta.md)

[BetaFallbackInfoParam](api/beta.md) from

Identifies one hop of a fallback transition.

[BetaFallbackInfoParam](api/beta.md) to

Identifies one hop of a fallback transition.

"fallback" type

[BetaContentBlockSource](api/beta.md)

Content content

"content" type

[BetaContentBlockSourceContent](api/beta.md)

One of the following:

[BetaTextBlockParam](api/beta.md)

string text

"text" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?list<[BetaTextCitationParam](api/beta.md)> citations

[BetaImageBlockParam](api/beta.md)

Source source

"image" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaContextManagementConfig](api/beta.md)

?list<Edit> edits

List of context management edits to apply

[BetaContextManagementResponse](api/beta.md)

list<AppliedEdit> appliedEdits

List of context management edits that were applied.

[BetaCountTokensContextManagementResponse](api/beta.md)

int originalInputTokens

The original token count before context management was applied

[BetaDiagnostics](api/beta.md)

?CacheMissReason cacheMissReason

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

[BetaDiagnosticsParam](api/beta.md)

?string previousMessageID

The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

[BetaDirectCaller](api/beta.md)

"direct" type

[BetaDocumentBlock](api/beta.md)

?[BetaCitationConfig](api/beta.md) citations

Citation configuration for the document

Source source

?string title

The title of the document

"document" type

[BetaEncryptedCodeExecutionResultBlock](api/beta.md)

list<[BetaCodeExecutionOutputBlock](api/beta.md)> content

string encryptedStdout

int returnCode

string stderr

"encrypted\_code\_execution\_result" type

[BetaEncryptedCodeExecutionResultBlockParam](api/beta.md)

list<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

string encryptedStdout

int returnCode

string stderr

"encrypted\_code\_execution\_result" type

[BetaFallbackBlock](api/beta.md)

[BetaFallbackInfo](api/beta.md) from

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

[BetaFallbackInfo](api/beta.md) to

The fallback model producing the content that follows this block. Its `model` is always the canonical id.

"fallback" type

[BetaFallbackBlockParam](api/beta.md)

[BetaFallbackInfoParam](api/beta.md) from

Identifies one hop of a fallback transition.

[BetaFallbackInfoParam](api/beta.md) to

Identifies one hop of a fallback transition.

"fallback" type

[BetaFallbackInfo](api/beta.md)

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

[BetaFallbackInfoParam](api/beta.md)

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

[BetaFallbackMessageIterationUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

int cacheReadInputTokens

The number of input tokens read from the cache.

int inputTokens

The number of input tokens which were used.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

int outputTokens

The number of output tokens which were used.

"fallback\_message" type

Usage for the fallback-model attempt that served the response

[BetaFallbackParam](api/beta.md)

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

?int maxTokens

?[BetaOutputConfig](api/beta.md) outputConfig

?Speed speed

?Thinking thinking

[BetaFileDocumentSource](api/beta.md)

string fileID

"file" type

[BetaFileImageSource](api/beta.md)

string fileID

"file" type

[BetaImageBlockParam](api/beta.md)

Source source

"image" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaInputJSONDelta](api/beta.md)

string partialJSON

"input\_json\_delta" type

[BetaInputTokensClearAtLeast](api/beta.md)

"input\_tokens" type

int value

[BetaInputTokensTrigger](api/beta.md)

"input\_tokens" type

int value

list<BetaIterationsUsageItem>

One of the following:

[BetaMessageIterationUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

int cacheReadInputTokens

The number of input tokens read from the cache.

int inputTokens

The number of input tokens which were used.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

int outputTokens

The number of output tokens which were used.

"message" type

Usage for a sampling iteration

[BetaCompactionIterationUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

int cacheReadInputTokens

The number of input tokens read from the cache.

int inputTokens

The number of input tokens which were used.

int outputTokens

The number of output tokens which were used.

"compaction" type

Usage for a compaction iteration

[BetaAdvisorMessageIterationUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

int cacheReadInputTokens

The number of input tokens read from the cache.

int inputTokens

The number of input tokens which were used.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

int outputTokens

The number of output tokens which were used.

"advisor\_message" type

Usage for an advisor sub-inference iteration

[BetaFallbackMessageIterationUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

int cacheReadInputTokens

The number of input tokens read from the cache.

int inputTokens

The number of input tokens which were used.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

int outputTokens

The number of output tokens which were used.

"fallback\_message" type

Usage for the fallback-model attempt that served the response

[BetaJSONOutputFormat](api/beta.md)

array<string,mixed> schema

The JSON schema of the format

"json\_schema" type

[BetaMCPToolConfig](api/beta.md)

?bool deferLoading

?bool enabled

[BetaMCPToolDefaultConfig](api/beta.md)

?bool deferLoading

?bool enabled

[BetaMCPToolResultBlock](api/beta.md)

Content content

bool isError

string toolUseID

"mcp\_tool\_result" type

[BetaMCPToolUseBlock](api/beta.md)

string id

array<string,mixed> input

string name

The name of the MCP tool

string serverName

The name of the MCP server

"mcp\_tool\_use" type

[BetaMCPToolUseBlockParam](api/beta.md)

string id

array<string,mixed> input

string name

string serverName

The name of the MCP server

"mcp\_tool\_use" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaMCPToolset](api/beta.md)

string mcpServerName

Name of the MCP server to configure tools for

"mcp\_toolset" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?array<string,[BetaMCPToolConfig](api/beta.md)> configs

Configuration overrides for specific tools, keyed by tool name

?[BetaMCPToolDefaultConfig](api/beta.md) defaultConfig

Default configuration applied to all tools from this server

[BetaMemoryTool20250818](api/beta.md)

"memory" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"memory\_20250818" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaMemoryTool20250818Command](api/beta.md)

One of the following:

[BetaMemoryTool20250818ViewCommand](api/beta.md)

"view" command

Command type identifier

string path

Path to directory or file to view

?list<int> viewRange

Optional line range for viewing specific lines

[BetaMemoryTool20250818CreateCommand](api/beta.md)

"create" command

Command type identifier

string fileText

Content to write to the file

string path

Path where the file should be created

[BetaMemoryTool20250818StrReplaceCommand](api/beta.md)

"str\_replace" command

Command type identifier

string newStr

Text to replace with

string oldStr

Text to search for and replace

string path

Path to the file where text should be replaced

[BetaMemoryTool20250818InsertCommand](api/beta.md)

"insert" command

Command type identifier

int insertLine

Line number where text should be inserted

string insertText

Text to insert at the specified line

string path

Path to the file where text should be inserted

[BetaMemoryTool20250818DeleteCommand](api/beta.md)

"delete" command

Command type identifier

string path

Path to the file or directory to delete

[BetaMemoryTool20250818RenameCommand](api/beta.md)

"rename" command

Command type identifier

string newPath

New path for the file or directory

string oldPath

Current path of the file or directory

[BetaMemoryTool20250818CreateCommand](api/beta.md)

"create" command

Command type identifier

string fileText

Content to write to the file

string path

Path where the file should be created

[BetaMemoryTool20250818DeleteCommand](api/beta.md)

"delete" command

Command type identifier

string path

Path to the file or directory to delete

[BetaMemoryTool20250818InsertCommand](api/beta.md)

"insert" command

Command type identifier

int insertLine

Line number where text should be inserted

string insertText

Text to insert at the specified line

string path

Path to the file where text should be inserted

[BetaMemoryTool20250818RenameCommand](api/beta.md)

"rename" command

Command type identifier

string newPath

New path for the file or directory

string oldPath

Current path of the file or directory

[BetaMemoryTool20250818StrReplaceCommand](api/beta.md)

"str\_replace" command

Command type identifier

string newStr

Text to replace with

string oldStr

Text to search for and replace

string path

Path to the file where text should be replaced

[BetaMemoryTool20250818ViewCommand](api/beta.md)

"view" command

Command type identifier

string path

Path to directory or file to view

?list<int> viewRange

Optional line range for viewing specific lines

[BetaMessage](api/beta.md)

string id

Unique object identifier.

The format and length of IDs may change over time.

?[BetaContainer](api/beta.md) container

Information about the container used in the request (for the code execution tool)

list<[BetaContentBlock](api/beta.md)> content

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

?[BetaContextManagementResponse](api/beta.md) contextManagement

Context management response.

Information about context management strategies applied during the request.

?[BetaDiagnostics](api/beta.md) diagnostics

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"assistant" role

Conversational role of the generated message.

This will always be `"assistant"`.

?[BetaRefusalStopDetails](api/beta.md) stopDetails

Structured information about a refusal.

?[BetaStopReason](api/beta.md) stopReason

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

?string stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

"message" type

Object type.

For Messages, this is always `"message"`.

[BetaUsage](api/beta.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

[BetaMessageDeltaUsage](api/beta.md)

?int cacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

?int cacheReadInputTokens

The cumulative number of input tokens read from the cache.

?int inputTokens

The cumulative number of input tokens which were used.

?list<BetaIterationsUsageItem> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

int outputTokens

The cumulative number of output tokens which were used.

?[BetaOutputTokensDetails](api/beta.md) outputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.

?[BetaServerToolUsage](api/beta.md) serverToolUse

The number of server tool requests.

[BetaMessageIterationUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

int cacheReadInputTokens

The number of input tokens read from the cache.

int inputTokens

The number of input tokens which were used.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

int outputTokens

The number of output tokens which were used.

"message" type

Usage for a sampling iteration

[BetaMessageParam](api/beta.md)

Content content

Role role

[BetaMessageTokensCount](api/beta.md)

?[BetaCountTokensContextManagementResponse](api/beta.md) contextManagement

Information about context management applied to the message.

int inputTokens

The total number of tokens across the provided list of messages, system prompt, and tools.

[BetaMetadata](api/beta.md)

?string userID

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

[BetaMidConversationSystemBlockParam](api/beta.md)

list<[BetaTextBlockParam](api/beta.md)> content

System instruction text blocks.

"mid\_conv\_system" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaOutputConfig](api/beta.md)

?Effort effort

All possible effort levels.

?[BetaJSONOutputFormat](api/beta.md) format

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

?[BetaTokenTaskBudget](api/beta.md) taskBudget

User-configurable total token budget across contexts.

[BetaOutputTokensDetails](api/beta.md)

int thinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

[BetaPlainTextSource](api/beta.md)

string data

"text/plain" mediaType

"text" type

[BetaRawContentBlockDelta](api/beta.md)

One of the following:

[BetaTextDelta](api/beta.md)

string text

"text\_delta" type

[BetaInputJSONDelta](api/beta.md)

string partialJSON

"input\_json\_delta" type

[BetaCitationsDelta](api/beta.md)

Citation citation

"citations\_delta" type

[BetaThinkingDelta](api/beta.md)

?int estimatedTokens

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

string thinking

"thinking\_delta" type

[BetaSignatureDelta](api/beta.md)

string signature

"signature\_delta" type

[BetaCompactionContentBlockDelta](api/beta.md)

?string content

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

"compaction\_delta" type

[BetaRawContentBlockDeltaEvent](api/beta.md)

[BetaRawContentBlockDelta](api/beta.md) delta

int index

"content\_block\_delta" type

[BetaRawContentBlockStartEvent](api/beta.md)

ContentBlock contentBlock

Response model for a file uploaded to the container.

int index

"content\_block\_start" type

[BetaRawContentBlockStopEvent](api/beta.md)

int index

"content\_block\_stop" type

[BetaRawMessageDeltaEvent](api/beta.md)

?[BetaContextManagementResponse](api/beta.md) contextManagement

Information about context management strategies applied during the request

Delta delta

"message\_delta" type

[BetaMessageDeltaUsage](api/beta.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

[BetaRawMessageStartEvent](api/beta.md)

[BetaMessage](api/beta.md) message

"message\_start" type

[BetaRawMessageStopEvent](api/beta.md)

"message\_stop" type

[BetaRawMessageStreamEvent](api/beta.md)

One of the following:

[BetaRawMessageStartEvent](api/beta.md)

[BetaMessage](api/beta.md) message

"message\_start" type

[BetaRawMessageDeltaEvent](api/beta.md)

?[BetaContextManagementResponse](api/beta.md) contextManagement

Information about context management strategies applied during the request

Delta delta

"message\_delta" type

[BetaMessageDeltaUsage](api/beta.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

[BetaRawMessageStopEvent](api/beta.md)

"message\_stop" type

[BetaRawContentBlockStartEvent](api/beta.md)

ContentBlock contentBlock

Response model for a file uploaded to the container.

int index

"content\_block\_start" type

[BetaRawContentBlockDeltaEvent](api/beta.md)

[BetaRawContentBlockDelta](api/beta.md) delta

int index

"content\_block\_delta" type

[BetaRawContentBlockStopEvent](api/beta.md)

int index

"content\_block\_stop" type

[BetaRedactedThinkingBlock](api/beta.md)

string data

"redacted\_thinking" type

[BetaRedactedThinkingBlockParam](api/beta.md)

string data

"redacted\_thinking" type

[BetaRefusalStopDetails](api/beta.md)

?Category category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

?string explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

?string fallbackCreditToken

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

?bool fallbackHasPrefillClaim

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

?string recommendedModel

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

"refusal" type

[BetaRequestDocumentBlock](api/beta.md)

Source source

"document" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

?string context

?string title

[BetaRequestMCPServerToolConfiguration](api/beta.md)

?list<string> allowedTools

?bool enabled

[BetaRequestMCPServerURLDefinition](api/beta.md)

string name

"url" type

string url

?string authorizationToken

?[BetaRequestMCPServerToolConfiguration](api/beta.md) toolConfiguration

[BetaRequestMCPToolResultBlockParam](api/beta.md)

string toolUseID

"mcp\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Content content

?bool isError

[BetaSearchResultBlockParam](api/beta.md)

list<[BetaTextBlockParam](api/beta.md)> content

string source

string title

"search\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

[BetaServerToolCaller](api/beta.md)

string toolID

"code\_execution\_20250825" type

[BetaServerToolCaller20260120](api/beta.md)

string toolID

"code\_execution\_20260120" type

[BetaServerToolUsage](api/beta.md)

int webFetchRequests

The number of web fetch tool requests.

int webSearchRequests

The number of web search tool requests.

[BetaServerToolUseBlock](api/beta.md)

string id

array<string,mixed> input

Name name

"server\_tool\_use" type

?Caller caller

Tool invocation directly from the model.

[BetaServerToolUseBlockParam](api/beta.md)

string id

array<string,mixed> input

Name name

"server\_tool\_use" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.

[BetaSignatureDelta](api/beta.md)

string signature

"signature\_delta" type

[BetaSkill](api/beta.md)

string skillID

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

string version

Skill version or 'latest' for most recent version

[BetaSkillParams](api/beta.md)

string skillID

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

?string version

Skill version or 'latest' for most recent version

[BetaStopReason](api/beta.md)

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

[BetaTextBlock](api/beta.md)

?list<[BetaTextCitation](api/beta.md)> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

string text

"text" type

[BetaTextBlockParam](api/beta.md)

string text

"text" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?list<[BetaTextCitationParam](api/beta.md)> citations

[BetaTextCitation](api/beta.md)

One of the following:

[BetaCitationCharLocation](api/beta.md)

string citedText

int documentIndex

?string documentTitle

int endCharIndex

?string fileID

int startCharIndex

"char\_location" type

[BetaCitationPageLocation](api/beta.md)

string citedText

int documentIndex

?string documentTitle

int endPageNumber

?string fileID

int startPageNumber

"page\_location" type

[BetaCitationContentBlockLocation](api/beta.md)

string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int documentIndex

?string documentTitle

int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

?string fileID

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

"content\_block\_location" type

[BetaCitationsWebSearchResultLocation](api/beta.md)

string citedText

string encryptedIndex

?string title

"web\_search\_result\_location" type

string url

[BetaCitationSearchResultLocation](api/beta.md)

string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

int searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

string source

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

?string title

"search\_result\_location" type

[BetaTextCitationParam](api/beta.md)

One of the following:

[BetaCitationCharLocationParam](api/beta.md)

string citedText

int documentIndex

?string documentTitle

int endCharIndex

int startCharIndex

"char\_location" type

[BetaCitationPageLocationParam](api/beta.md)

string citedText

int documentIndex

?string documentTitle

int endPageNumber

int startPageNumber

"page\_location" type

[BetaCitationContentBlockLocationParam](api/beta.md)

string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int documentIndex

?string documentTitle

int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

"content\_block\_location" type

[BetaCitationWebSearchResultLocationParam](api/beta.md)

string citedText

string encryptedIndex

?string title

"web\_search\_result\_location" type

string url

[BetaCitationSearchResultLocationParam](api/beta.md)

string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

int searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

string source

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

?string title

"search\_result\_location" type

[BetaTextDelta](api/beta.md)

string text

"text\_delta" type

[BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md)

bool isFileUpdate

"text\_editor\_code\_execution\_create\_result" type

[BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta.md)

bool isFileUpdate

"text\_editor\_code\_execution\_create\_result" type

[BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md)

?list<string> lines

?int newLines

?int newStart

?int oldLines

?int oldStart

"text\_editor\_code\_execution\_str\_replace\_result" type

[BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta.md)

"text\_editor\_code\_execution\_str\_replace\_result" type

?list<string> lines

?int newLines

?int newStart

?int oldLines

?int oldStart

[BetaTextEditorCodeExecutionToolResultBlock](api/beta.md)

Content content

string toolUseID

"text\_editor\_code\_execution\_tool\_result" type

[BetaTextEditorCodeExecutionToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"text\_editor\_code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaTextEditorCodeExecutionToolResultError](api/beta.md)

ErrorCode errorCode

?string errorMessage

"text\_editor\_code\_execution\_tool\_result\_error" type

[BetaTextEditorCodeExecutionToolResultErrorParam](api/beta.md)

ErrorCode errorCode

"text\_editor\_code\_execution\_tool\_result\_error" type

?string errorMessage

[BetaTextEditorCodeExecutionViewResultBlock](api/beta.md)

string content

FileType fileType

?int numLines

?int startLine

?int totalLines

"text\_editor\_code\_execution\_view\_result" type

[BetaTextEditorCodeExecutionViewResultBlockParam](api/beta.md)

string content

FileType fileType

"text\_editor\_code\_execution\_view\_result" type

?int numLines

?int startLine

?int totalLines

[BetaThinkingBlock](api/beta.md)

string signature

string thinking

"thinking" type

[BetaThinkingBlockParam](api/beta.md)

string signature

string thinking

"thinking" type

[BetaThinkingConfigAdaptive](api/beta.md)

"adaptive" type

?Display display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

[BetaThinkingConfigDisabled](api/beta.md)

"disabled" type

[BetaThinkingConfigEnabled](api/beta.md)

int budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

"enabled" type

?Display display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

[BetaThinkingConfigParam](api/beta.md)

One of the following:

[BetaThinkingConfigEnabled](api/beta.md)

int budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

"enabled" type

?Display display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

[BetaThinkingConfigDisabled](api/beta.md)

"disabled" type

[BetaThinkingConfigAdaptive](api/beta.md)

"adaptive" type

?Display display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

[BetaThinkingDelta](api/beta.md)

?int estimatedTokens

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

string thinking

"thinking\_delta" type

[BetaThinkingTurns](api/beta.md)

"thinking\_turns" type

int value

[BetaTokenTaskBudget](api/beta.md)

int total

Total token budget across all contexts in the session.

"tokens" type

The budget type. Currently only 'tokens' is supported.

?int remaining

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

[BetaTool](api/beta.md)

InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

string name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?string description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

?bool eagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

?Type type

[BetaToolBash20241022](api/beta.md)

"bash" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"bash\_20241022" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolBash20250124](api/beta.md)

"bash" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"bash\_20250124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolChoice](api/beta.md)

One of the following:

[BetaToolChoiceAuto](api/beta.md)

"auto" type

?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

[BetaToolChoiceAny](api/beta.md)

"any" type

?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

[BetaToolChoiceTool](api/beta.md)

string name

The name of the tool to use.

"tool" type

?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

[BetaToolChoiceNone](api/beta.md)

"none" type

[BetaToolChoiceAny](api/beta.md)

"any" type

?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

[BetaToolChoiceAuto](api/beta.md)

"auto" type

?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

[BetaToolChoiceNone](api/beta.md)

"none" type

[BetaToolChoiceTool](api/beta.md)

string name

The name of the tool to use.

"tool" type

?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

[BetaToolComputerUse20241022](api/beta.md)

int displayHeightPx

The height of the display in pixels.

int displayWidthPx

The width of the display in pixels.

"computer" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"computer\_20241022" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int displayNumber

The X11 display number (e.g. 0, 1) for the display.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolComputerUse20250124](api/beta.md)

int displayHeightPx

The height of the display in pixels.

int displayWidthPx

The width of the display in pixels.

"computer" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"computer\_20250124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int displayNumber

The X11 display number (e.g. 0, 1) for the display.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolComputerUse20251124](api/beta.md)

int displayHeightPx

The height of the display in pixels.

int displayWidthPx

The width of the display in pixels.

"computer" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"computer\_20251124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int displayNumber

The X11 display number (e.g. 0, 1) for the display.

?bool enableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolReferenceBlock](api/beta.md)

string toolName

"tool\_reference" type

[BetaToolReferenceBlockParam](api/beta.md)

string toolName

"tool\_reference" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaToolResultBlockParam](api/beta.md)

string toolUseID

"tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Content content

?bool isError

[BetaToolSearchToolBm25\_20251119](api/beta.md)

"tool\_search\_tool\_bm25" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolSearchToolRegex20251119](api/beta.md)

"tool\_search\_tool\_regex" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolSearchToolResultBlock](api/beta.md)

Content content

string toolUseID

"tool\_search\_tool\_result" type

[BetaToolSearchToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"tool\_search\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

[BetaToolSearchToolResultError](api/beta.md)

ErrorCode errorCode

?string errorMessage

"tool\_search\_tool\_result\_error" type

[BetaToolSearchToolResultErrorParam](api/beta.md)

ErrorCode errorCode

"tool\_search\_tool\_result\_error" type

?string errorMessage

[BetaToolSearchToolSearchResultBlock](api/beta.md)

list<[BetaToolReferenceBlock](api/beta.md)> toolReferences

"tool\_search\_tool\_search\_result" type

[BetaToolSearchToolSearchResultBlockParam](api/beta.md)

list<[BetaToolReferenceBlockParam](api/beta.md)> toolReferences

"tool\_search\_tool\_search\_result" type

[BetaToolTextEditor20241022](api/beta.md)

"str\_replace\_editor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20241022" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolTextEditor20250124](api/beta.md)

"str\_replace\_editor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolTextEditor20250429](api/beta.md)

"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250429" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolTextEditor20250728](api/beta.md)

"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250728" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?int maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolUnion](api/beta.md)

One of the following:

[BetaTool](api/beta.md)

InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

string name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?string description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

?bool eagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

?Type type

[BetaToolBash20241022](api/beta.md)

"bash" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"bash\_20241022" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolBash20250124](api/beta.md)

"bash" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"bash\_20250124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaCodeExecutionTool20250522](api/beta.md)

"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250522" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaCodeExecutionTool20250825](api/beta.md)

"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250825" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaCodeExecutionTool20260120](api/beta.md)

"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20260120" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolComputerUse20241022](api/beta.md)

int displayHeightPx

The height of the display in pixels.

int displayWidthPx

The width of the display in pixels.

"computer" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"computer\_20241022" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int displayNumber

The X11 display number (e.g. 0, 1) for the display.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaMemoryTool20250818](api/beta.md)

"memory" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"memory\_20250818" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolComputerUse20250124](api/beta.md)

int displayHeightPx

The height of the display in pixels.

int displayWidthPx

The width of the display in pixels.

"computer" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"computer\_20250124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int displayNumber

The X11 display number (e.g. 0, 1) for the display.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolTextEditor20241022](api/beta.md)

"str\_replace\_editor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20241022" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolComputerUse20251124](api/beta.md)

int displayHeightPx

The height of the display in pixels.

int displayWidthPx

The width of the display in pixels.

"computer" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"computer\_20251124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int displayNumber

The X11 display number (e.g. 0, 1) for the display.

?bool enableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolTextEditor20250124](api/beta.md)

"str\_replace\_editor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolTextEditor20250429](api/beta.md)

"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250429" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolTextEditor20250728](api/beta.md)

"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250728" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?int maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaWebSearchTool20250305](api/beta.md)

"web\_search" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_search\_20250305" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

?list<string> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[BetaUserLocation](api/beta.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.

[BetaWebFetchTool20250910](api/beta.md)

"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20250910" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaWebSearchTool20260209](api/beta.md)

"web\_search" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_search\_20260209" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

?list<string> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[BetaUserLocation](api/beta.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.

[BetaWebFetchTool20260209](api/beta.md)

"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20260209" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaWebFetchTool20260309](api/beta.md)

"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20260309" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?bool useCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

[BetaAdvisorTool20260301](api/beta.md)

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"advisor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"advisor\_20260301" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCacheControlEphemeral](api/beta.md) caching

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxTokens

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolSearchToolBm25\_20251119](api/beta.md)

"tool\_search\_tool\_bm25" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaToolSearchToolRegex20251119](api/beta.md)

"tool\_search\_tool\_regex" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaMCPToolset](api/beta.md)

string mcpServerName

Name of the MCP server to configure tools for

"mcp\_toolset" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?array<string,[BetaMCPToolConfig](api/beta.md)> configs

Configuration overrides for specific tools, keyed by tool name

?[BetaMCPToolDefaultConfig](api/beta.md) defaultConfig

Default configuration applied to all tools from this server

[BetaToolUseBlock](api/beta.md)

string id

array<string,mixed> input

string name

"tool\_use" type

?Caller caller

Tool invocation directly from the model.

[BetaToolUseBlockParam](api/beta.md)

string id

array<string,mixed> input

string name

"tool\_use" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.

[BetaToolUsesKeep](api/beta.md)

"tool\_uses" type

int value

[BetaToolUsesTrigger](api/beta.md)

"tool\_uses" type

int value

[BetaURLImageSource](api/beta.md)

"url" type

string url

[BetaURLPDFSource](api/beta.md)

"url" type

string url

[BetaUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

?int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

?int cacheReadInputTokens

The number of input tokens read from the cache.

?string inferenceGeo

The geographic region where inference was performed for this request.

int inputTokens

The number of input tokens which were used.

?list<BetaIterationsUsageItem> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

int outputTokens

The number of output tokens which were used.

?[BetaOutputTokensDetails](api/beta.md) outputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.

?[BetaServerToolUsage](api/beta.md) serverToolUse

The number of server tool requests.

?ServiceTier serviceTier

If the request used the priority, standard, or batch tier.

?Speed speed

The inference speed mode used for this request.

[BetaUserLocation](api/beta.md)

"approximate" type

?string city

The city of the user.

?string country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

?string region

The region of the user.

?string timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

[BetaWebFetchBlock](api/beta.md)

[BetaDocumentBlock](api/beta.md) content

?string retrievedAt

ISO 8601 timestamp when the content was retrieved

"web\_fetch\_result" type

string url

Fetched content URL

[BetaWebFetchBlockParam](api/beta.md)

[BetaRequestDocumentBlock](api/beta.md) content

"web\_fetch\_result" type

string url

Fetched content URL

?string retrievedAt

ISO 8601 timestamp when the content was retrieved

[BetaWebFetchTool20250910](api/beta.md)

"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20250910" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaWebFetchTool20260209](api/beta.md)

"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20260209" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

[BetaWebFetchTool20260309](api/beta.md)

"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20260309" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?bool useCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

[BetaWebFetchToolResultBlock](api/beta.md)

Content content

string toolUseID

"web\_fetch\_tool\_result" type

?Caller caller

Tool invocation directly from the model.

[BetaWebFetchToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"web\_fetch\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.

[BetaWebFetchToolResultErrorBlock](api/beta.md)

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

"web\_fetch\_tool\_result\_error" type

[BetaWebFetchToolResultErrorBlockParam](api/beta.md)

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

"web\_fetch\_tool\_result\_error" type

[BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

[BetaWebSearchResultBlock](api/beta.md)

string encryptedContent

?string pageAge

string title

"web\_search\_result" type

string url

[BetaWebSearchResultBlockParam](api/beta.md)

string encryptedContent

string title

"web\_search\_result" type

string url

?string pageAge

[BetaWebSearchTool20250305](api/beta.md)

"web\_search" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_search\_20250305" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

?list<string> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[BetaUserLocation](api/beta.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.

[BetaWebSearchTool20260209](api/beta.md)

"web\_search" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_search\_20260209" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

?list<string> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[BetaUserLocation](api/beta.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.

[BetaWebSearchToolRequestError](api/beta.md)

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

"web\_search\_tool\_result\_error" type

[BetaWebSearchToolResultBlock](api/beta.md)

[BetaWebSearchToolResultBlockContent](api/beta.md) content

string toolUseID

"web\_search\_tool\_result" type

?Caller caller

Tool invocation directly from the model.

[BetaWebSearchToolResultBlockContent](api/beta.md)

One of the following:

[BetaWebSearchToolResultError](api/beta.md)

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

"web\_search\_tool\_result\_error" type

list<[BetaWebSearchResultBlock](api/beta.md)>

string encryptedContent

?string pageAge

string title

"web\_search\_result" type

string url

[BetaWebSearchToolResultBlockParam](api/beta.md)

[BetaWebSearchToolResultBlockParamContent](api/beta.md) content

string toolUseID

"web\_search\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.

[BetaWebSearchToolResultBlockParamContent](api/beta.md)

One of the following:

list<[BetaWebSearchResultBlockParam](api/beta.md)>

string encryptedContent

string title

"web\_search\_result" type

string url

?string pageAge

[BetaWebSearchToolRequestError](api/beta.md)

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

"web\_search\_tool\_result\_error" type

[BetaWebSearchToolResultError](api/beta.md)

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

"web\_search\_tool\_result\_error" type

[BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

#### BetaMessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

$client->beta->messages->batches->create(list<Request> requests, ?list<AnthropicBeta> betas): [MessageBatch](api/beta.md)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

$client->beta->messages->batches->retrieve(string messageBatchID, ?list<AnthropicBeta> betas): [MessageBatch](api/beta.md)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

$client->beta->messages->batches->list(?string afterID, ?string beforeID, ?int limit, ?list<AnthropicBeta> betas): Page<[MessageBatch](api/beta.md)>

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

$client->beta->messages->batches->cancel(string messageBatchID, ?list<AnthropicBeta> betas): [MessageBatch](api/beta.md)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

$client->beta->messages->batches->delete(string messageBatchID, ?list<AnthropicBeta> betas): [DeletedMessageBatch](api/beta.md)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

$client->beta->messages->batches->results(string messageBatchID, ?list<AnthropicBeta> betas): [MessageBatchIndividualResponse](api/beta.md)

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

[DeletedMessageBatch](api/beta.md)

string id

ID of the Message Batch.

"message\_batch\_deleted" type

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

[MessageBatch](api/beta.md)

string id

Unique object identifier.

The format and length of IDs may change over time.

?\Datetime archivedAt

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

?\Datetime cancelInitiatedAt

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

\Datetime createdAt

RFC 3339 datetime string representing the time at which the Message Batch was created.

?\Datetime endedAt

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

\Datetime expiresAt

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

ProcessingStatus processingStatus

Processing status of the Message Batch.

[MessageBatchRequestCounts](api/beta.md) requestCounts

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

?string resultsURL

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

"message\_batch" type

Object type.

For Message Batches, this is always `"message_batch"`.

[MessageBatchCanceledResult](api/beta.md)

"canceled" type

[MessageBatchErroredResult](api/beta.md)

[BetaErrorResponse](api/beta.md) error

"errored" type

[MessageBatchExpiredResult](api/beta.md)

"expired" type

[MessageBatchIndividualResponse](api/beta.md)

string customID

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

[MessageBatchResult](api/beta.md) result

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

[MessageBatchRequestCounts](api/beta.md)

int canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

int errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

int expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

int processing

Number of requests in the Message Batch that are processing.

int succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

[MessageBatchResult](api/beta.md)

One of the following:

[MessageBatchSucceededResult](api/beta.md)

[BetaMessage](api/beta.md) message

"succeeded" type

[MessageBatchErroredResult](api/beta.md)

[BetaErrorResponse](api/beta.md) error

"errored" type

[MessageBatchCanceledResult](api/beta.md)

"canceled" type

[MessageBatchExpiredResult](api/beta.md)

"expired" type

[MessageBatchSucceededResult](api/beta.md)

[BetaMessage](api/beta.md) message

"succeeded" type

#### BetaAgents

##### [Create Agent](api/beta/agents/create.md)

$client->beta->agents->create([Model](api/beta/agents/create.md) model, string name, ?string description, ?list<[BetaManagedAgentsURLMCPServerParams](api/beta.md)> mcpServers, ?array<string,string> metadata, ?[BetaManagedAgentsMultiagentParams](api/beta.md) multiagent, ?list<[BetaManagedAgentsSkillParams](api/beta.md)> skills, ?string system, ?list<Tool> tools, ?list<AnthropicBeta> betas): [BetaManagedAgentsAgent](api/beta.md)

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

$client->beta->agents->list(?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsAgent](api/beta.md)>

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

$client->beta->agents->retrieve(string agentID, ?int version, ?list<AnthropicBeta> betas): [BetaManagedAgentsAgent](api/beta.md)

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

$client->beta->agents->update(string agentID, int version, ?string description, ?list<[BetaManagedAgentsURLMCPServerParams](api/beta.md)> mcpServers, ?array<string,string> metadata, ?[Model](api/beta/agents/update.md) model, ?[BetaManagedAgentsMultiagentParams](api/beta.md) multiagent, ?string name, ?list<[BetaManagedAgentsSkillParams](api/beta.md)> skills, ?string system, ?list<Tool> tools, ?list<AnthropicBeta> betas): [BetaManagedAgentsAgent](api/beta.md)

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

$client->beta->agents->archive(string agentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsAgent](api/beta.md)

POST/v1/agents/{agent\_id}/archive

##### ModelsExpand Collapse

[BetaManagedAgentsAgent](api/beta.md)

string id

?\Datetime archivedAt

A timestamp in RFC 3339 format

\Datetime createdAt

A timestamp in RFC 3339 format

?string description

list<[BetaManagedAgentsMCPServerURLDefinition](api/beta.md)> mcpServers

array<string,string> metadata

[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.

?[BetaManagedAgentsMultiagent](api/beta.md) multiagent

Resolved coordinator topology with a concrete agent roster.

string name

list<Skill> skills

?string system

list<Tool> tools

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

int version

The agent's current version. Starts at 1 and increments when the agent is modified.

[BetaManagedAgentsAgentReference](api/beta.md)

string id

Type type

int version

[BetaManagedAgentsAgentToolConfig](api/beta.md)

bool enabled

Name name

Built-in agent tool identifier.

PermissionPolicy permissionPolicy

Permission policy for tool execution.

[BetaManagedAgentsAgentToolConfigParams](api/beta.md)

Name name

Built-in agent tool identifier.

?bool enabled

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

?PermissionPolicy permissionPolicy

Permission policy for tool execution.

[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md)

bool enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

[BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta.md)

?bool enabled

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

?PermissionPolicy permissionPolicy

Permission policy for tool execution.

[BetaManagedAgentsAgentToolset20260401](api/beta.md)

list<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

Type type

[BetaManagedAgentsAgentToolset20260401BashInput](api/beta.md)

?string command

Shell command to execute. Omit only when `restart` is true.

?bool restart

When true, restart the persistent bash session instead of
running a command. Subsequent calls without `restart` will
run against the fresh session.

?int timeoutMs

Per-call timeout in milliseconds. Defaults to the
runner-wide tool timeout when omitted or zero.

[BetaManagedAgentsAgentToolset20260401EditInput](api/beta.md)

string filePath

Path of the file to edit.

string newString

Replacement text.

string oldString

Substring to find and replace.

?bool replaceAll

When true, replace every occurrence of `old_string`
instead of requiring a unique match.

[BetaManagedAgentsAgentToolset20260401GlobInput](api/beta.md)

string pattern

Doublestar glob pattern (e.g. `**/*.go`). Absolute patterns
are only permitted when the runner is configured to allow
them.

?string path

Optional directory root to search under. Defaults to the
runner's working directory.

[BetaManagedAgentsAgentToolset20260401GrepInput](api/beta.md)

string pattern

Regular expression to search for.

?string path

Optional directory root to search under. Defaults to the
runner's working directory.

[BetaManagedAgentsAgentToolset20260401Params](api/beta.md)

Type type

?list<[BetaManagedAgentsAgentToolConfigParams](api/beta.md)> configs

Per-tool configuration overrides.

?[BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta.md) defaultConfig

Default configuration for all tools in a toolset.

[BetaManagedAgentsAgentToolset20260401ReadInput](api/beta.md)

string filePath

Path of the file to read.

?list<int> viewRange

Optional `[start_line, end_line]` 1-indexed inclusive
range. When omitted the entire file is returned.
`end_line` of 0 or negative means "to end of file".

[BetaManagedAgentsAgentToolset20260401WriteInput](api/beta.md)

string content

Full file contents to write.

string filePath

Path of the file to write.

[BetaManagedAgentsAlwaysAllowPolicy](api/beta.md)

Type type

[BetaManagedAgentsAlwaysAskPolicy](api/beta.md)

Type type

[BetaManagedAgentsAnthropicSkill](api/beta.md)

string skillID

Type type

string version

[BetaManagedAgentsAnthropicSkillParams](api/beta.md)

string skillID

Identifier of the Anthropic skill (e.g., "xlsx").

Type type

?string version

Version to pin. Defaults to latest if omitted.

[BetaManagedAgentsCustomSkill](api/beta.md)

string skillID

Type type

string version

[BetaManagedAgentsCustomSkillParams](api/beta.md)

string skillID

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

Type type

?string version

Version to pin. Defaults to latest if omitted.

[BetaManagedAgentsCustomTool](api/beta.md)

string description

[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

string name

Type type

[BetaManagedAgentsCustomToolInputSchema](api/beta.md)

"object" type

?array<string,mixed> properties

?list<string> required

[BetaManagedAgentsCustomToolParams](api/beta.md)

string description

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

string name

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

Type type

[BetaManagedAgentsMCPServerURLDefinition](api/beta.md)

string name

Type type

string url

[BetaManagedAgentsMCPToolConfig](api/beta.md)

bool enabled

string name

PermissionPolicy permissionPolicy

Permission policy for tool execution.

[BetaManagedAgentsMCPToolConfigParams](api/beta.md)

string name

Name of the MCP tool to configure. 1-128 characters.

?bool enabled

Whether this tool is enabled. Overrides the `default_config` setting.

?PermissionPolicy permissionPolicy

Permission policy for tool execution.

[BetaManagedAgentsMCPToolset](api/beta.md)

list<[BetaManagedAgentsMCPToolConfig](api/beta.md)> configs

[BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

string mcpServerName

Type type

[BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md)

bool enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

[BetaManagedAgentsMCPToolsetDefaultConfigParams](api/beta.md)

?bool enabled

Whether tools are enabled by default. Defaults to true if not specified.

?PermissionPolicy permissionPolicy

Permission policy for tool execution.

[BetaManagedAgentsMCPToolsetParams](api/beta.md)

string mcpServerName

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

Type type

?list<[BetaManagedAgentsMCPToolConfigParams](api/beta.md)> configs

Per-tool configuration overrides.

?[BetaManagedAgentsMCPToolsetDefaultConfigParams](api/beta.md) defaultConfig

Default configuration for all tools from an MCP server.

BetaManagedAgentsModel

One of the following:

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

[BetaManagedAgentsModelConfig](api/beta.md)

BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

?Speed speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

[BetaManagedAgentsModelConfigParams](api/beta.md)

BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

?Speed speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

[BetaManagedAgentsMultiagentCoordinator](api/beta.md)

list<[BetaManagedAgentsAgentReference](api/beta.md)> agents

Agents the coordinator may spawn as session threads, each resolved to a specific version.

Type type

[BetaManagedAgentsMultiagentCoordinatorParams](api/beta.md)

list<[BetaManagedAgentsMultiagentRosterEntryParams](api/beta.md)> agents

Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

Type type

[BetaManagedAgentsMultiagentSelfParams](api/beta.md)

Type type

[BetaManagedAgentsSessionThreadAgent](api/beta.md)

string id

?string description

list<[BetaManagedAgentsMCPServerURLDefinition](api/beta.md)> mcpServers

[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.

string name

list<Skill> skills

?string system

list<Tool> tools

Type type

int version

[BetaManagedAgentsSkillParams](api/beta.md)

One of the following:

[BetaManagedAgentsAnthropicSkillParams](api/beta.md)

string skillID

Identifier of the Anthropic skill (e.g., "xlsx").

Type type

?string version

Version to pin. Defaults to latest if omitted.

[BetaManagedAgentsCustomSkillParams](api/beta.md)

string skillID

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

Type type

?string version

Version to pin. Defaults to latest if omitted.

[BetaManagedAgentsURLMCPServerParams](api/beta.md)

string name

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

Type type

string url

Endpoint URL for the MCP server.

#### BetaAgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

$client->beta->agents->versions->list(string agentID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsAgent](api/beta.md)>

GET/v1/agents/{agent\_id}/versions

#### BetaEnvironments

##### [Create Environment](api/beta/environments/create.md)

$client->beta->environments->create(string name, ?[Config](api/beta/environments/create.md) config, ?string description, ?array<string,string> metadata, ?[Scope](api/beta/environments/create.md) scope, ?list<AnthropicBeta> betas): [BetaEnvironment](api/beta.md)

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

$client->beta->environments->list(?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaEnvironment](api/beta.md)>

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

$client->beta->environments->retrieve(string environmentID, ?list<AnthropicBeta> betas): [BetaEnvironment](api/beta.md)

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

$client->beta->environments->update(string environmentID, ?[Config](api/beta/environments/update.md) config, ?string description, ?array<string,string> metadata, ?string name, ?[Scope](api/beta/environments/update.md) scope, ?list<AnthropicBeta> betas): [BetaEnvironment](api/beta.md)

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

$client->beta->environments->delete(string environmentID, ?list<AnthropicBeta> betas): [BetaEnvironmentDeleteResponse](api/beta.md)

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

$client->beta->environments->archive(string environmentID, ?list<AnthropicBeta> betas): [BetaEnvironment](api/beta.md)

POST/v1/environments/{environment\_id}/archive

##### ModelsExpand Collapse

[BetaCloudConfig](api/beta.md)

Networking networking

Network configuration policy.

[BetaPackages](api/beta.md) packages

Package manager configuration.

"cloud" type

Environment type

[BetaCloudConfigParams](api/beta.md)

"cloud" type

Environment type

?Networking networking

Network configuration policy. Omit on update to preserve the existing value.

?[BetaPackagesParams](api/beta.md) packages

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

[BetaEnvironment](api/beta.md)

string id

Environment identifier (e.g., 'env\_...')

?string archivedAt

RFC 3339 timestamp when environment was archived, or null if not archived

Config config

Environment configuration (either Anthropic Cloud or self-hosted)

string createdAt

RFC 3339 timestamp when environment was created

string description

User-provided description for the environment

array<string,string> metadata

User-provided metadata key-value pairs

string name

Human-readable name for the environment

"environment" type

The type of object (always 'environment')

string updatedAt

RFC 3339 timestamp when environment was last updated

?Scope scope

The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

[BetaEnvironmentDeleteResponse](api/beta.md)

string id

Environment identifier

"environment\_deleted" type

The type of response

[BetaLimitedNetwork](api/beta.md)

bool allowMCPServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

bool allowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

list<string> allowedHosts

Specifies domains the container can reach.

"limited" type

Network policy type

[BetaLimitedNetworkParams](api/beta.md)

"limited" type

Network policy type

?bool allowMCPServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

?bool allowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

?list<string> allowedHosts

Specifies domains the container can reach.

[BetaPackages](api/beta.md)

list<string> apt

Ubuntu/Debian packages to install

list<string> cargo

Rust packages to install

list<string> gem

Ruby packages to install

list<string> go

Go packages to install

list<string> npm

Node.js packages to install

list<string> pip

Python packages to install

?Type type

Package configuration type

[BetaPackagesParams](api/beta.md)

?list<string> apt

Ubuntu/Debian packages to install

?list<string> cargo

Rust packages to install

?list<string> gem

Ruby packages to install

?list<string> go

Go packages to install

?list<string> npm

Node.js packages to install

?list<string> pip

Python packages to install

?Type type

Package configuration type

[BetaSelfHostedConfig](api/beta.md)

"self\_hosted" type

Environment type

[BetaSelfHostedConfigParams](api/beta.md)

"self\_hosted" type

Environment type

[BetaUnrestrictedNetwork](api/beta.md)

"unrestricted" type

Network policy type

#### BetaEnvironmentsWork

##### [Get Work Item](api/beta/environments/work/retrieve.md)

$client->beta->environments->work->retrieve(string workID, string environmentID, ?list<AnthropicBeta> betas): [SelfHostedWork](api/beta.md)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

$client->beta->environments->work->poll(string environmentID, ?int blockMs, ?int reclaimOlderThanMs, ?list<AnthropicBeta> betas, ?string anthropicWorkerID): [SelfHostedWork](api/beta.md)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

$client->beta->environments->work->ack(string workID, string environmentID, ?list<AnthropicBeta> betas): [SelfHostedWork](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

$client->beta->environments->work->heartbeat(string workID, string environmentID, ?int desiredTTLSeconds, ?string expectedLastHeartbeat, ?list<AnthropicBeta> betas): [SelfHostedWorkHeartbeatResponse](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

$client->beta->environments->work->stop(string workID, string environmentID, ?bool force, ?list<AnthropicBeta> betas): [SelfHostedWork](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

$client->beta->environments->work->list(string environmentID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[SelfHostedWork](api/beta.md)>

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

$client->beta->environments->work->update(string workID, string environmentID, array<string,string> metadata, ?list<AnthropicBeta> betas): [SelfHostedWork](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

$client->beta->environments->work->stats(string environmentID, ?list<AnthropicBeta> betas): [SelfHostedWorkQueueStats](api/beta.md)

GET/v1/environments/{environment\_id}/work/stats

##### ModelsExpand Collapse

[SelfHostedWork](api/beta.md)

string id

Work identifier (e.g., 'work\_...')

?string acknowledgedAt

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

string createdAt

RFC 3339 timestamp when work was created

[SessionWorkData](api/beta.md) data

The actual work to be performed

string environmentID

Environment identifier this work belongs to (e.g., `env_...`)

?string latestHeartbeatAt

RFC 3339 timestamp of the most recent heartbeat

array<string,string> metadata

User-provided metadata key-value pairs associated with this work item

?string startedAt

RFC 3339 timestamp when work execution started

State state

Current state of the work item

?string stopRequestedAt

RFC 3339 timestamp when stop was requested

?string stoppedAt

RFC 3339 timestamp when work execution stopped

"work" type

The type of object (always 'work')

[SelfHostedWorkHeartbeatResponse](api/beta.md)

string lastHeartbeat

RFC 3339 timestamp of the actual heartbeat from DB

bool leaseExtended

Whether the heartbeat succeeded in extending the lease

State state

Current state of the work item (active/stopping/stopped)

int ttlSeconds

Effective TTL applied to the lease

"work\_heartbeat" type

The type of response

[SelfHostedWorkListResponse](api/beta.md)

list<[SelfHostedWork](api/beta.md)> data

List of work items

?string nextPage

Opaque cursor for fetching the next page of results

[SelfHostedWorkQueueStats](api/beta.md)

int depth

Number of work items waiting to be picked up (lag from consumer group)

?string oldestQueuedAt

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

int pending

Number of work items being processed (polled but not acknowledged)

"work\_queue\_stats" type

The type of object

?int workersPolling

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.

[SelfHostedWorkStopRequest](api/beta.md)

?bool force

If true, immediately stop work without graceful shutdown

[SelfHostedWorkUpdateRequest](api/beta.md)

array<string,string> metadata

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

[SessionWorkData](api/beta.md)

string id

Session identifier (e.g., 'session\_...')

"session" type

Type of work data

#### BetaSessions

##### [Create Session](api/beta/sessions/create.md)

$client->beta->sessions->create([Agent](api/beta/sessions/create.md) agent, string environmentID, ?array<string,string> metadata, ?list<Resource> resources, ?string title, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): [BetaManagedAgentsSession](api/beta.md)

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

$client->beta->sessions->list(?string agentID, ?int agentVersion, ?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?string deploymentID, ?bool includeArchived, ?int limit, ?string memoryStoreID, ?[Order](api/beta/sessions/list.md) order, ?string page, ?list<Status> statuses, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsSession](api/beta.md)>

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

$client->beta->sessions->retrieve(string sessionID, ?list<AnthropicBeta> betas): [BetaManagedAgentsSession](api/beta.md)

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

$client->beta->sessions->update(string sessionID, ?[BetaManagedAgentsSessionAgentUpdate](api/beta.md) agent, ?array<string,string> metadata, ?string title, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): [BetaManagedAgentsSession](api/beta.md)

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

$client->beta->sessions->delete(string sessionID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeletedSession](api/beta.md)

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

$client->beta->sessions->archive(string sessionID, ?list<AnthropicBeta> betas): [BetaManagedAgentsSession](api/beta.md)

POST/v1/sessions/{session\_id}/archive

##### ModelsExpand Collapse

[BetaManagedAgentsAgentParams](api/beta.md)

string id

The `agent` ID.

Type type

?int version

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

[BetaManagedAgentsBranchCheckout](api/beta.md)

string name

Branch name to check out.

Type type

[BetaManagedAgentsCacheCreationUsage](api/beta.md)

?int ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

?int ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

[BetaManagedAgentsCommitCheckout](api/beta.md)

string sha

Full commit SHA to check out.

Type type

[BetaManagedAgentsDeletedSession](api/beta.md)

string id

Type type

[BetaManagedAgentsFileResourceParams](api/beta.md)

string fileID

ID of a previously uploaded file.

Type type

?string mountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

[BetaManagedAgentsGitHubRepositoryResourceParams](api/beta.md)

string authorizationToken

GitHub authorization token used to clone the repository.

Type type

string url

Github URL of the repository

?Checkout checkout

Branch or commit to check out. Defaults to the repository's default branch.

?string mountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.

[BetaManagedAgentsMemoryStoreResourceParam](api/beta.md)

string memoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type

?Access access

Access mode for an attached memory store.

?string instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

[BetaManagedAgentsMultiagent](api/beta.md)

list<[BetaManagedAgentsAgentReference](api/beta.md)> agents

Agents the coordinator may spawn as session threads, each resolved to a specific version.

Type type

[BetaManagedAgentsMultiagentParams](api/beta.md)

list<[BetaManagedAgentsMultiagentRosterEntryParams](api/beta.md)> agents

Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

Type type

[BetaManagedAgentsMultiagentRosterEntryParams](api/beta.md)

One of the following:

string

[BetaManagedAgentsAgentParams](api/beta.md)

string id

The `agent` ID.

Type type

?int version

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

[BetaManagedAgentsMultiagentSelfParams](api/beta.md)

Type type

[BetaManagedAgentsOutcomeEvaluationResource](api/beta.md)

?\Datetime completedAt

A timestamp in RFC 3339 format

string description

What the agent should produce.

?string explanation

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

int iteration

0-indexed revision cycle the outcome is currently on.

string outcomeID

Server-generated outc\_ ID for this outcome.

string result

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

Type type

[BetaManagedAgentsSession](api/beta.md)

string id

[BetaManagedAgentsSessionAgent](api/beta.md) agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

?\Datetime archivedAt

A timestamp in RFC 3339 format

\Datetime createdAt

A timestamp in RFC 3339 format

string environmentID

array<string,string> metadata

list<[BetaManagedAgentsOutcomeEvaluationResource](api/beta.md)> outcomeEvaluations

Per-outcome evaluation state. One entry per define\_outcome event sent to the session.

list<[ManagedAgentsSessionResource](api/beta.md)> resources

[BetaManagedAgentsSessionStats](api/beta.md) stats

Timing statistics for a session.

Status status

SessionStatus enum

?string title

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

[BetaManagedAgentsSessionUsage](api/beta.md) usage

Cumulative token usage for a session across all turns.

list<string> vaultIDs

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

?string deploymentID

Deployment ID when the session was created from a deployment reference. Null otherwise.

[BetaManagedAgentsSessionAgent](api/beta.md)

string id

?string description

list<[BetaManagedAgentsMCPServerURLDefinition](api/beta.md)> mcpServers

[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.

?[BetaManagedAgentsSessionMultiagentCoordinator](api/beta.md) multiagent

Resolved coordinator topology with full agent definitions for each roster member.

string name

list<Skill> skills

?string system

list<Tool> tools

Type type

int version

[BetaManagedAgentsSessionAgentUpdate](api/beta.md)

?list<[BetaManagedAgentsURLMCPServerParams](api/beta.md)> mcpServers

Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

?list<Tool> tools

Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

[BetaManagedAgentsSessionMultiagentCoordinator](api/beta.md)

list<[BetaManagedAgentsSessionThreadAgent](api/beta.md)> agents

Full `agent` definitions the coordinator may spawn as session threads.

Type type

[BetaManagedAgentsSessionStats](api/beta.md)

?float activeSeconds

Cumulative time in seconds the session spent in running status. Excludes idle time.

?float durationSeconds

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

[BetaManagedAgentsSessionUpdatedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?[BetaManagedAgentsSessionAgent](api/beta.md) agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

?array<string,string> metadata

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

?string title

The session's new title. Present only when the update changed it.

[BetaManagedAgentsSessionUsage](api/beta.md)

?[BetaManagedAgentsCacheCreationUsage](api/beta.md) cacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

?int cacheReadInputTokens

Total tokens read from prompt cache.

?int inputTokens

Total input tokens consumed across all turns.

?int outputTokens

Total output tokens generated across all turns.

[BetaManagedAgentsSystemContentBlock](api/beta.md)

string text

The text content.

Type type

[BetaManagedAgentsSystemMessageEvent](api/beta.md)

string id

Unique identifier for this event.

list<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks. Text-only.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

[BetaManagedAgentsUserToolResultEvent](api/beta.md)

string id

Unique identifier for this event.

string toolUseID

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

#### BetaSessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

$client->beta->sessions->events->list(string sessionID, ?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?int limit, ?[Order](api/beta/sessions/events/list.md) order, ?string page, ?list<string> types, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionEvent](api/beta.md)>

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

$client->beta->sessions->events->send(string sessionID, list<[ManagedAgentsEventParams](api/beta.md)> events, ?list<AnthropicBeta> betas): [ManagedAgentsSendSessionEvents](api/beta.md)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

$client->beta->sessions->events->stream(string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsStreamSessionEvents](api/beta.md)

GET/v1/sessions/{session\_id}/events/stream

##### ModelsExpand Collapse

[ManagedAgentsAgentCustomToolUseEvent](api/beta.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string name

Name of the custom tool being called.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

[ManagedAgentsAgentMCPToolResultEvent](api/beta.md)

string id

Unique identifier for this event.

string mcpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

[ManagedAgentsAgentMCPToolUseEvent](api/beta.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string mcpServerName

Name of the MCP server providing the tool.

string name

Name of the MCP tool being used.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?EvaluatedPermission evaluatedPermission

AgentEvaluatedPermission enum

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

[ManagedAgentsAgentMessageEvent](api/beta.md)

string id

Unique identifier for this event.

list<[ManagedAgentsTextBlock](api/beta.md)> content

Array of text blocks comprising the agent response.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsAgentThinkingEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsAgentThreadContextCompactedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsAgentThreadMessageReceivedEvent](api/beta.md)

string id

Unique identifier for this event.

list<Content> content

Message content blocks.

string fromSessionThreadID

Public `sthr_` ID of the thread that sent the message.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?string fromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.

[ManagedAgentsAgentThreadMessageSentEvent](api/beta.md)

string id

Unique identifier for this event.

list<Content> content

Message content blocks.

\Datetime processedAt

A timestamp in RFC 3339 format

string toSessionThreadID

Public `sthr_` ID of the thread the message was sent to.

Type type

?string toAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

[ManagedAgentsAgentToolResultEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

string toolUseID

The id of the `agent.tool_use` event this result corresponds to.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

[ManagedAgentsAgentToolUseEvent](api/beta.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string name

Name of the agent tool being used.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?EvaluatedPermission evaluatedPermission

AgentEvaluatedPermission enum

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

[ManagedAgentsBase64DocumentSource](api/beta.md)

string data

Base64-encoded document data.

string mediaType

MIME type of the document (e.g., "application/pdf").

Type type

[ManagedAgentsBase64ImageSource](api/beta.md)

string data

Base64-encoded image data.

string mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

[ManagedAgentsBillingError](api/beta.md)

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type

[ManagedAgentsCredentialHostUnreachableError](api/beta.md)

string credentialID

ID of the affected credential.

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type

string vaultID

ID of the vault containing the affected credential.

[ManagedAgentsDocumentBlock](api/beta.md)

Source source

Union type for document source variants.

Type type

?string context

Additional context about the document for the model.

?string title

The title of the document.

[ManagedAgentsEventParams](api/beta.md)

One of the following:

[ManagedAgentsUserMessageEventParams](api/beta.md)

list<Content> content

Array of content blocks for the user message.

Type type

[ManagedAgentsUserInterruptEventParams](api/beta.md)

Type type

?string sessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

[ManagedAgentsUserToolConfirmationEventParams](api/beta.md)

Result result

UserToolConfirmationResult enum

string toolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?string denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

[ManagedAgentsUserCustomToolResultEventParams](api/beta.md)

string customToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

[ManagedAgentsUserDefineOutcomeEventParams](api/beta.md)

string description

What the agent should produce. This is the task specification.

Rubric rubric

Rubric for grading the quality of an outcome.

Type type

?int maxIterations

Eval→revision cycles before giving up. Default 3, max 20.

[ManagedAgentsUserToolResultEventParams](api/beta.md)

string toolUseID

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

[ManagedAgentsSystemMessageEventParams](api/beta.md)

list<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks to append. Text-only.

Type type

[ManagedAgentsFileDocumentSource](api/beta.md)

string fileID

ID of a previously uploaded file.

Type type

[ManagedAgentsFileImageSource](api/beta.md)

string fileID

ID of a previously uploaded file.

Type type

[ManagedAgentsFileRubric](api/beta.md)

string fileID

ID of the rubric file.

Type type

[ManagedAgentsFileRubricParams](api/beta.md)

string fileID

ID of the rubric file.

Type type

[ManagedAgentsImageBlock](api/beta.md)

Source source

Union type for image source variants.

Type type

[ManagedAgentsMCPAuthenticationFailedError](api/beta.md)

string mcpServerName

Name of the MCP server that failed authentication.

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type

[ManagedAgentsMCPConnectionFailedError](api/beta.md)

string mcpServerName

Name of the MCP server that failed to connect.

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type

[ManagedAgentsModelOverloadedError](api/beta.md)

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type

[ManagedAgentsModelRateLimitedError](api/beta.md)

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type

[ManagedAgentsModelRequestFailedError](api/beta.md)

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type

[ManagedAgentsPlainTextDocumentSource](api/beta.md)

string data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

[ManagedAgentsRetryStatusExhausted](api/beta.md)

Type type

[ManagedAgentsRetryStatusRetrying](api/beta.md)

Type type

[ManagedAgentsRetryStatusTerminal](api/beta.md)

Type type

[ManagedAgentsSearchResultBlock](api/beta.md)

[ManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

list<[ManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

string source

The URL source of the search result.

string title

The title of the search result.

Type type

[ManagedAgentsSearchResultCitations](api/beta.md)

bool enabled

Whether citations are enabled for this search result.

[ManagedAgentsSearchResultContent](api/beta.md)

string text

The text content.

Type type

[ManagedAgentsSendSessionEvents](api/beta.md)

?list<Data> data

Sent events

[ManagedAgentsSessionDeletedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionEndTurn](api/beta.md)

Type type

[ManagedAgentsSessionErrorEvent](api/beta.md)

string id

Unique identifier for this event.

Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionEvent](api/beta.md)

One of the following:

[ManagedAgentsUserMessageEvent](api/beta.md)

string id

Unique identifier for this event.

list<Content> content

Array of content blocks comprising the user message.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

[ManagedAgentsUserInterruptEvent](api/beta.md)

string id

Unique identifier for this event.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

[ManagedAgentsUserToolConfirmationEvent](api/beta.md)

string id

Unique identifier for this event.

Result result

UserToolConfirmationResult enum

string toolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?string denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

[ManagedAgentsUserCustomToolResultEvent](api/beta.md)

string id

Unique identifier for this event.

string customToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

[ManagedAgentsAgentCustomToolUseEvent](api/beta.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string name

Name of the custom tool being called.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

[ManagedAgentsAgentMessageEvent](api/beta.md)

string id

Unique identifier for this event.

list<[ManagedAgentsTextBlock](api/beta.md)> content

Array of text blocks comprising the agent response.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsAgentThinkingEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsAgentMCPToolUseEvent](api/beta.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string mcpServerName

Name of the MCP server providing the tool.

string name

Name of the MCP tool being used.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?EvaluatedPermission evaluatedPermission

AgentEvaluatedPermission enum

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

[ManagedAgentsAgentMCPToolResultEvent](api/beta.md)

string id

Unique identifier for this event.

string mcpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

[ManagedAgentsAgentToolUseEvent](api/beta.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string name

Name of the agent tool being used.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?EvaluatedPermission evaluatedPermission

AgentEvaluatedPermission enum

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

[ManagedAgentsAgentToolResultEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

string toolUseID

The id of the `agent.tool_use` event this result corresponds to.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

[ManagedAgentsAgentThreadMessageReceivedEvent](api/beta.md)

string id

Unique identifier for this event.

list<Content> content

Message content blocks.

string fromSessionThreadID

Public `sthr_` ID of the thread that sent the message.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?string fromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.

[ManagedAgentsAgentThreadMessageSentEvent](api/beta.md)

string id

Unique identifier for this event.

list<Content> content

Message content blocks.

\Datetime processedAt

A timestamp in RFC 3339 format

string toSessionThreadID

Public `sthr_` ID of the thread the message was sent to.

Type type

?string toAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

[ManagedAgentsAgentThreadContextCompactedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionErrorEvent](api/beta.md)

string id

Unique identifier for this event.

Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionStatusRescheduledEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionStatusRunningEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionStatusIdleEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Type type

[ManagedAgentsSessionStatusTerminatedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionThreadCreatedEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the callable agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public `sthr_` ID of the newly created thread.

Type type

[ManagedAgentsSpanOutcomeEvaluationStartEvent](api/beta.md)

string id

Unique identifier for this event.

int iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSpanOutcomeEvaluationEndEvent](api/beta.md)

string id

Unique identifier for this event.

string explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

int iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

string outcomeEvaluationStartID

The id of the corresponding `span.outcome_evaluation_start` event.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

string result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

Type type

[ManagedAgentsSpanModelUsage](api/beta.md) usage

Token usage for a single model request.

[ManagedAgentsSpanModelRequestStartEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSpanModelRequestEndEvent](api/beta.md)

string id

Unique identifier for this event.

?bool isError

Whether the model request resulted in an error.

string modelRequestStartID

The id of the corresponding `span.model_request_start` event.

[ManagedAgentsSpanModelUsage](api/beta.md) modelUsage

Token usage for a single model request.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSpanOutcomeEvaluationOngoingEvent](api/beta.md)

string id

Unique identifier for this event.

int iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsUserDefineOutcomeEvent](api/beta.md)

string id

Unique identifier for this event.

string description

What the agent should produce. Copied from the input event.

?int maxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

string outcomeID

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

\Datetime processedAt

A timestamp in RFC 3339 format

Rubric rubric

Rubric for grading the quality of an outcome.

Type type

[ManagedAgentsSessionDeletedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionThreadStatusRunningEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that started running.

Type type

[ManagedAgentsSessionThreadStatusIdleEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that went idle.

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Type type

[ManagedAgentsSessionThreadStatusTerminatedEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that terminated.

Type type

[BetaManagedAgentsUserToolResultEvent](api/beta.md)

string id

Unique identifier for this event.

string toolUseID

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

[ManagedAgentsSessionThreadStatusRescheduledEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that is retrying.

Type type

[BetaManagedAgentsSessionUpdatedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?[BetaManagedAgentsSessionAgent](api/beta.md) agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

?array<string,string> metadata

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

?string title

The session's new title. Present only when the update changed it.

[BetaManagedAgentsSystemMessageEvent](api/beta.md)

string id

Unique identifier for this event.

list<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks. Text-only.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

[ManagedAgentsSessionRequiresAction](api/beta.md)

list<string> eventIDs

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type

[ManagedAgentsSessionRetriesExhausted](api/beta.md)

Type type

[ManagedAgentsSessionStatusIdleEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Type type

[ManagedAgentsSessionStatusRescheduledEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionStatusRunningEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionStatusTerminatedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionThreadCreatedEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the callable agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public `sthr_` ID of the newly created thread.

Type type

[ManagedAgentsSessionThreadStatusIdleEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that went idle.

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Type type

[ManagedAgentsSessionThreadStatusRescheduledEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that is retrying.

Type type

[ManagedAgentsSessionThreadStatusRunningEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that started running.

Type type

[ManagedAgentsSessionThreadStatusTerminatedEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that terminated.

Type type

[ManagedAgentsSpanModelRequestEndEvent](api/beta.md)

string id

Unique identifier for this event.

?bool isError

Whether the model request resulted in an error.

string modelRequestStartID

The id of the corresponding `span.model_request_start` event.

[ManagedAgentsSpanModelUsage](api/beta.md) modelUsage

Token usage for a single model request.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSpanModelRequestStartEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSpanModelUsage](api/beta.md)

int cacheCreationInputTokens

Tokens used to create prompt cache in this request.

int cacheReadInputTokens

Tokens read from prompt cache in this request.

int inputTokens

Input tokens consumed by this request.

int outputTokens

Output tokens generated by this request.

?Speed speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

[ManagedAgentsSpanOutcomeEvaluationEndEvent](api/beta.md)

string id

Unique identifier for this event.

string explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

int iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

string outcomeEvaluationStartID

The id of the corresponding `span.outcome_evaluation_start` event.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

string result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

Type type

[ManagedAgentsSpanModelUsage](api/beta.md) usage

Token usage for a single model request.

[ManagedAgentsSpanOutcomeEvaluationOngoingEvent](api/beta.md)

string id

Unique identifier for this event.

int iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSpanOutcomeEvaluationStartEvent](api/beta.md)

string id

Unique identifier for this event.

int iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsStreamSessionEvents](api/beta.md)

One of the following:

[ManagedAgentsUserMessageEvent](api/beta.md)

string id

Unique identifier for this event.

list<Content> content

Array of content blocks comprising the user message.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

[ManagedAgentsUserInterruptEvent](api/beta.md)

string id

Unique identifier for this event.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

[ManagedAgentsUserToolConfirmationEvent](api/beta.md)

string id

Unique identifier for this event.

Result result

UserToolConfirmationResult enum

string toolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?string denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

[ManagedAgentsUserCustomToolResultEvent](api/beta.md)

string id

Unique identifier for this event.

string customToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

[ManagedAgentsAgentCustomToolUseEvent](api/beta.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string name

Name of the custom tool being called.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

[ManagedAgentsAgentMessageEvent](api/beta.md)

string id

Unique identifier for this event.

list<[ManagedAgentsTextBlock](api/beta.md)> content

Array of text blocks comprising the agent response.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsAgentThinkingEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsAgentMCPToolUseEvent](api/beta.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string mcpServerName

Name of the MCP server providing the tool.

string name

Name of the MCP tool being used.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?EvaluatedPermission evaluatedPermission

AgentEvaluatedPermission enum

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

[ManagedAgentsAgentMCPToolResultEvent](api/beta.md)

string id

Unique identifier for this event.

string mcpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

[ManagedAgentsAgentToolUseEvent](api/beta.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string name

Name of the agent tool being used.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?EvaluatedPermission evaluatedPermission

AgentEvaluatedPermission enum

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

[ManagedAgentsAgentToolResultEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

string toolUseID

The id of the `agent.tool_use` event this result corresponds to.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

[ManagedAgentsAgentThreadMessageReceivedEvent](api/beta.md)

string id

Unique identifier for this event.

list<Content> content

Message content blocks.

string fromSessionThreadID

Public `sthr_` ID of the thread that sent the message.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?string fromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.

[ManagedAgentsAgentThreadMessageSentEvent](api/beta.md)

string id

Unique identifier for this event.

list<Content> content

Message content blocks.

\Datetime processedAt

A timestamp in RFC 3339 format

string toSessionThreadID

Public `sthr_` ID of the thread the message was sent to.

Type type

?string toAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

[ManagedAgentsAgentThreadContextCompactedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionErrorEvent](api/beta.md)

string id

Unique identifier for this event.

Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionStatusRescheduledEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionStatusRunningEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionStatusIdleEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Type type

[ManagedAgentsSessionStatusTerminatedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionThreadCreatedEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the callable agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public `sthr_` ID of the newly created thread.

Type type

[ManagedAgentsSpanOutcomeEvaluationStartEvent](api/beta.md)

string id

Unique identifier for this event.

int iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSpanOutcomeEvaluationEndEvent](api/beta.md)

string id

Unique identifier for this event.

string explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

int iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

string outcomeEvaluationStartID

The id of the corresponding `span.outcome_evaluation_start` event.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

string result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

Type type

[ManagedAgentsSpanModelUsage](api/beta.md) usage

Token usage for a single model request.

[ManagedAgentsSpanModelRequestStartEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSpanModelRequestEndEvent](api/beta.md)

string id

Unique identifier for this event.

?bool isError

Whether the model request resulted in an error.

string modelRequestStartID

The id of the corresponding `span.model_request_start` event.

[ManagedAgentsSpanModelUsage](api/beta.md) modelUsage

Token usage for a single model request.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSpanOutcomeEvaluationOngoingEvent](api/beta.md)

string id

Unique identifier for this event.

int iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsUserDefineOutcomeEvent](api/beta.md)

string id

Unique identifier for this event.

string description

What the agent should produce. Copied from the input event.

?int maxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

string outcomeID

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

\Datetime processedAt

A timestamp in RFC 3339 format

Rubric rubric

Rubric for grading the quality of an outcome.

Type type

[ManagedAgentsSessionDeletedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionThreadStatusRunningEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that started running.

Type type

[ManagedAgentsSessionThreadStatusIdleEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that went idle.

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Type type

[ManagedAgentsSessionThreadStatusTerminatedEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that terminated.

Type type

[BetaManagedAgentsUserToolResultEvent](api/beta.md)

string id

Unique identifier for this event.

string toolUseID

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

[ManagedAgentsSessionThreadStatusRescheduledEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that is retrying.

Type type

[BetaManagedAgentsSessionUpdatedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?[BetaManagedAgentsSessionAgent](api/beta.md) agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

?array<string,string> metadata

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

?string title

The session's new title. Present only when the update changed it.

[BetaManagedAgentsSystemMessageEvent](api/beta.md)

string id

Unique identifier for this event.

list<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks. Text-only.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

[ManagedAgentsSystemMessageEventParams](api/beta.md)

list<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks to append. Text-only.

Type type

[ManagedAgentsTextBlock](api/beta.md)

string text

The text content.

Type type

[ManagedAgentsTextRubric](api/beta.md)

string content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type type

[ManagedAgentsTextRubricParams](api/beta.md)

string content

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

Type type

[ManagedAgentsUnknownError](api/beta.md)

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type

[ManagedAgentsURLDocumentSource](api/beta.md)

Type type

string url

URL of the document to fetch.

[ManagedAgentsURLImageSource](api/beta.md)

Type type

string url

URL of the image to fetch.

[ManagedAgentsUserCustomToolResultEvent](api/beta.md)

string id

Unique identifier for this event.

string customToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

[ManagedAgentsUserCustomToolResultEventParams](api/beta.md)

string customToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

[ManagedAgentsUserDefineOutcomeEvent](api/beta.md)

string id

Unique identifier for this event.

string description

What the agent should produce. Copied from the input event.

?int maxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

string outcomeID

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

\Datetime processedAt

A timestamp in RFC 3339 format

Rubric rubric

Rubric for grading the quality of an outcome.

Type type

[ManagedAgentsUserDefineOutcomeEventParams](api/beta.md)

string description

What the agent should produce. This is the task specification.

Rubric rubric

Rubric for grading the quality of an outcome.

Type type

?int maxIterations

Eval→revision cycles before giving up. Default 3, max 20.

[ManagedAgentsUserInterruptEvent](api/beta.md)

string id

Unique identifier for this event.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

[ManagedAgentsUserInterruptEventParams](api/beta.md)

Type type

?string sessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

[ManagedAgentsUserMessageEvent](api/beta.md)

string id

Unique identifier for this event.

list<Content> content

Array of content blocks comprising the user message.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

[ManagedAgentsUserMessageEventParams](api/beta.md)

list<Content> content

Array of content blocks for the user message.

Type type

[ManagedAgentsUserToolConfirmationEvent](api/beta.md)

string id

Unique identifier for this event.

Result result

UserToolConfirmationResult enum

string toolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?string denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

[ManagedAgentsUserToolConfirmationEventParams](api/beta.md)

Result result

UserToolConfirmationResult enum

string toolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?string denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

[ManagedAgentsUserToolResultEventParams](api/beta.md)

string toolUseID

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

#### BetaSessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

$client->beta->sessions->resources->add(string sessionID, string fileID, [Type](api/beta/sessions/resources/add.md) type, ?string mountPath, ?list<AnthropicBeta> betas): [ManagedAgentsFileResource](api/beta.md)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

$client->beta->sessions->resources->list(string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionResource](api/beta.md)>

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

$client->beta->sessions->resources->retrieve(string resourceID, string sessionID, ?list<AnthropicBeta> betas): [ResourceGetResponse](api/beta.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

$client->beta->sessions->resources->update(string resourceID, string sessionID, string authorizationToken, ?list<AnthropicBeta> betas): [ResourceUpdateResponse](api/beta.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

$client->beta->sessions->resources->delete(string resourceID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsDeleteSessionResource](api/beta.md)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse

[ManagedAgentsDeleteSessionResource](api/beta.md)

string id

Type type

[ManagedAgentsFileResource](api/beta.md)

string id

\Datetime createdAt

A timestamp in RFC 3339 format

string fileID

string mountPath

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

[ManagedAgentsGitHubRepositoryResource](api/beta.md)

string id

\Datetime createdAt

A timestamp in RFC 3339 format

string mountPath

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

string url

?Checkout checkout

[ManagedAgentsMemoryStoreResource](api/beta.md)

string memoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type

?Access access

Access mode for an attached memory store.

?string description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

?string instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

?string mountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

?string name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

[ManagedAgentsSessionResource](api/beta.md)

One of the following:

[ManagedAgentsGitHubRepositoryResource](api/beta.md)

string id

\Datetime createdAt

A timestamp in RFC 3339 format

string mountPath

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

string url

?Checkout checkout

[ManagedAgentsFileResource](api/beta.md)

string id

\Datetime createdAt

A timestamp in RFC 3339 format

string fileID

string mountPath

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

[ManagedAgentsMemoryStoreResource](api/beta.md)

string memoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type

?Access access

Access mode for an attached memory store.

?string description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

?string instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

?string mountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

?string name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### BetaSessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

$client->beta->sessions->threads->list(string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionThread](api/beta.md)>

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

$client->beta->sessions->threads->retrieve(string threadID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsSessionThread](api/beta.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

$client->beta->sessions->threads->archive(string threadID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsSessionThread](api/beta.md)

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

##### ModelsExpand Collapse

[ManagedAgentsSessionThread](api/beta.md)

string id

Unique identifier for this thread.

[BetaManagedAgentsSessionThreadAgent](api/beta.md) agent

Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

?\Datetime archivedAt

A timestamp in RFC 3339 format

\Datetime createdAt

A timestamp in RFC 3339 format

?string parentThreadID

Parent thread that spawned this thread. Null for the primary thread.

string sessionID

The session this thread belongs to.

?[ManagedAgentsSessionThreadStats](api/beta.md) stats

Timing statistics for a session thread.

[ManagedAgentsSessionThreadStatus](api/beta.md) status

SessionThreadStatus enum

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

?[ManagedAgentsSessionThreadUsage](api/beta.md) usage

Cumulative token usage for a session thread across all turns.

[ManagedAgentsSessionThreadStats](api/beta.md)

?float activeSeconds

Cumulative time in seconds the thread spent actively running. Excludes idle time.

?float durationSeconds

Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

?float startupSeconds

Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

[ManagedAgentsSessionThreadStatus](api/beta.md)

One of the following:

"running"

"idle"

"rescheduling"

"terminated"

[ManagedAgentsSessionThreadUsage](api/beta.md)

?[BetaManagedAgentsCacheCreationUsage](api/beta.md) cacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

?int cacheReadInputTokens

Total tokens read from prompt cache.

?int inputTokens

Total input tokens consumed across all turns.

?int outputTokens

Total output tokens generated across all turns.

[ManagedAgentsStreamSessionThreadEvents](api/beta.md)

One of the following:

[ManagedAgentsUserMessageEvent](api/beta.md)

string id

Unique identifier for this event.

list<Content> content

Array of content blocks comprising the user message.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

[ManagedAgentsUserInterruptEvent](api/beta.md)

string id

Unique identifier for this event.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

[ManagedAgentsUserToolConfirmationEvent](api/beta.md)

string id

Unique identifier for this event.

Result result

UserToolConfirmationResult enum

string toolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?string denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

[ManagedAgentsUserCustomToolResultEvent](api/beta.md)

string id

Unique identifier for this event.

string customToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

[ManagedAgentsAgentCustomToolUseEvent](api/beta.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string name

Name of the custom tool being called.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

[ManagedAgentsAgentMessageEvent](api/beta.md)

string id

Unique identifier for this event.

list<[ManagedAgentsTextBlock](api/beta.md)> content

Array of text blocks comprising the agent response.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsAgentThinkingEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsAgentMCPToolUseEvent](api/beta.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string mcpServerName

Name of the MCP server providing the tool.

string name

Name of the MCP tool being used.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?EvaluatedPermission evaluatedPermission

AgentEvaluatedPermission enum

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

[ManagedAgentsAgentMCPToolResultEvent](api/beta.md)

string id

Unique identifier for this event.

string mcpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

[ManagedAgentsAgentToolUseEvent](api/beta.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string name

Name of the agent tool being used.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?EvaluatedPermission evaluatedPermission

AgentEvaluatedPermission enum

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

[ManagedAgentsAgentToolResultEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

string toolUseID

The id of the `agent.tool_use` event this result corresponds to.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

[ManagedAgentsAgentThreadMessageReceivedEvent](api/beta.md)

string id

Unique identifier for this event.

list<Content> content

Message content blocks.

string fromSessionThreadID

Public `sthr_` ID of the thread that sent the message.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?string fromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.

[ManagedAgentsAgentThreadMessageSentEvent](api/beta.md)

string id

Unique identifier for this event.

list<Content> content

Message content blocks.

\Datetime processedAt

A timestamp in RFC 3339 format

string toSessionThreadID

Public `sthr_` ID of the thread the message was sent to.

Type type

?string toAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

[ManagedAgentsAgentThreadContextCompactedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionErrorEvent](api/beta.md)

string id

Unique identifier for this event.

Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionStatusRescheduledEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionStatusRunningEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionStatusIdleEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Type type

[ManagedAgentsSessionStatusTerminatedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionThreadCreatedEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the callable agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public `sthr_` ID of the newly created thread.

Type type

[ManagedAgentsSpanOutcomeEvaluationStartEvent](api/beta.md)

string id

Unique identifier for this event.

int iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSpanOutcomeEvaluationEndEvent](api/beta.md)

string id

Unique identifier for this event.

string explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

int iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

string outcomeEvaluationStartID

The id of the corresponding `span.outcome_evaluation_start` event.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

string result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

Type type

[ManagedAgentsSpanModelUsage](api/beta.md) usage

Token usage for a single model request.

[ManagedAgentsSpanModelRequestStartEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSpanModelRequestEndEvent](api/beta.md)

string id

Unique identifier for this event.

?bool isError

Whether the model request resulted in an error.

string modelRequestStartID

The id of the corresponding `span.model_request_start` event.

[ManagedAgentsSpanModelUsage](api/beta.md) modelUsage

Token usage for a single model request.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSpanOutcomeEvaluationOngoingEvent](api/beta.md)

string id

Unique identifier for this event.

int iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsUserDefineOutcomeEvent](api/beta.md)

string id

Unique identifier for this event.

string description

What the agent should produce. Copied from the input event.

?int maxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

string outcomeID

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

\Datetime processedAt

A timestamp in RFC 3339 format

Rubric rubric

Rubric for grading the quality of an outcome.

Type type

[ManagedAgentsSessionDeletedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

[ManagedAgentsSessionThreadStatusRunningEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that started running.

Type type

[ManagedAgentsSessionThreadStatusIdleEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that went idle.

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Type type

[ManagedAgentsSessionThreadStatusTerminatedEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that terminated.

Type type

[BetaManagedAgentsUserToolResultEvent](api/beta.md)

string id

Unique identifier for this event.

string toolUseID

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

[ManagedAgentsSessionThreadStatusRescheduledEvent](api/beta.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that is retrying.

Type type

[BetaManagedAgentsSessionUpdatedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?[BetaManagedAgentsSessionAgent](api/beta.md) agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

?array<string,string> metadata

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

?string title

The session's new title. Present only when the update changed it.

[BetaManagedAgentsSystemMessageEvent](api/beta.md)

string id

Unique identifier for this event.

list<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks. Text-only.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

#### BetaSessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

$client->beta->sessions->threads->events->list(string threadID, string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionEvent](api/beta.md)>

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

$client->beta->sessions->threads->events->stream(string threadID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsStreamSessionThreadEvents](api/beta.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

#### BetaDeployments

##### [Create Deployment](api/beta/deployments/create.md)

$client->beta->deployments->create([Agent](api/beta/deployments/create.md) agent, string environmentID, list<[BetaManagedAgentsDeploymentInitialEventParams](api/beta.md)> initialEvents, string name, ?string description, ?array<string,string> metadata, ?list<Resource> resources, ?[BetaManagedAgentsScheduleParams](api/beta.md) schedule, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments

##### [List Deployments](api/beta/deployments/list.md)

$client->beta->deployments->list(?string agentID, ?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?[BetaManagedAgentsDeploymentStatus](api/beta.md) status, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsDeployment](api/beta.md)>

GET/v1/deployments

##### [Get Deployment](api/beta/deployments/retrieve.md)

$client->beta->deployments->retrieve(string deploymentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta.md)

GET/v1/deployments/{deployment\_id}

##### [Update Deployment](api/beta/deployments/update.md)

$client->beta->deployments->update(string deploymentID, ?[Agent](api/beta/deployments/update.md) agent, ?string description, ?string environmentID, ?list<[BetaManagedAgentsDeploymentInitialEventParams](api/beta.md)> initialEvents, ?array<string,string> metadata, ?string name, ?list<Resource> resources, ?[BetaManagedAgentsScheduleParams](api/beta.md) schedule, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments/{deployment\_id}

##### [Archive Deployment](api/beta/deployments/archive.md)

$client->beta->deployments->archive(string deploymentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments/{deployment\_id}/archive

##### [Run Deployment Now](api/beta/deployments/run.md)

$client->beta->deployments->run(string deploymentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeploymentRun](api/beta.md)

POST/v1/deployments/{deployment\_id}/run

##### [Pause Deployment](api/beta/deployments/pause.md)

$client->beta->deployments->pause(string deploymentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments/{deployment\_id}/pause

##### [Unpause Deployment](api/beta/deployments/unpause.md)

$client->beta->deployments->unpause(string deploymentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments/{deployment\_id}/unpause

##### ModelsExpand Collapse

[BetaManagedAgentsAgentArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsCronSchedule](api/beta.md)

string expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

string timezone

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

Type type

?\Datetime lastRunAt

A timestamp in RFC 3339 format

?list<\Datetime> upcomingRunsAt

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

[BetaManagedAgentsCronScheduleParams](api/beta.md)

string expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

string timezone

Required. IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC"). Validated against the IANA timezone database.

Type type

[BetaManagedAgentsDeployment](api/beta.md)

string id

Unique identifier for this deployment.

[BetaManagedAgentsAgentReference](api/beta.md) agent

A resolved agent reference with a concrete version.

?\Datetime archivedAt

A timestamp in RFC 3339 format

\Datetime createdAt

A timestamp in RFC 3339 format

?string description

Description of what the deployment does.

string environmentID

ID of the `environment` where sessions run.

list<[BetaManagedAgentsDeploymentInitialEvent](api/beta.md)> initialEvents

Events sent to each session immediately after creation.

array<string,string> metadata

Arbitrary key-value metadata. Maximum 16 pairs.

string name

Human-readable name.

?[BetaManagedAgentsDeploymentPausedReason](api/beta.md) pausedReason

Why a deployment is paused. Non-null exactly when `status` is `paused`.

list<[BetaManagedAgentsSessionResourceConfig](api/beta.md)> resources

Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

?[BetaManagedAgentsSchedule](api/beta.md) schedule

5-field POSIX cron schedule with computed runtime timestamps.

[BetaManagedAgentsDeploymentStatus](api/beta.md) status

Lifecycle status of a deployment.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

list<string> vaultIDs

Vault IDs supplying stored credentials for sessions created from this deployment.

[BetaManagedAgentsDeploymentInitialEvent](api/beta.md)

One of the following:

[BetaManagedAgentsDeploymentUserMessageEvent](api/beta.md)

list<Content> content

Array of content blocks for the user message.

Type type

[BetaManagedAgentsDeploymentUserDefineOutcomeEvent](api/beta.md)

string description

What the agent should produce. This is the task specification.

Rubric rubric

Rubric for grading the quality of an outcome.

Type type

?int maxIterations

Eval→revision cycles before giving up. Default 3, max 20.

[BetaManagedAgentsDeploymentSystemMessageEvent](api/beta.md)

list<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks to append. Text-only.

Type type

[BetaManagedAgentsDeploymentInitialEventParams](api/beta.md)

One of the following:

[ManagedAgentsUserMessageEventParams](api/beta.md)

list<Content> content

Array of content blocks for the user message.

Type type

[ManagedAgentsUserDefineOutcomeEventParams](api/beta.md)

string description

What the agent should produce. This is the task specification.

Rubric rubric

Rubric for grading the quality of an outcome.

Type type

?int maxIterations

Eval→revision cycles before giving up. Default 3, max 20.

[ManagedAgentsSystemMessageEventParams](api/beta.md)

list<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks to append. Text-only.

Type type

[BetaManagedAgentsDeploymentPausedReason](api/beta.md)

One of the following:

[BetaManagedAgentsManualDeploymentPausedReason](api/beta.md)

Type type

[BetaManagedAgentsErrorDeploymentPausedReason](api/beta.md)

[BetaManagedAgentsDeploymentPausedReasonError](api/beta.md) error

The error that triggered an auto-pause. Matches the failed run's `error.type`.

Type type

[BetaManagedAgentsDeploymentPausedReasonError](api/beta.md)

One of the following:

[BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsAgentArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsFileNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsVaultArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsUnknownDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsDeploymentStatus](api/beta.md)

One of the following:

"active"

"paused"

[BetaManagedAgentsDeploymentSystemMessageEvent](api/beta.md)

list<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks to append. Text-only.

Type type

[BetaManagedAgentsDeploymentUserDefineOutcomeEvent](api/beta.md)

string description

What the agent should produce. This is the task specification.

Rubric rubric

Rubric for grading the quality of an outcome.

Type type

?int maxIterations

Eval→revision cycles before giving up. Default 3, max 20.

[BetaManagedAgentsDeploymentUserMessageEvent](api/beta.md)

list<Content> content

Array of content blocks for the user message.

Type type

[BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsErrorDeploymentPausedReason](api/beta.md)

[BetaManagedAgentsDeploymentPausedReasonError](api/beta.md) error

The error that triggered an auto-pause. Matches the failed run's `error.type`.

Type type

[BetaManagedAgentsFileNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsFileResourceConfig](api/beta.md)

string fileID

ID of a previously uploaded file.

Type type

?string mountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

[BetaManagedAgentsGitHubRepositoryResourceConfig](api/beta.md)

Type type

string url

Github URL of the repository

?Checkout checkout

Branch or commit to check out. Defaults to the repository's default branch.

?string mountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.

[BetaManagedAgentsManualDeploymentPausedReason](api/beta.md)

Type type

[BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsMemoryStoreResourceConfig](api/beta.md)

string memoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type

?Access access

Access mode for an attached memory store.

?string instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

[BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsSchedule](api/beta.md)

string expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

string timezone

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

Type type

?\Datetime lastRunAt

A timestamp in RFC 3339 format

?list<\Datetime> upcomingRunsAt

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

[BetaManagedAgentsScheduleParams](api/beta.md)

string expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

string timezone

Required. IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC"). Validated against the IANA timezone database.

Type type

[BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsSessionResourceConfig](api/beta.md)

One of the following:

[BetaManagedAgentsGitHubRepositoryResourceConfig](api/beta.md)

Type type

string url

Github URL of the repository

?Checkout checkout

Branch or commit to check out. Defaults to the repository's default branch.

?string mountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.

[BetaManagedAgentsFileResourceConfig](api/beta.md)

string fileID

ID of a previously uploaded file.

Type type

?string mountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

[BetaManagedAgentsMemoryStoreResourceConfig](api/beta.md)

string memoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type

?Access access

Access mode for an attached memory store.

?string instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

[BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsUnknownDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsVaultArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError](api/beta.md)

Type type

#### BetaDeployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

$client->beta->deploymentRuns->list(?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?string deploymentID, ?bool hasError, ?int limit, ?string page, ?[BetaManagedAgentsTriggerType](api/beta.md) triggerType, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsDeploymentRun](api/beta.md)>

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

$client->beta->deploymentRuns->retrieve(string deploymentRunID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeploymentRun](api/beta.md)

GET/v1/deployment\_runs/{deployment\_run\_id}

##### ModelsExpand Collapse

[BetaManagedAgentsAgentArchivedRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsDeploymentRun](api/beta.md)

string id

Unique identifier for this run (`drun_...`).

[BetaManagedAgentsAgentReference](api/beta.md) agent

A resolved agent reference with a concrete version.

\Datetime createdAt

A timestamp in RFC 3339 format

string deploymentID

ID of the deployment that produced this run.

?Error error

Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

?string sessionID

Populated on success. Null on creation failure. Exactly one of session\_id or error is non-null.

[BetaManagedAgentsTriggerContext](api/beta.md) triggerContext

Describes what triggered a deployment run, with trigger-specific metadata.

Type type

[BetaManagedAgentsEnvironmentArchivedRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsEnvironmentNotFoundRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsFileNotFoundRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsManualTriggerContext](api/beta.md)

Type type

[BetaManagedAgentsMCPEgressBlockedRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsMemoryStoreArchivedRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsOrganizationDisabledRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsScheduleTriggerContext](api/beta.md)

\Datetime scheduledAt

A timestamp in RFC 3339 format

Type type

[BetaManagedAgentsSelfHostedResourcesUnsupportedRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsSessionCreationRejectedRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsSessionRateLimitedRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsSessionResourceNotFoundRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsSkillNotFoundRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsTriggerContext](api/beta.md)

One of the following:

[BetaManagedAgentsScheduleTriggerContext](api/beta.md)

\Datetime scheduledAt

A timestamp in RFC 3339 format

Type type

[BetaManagedAgentsManualTriggerContext](api/beta.md)

Type type

[BetaManagedAgentsTriggerType](api/beta.md)

One of the following:

"schedule"

"manual"

[BetaManagedAgentsUnknownRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsVaultArchivedRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsVaultNotFoundRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsWorkspaceArchivedRunError](api/beta.md)

string message

Human-readable error description.

Type type

#### BetaVaults

##### [Create Vault](api/beta/vaults/create.md)

$client->beta->vaults->create(string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [BetaManagedAgentsVault](api/beta.md)

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

$client->beta->vaults->list(?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsVault](api/beta.md)>

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

$client->beta->vaults->retrieve(string vaultID, ?list<AnthropicBeta> betas): [BetaManagedAgentsVault](api/beta.md)

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

$client->beta->vaults->update(string vaultID, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [BetaManagedAgentsVault](api/beta.md)

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

$client->beta->vaults->delete(string vaultID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeletedVault](api/beta.md)

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

$client->beta->vaults->archive(string vaultID, ?list<AnthropicBeta> betas): [BetaManagedAgentsVault](api/beta.md)

POST/v1/vaults/{vault\_id}/archive

##### ModelsExpand Collapse

[BetaManagedAgentsDeletedVault](api/beta.md)

string id

Unique identifier of the deleted vault.

Type type

[BetaManagedAgentsVault](api/beta.md)

string id

Unique identifier for the vault.

?\Datetime archivedAt

A timestamp in RFC 3339 format

\Datetime createdAt

A timestamp in RFC 3339 format

string displayName

Human-readable name for the vault.

array<string,string> metadata

Arbitrary key-value metadata attached to the vault.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

#### BetaVaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

$client->beta->vaults->credentials->create(string vaultID, [Auth](api/beta/vaults/credentials/create.md) auth, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [ManagedAgentsCredential](api/beta.md)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

$client->beta->vaults->credentials->list(string vaultID, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsCredential](api/beta.md)>

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

$client->beta->vaults->credentials->retrieve(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsCredential](api/beta.md)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

$client->beta->vaults->credentials->update(string credentialID, string vaultID, ?[Auth](api/beta/vaults/credentials/update.md) auth, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [ManagedAgentsCredential](api/beta.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

$client->beta->vaults->credentials->delete(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsDeletedCredential](api/beta.md)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

$client->beta->vaults->credentials->archive(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsCredential](api/beta.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

$client->beta->vaults->credentials->mcpOAuthValidate(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsCredentialValidation](api/beta.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

##### ModelsExpand Collapse

[ManagedAgentsCredential](api/beta.md)

string id

Unique identifier for the credential.

?\Datetime archivedAt

A timestamp in RFC 3339 format

Auth auth

Authentication details for a credential.

\Datetime createdAt

A timestamp in RFC 3339 format

array<string,string> metadata

Arbitrary key-value metadata attached to the credential.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

string vaultID

Identifier of the vault this credential belongs to.

?string displayName

Human-readable name for the credential.

[ManagedAgentsCredentialNetworkingParams](api/beta.md)

One of the following:

[ManagedAgentsUnrestrictedCredentialNetworkingParams](api/beta.md)

Type type

[ManagedAgentsLimitedCredentialNetworkingParams](api/beta.md)

list<string> allowedHosts

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

Type type

[ManagedAgentsCredentialValidation](api/beta.md)

string credentialID

Unique identifier of the credential that was validated.

bool hasRefreshToken

Whether the credential has a refresh token configured.

?[ManagedAgentsMCPProbe](api/beta.md) mcpProbe

The failing step of an MCP validation probe.

?[ManagedAgentsRefreshObject](api/beta.md) refresh

Outcome of a refresh-token exchange attempted during credential validation.

[ManagedAgentsCredentialValidationStatus](api/beta.md) status

Overall verdict of a credential validation probe.

Type type

\Datetime validatedAt

A timestamp in RFC 3339 format

string vaultID

Identifier of the vault containing the credential.

[ManagedAgentsCredentialValidationStatus](api/beta.md)

One of the following:

"valid"

"invalid"

"unknown"

[ManagedAgentsDeletedCredential](api/beta.md)

string id

Unique identifier of the deleted credential.

Type type

[ManagedAgentsEnvironmentVariableAuthResponse](api/beta.md)

Networking networking

Outbound hosts the secret value is substituted on.

string secretName

Name of the environment variable.

Type type

[ManagedAgentsEnvironmentVariableCreateParams](api/beta.md)

[ManagedAgentsCredentialNetworkingParams](api/beta.md) networking

Outbound hosts the secret value is substituted on.

string secretName

Name of the environment variable. Immutable after create.

string secretValue

Secret value. Write-only; never returned in responses.

Type type

[ManagedAgentsEnvironmentVariableUpdateParams](api/beta.md)

Type type

?[ManagedAgentsCredentialNetworkingParams](api/beta.md) networking

Updated networking scope. Full replacement.

?string secretValue

Updated secret value.

[ManagedAgentsLimitedCredentialNetworkingParams](api/beta.md)

list<string> allowedHosts

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

Type type

[ManagedAgentsLimitedCredentialNetworkingResponse](api/beta.md)

list<string> allowedHosts

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

Type type

[ManagedAgentsMCPOAuthAuthResponse](api/beta.md)

string mcpServerURL

URL of the MCP server this credential authenticates against.

Type type

?\Datetime expiresAt

A timestamp in RFC 3339 format

?[ManagedAgentsMCPOAuthRefreshResponse](api/beta.md) refresh

OAuth refresh token configuration returned in credential responses.

[ManagedAgentsMCPOAuthCreateParams](api/beta.md)

string accessToken

OAuth access token.

string mcpServerURL

URL of the MCP server this credential authenticates against.

Type type

?\Datetime expiresAt

A timestamp in RFC 3339 format

?[ManagedAgentsMCPOAuthRefreshParams](api/beta.md) refresh

OAuth refresh token parameters for creating a credential with refresh support.

[ManagedAgentsMCPOAuthRefreshParams](api/beta.md)

string clientID

OAuth client ID.

string refreshToken

OAuth refresh token.

string tokenEndpoint

Token endpoint URL used to refresh the access token.

TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

?string resource

OAuth resource indicator.

?string scope

OAuth scope for the refresh request.

[ManagedAgentsMCPOAuthRefreshResponse](api/beta.md)

string clientID

OAuth client ID.

string tokenEndpoint

Token endpoint URL used to refresh the access token.

TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

?string resource

OAuth resource indicator.

?string scope

OAuth scope for the refresh request.

[ManagedAgentsMCPOAuthRefreshUpdateParams](api/beta.md)

?string refreshToken

Updated OAuth refresh token.

?string scope

Updated OAuth scope for the refresh request.

?TokenEndpointAuth tokenEndpointAuth

Updated HTTP Basic authentication parameters for the token endpoint.

[ManagedAgentsMCPOAuthUpdateParams](api/beta.md)

Type type

?string accessToken

Updated OAuth access token.

?\Datetime expiresAt

A timestamp in RFC 3339 format

?[ManagedAgentsMCPOAuthRefreshUpdateParams](api/beta.md) refresh

Parameters for updating OAuth refresh token configuration.

[ManagedAgentsMCPProbe](api/beta.md)

?[ManagedAgentsRefreshHTTPResponse](api/beta.md) httpResponse

An HTTP response captured during a credential validation probe.

string method

The MCP method that failed (for example `initialize` or `tools/list`).

[ManagedAgentsRefreshHTTPResponse](api/beta.md)

string body

Response body. May be truncated and has sensitive values scrubbed.

bool bodyTruncated

Whether `body` was truncated.

string contentType

Value of the `Content-Type` response header.

int statusCode

HTTP status code.

[ManagedAgentsRefreshObject](api/beta.md)

?[ManagedAgentsRefreshHTTPResponse](api/beta.md) httpResponse

An HTTP response captured during a credential validation probe.

Status status

Outcome of a refresh-token exchange attempted during credential validation.

[ManagedAgentsStaticBearerAuthResponse](api/beta.md)

string mcpServerURL

URL of the MCP server this credential authenticates against.

Type type

[ManagedAgentsStaticBearerCreateParams](api/beta.md)

string token

Static bearer token value.

string mcpServerURL

URL of the MCP server this credential authenticates against.

Type type

[ManagedAgentsStaticBearerUpdateParams](api/beta.md)

Type type

?string token

Updated static bearer token value.

[ManagedAgentsTokenEndpointAuthBasicParam](api/beta.md)

string clientSecret

OAuth client secret.

Type type

[ManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md)

Type type

[ManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta.md)

Type type

?string clientSecret

Updated OAuth client secret.

[ManagedAgentsTokenEndpointAuthNoneParam](api/beta.md)

Type type

[ManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md)

Type type

[ManagedAgentsTokenEndpointAuthPostParam](api/beta.md)

string clientSecret

OAuth client secret.

Type type

[ManagedAgentsTokenEndpointAuthPostResponse](api/beta.md)

Type type

[ManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta.md)

Type type

?string clientSecret

Updated OAuth client secret.

[ManagedAgentsUnrestrictedCredentialNetworkingParams](api/beta.md)

Type type

[ManagedAgentsUnrestrictedCredentialNetworkingResponse](api/beta.md)

Type type

#### BetaMemory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

$client->beta->memoryStores->create(string name, ?string description, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [BetaManagedAgentsMemoryStore](api/beta.md)

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

$client->beta->memoryStores->list(?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsMemoryStore](api/beta.md)>

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

$client->beta->memoryStores->retrieve(string memoryStoreID, ?list<AnthropicBeta> betas): [BetaManagedAgentsMemoryStore](api/beta.md)

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

$client->beta->memoryStores->update(string memoryStoreID, ?string description, ?array<string,string> metadata, ?string name, ?list<AnthropicBeta> betas): [BetaManagedAgentsMemoryStore](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

$client->beta->memoryStores->delete(string memoryStoreID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeletedMemoryStore](api/beta.md)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

$client->beta->memoryStores->archive(string memoryStoreID, ?list<AnthropicBeta> betas): [BetaManagedAgentsMemoryStore](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse

[BetaManagedAgentsDeletedMemoryStore](api/beta.md)

string id

ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

Type type

[BetaManagedAgentsMemoryStore](api/beta.md)

string id

Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

\Datetime createdAt

A timestamp in RFC 3339 format

string name

Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

?\Datetime archivedAt

A timestamp in RFC 3339 format

?string description

Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

?array<string,string> metadata

Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### BetaMemory StoresMemories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

$client->beta->memoryStores->memories->create(string memoryStoreID, ?string content, string path, ?[ManagedAgentsMemoryView](api/beta.md) view, ?list<AnthropicBeta> betas): [ManagedAgentsMemory](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

$client->beta->memoryStores->memories->list(string memoryStoreID, ?int depth, ?int limit, ?[Order](api/beta/memory_stores/memories/list.md) order, ?string orderBy, ?string page, ?string pathPrefix, ?[ManagedAgentsMemoryView](api/beta.md) view, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsMemoryListItem](api/beta.md)>

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

$client->beta->memoryStores->memories->retrieve(string memoryID, string memoryStoreID, ?[ManagedAgentsMemoryView](api/beta.md) view, ?list<AnthropicBeta> betas): [ManagedAgentsMemory](api/beta.md)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

$client->beta->memoryStores->memories->update(string memoryID, string memoryStoreID, ?[ManagedAgentsMemoryView](api/beta.md) view, ?string content, ?string path, ?[ManagedAgentsPrecondition](api/beta.md) precondition, ?list<AnthropicBeta> betas): [ManagedAgentsMemory](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

$client->beta->memoryStores->memories->delete(string memoryID, string memoryStoreID, ?string expectedContentSha256, ?list<AnthropicBeta> betas): [ManagedAgentsDeletedMemory](api/beta.md)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### ModelsExpand Collapse

[ManagedAgentsConflictError](api/beta.md)

Type type

?string message

[ManagedAgentsContentSha256Precondition](api/beta.md)

Type type

?string contentSha256

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

[ManagedAgentsDeletedMemory](api/beta.md)

string id

ID of the deleted memory (a `mem_...` value).

Type type

[ManagedAgentsError](api/beta.md)

One of the following:

[BetaInvalidRequestError](api/beta.md)

string message

"invalid\_request\_error" type

[BetaAuthenticationError](api/beta.md)

string message

"authentication\_error" type

[BetaBillingError](api/beta.md)

string message

"billing\_error" type

[BetaPermissionError](api/beta.md)

string message

"permission\_error" type

[BetaNotFoundError](api/beta.md)

string message

"not\_found\_error" type

[BetaRateLimitError](api/beta.md)

string message

"rate\_limit\_error" type

[BetaGatewayTimeoutError](api/beta.md)

string message

"timeout\_error" type

[BetaAPIError](api/beta.md)

string message

"api\_error" type

[BetaOverloadedError](api/beta.md)

string message

"overloaded\_error" type

[ManagedAgentsMemoryPreconditionFailedError](api/beta.md)

Type type

?string message

[ManagedAgentsMemoryPathConflictError](api/beta.md)

Type type

?string conflictingMemoryID

?string conflictingPath

?string message

[ManagedAgentsConflictError](api/beta.md)

Type type

?string message

[ManagedAgentsMemory](api/beta.md)

string id

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

string contentSha256

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

int contentSizeBytes

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

\Datetime createdAt

A timestamp in RFC 3339 format

string memoryStoreID

ID of the memory store this memory belongs to (a `memstore_...` value).

string memoryVersionID

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

string path

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

?string content

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

[ManagedAgentsMemoryListItem](api/beta.md)

One of the following:

[ManagedAgentsMemory](api/beta.md)

string id

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

string contentSha256

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

int contentSizeBytes

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

\Datetime createdAt

A timestamp in RFC 3339 format

string memoryStoreID

ID of the memory store this memory belongs to (a `memstore_...` value).

string memoryVersionID

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

string path

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

?string content

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

[ManagedAgentsMemoryPrefix](api/beta.md)

string path

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

Type type

[ManagedAgentsMemoryPathConflictError](api/beta.md)

Type type

?string conflictingMemoryID

?string conflictingPath

?string message

[ManagedAgentsMemoryPreconditionFailedError](api/beta.md)

Type type

?string message

[ManagedAgentsMemoryPrefix](api/beta.md)

string path

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

Type type

[ManagedAgentsMemoryView](api/beta.md)

One of the following:

"basic"

"full"

[ManagedAgentsPrecondition](api/beta.md)

Type type

?string contentSha256

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

#### BetaMemory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

$client->beta->memoryStores->memoryVersions->list(string memoryStoreID, ?string apiKeyID, ?\Datetime createdAtGte, ?\Datetime createdAtLte, ?int limit, ?string memoryID, ?[ManagedAgentsMemoryVersionOperation](api/beta.md) operation, ?string page, ?string sessionID, ?[ManagedAgentsMemoryView](api/beta.md) view, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsMemoryVersion](api/beta.md)>

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

$client->beta->memoryStores->memoryVersions->retrieve(string memoryVersionID, string memoryStoreID, ?[ManagedAgentsMemoryView](api/beta.md) view, ?list<AnthropicBeta> betas): [ManagedAgentsMemoryVersion](api/beta.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

$client->beta->memoryStores->memoryVersions->redact(string memoryVersionID, string memoryStoreID, ?list<AnthropicBeta> betas): [ManagedAgentsMemoryVersion](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

[ManagedAgentsActor](api/beta.md)

One of the following:

[ManagedAgentsSessionActor](api/beta.md)

string sessionID

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type type

[ManagedAgentsAPIActor](api/beta.md)

string apiKeyID

ID of the API key that performed the write. This identifies the key, not the secret.

Type type

[ManagedAgentsUserActor](api/beta.md)

Type type

string userID

ID of the user who performed the write (a `user_...` value).

[ManagedAgentsAPIActor](api/beta.md)

string apiKeyID

ID of the API key that performed the write. This identifies the key, not the secret.

Type type

[ManagedAgentsMemoryVersion](api/beta.md)

string id

Unique identifier for this version (a `memver_...` value).

\Datetime createdAt

A timestamp in RFC 3339 format

string memoryID

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

string memoryStoreID

ID of the memory store this version belongs to (a `memstore_...` value).

[ManagedAgentsMemoryVersionOperation](api/beta.md) operation

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

Type type

?string content

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

?string contentSha256

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

?int contentSizeBytes

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

?[ManagedAgentsActor](api/beta.md) createdBy

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

?string path

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

?\Datetime redactedAt

A timestamp in RFC 3339 format

?[ManagedAgentsActor](api/beta.md) redactedBy

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

[ManagedAgentsMemoryVersionOperation](api/beta.md)

One of the following:

"created"

"modified"

"deleted"

[ManagedAgentsSessionActor](api/beta.md)

string sessionID

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type type

[ManagedAgentsUserActor](api/beta.md)

Type type

string userID

ID of the user who performed the write (a `user_...` value).

#### BetaFiles

##### [Upload File](api/beta/files/upload.md)

$client->beta->files->upload(string file, ?list<AnthropicBeta> betas): [FileMetadata](api/beta.md)

POST/v1/files

##### [List Files](api/beta/files/list.md)

$client->beta->files->list(?string afterID, ?string beforeID, ?int limit, ?string scopeID, ?list<AnthropicBeta> betas): Page<[FileMetadata](api/beta.md)>

GET/v1/files

##### [Download File](api/beta/files/download.md)

$client->beta->files->download(string fileID, ?list<AnthropicBeta> betas): download

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

$client->beta->files->retrieveMetadata(string fileID, ?list<AnthropicBeta> betas): [FileMetadata](api/beta.md)

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

$client->beta->files->delete(string fileID, ?list<AnthropicBeta> betas): [DeletedFile](api/beta.md)

DELETE/v1/files/{file\_id}

##### ModelsExpand Collapse

[BetaFileScope](api/beta.md)

string id

The ID of the scoping resource (e.g., the session ID).

"session" type

The type of scope (e.g., `"session"`).

[DeletedFile](api/beta.md)

string id

ID of the deleted file.

?Type type

Deleted object type.

For file deletion, this is always `"file_deleted"`.

[FileMetadata](api/beta.md)

string id

Unique object identifier.

The format and length of IDs may change over time.

\Datetime createdAt

RFC 3339 datetime string representing when the file was created.

string filename

Original filename of the uploaded file.

string mimeType

MIME type of the file.

int sizeBytes

Size of the file in bytes.

"file" type

Object type.

For files, this is always `"file"`.

?bool downloadable

Whether the file can be downloaded.

?[BetaFileScope](api/beta.md) scope

The scope of this file, indicating the context in which it was created (e.g., a session).

#### BetaSkills

##### [Create Skill](api/beta/skills/create.md)

$client->beta->skills->create(?string displayTitle, ?list<string> files, ?list<AnthropicBeta> betas): [SkillNewResponse](api/beta.md)

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

$client->beta->skills->list(?int limit, ?string page, ?string source, ?list<AnthropicBeta> betas): PageCursor<[SkillListResponse](api/beta.md)>

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

$client->beta->skills->retrieve(string skillID, ?list<AnthropicBeta> betas): [SkillGetResponse](api/beta.md)

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

$client->beta->skills->delete(string skillID, ?list<AnthropicBeta> betas): [SkillDeleteResponse](api/beta.md)

DELETE/v1/skills/{skill\_id}

#### BetaSkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

$client->beta->skills->versions->create(string skillID, ?list<string> files, ?list<AnthropicBeta> betas): [VersionNewResponse](api/beta.md)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

$client->beta->skills->versions->list(string skillID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[VersionListResponse](api/beta.md)>

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/beta/skills/versions/download.md)

$client->beta->skills->versions->download(string version, string skillID, ?list<AnthropicBeta> betas): download

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

$client->beta->skills->versions->retrieve(string version, string skillID, ?list<AnthropicBeta> betas): [VersionGetResponse](api/beta.md)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

$client->beta->skills->versions->delete(string version, string skillID, ?list<AnthropicBeta> betas): [VersionDeleteResponse](api/beta.md)

DELETE/v1/skills/{skill\_id}/versions/{version}

#### BetaUser Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

$client->beta->userProfiles->create(?string externalID, ?array<string,string> metadata, ?string name, ?[Relationship](api/beta/user_profiles/create.md) relationship, ?list<AnthropicBeta> betas): [BetaUserProfile](api/beta.md)

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

$client->beta->userProfiles->list(?int limit, ?[Order](api/beta/user_profiles/list.md) order, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaUserProfile](api/beta.md)>

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

$client->beta->userProfiles->retrieve(string userProfileID, ?list<AnthropicBeta> betas): [BetaUserProfile](api/beta.md)

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

$client->beta->userProfiles->update(string userProfileID, ?string externalID, ?array<string,string> metadata, ?string name, ?[Relationship](api/beta/user_profiles/update.md) relationship, ?list<AnthropicBeta> betas): [BetaUserProfile](api/beta.md)

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

$client->beta->userProfiles->createEnrollmentURL(string userProfileID, ?list<AnthropicBeta> betas): [BetaUserProfileEnrollmentURL](api/beta.md)

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

##### ModelsExpand Collapse

[BetaUserProfile](api/beta.md)

string id

Unique identifier for this user profile, prefixed `uprof_`.

\Datetime createdAt

A timestamp in RFC 3339 format

array<string,string> metadata

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

Relationship relationship

How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

array<string,[BetaUserProfileTrustGrant](api/beta.md)> trustGrants

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

Type type

Object type. Always `user_profile`.

\Datetime updatedAt

A timestamp in RFC 3339 format

?string externalID

Platform's own identifier for this user. Not enforced unique.

?string name

Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

[BetaUserProfileEnrollmentURL](api/beta.md)

\Datetime expiresAt

A timestamp in RFC 3339 format

Type type

Object type. Always `enrollment_url`.

string url

Enrollment URL to send to the end user. Valid until `expires_at`.

[BetaUserProfileTrustGrant](api/beta.md)

Status status

Status of the trust grant.

#### BetaWebhooks

Helpers for receiving and verifying webhook events. Use `unwrap` in your SDK to verify signatures and parse payloads; see the [webhooks guide](managed-agents/webhooks.md) for handler examples.

Possible `data.type` values:

- `session.archived`
- `session.created`
- `session.deleted`
- `session.idled`
- `session.outcome_evaluation_ended`
- `session.pending`
- `session.requires_action`
- `session.running`
- `session.status_idled`
- `session.status_rescheduled`
- `session.status_run_started`
- `session.status_terminated`
- `session.thread_created`
- `session.thread_idled`
- `session.thread_terminated`
- `vault.archived`
- `vault.created`
- `vault.deleted`
- `vault_credential.archived`
- `vault_credential.created`
- `vault_credential.deleted`
- `vault_credential.refresh_failed`

##### ModelsExpand Collapse

[BetaWebhookEvent](api/beta.md)

string id

Unique event identifier for idempotency.

\Datetime createdAt

RFC 3339 timestamp when the event occurred.

[BetaWebhookEventData](api/beta.md) data

"event" type

Object type. Always `event` for webhook payloads.

[BetaWebhookEventData](api/beta.md)

One of the following:

[BetaWebhookSessionCreatedEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.created" type

string workspaceID

[BetaWebhookSessionPendingEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.pending" type

string workspaceID

[BetaWebhookSessionRunningEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.running" type

string workspaceID

[BetaWebhookSessionIdledEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.idled" type

string workspaceID

[BetaWebhookSessionRequiresActionEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.requires\_action" type

string workspaceID

[BetaWebhookSessionArchivedEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.archived" type

string workspaceID

[BetaWebhookSessionDeletedEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.deleted" type

string workspaceID

[BetaWebhookSessionStatusRescheduledEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.status\_rescheduled" type

string workspaceID

[BetaWebhookSessionStatusRunStartedEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.status\_run\_started" type

string workspaceID

[BetaWebhookSessionStatusIdledEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.status\_idled" type

string workspaceID

[BetaWebhookSessionStatusTerminatedEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.status\_terminated" type

string workspaceID

[BetaWebhookSessionThreadCreatedEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

string sessionThreadID

ID of the session thread this event refers to.

"session.thread\_created" type

string workspaceID

[BetaWebhookSessionThreadIdledEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

string sessionThreadID

ID of the session thread this event refers to.

"session.thread\_idled" type

string workspaceID

[BetaWebhookSessionThreadTerminatedEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

string sessionThreadID

ID of the session thread this event refers to.

"session.thread\_terminated" type

string workspaceID

[BetaWebhookSessionOutcomeEvaluationEndedEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.outcome\_evaluation\_ended" type

string workspaceID

[BetaWebhookVaultCreatedEventData](api/beta.md)

string id

ID of the vault that triggered the event.

string organizationID

"vault.created" type

string workspaceID

[BetaWebhookVaultArchivedEventData](api/beta.md)

string id

ID of the vault that triggered the event.

string organizationID

"vault.archived" type

string workspaceID

[BetaWebhookVaultDeletedEventData](api/beta.md)

string id

ID of the vault that triggered the event.

string organizationID

"vault.deleted" type

string workspaceID

[BetaWebhookVaultCredentialCreatedEventData](api/beta.md)

string id

ID of the vault credential that triggered the event.

string organizationID

"vault\_credential.created" type

string vaultID

ID of the vault that owns this credential.

string workspaceID

[BetaWebhookVaultCredentialArchivedEventData](api/beta.md)

string id

ID of the vault credential that triggered the event.

string organizationID

"vault\_credential.archived" type

string vaultID

ID of the vault that owns this credential.

string workspaceID

[BetaWebhookVaultCredentialDeletedEventData](api/beta.md)

string id

ID of the vault credential that triggered the event.

string organizationID

"vault\_credential.deleted" type

string vaultID

ID of the vault that owns this credential.

string workspaceID

[BetaWebhookVaultCredentialRefreshFailedEventData](api/beta.md)

string id

ID of the vault credential that triggered the event.

string organizationID

"vault\_credential.refresh\_failed" type

string vaultID

ID of the vault that owns this credential.

string workspaceID

[BetaWebhookSessionArchivedEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.archived" type

string workspaceID

[BetaWebhookSessionCreatedEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.created" type

string workspaceID

[BetaWebhookSessionDeletedEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.deleted" type

string workspaceID

[BetaWebhookSessionIdledEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.idled" type

string workspaceID

[BetaWebhookSessionOutcomeEvaluationEndedEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.outcome\_evaluation\_ended" type

string workspaceID

[BetaWebhookSessionPendingEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.pending" type

string workspaceID

[BetaWebhookSessionRequiresActionEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.requires\_action" type

string workspaceID

[BetaWebhookSessionRunningEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.running" type

string workspaceID

[BetaWebhookSessionStatusIdledEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.status\_idled" type

string workspaceID

[BetaWebhookSessionStatusRescheduledEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.status\_rescheduled" type

string workspaceID

[BetaWebhookSessionStatusRunStartedEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.status\_run\_started" type

string workspaceID

[BetaWebhookSessionStatusTerminatedEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

"session.status\_terminated" type

string workspaceID

[BetaWebhookSessionThreadCreatedEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

string sessionThreadID

ID of the session thread this event refers to.

"session.thread\_created" type

string workspaceID

[BetaWebhookSessionThreadIdledEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

string sessionThreadID

ID of the session thread this event refers to.

"session.thread\_idled" type

string workspaceID

[BetaWebhookSessionThreadTerminatedEventData](api/beta.md)

string id

ID of the session that triggered the event.

string organizationID

string sessionThreadID

ID of the session thread this event refers to.

"session.thread\_terminated" type

string workspaceID

[BetaWebhookVaultArchivedEventData](api/beta.md)

string id

ID of the vault that triggered the event.

string organizationID

"vault.archived" type

string workspaceID

[BetaWebhookVaultCreatedEventData](api/beta.md)

string id

ID of the vault that triggered the event.

string organizationID

"vault.created" type

string workspaceID

[BetaWebhookVaultCredentialArchivedEventData](api/beta.md)

string id

ID of the vault credential that triggered the event.

string organizationID

"vault\_credential.archived" type

string vaultID

ID of the vault that owns this credential.

string workspaceID

[BetaWebhookVaultCredentialCreatedEventData](api/beta.md)

string id

ID of the vault credential that triggered the event.

string organizationID

"vault\_credential.created" type

string vaultID

ID of the vault that owns this credential.

string workspaceID

[BetaWebhookVaultCredentialDeletedEventData](api/beta.md)

string id

ID of the vault credential that triggered the event.

string organizationID

"vault\_credential.deleted" type

string vaultID

ID of the vault that owns this credential.

string workspaceID

[BetaWebhookVaultCredentialRefreshFailedEventData](api/beta.md)

string id

ID of the vault credential that triggered the event.

string organizationID

"vault\_credential.refresh\_failed" type

string vaultID

ID of the vault that owns this credential.

string workspaceID

[BetaWebhookVaultDeletedEventData](api/beta.md)

string id

ID of the vault that triggered the event.

string organizationID

"vault.deleted" type

string workspaceID

[UnwrapWebhookEvent](api/beta.md)

string id

Unique event identifier for idempotency.

\Datetime createdAt

RFC 3339 timestamp when the event occurred.

[BetaWebhookEventData](api/beta.md) data

"event" type

Object type. Always `event` for webhook payloads.

---

*Copyright © Anthropic. All rights reserved.*
