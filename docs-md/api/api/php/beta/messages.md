# Messages

Copy page

SDK language

PHP

# Messages

##### [Create a Message](api/beta/messages/create.md)

$client->beta->messages->create(int maxTokens, list<[BetaMessageParam](api/beta.md)> messages, Model model, ?[BetaCacheControlEphemeral](api/beta.md) cacheControl, ?[Container](api/beta/messages/create.md) container, ?[BetaContextManagementConfig](api/beta.md) contextManagement, ?[BetaDiagnosticsParam](api/beta.md) diagnostics, ?string fallbackCreditToken, ?list<[BetaFallbackParam](api/beta.md)> fallbacks, ?string inferenceGeo, ?list<[BetaRequestMCPServerURLDefinition](api/beta.md)> mcpServers, ?[BetaMetadata](api/beta.md) metadata, ?[BetaOutputConfig](api/beta.md) outputConfig, ?[BetaJSONOutputFormat](api/beta.md) outputFormat, ?[ServiceTier](api/beta/messages/create.md) serviceTier, ?[Speed](api/beta/messages/create.md) speed, ?list<string> stopSequences, ?[System](api/beta/messages/create.md) system, ?float temperature, ?[BetaThinkingConfigParam](api/beta.md) thinking, ?[BetaToolChoice](api/beta.md) toolChoice, ?list<[BetaToolUnion](api/beta.md)> tools, ?int topK, ?float topP, ?string userProfileID, ?list<AnthropicBeta> betas): [BetaMessage](api/beta.md)

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

$client->beta->messages->countTokens(list<[BetaMessageParam](api/beta.md)> messages, Model model, ?[BetaCacheControlEphemeral](api/beta.md) cacheControl, ?[BetaContextManagementConfig](api/beta.md) contextManagement, ?list<[BetaRequestMCPServerURLDefinition](api/beta.md)> mcpServers, ?[BetaOutputConfig](api/beta.md) outputConfig, ?[BetaJSONOutputFormat](api/beta.md) outputFormat, ?[Speed](api/beta/messages/count_tokens.md) speed, ?[System](api/beta/messages/count_tokens.md) system, ?[BetaThinkingConfigParam](api/beta.md) thinking, ?[BetaToolChoice](api/beta.md) toolChoice, ?list<Tool> tools, ?list<AnthropicBeta> betas): [BetaMessageTokensCount](api/beta.md)

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse



[BetaAdvisorMessageIterationUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

int cacheReadInputTokens

The number of input tokens read from the cache.

int inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

int outputTokens

The number of output tokens which were used.

"advisor\_message" type

Usage for an advisor sub-inference iteration



[BetaAdvisorRedactedResultBlock](api/beta.md)

string encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

?string stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

"advisor\_redacted\_result" type



[BetaAdvisorRedactedResultBlockParam](api/beta.md)

string encryptedContent

Opaque blob produced by a prior response; must be round-tripped verbatim.

"advisor\_redacted\_result" type

?string stopReason



[BetaAdvisorResultBlock](api/beta.md)

?string stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

string text

"advisor\_result" type



[BetaAdvisorResultBlockParam](api/beta.md)

string text

"advisor\_result" type

?string stopReason



[BetaAdvisorTool20260301](api/beta.md)



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.



"advisor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"advisor\_20260301" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCacheControlEphemeral](api/beta.md) caching

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxTokens

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaAdvisorToolResultBlock](api/beta.md)

Content content

string toolUseID

"advisor\_tool\_result" type



[BetaAdvisorToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"advisor\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaAdvisorToolResultError](api/beta.md)

ErrorCode errorCode

"advisor\_tool\_result\_error" type



[BetaAdvisorToolResultErrorParam](api/beta.md)

ErrorCode errorCode

"advisor\_tool\_result\_error" type



[BetaAllThinkingTurns](api/beta.md)

"all" type



[BetaBase64ImageSource](api/beta.md)

string data

MediaType mediaType

"base64" type



[BetaBase64PDFSource](api/beta.md)

string data

"application/pdf" mediaType

"base64" type



[BetaBashCodeExecutionOutputBlock](api/beta.md)

string fileID

"bash\_code\_execution\_output" type



[BetaBashCodeExecutionOutputBlockParam](api/beta.md)

string fileID

"bash\_code\_execution\_output" type



[BetaBashCodeExecutionResultBlock](api/beta.md)

list<[BetaBashCodeExecutionOutputBlock](api/beta.md)> content

int returnCode

string stderr

string stdout

"bash\_code\_execution\_result" type



[BetaBashCodeExecutionResultBlockParam](api/beta.md)

list<[BetaBashCodeExecutionOutputBlockParam](api/beta.md)> content

int returnCode

string stderr

string stdout

"bash\_code\_execution\_result" type



[BetaBashCodeExecutionToolResultBlock](api/beta.md)

Content content

string toolUseID

"bash\_code\_execution\_tool\_result" type



[BetaBashCodeExecutionToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"bash\_code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaBashCodeExecutionToolResultError](api/beta.md)

ErrorCode errorCode

"bash\_code\_execution\_tool\_result\_error" type



[BetaBashCodeExecutionToolResultErrorParam](api/beta.md)

ErrorCode errorCode

"bash\_code\_execution\_tool\_result\_error" type



[BetaCacheControlEphemeral](api/beta.md)

"ephemeral" type



?TTL ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.



[BetaCacheCreation](api/beta.md)

int ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

int ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.



[BetaCacheMissMessagesChanged](api/beta.md)

int cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

"messages\_changed" type



[BetaCacheMissModelChanged](api/beta.md)

int cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

"model\_changed" type



[BetaCacheMissPreviousMessageNotFound](api/beta.md)

"previous\_message\_not\_found" type



[BetaCacheMissSystemChanged](api/beta.md)

int cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

"system\_changed" type



[BetaCacheMissToolsChanged](api/beta.md)

int cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

"tools\_changed" type



[BetaCacheMissUnavailable](api/beta.md)

"unavailable" type



[BetaCitationCharLocation](api/beta.md)

string citedText

int documentIndex

?string documentTitle

int endCharIndex

?string fileID

int startCharIndex

"char\_location" type



[BetaCitationCharLocationParam](api/beta.md)

string citedText

int documentIndex

?string documentTitle

int endCharIndex

int startCharIndex

"char\_location" type



[BetaCitationConfig](api/beta.md)

bool enabled



[BetaCitationContentBlockLocation](api/beta.md)



string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int documentIndex

?string documentTitle



int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

?string fileID

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

"content\_block\_location" type



[BetaCitationContentBlockLocationParam](api/beta.md)



string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int documentIndex

?string documentTitle



int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

"content\_block\_location" type



[BetaCitationPageLocation](api/beta.md)

string citedText

int documentIndex

?string documentTitle

int endPageNumber

?string fileID

int startPageNumber

"page\_location" type



[BetaCitationPageLocationParam](api/beta.md)

string citedText

int documentIndex

?string documentTitle

int endPageNumber

int startPageNumber

"page\_location" type



[BetaCitationSearchResultLocation](api/beta.md)



string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



int searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

string source

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

?string title

"search\_result\_location" type



[BetaCitationSearchResultLocationParam](api/beta.md)



string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



int searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

string source

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

?string title

"search\_result\_location" type



[BetaCitationWebSearchResultLocationParam](api/beta.md)

string citedText

string encryptedIndex

?string title

"web\_search\_result\_location" type

string url



[BetaCitationsConfigParam](api/beta.md)

?bool enabled



[BetaCitationsDelta](api/beta.md)

Citation citation

"citations\_delta" type



[BetaCitationsWebSearchResultLocation](api/beta.md)

string citedText

string encryptedIndex

?string title

"web\_search\_result\_location" type

string url



[BetaClearThinking20251015Edit](api/beta.md)

"clear\_thinking\_20251015" type

?Keep keep

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.



[BetaClearThinking20251015EditResponse](api/beta.md)

int clearedInputTokens

Number of input tokens cleared by this edit.

int clearedThinkingTurns

Number of thinking turns that were cleared.

"clear\_thinking\_20251015" type

The type of context management edit applied.



[BetaClearToolUses20250919Edit](api/beta.md)

"clear\_tool\_uses\_20250919" type

?[BetaInputTokensClearAtLeast](api/beta.md) clearAtLeast

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

?ClearToolInputs clearToolInputs

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

?list<string> excludeTools

Tool names whose uses are preserved from clearing

?[BetaToolUsesKeep](api/beta.md) keep

Number of tool uses to retain in the conversation

?Trigger trigger

Condition that triggers the context management strategy



[BetaClearToolUses20250919EditResponse](api/beta.md)

int clearedInputTokens

Number of input tokens cleared by this edit.

int clearedToolUses

Number of tool uses that were cleared.

"clear\_tool\_uses\_20250919" type

The type of context management edit applied.



[BetaCodeExecutionOutputBlock](api/beta.md)

string fileID

"code\_execution\_output" type



[BetaCodeExecutionOutputBlockParam](api/beta.md)

string fileID

"code\_execution\_output" type



[BetaCodeExecutionResultBlock](api/beta.md)

list<[BetaCodeExecutionOutputBlock](api/beta.md)> content

int returnCode

string stderr

string stdout

"code\_execution\_result" type



[BetaCodeExecutionResultBlockParam](api/beta.md)

list<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

int returnCode

string stderr

string stdout

"code\_execution\_result" type



[BetaCodeExecutionTool20250522](api/beta.md)



"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250522" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaCodeExecutionTool20250825](api/beta.md)



"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250825" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaCodeExecutionTool20260120](api/beta.md)



"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20260120" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaCodeExecutionToolResultBlock](api/beta.md)

[BetaCodeExecutionToolResultBlockContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

string toolUseID

"code\_execution\_tool\_result" type



[BetaCodeExecutionToolResultBlockContent](api/beta.md)

One of the following:



[BetaCodeExecutionToolResultError](api/beta.md)

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

"code\_execution\_tool\_result\_error" type



[BetaCodeExecutionResultBlock](api/beta.md)

list<[BetaCodeExecutionOutputBlock](api/beta.md)> content

int returnCode

string stderr

string stdout

"code\_execution\_result" type



[BetaEncryptedCodeExecutionResultBlock](api/beta.md)

list<[BetaCodeExecutionOutputBlock](api/beta.md)> content

string encryptedStdout

int returnCode

string stderr

"encrypted\_code\_execution\_result" type



[BetaCodeExecutionToolResultBlockParam](api/beta.md)

[BetaCodeExecutionToolResultBlockParamContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

string toolUseID

"code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaCodeExecutionToolResultBlockParamContent](api/beta.md)

One of the following:



[BetaCodeExecutionToolResultErrorParam](api/beta.md)

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

"code\_execution\_tool\_result\_error" type



[BetaCodeExecutionResultBlockParam](api/beta.md)

list<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

int returnCode

string stderr

string stdout

"code\_execution\_result" type



[BetaEncryptedCodeExecutionResultBlockParam](api/beta.md)

list<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

string encryptedStdout

int returnCode

string stderr

"encrypted\_code\_execution\_result" type



[BetaCodeExecutionToolResultError](api/beta.md)

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

"code\_execution\_tool\_result\_error" type



[BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"



[BetaCodeExecutionToolResultErrorParam](api/beta.md)

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

"code\_execution\_tool\_result\_error" type



[BetaCompact20260112Edit](api/beta.md)

"compact\_20260112" type

?string instructions

Additional instructions for summarization.

?bool pauseAfterCompaction

Whether to pause after compaction and return the compaction block to the user.

?[BetaInputTokensTrigger](api/beta.md) trigger

When to trigger compaction. Defaults to 150000 input tokens.



[BetaCompactionBlock](api/beta.md)

?string content

Summary of compacted content, or null if compaction failed

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

"compaction" type



[BetaCompactionBlockParam](api/beta.md)

"compaction" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?string content

Summary of previously compacted content, or null if compaction failed

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim



[BetaCompactionContentBlockDelta](api/beta.md)

?string content

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

"compaction\_delta" type



[BetaCompactionIterationUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

int cacheReadInputTokens

The number of input tokens read from the cache.

int inputTokens

The number of input tokens which were used.

int outputTokens

The number of output tokens which were used.

"compaction" type

Usage for a compaction iteration



[BetaContainer](api/beta.md)

string id

Identifier for the container used in this request

\Datetime expiresAt

The time at which the container will expire.

?list<[BetaSkill](api/beta.md)> skills

Skills loaded in the container



[BetaContainerParams](api/beta.md)

?string id

Container id

?list<[BetaSkillParams](api/beta.md)> skills

List of skills to load in the container



[BetaContainerUploadBlock](api/beta.md)

string fileID

"container\_upload" type



[BetaContainerUploadBlockParam](api/beta.md)

string fileID

"container\_upload" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaContentBlock](api/beta.md)

One of the following:



[BetaTextBlock](api/beta.md)



?list<[BetaTextCitation](api/beta.md)> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

string text

"text" type



[BetaThinkingBlock](api/beta.md)

string signature

string thinking

"thinking" type



[BetaRedactedThinkingBlock](api/beta.md)

string data

"redacted\_thinking" type



[BetaToolUseBlock](api/beta.md)

string id

array<string,mixed> input

string name

"tool\_use" type

?Caller caller

Tool invocation directly from the model.



[BetaServerToolUseBlock](api/beta.md)

string id

array<string,mixed> input

Name name

"server\_tool\_use" type

?Caller caller

Tool invocation directly from the model.



[BetaWebSearchToolResultBlock](api/beta.md)

[BetaWebSearchToolResultBlockContent](api/beta.md) content

string toolUseID

"web\_search\_tool\_result" type

?Caller caller

Tool invocation directly from the model.



[BetaWebFetchToolResultBlock](api/beta.md)

Content content

string toolUseID

"web\_fetch\_tool\_result" type

?Caller caller

Tool invocation directly from the model.



[BetaAdvisorToolResultBlock](api/beta.md)

Content content

string toolUseID

"advisor\_tool\_result" type



[BetaCodeExecutionToolResultBlock](api/beta.md)

[BetaCodeExecutionToolResultBlockContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

string toolUseID

"code\_execution\_tool\_result" type



[BetaBashCodeExecutionToolResultBlock](api/beta.md)

Content content

string toolUseID

"bash\_code\_execution\_tool\_result" type



[BetaTextEditorCodeExecutionToolResultBlock](api/beta.md)

Content content

string toolUseID

"text\_editor\_code\_execution\_tool\_result" type



[BetaToolSearchToolResultBlock](api/beta.md)

Content content

string toolUseID

"tool\_search\_tool\_result" type



[BetaMCPToolUseBlock](api/beta.md)

string id

array<string,mixed> input

string name

The name of the MCP tool

string serverName

The name of the MCP server

"mcp\_tool\_use" type



[BetaMCPToolResultBlock](api/beta.md)

Content content

bool isError

string toolUseID

"mcp\_tool\_result" type



[BetaContainerUploadBlock](api/beta.md)

string fileID

"container\_upload" type



[BetaCompactionBlock](api/beta.md)

?string content

Summary of compacted content, or null if compaction failed

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

"compaction" type



[BetaFallbackBlock](api/beta.md)

[BetaFallbackInfo](api/beta.md) from

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

[BetaFallbackInfo](api/beta.md) to

The fallback model producing the content that follows this block. Its `model` is always the canonical id.

"fallback" type



[BetaContentBlockParam](api/beta.md)

One of the following:



[BetaTextBlockParam](api/beta.md)

string text

"text" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?list<[BetaTextCitationParam](api/beta.md)> citations



[BetaImageBlockParam](api/beta.md)

Source source

"image" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaRequestDocumentBlock](api/beta.md)

Source source

"document" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

?string context

?string title



[BetaSearchResultBlockParam](api/beta.md)

list<[BetaTextBlockParam](api/beta.md)> content

string source

string title

"search\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations



[BetaThinkingBlockParam](api/beta.md)

string signature

string thinking

"thinking" type



[BetaRedactedThinkingBlockParam](api/beta.md)

string data

"redacted\_thinking" type



[BetaToolUseBlockParam](api/beta.md)

string id

array<string,mixed> input

string name

"tool\_use" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.



[BetaToolResultBlockParam](api/beta.md)

string toolUseID

"tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Content content

?bool isError



[BetaServerToolUseBlockParam](api/beta.md)

string id

array<string,mixed> input

Name name

"server\_tool\_use" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.



[BetaWebSearchToolResultBlockParam](api/beta.md)

[BetaWebSearchToolResultBlockParamContent](api/beta.md) content

string toolUseID

"web\_search\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.



[BetaWebFetchToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"web\_fetch\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.



[BetaAdvisorToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"advisor\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaCodeExecutionToolResultBlockParam](api/beta.md)

[BetaCodeExecutionToolResultBlockParamContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

string toolUseID

"code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaBashCodeExecutionToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"bash\_code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaTextEditorCodeExecutionToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"text\_editor\_code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaToolSearchToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"tool\_search\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaMCPToolUseBlockParam](api/beta.md)

string id

array<string,mixed> input

string name

string serverName

The name of the MCP server

"mcp\_tool\_use" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaRequestMCPToolResultBlockParam](api/beta.md)

string toolUseID

"mcp\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Content content

?bool isError



[BetaContainerUploadBlockParam](api/beta.md)

string fileID

"container\_upload" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaCompactionBlockParam](api/beta.md)

"compaction" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?string content

Summary of previously compacted content, or null if compaction failed

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim



[BetaMidConversationSystemBlockParam](api/beta.md)

list<[BetaTextBlockParam](api/beta.md)> content

System instruction text blocks.

"mid\_conv\_system" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaFallbackBlockParam](api/beta.md)

[BetaFallbackInfoParam](api/beta.md) from

Identifies one hop of a fallback transition.

[BetaFallbackInfoParam](api/beta.md) to

Identifies one hop of a fallback transition.

"fallback" type



[BetaContentBlockSource](api/beta.md)

Content content

"content" type



[BetaContentBlockSourceContent](api/beta.md)

One of the following:



[BetaTextBlockParam](api/beta.md)

string text

"text" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?list<[BetaTextCitationParam](api/beta.md)> citations



[BetaImageBlockParam](api/beta.md)

Source source

"image" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaContextManagementConfig](api/beta.md)

?list<Edit> edits

List of context management edits to apply



[BetaContextManagementResponse](api/beta.md)

list<AppliedEdit> appliedEdits

List of context management edits that were applied.



[BetaCountTokensContextManagementResponse](api/beta.md)

int originalInputTokens

The original token count before context management was applied



[BetaDiagnostics](api/beta.md)

?CacheMissReason cacheMissReason

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.



[BetaDiagnosticsParam](api/beta.md)

?string previousMessageID

The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.



[BetaDirectCaller](api/beta.md)

"direct" type



[BetaDocumentBlock](api/beta.md)

?[BetaCitationConfig](api/beta.md) citations

Citation configuration for the document

Source source

?string title

The title of the document

"document" type



[BetaEncryptedCodeExecutionResultBlock](api/beta.md)

list<[BetaCodeExecutionOutputBlock](api/beta.md)> content

string encryptedStdout

int returnCode

string stderr

"encrypted\_code\_execution\_result" type



[BetaEncryptedCodeExecutionResultBlockParam](api/beta.md)

list<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

string encryptedStdout

int returnCode

string stderr

"encrypted\_code\_execution\_result" type



[BetaFallbackBlock](api/beta.md)

[BetaFallbackInfo](api/beta.md) from

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

[BetaFallbackInfo](api/beta.md) to

The fallback model producing the content that follows this block. Its `model` is always the canonical id.

"fallback" type



[BetaFallbackBlockParam](api/beta.md)

[BetaFallbackInfoParam](api/beta.md) from

Identifies one hop of a fallback transition.

[BetaFallbackInfoParam](api/beta.md) to

Identifies one hop of a fallback transition.

"fallback" type



[BetaFallbackInfo](api/beta.md)



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.



[BetaFallbackInfoParam](api/beta.md)



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.



[BetaFallbackMessageIterationUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

int cacheReadInputTokens

The number of input tokens read from the cache.

int inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

int outputTokens

The number of output tokens which were used.

"fallback\_message" type

Usage for the fallback-model attempt that served the response



[BetaFallbackParam](api/beta.md)



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

?int maxTokens

?[BetaOutputConfig](api/beta.md) outputConfig

?Speed speed

?Thinking thinking



[BetaFileDocumentSource](api/beta.md)

string fileID

"file" type



[BetaFileImageSource](api/beta.md)

string fileID

"file" type



[BetaImageBlockParam](api/beta.md)

Source source

"image" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaInputJSONDelta](api/beta.md)

string partialJSON

"input\_json\_delta" type



[BetaInputTokensClearAtLeast](api/beta.md)

"input\_tokens" type

int value



[BetaInputTokensTrigger](api/beta.md)

"input\_tokens" type

int value



list<BetaIterationsUsageItem>

One of the following:



[BetaMessageIterationUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

int cacheReadInputTokens

The number of input tokens read from the cache.

int inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

int outputTokens

The number of output tokens which were used.

"message" type

Usage for a sampling iteration



[BetaCompactionIterationUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

int cacheReadInputTokens

The number of input tokens read from the cache.

int inputTokens

The number of input tokens which were used.

int outputTokens

The number of output tokens which were used.

"compaction" type

Usage for a compaction iteration



[BetaAdvisorMessageIterationUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

int cacheReadInputTokens

The number of input tokens read from the cache.

int inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

int outputTokens

The number of output tokens which were used.

"advisor\_message" type

Usage for an advisor sub-inference iteration



[BetaFallbackMessageIterationUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

int cacheReadInputTokens

The number of input tokens read from the cache.

int inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

int outputTokens

The number of output tokens which were used.

"fallback\_message" type

Usage for the fallback-model attempt that served the response



[BetaJSONOutputFormat](api/beta.md)

array<string,mixed> schema

The JSON schema of the format

"json\_schema" type



[BetaMCPToolConfig](api/beta.md)

?bool deferLoading

?bool enabled



[BetaMCPToolDefaultConfig](api/beta.md)

?bool deferLoading

?bool enabled



[BetaMCPToolResultBlock](api/beta.md)

Content content

bool isError

string toolUseID

"mcp\_tool\_result" type



[BetaMCPToolUseBlock](api/beta.md)

string id

array<string,mixed> input

string name

The name of the MCP tool

string serverName

The name of the MCP server

"mcp\_tool\_use" type



[BetaMCPToolUseBlockParam](api/beta.md)

string id

array<string,mixed> input

string name

string serverName

The name of the MCP server

"mcp\_tool\_use" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaMCPToolset](api/beta.md)

string mcpServerName

Name of the MCP server to configure tools for

"mcp\_toolset" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?array<string,[BetaMCPToolConfig](api/beta.md)> configs

Configuration overrides for specific tools, keyed by tool name

?[BetaMCPToolDefaultConfig](api/beta.md) defaultConfig

Default configuration applied to all tools from this server



[BetaMemoryTool20250818](api/beta.md)



"memory" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"memory\_20250818" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaMemoryTool20250818Command](api/beta.md)

One of the following:



[BetaMemoryTool20250818ViewCommand](api/beta.md)

"view" command

Command type identifier

string path

Path to directory or file to view

?list<int> viewRange

Optional line range for viewing specific lines



[BetaMemoryTool20250818CreateCommand](api/beta.md)

"create" command

Command type identifier

string fileText

Content to write to the file

string path

Path where the file should be created



[BetaMemoryTool20250818StrReplaceCommand](api/beta.md)

"str\_replace" command

Command type identifier

string newStr

Text to replace with

string oldStr

Text to search for and replace

string path

Path to the file where text should be replaced



[BetaMemoryTool20250818InsertCommand](api/beta.md)

"insert" command

Command type identifier

int insertLine

Line number where text should be inserted

string insertText

Text to insert at the specified line

string path

Path to the file where text should be inserted



[BetaMemoryTool20250818DeleteCommand](api/beta.md)

"delete" command

Command type identifier

string path

Path to the file or directory to delete



[BetaMemoryTool20250818RenameCommand](api/beta.md)

"rename" command

Command type identifier

string newPath

New path for the file or directory

string oldPath

Current path of the file or directory



[BetaMemoryTool20250818CreateCommand](api/beta.md)

"create" command

Command type identifier

string fileText

Content to write to the file

string path

Path where the file should be created



[BetaMemoryTool20250818DeleteCommand](api/beta.md)

"delete" command

Command type identifier

string path

Path to the file or directory to delete



[BetaMemoryTool20250818InsertCommand](api/beta.md)

"insert" command

Command type identifier

int insertLine

Line number where text should be inserted

string insertText

Text to insert at the specified line

string path

Path to the file where text should be inserted



[BetaMemoryTool20250818RenameCommand](api/beta.md)

"rename" command

Command type identifier

string newPath

New path for the file or directory

string oldPath

Current path of the file or directory



[BetaMemoryTool20250818StrReplaceCommand](api/beta.md)

"str\_replace" command

Command type identifier

string newStr

Text to replace with

string oldStr

Text to search for and replace

string path

Path to the file where text should be replaced



[BetaMemoryTool20250818ViewCommand](api/beta.md)

"view" command

Command type identifier

string path

Path to directory or file to view

?list<int> viewRange

Optional line range for viewing specific lines



[BetaMessage](api/beta.md)



string id

Unique object identifier.

The format and length of IDs may change over time.

?[BetaContainer](api/beta.md) container

Information about the container used in the request (for the code execution tool)



list<[BetaContentBlock](api/beta.md)> content

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



?[BetaContextManagementResponse](api/beta.md) contextManagement

Context management response.

Information about context management strategies applied during the request.

?[BetaDiagnostics](api/beta.md) diagnostics

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.



"assistant" role

Conversational role of the generated message.

This will always be `"assistant"`.

?[BetaRefusalStopDetails](api/beta.md) stopDetails

Structured information about a refusal.



?[BetaStopReason](api/beta.md) stopReason

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.



?string stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



"message" type

Object type.

For Messages, this is always `"message"`.



[BetaUsage](api/beta.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



[BetaMessageDeltaUsage](api/beta.md)

?int cacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

?int cacheReadInputTokens

The cumulative number of input tokens read from the cache.

?int inputTokens

The cumulative number of input tokens which were used.



?list<BetaIterationsUsageItem> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

int outputTokens

The cumulative number of output tokens which were used.



?[BetaOutputTokensDetails](api/beta.md) outputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.

?[BetaServerToolUsage](api/beta.md) serverToolUse

The number of server tool requests.



[BetaMessageIterationUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

int cacheReadInputTokens

The number of input tokens read from the cache.

int inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

int outputTokens

The number of output tokens which were used.

"message" type

Usage for a sampling iteration



[BetaMessageParam](api/beta.md)

Content content

Role role



[BetaMessageTokensCount](api/beta.md)

?[BetaCountTokensContextManagementResponse](api/beta.md) contextManagement

Information about context management applied to the message.

int inputTokens

The total number of tokens across the provided list of messages, system prompt, and tools.



[BetaMetadata](api/beta.md)



?string userID

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.



[BetaMidConversationSystemBlockParam](api/beta.md)

list<[BetaTextBlockParam](api/beta.md)> content

System instruction text blocks.

"mid\_conv\_system" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaOutputConfig](api/beta.md)

?Effort effort

All possible effort levels.

?[BetaJSONOutputFormat](api/beta.md) format

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

?[BetaTokenTaskBudget](api/beta.md) taskBudget

User-configurable total token budget across contexts.



[BetaOutputTokensDetails](api/beta.md)



int thinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.



[BetaPlainTextSource](api/beta.md)

string data

"text/plain" mediaType

"text" type



[BetaRawContentBlockDelta](api/beta.md)

One of the following:



[BetaTextDelta](api/beta.md)

string text

"text\_delta" type



[BetaInputJSONDelta](api/beta.md)

string partialJSON

"input\_json\_delta" type



[BetaCitationsDelta](api/beta.md)

Citation citation

"citations\_delta" type



[BetaThinkingDelta](api/beta.md)

?int estimatedTokens

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

string thinking

"thinking\_delta" type



[BetaSignatureDelta](api/beta.md)

string signature

"signature\_delta" type



[BetaCompactionContentBlockDelta](api/beta.md)

?string content

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

"compaction\_delta" type



[BetaRawContentBlockDeltaEvent](api/beta.md)

[BetaRawContentBlockDelta](api/beta.md) delta

int index

"content\_block\_delta" type



[BetaRawContentBlockStartEvent](api/beta.md)

ContentBlock contentBlock

Response model for a file uploaded to the container.

int index

"content\_block\_start" type



[BetaRawContentBlockStopEvent](api/beta.md)

int index

"content\_block\_stop" type



[BetaRawMessageDeltaEvent](api/beta.md)

?[BetaContextManagementResponse](api/beta.md) contextManagement

Information about context management strategies applied during the request

Delta delta

"message\_delta" type



[BetaMessageDeltaUsage](api/beta.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



[BetaRawMessageStartEvent](api/beta.md)

[BetaMessage](api/beta.md) message

"message\_start" type



[BetaRawMessageStopEvent](api/beta.md)

"message\_stop" type



[BetaRawMessageStreamEvent](api/beta.md)

One of the following:



[BetaRawMessageStartEvent](api/beta.md)

[BetaMessage](api/beta.md) message

"message\_start" type



[BetaRawMessageDeltaEvent](api/beta.md)

?[BetaContextManagementResponse](api/beta.md) contextManagement

Information about context management strategies applied during the request

Delta delta

"message\_delta" type



[BetaMessageDeltaUsage](api/beta.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



[BetaRawMessageStopEvent](api/beta.md)

"message\_stop" type



[BetaRawContentBlockStartEvent](api/beta.md)

ContentBlock contentBlock

Response model for a file uploaded to the container.

int index

"content\_block\_start" type



[BetaRawContentBlockDeltaEvent](api/beta.md)

[BetaRawContentBlockDelta](api/beta.md) delta

int index

"content\_block\_delta" type



[BetaRawContentBlockStopEvent](api/beta.md)

int index

"content\_block\_stop" type



[BetaRedactedThinkingBlock](api/beta.md)

string data

"redacted\_thinking" type



[BetaRedactedThinkingBlockParam](api/beta.md)

string data

"redacted\_thinking" type



[BetaRefusalStopDetails](api/beta.md)



?Category category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.



?string explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



?string fallbackCreditToken

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

?bool fallbackHasPrefillClaim

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

?string recommendedModel

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

"refusal" type



[BetaRequestDocumentBlock](api/beta.md)

Source source

"document" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

?string context

?string title



[BetaRequestMCPServerToolConfiguration](api/beta.md)

?list<string> allowedTools

?bool enabled



[BetaRequestMCPServerURLDefinition](api/beta.md)

string name

"url" type

string url

?string authorizationToken

?[BetaRequestMCPServerToolConfiguration](api/beta.md) toolConfiguration



[BetaRequestMCPToolResultBlockParam](api/beta.md)

string toolUseID

"mcp\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Content content

?bool isError



[BetaSearchResultBlockParam](api/beta.md)

list<[BetaTextBlockParam](api/beta.md)> content

string source

string title

"search\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations



[BetaServerToolCaller](api/beta.md)

string toolID

"code\_execution\_20250825" type



[BetaServerToolCaller20260120](api/beta.md)

string toolID

"code\_execution\_20260120" type



[BetaServerToolUsage](api/beta.md)

int webFetchRequests

The number of web fetch tool requests.

int webSearchRequests

The number of web search tool requests.



[BetaServerToolUseBlock](api/beta.md)

string id

array<string,mixed> input

Name name

"server\_tool\_use" type

?Caller caller

Tool invocation directly from the model.



[BetaServerToolUseBlockParam](api/beta.md)

string id

array<string,mixed> input

Name name

"server\_tool\_use" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.



[BetaSignatureDelta](api/beta.md)

string signature

"signature\_delta" type



[BetaSkill](api/beta.md)

string skillID

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

string version

Skill version or 'latest' for most recent version



[BetaSkillParams](api/beta.md)

string skillID

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

?string version

Skill version or 'latest' for most recent version



[BetaStopReason](api/beta.md)

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"



[BetaTextBlock](api/beta.md)



?list<[BetaTextCitation](api/beta.md)> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

string text

"text" type



[BetaTextBlockParam](api/beta.md)

string text

"text" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?list<[BetaTextCitationParam](api/beta.md)> citations



[BetaTextCitation](api/beta.md)

One of the following:



[BetaCitationCharLocation](api/beta.md)

string citedText

int documentIndex

?string documentTitle

int endCharIndex

?string fileID

int startCharIndex

"char\_location" type



[BetaCitationPageLocation](api/beta.md)

string citedText

int documentIndex

?string documentTitle

int endPageNumber

?string fileID

int startPageNumber

"page\_location" type



[BetaCitationContentBlockLocation](api/beta.md)



string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int documentIndex

?string documentTitle



int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

?string fileID

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

"content\_block\_location" type



[BetaCitationsWebSearchResultLocation](api/beta.md)

string citedText

string encryptedIndex

?string title

"web\_search\_result\_location" type

string url



[BetaCitationSearchResultLocation](api/beta.md)



string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



int searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

string source

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

?string title

"search\_result\_location" type



[BetaTextCitationParam](api/beta.md)

One of the following:



[BetaCitationCharLocationParam](api/beta.md)

string citedText

int documentIndex

?string documentTitle

int endCharIndex

int startCharIndex

"char\_location" type



[BetaCitationPageLocationParam](api/beta.md)

string citedText

int documentIndex

?string documentTitle

int endPageNumber

int startPageNumber

"page\_location" type



[BetaCitationContentBlockLocationParam](api/beta.md)



string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int documentIndex

?string documentTitle



int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

"content\_block\_location" type



[BetaCitationWebSearchResultLocationParam](api/beta.md)

string citedText

string encryptedIndex

?string title

"web\_search\_result\_location" type

string url



[BetaCitationSearchResultLocationParam](api/beta.md)



string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



int searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

string source

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

?string title

"search\_result\_location" type



[BetaTextDelta](api/beta.md)

string text

"text\_delta" type



[BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md)

bool isFileUpdate

"text\_editor\_code\_execution\_create\_result" type



[BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta.md)

bool isFileUpdate

"text\_editor\_code\_execution\_create\_result" type



[BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md)

?list<string> lines

?int newLines

?int newStart

?int oldLines

?int oldStart

"text\_editor\_code\_execution\_str\_replace\_result" type



[BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta.md)

"text\_editor\_code\_execution\_str\_replace\_result" type

?list<string> lines

?int newLines

?int newStart

?int oldLines

?int oldStart



[BetaTextEditorCodeExecutionToolResultBlock](api/beta.md)

Content content

string toolUseID

"text\_editor\_code\_execution\_tool\_result" type



[BetaTextEditorCodeExecutionToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"text\_editor\_code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaTextEditorCodeExecutionToolResultError](api/beta.md)

ErrorCode errorCode

?string errorMessage

"text\_editor\_code\_execution\_tool\_result\_error" type



[BetaTextEditorCodeExecutionToolResultErrorParam](api/beta.md)

ErrorCode errorCode

"text\_editor\_code\_execution\_tool\_result\_error" type

?string errorMessage



[BetaTextEditorCodeExecutionViewResultBlock](api/beta.md)

string content

FileType fileType

?int numLines

?int startLine

?int totalLines

"text\_editor\_code\_execution\_view\_result" type



[BetaTextEditorCodeExecutionViewResultBlockParam](api/beta.md)

string content

FileType fileType

"text\_editor\_code\_execution\_view\_result" type

?int numLines

?int startLine

?int totalLines



[BetaThinkingBlock](api/beta.md)

string signature

string thinking

"thinking" type



[BetaThinkingBlockParam](api/beta.md)

string signature

string thinking

"thinking" type



[BetaThinkingConfigAdaptive](api/beta.md)

"adaptive" type

?Display display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.



[BetaThinkingConfigDisabled](api/beta.md)

"disabled" type



[BetaThinkingConfigEnabled](api/beta.md)



int budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

"enabled" type

?Display display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.



[BetaThinkingConfigParam](api/beta.md)

One of the following:



[BetaThinkingConfigEnabled](api/beta.md)



int budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

"enabled" type

?Display display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.



[BetaThinkingConfigDisabled](api/beta.md)

"disabled" type



[BetaThinkingConfigAdaptive](api/beta.md)

"adaptive" type

?Display display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.



[BetaThinkingDelta](api/beta.md)

?int estimatedTokens

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

string thinking

"thinking\_delta" type



[BetaThinkingTurns](api/beta.md)

"thinking\_turns" type

int value



[BetaTokenTaskBudget](api/beta.md)

int total

Total token budget across all contexts in the session.

"tokens" type

The budget type. Currently only 'tokens' is supported.

?int remaining

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



[BetaTool](api/beta.md)



InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.



string name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



?string description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

?bool eagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

?Type type



[BetaToolBash20241022](api/beta.md)



"bash" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"bash\_20241022" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolBash20250124](api/beta.md)



"bash" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"bash\_20250124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolChoice](api/beta.md)

One of the following:



[BetaToolChoiceAuto](api/beta.md)

"auto" type



?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



[BetaToolChoiceAny](api/beta.md)

"any" type



?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



[BetaToolChoiceTool](api/beta.md)

string name

The name of the tool to use.

"tool" type



?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



[BetaToolChoiceNone](api/beta.md)

"none" type



[BetaToolChoiceAny](api/beta.md)

"any" type



?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



[BetaToolChoiceAuto](api/beta.md)

"auto" type



?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



[BetaToolChoiceNone](api/beta.md)

"none" type



[BetaToolChoiceTool](api/beta.md)

string name

The name of the tool to use.

"tool" type



?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



[BetaToolComputerUse20241022](api/beta.md)

int displayHeightPx

The height of the display in pixels.

int displayWidthPx

The width of the display in pixels.



"computer" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"computer\_20241022" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int displayNumber

The X11 display number (e.g. 0, 1) for the display.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolComputerUse20250124](api/beta.md)

int displayHeightPx

The height of the display in pixels.

int displayWidthPx

The width of the display in pixels.



"computer" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"computer\_20250124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int displayNumber

The X11 display number (e.g. 0, 1) for the display.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolComputerUse20251124](api/beta.md)

int displayHeightPx

The height of the display in pixels.

int displayWidthPx

The width of the display in pixels.



"computer" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"computer\_20251124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int displayNumber

The X11 display number (e.g. 0, 1) for the display.

?bool enableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolReferenceBlock](api/beta.md)

string toolName

"tool\_reference" type



[BetaToolReferenceBlockParam](api/beta.md)

string toolName

"tool\_reference" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaToolResultBlockParam](api/beta.md)

string toolUseID

"tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Content content

?bool isError



[BetaToolSearchToolBm25\_20251119](api/beta.md)



"tool\_search\_tool\_bm25" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolSearchToolRegex20251119](api/beta.md)



"tool\_search\_tool\_regex" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolSearchToolResultBlock](api/beta.md)

Content content

string toolUseID

"tool\_search\_tool\_result" type



[BetaToolSearchToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"tool\_search\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaToolSearchToolResultError](api/beta.md)

ErrorCode errorCode

?string errorMessage

"tool\_search\_tool\_result\_error" type



[BetaToolSearchToolResultErrorParam](api/beta.md)

ErrorCode errorCode

"tool\_search\_tool\_result\_error" type

?string errorMessage



[BetaToolSearchToolSearchResultBlock](api/beta.md)

list<[BetaToolReferenceBlock](api/beta.md)> toolReferences

"tool\_search\_tool\_search\_result" type



[BetaToolSearchToolSearchResultBlockParam](api/beta.md)

list<[BetaToolReferenceBlockParam](api/beta.md)> toolReferences

"tool\_search\_tool\_search\_result" type



[BetaToolTextEditor20241022](api/beta.md)



"str\_replace\_editor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20241022" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolTextEditor20250124](api/beta.md)



"str\_replace\_editor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolTextEditor20250429](api/beta.md)



"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250429" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolTextEditor20250728](api/beta.md)



"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250728" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?int maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolUnion](api/beta.md)

One of the following:



[BetaTool](api/beta.md)



InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.



string name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



?string description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

?bool eagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

?Type type



[BetaToolBash20241022](api/beta.md)



"bash" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"bash\_20241022" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolBash20250124](api/beta.md)



"bash" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"bash\_20250124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaCodeExecutionTool20250522](api/beta.md)



"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250522" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaCodeExecutionTool20250825](api/beta.md)



"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250825" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaCodeExecutionTool20260120](api/beta.md)



"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20260120" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolComputerUse20241022](api/beta.md)

int displayHeightPx

The height of the display in pixels.

int displayWidthPx

The width of the display in pixels.



"computer" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"computer\_20241022" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int displayNumber

The X11 display number (e.g. 0, 1) for the display.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaMemoryTool20250818](api/beta.md)



"memory" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"memory\_20250818" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolComputerUse20250124](api/beta.md)

int displayHeightPx

The height of the display in pixels.

int displayWidthPx

The width of the display in pixels.



"computer" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"computer\_20250124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int displayNumber

The X11 display number (e.g. 0, 1) for the display.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolTextEditor20241022](api/beta.md)



"str\_replace\_editor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20241022" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolComputerUse20251124](api/beta.md)

int displayHeightPx

The height of the display in pixels.

int displayWidthPx

The width of the display in pixels.



"computer" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"computer\_20251124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int displayNumber

The X11 display number (e.g. 0, 1) for the display.

?bool enableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolTextEditor20250124](api/beta.md)



"str\_replace\_editor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolTextEditor20250429](api/beta.md)



"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250429" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolTextEditor20250728](api/beta.md)



"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250728" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?int maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaWebSearchTool20250305](api/beta.md)



"web\_search" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_search\_20250305" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

?list<string> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[BetaUserLocation](api/beta.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.



[BetaWebFetchTool20250910](api/beta.md)



"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20250910" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaWebSearchTool20260209](api/beta.md)



"web\_search" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_search\_20260209" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

?list<string> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[BetaUserLocation](api/beta.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.



[BetaWebFetchTool20260209](api/beta.md)



"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20260209" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaWebFetchTool20260309](api/beta.md)



"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20260309" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?bool useCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



[BetaAdvisorTool20260301](api/beta.md)



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.



"advisor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"advisor\_20260301" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCacheControlEphemeral](api/beta.md) caching

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxTokens

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolSearchToolBm25\_20251119](api/beta.md)



"tool\_search\_tool\_bm25" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolSearchToolRegex20251119](api/beta.md)



"tool\_search\_tool\_regex" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaMCPToolset](api/beta.md)

string mcpServerName

Name of the MCP server to configure tools for

"mcp\_toolset" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?array<string,[BetaMCPToolConfig](api/beta.md)> configs

Configuration overrides for specific tools, keyed by tool name

?[BetaMCPToolDefaultConfig](api/beta.md) defaultConfig

Default configuration applied to all tools from this server



[BetaToolUseBlock](api/beta.md)

string id

array<string,mixed> input

string name

"tool\_use" type

?Caller caller

Tool invocation directly from the model.



[BetaToolUseBlockParam](api/beta.md)

string id

array<string,mixed> input

string name

"tool\_use" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.



[BetaToolUsesKeep](api/beta.md)

"tool\_uses" type

int value



[BetaToolUsesTrigger](api/beta.md)

"tool\_uses" type

int value



[BetaURLImageSource](api/beta.md)

"url" type

string url



[BetaURLPDFSource](api/beta.md)

"url" type

string url



[BetaUsage](api/beta.md)

?[BetaCacheCreation](api/beta.md) cacheCreation

Breakdown of cached tokens by TTL

?int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

?int cacheReadInputTokens

The number of input tokens read from the cache.

?string inferenceGeo

The geographic region where inference was performed for this request.

int inputTokens

The number of input tokens which were used.



?list<BetaIterationsUsageItem> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

int outputTokens

The number of output tokens which were used.



?[BetaOutputTokensDetails](api/beta.md) outputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.

?[BetaServerToolUsage](api/beta.md) serverToolUse

The number of server tool requests.

?ServiceTier serviceTier

If the request used the priority, standard, or batch tier.

?Speed speed

The inference speed mode used for this request.



[BetaUserLocation](api/beta.md)

"approximate" type

?string city

The city of the user.

?string country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

?string region

The region of the user.

?string timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



[BetaWebFetchBlock](api/beta.md)

[BetaDocumentBlock](api/beta.md) content

?string retrievedAt

ISO 8601 timestamp when the content was retrieved

"web\_fetch\_result" type

string url

Fetched content URL



[BetaWebFetchBlockParam](api/beta.md)

[BetaRequestDocumentBlock](api/beta.md) content

"web\_fetch\_result" type

string url

Fetched content URL

?string retrievedAt

ISO 8601 timestamp when the content was retrieved



[BetaWebFetchTool20250910](api/beta.md)



"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20250910" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaWebFetchTool20260209](api/beta.md)



"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20260209" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaWebFetchTool20260309](api/beta.md)



"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20260309" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?bool useCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



[BetaWebFetchToolResultBlock](api/beta.md)

Content content

string toolUseID

"web\_fetch\_tool\_result" type

?Caller caller

Tool invocation directly from the model.



[BetaWebFetchToolResultBlockParam](api/beta.md)

Content content

string toolUseID

"web\_fetch\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.



[BetaWebFetchToolResultErrorBlock](api/beta.md)

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

"web\_fetch\_tool\_result\_error" type



[BetaWebFetchToolResultErrorBlockParam](api/beta.md)

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

"web\_fetch\_tool\_result\_error" type



[BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"



[BetaWebSearchResultBlock](api/beta.md)

string encryptedContent

?string pageAge

string title

"web\_search\_result" type

string url



[BetaWebSearchResultBlockParam](api/beta.md)

string encryptedContent

string title

"web\_search\_result" type

string url

?string pageAge



[BetaWebSearchTool20250305](api/beta.md)



"web\_search" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_search\_20250305" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

?list<string> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[BetaUserLocation](api/beta.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.



[BetaWebSearchTool20260209](api/beta.md)



"web\_search" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_search\_20260209" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

?list<string> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[BetaUserLocation](api/beta.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.



[BetaWebSearchToolRequestError](api/beta.md)

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

"web\_search\_tool\_result\_error" type



[BetaWebSearchToolResultBlock](api/beta.md)

[BetaWebSearchToolResultBlockContent](api/beta.md) content

string toolUseID

"web\_search\_tool\_result" type

?Caller caller

Tool invocation directly from the model.



[BetaWebSearchToolResultBlockContent](api/beta.md)

One of the following:



[BetaWebSearchToolResultError](api/beta.md)

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

"web\_search\_tool\_result\_error" type



list<[BetaWebSearchResultBlock](api/beta.md)>

string encryptedContent

?string pageAge

string title

"web\_search\_result" type

string url



[BetaWebSearchToolResultBlockParam](api/beta.md)

[BetaWebSearchToolResultBlockParamContent](api/beta.md) content

string toolUseID

"web\_search\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.



[BetaWebSearchToolResultBlockParamContent](api/beta.md)

One of the following:



list<[BetaWebSearchResultBlockParam](api/beta.md)>

string encryptedContent

string title

"web\_search\_result" type

string url

?string pageAge



[BetaWebSearchToolRequestError](api/beta.md)

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

"web\_search\_tool\_result\_error" type



[BetaWebSearchToolResultError](api/beta.md)

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

"web\_search\_tool\_result\_error" type



[BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

#### MessagesBatches

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



[DeletedMessageBatch](api/beta.md)

string id

ID of the Message Batch.



"message\_batch\_deleted" type

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.



[MessageBatch](api/beta.md)



string id

Unique object identifier.

The format and length of IDs may change over time.

?\Datetime archivedAt

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

?\Datetime cancelInitiatedAt

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

\Datetime createdAt

RFC 3339 datetime string representing the time at which the Message Batch was created.



?\Datetime endedAt

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

\Datetime expiresAt

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

ProcessingStatus processingStatus

Processing status of the Message Batch.



[MessageBatchRequestCounts](api/beta.md) requestCounts

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.



?string resultsURL

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.



"message\_batch" type

Object type.

For Message Batches, this is always `"message_batch"`.



[MessageBatchCanceledResult](api/beta.md)

"canceled" type



[MessageBatchErroredResult](api/beta.md)

[BetaErrorResponse](api/beta.md) error

"errored" type



[MessageBatchExpiredResult](api/beta.md)

"expired" type



[MessageBatchIndividualResponse](api/beta.md)



string customID

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.



[MessageBatchResult](api/beta.md) result

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.



[MessageBatchRequestCounts](api/beta.md)



int canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



int errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



int expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

int processing

Number of requests in the Message Batch that are processing.



int succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



[MessageBatchResult](api/beta.md)

One of the following:



[MessageBatchSucceededResult](api/beta.md)

[BetaMessage](api/beta.md) message

"succeeded" type



[MessageBatchErroredResult](api/beta.md)

[BetaErrorResponse](api/beta.md) error

"errored" type



[MessageBatchCanceledResult](api/beta.md)

"canceled" type



[MessageBatchExpiredResult](api/beta.md)

"expired" type



[MessageBatchSucceededResult](api/beta.md)

[BetaMessage](api/beta.md) message

"succeeded" type

---

*Copyright © Anthropic. All rights reserved.*
