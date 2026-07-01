# Messages

Copy page



PHP

# Messages

##### [Create a Message](api/beta/messages/create.md)

$client->beta->messages->create(int maxTokens, list<[BetaMessageParam](api/beta/messages.md)> messages, Model model, ?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl, ?[Container](api/beta/messages/create.md) container, ?[BetaContextManagementConfig](api/beta/messages.md) contextManagement, ?[BetaDiagnosticsParam](api/beta/messages.md) diagnostics, ?string fallbackCreditToken, ?list<[BetaFallbackParam](api/beta/messages.md)> fallbacks, ?string inferenceGeo, ?list<[BetaRequestMCPServerURLDefinition](api/beta/messages.md)> mcpServers, ?[BetaMetadata](api/beta/messages.md) metadata, ?[BetaOutputConfig](api/beta/messages.md) outputConfig, ?[BetaJSONOutputFormat](api/beta/messages.md) outputFormat, ?[ServiceTier](api/beta/messages/create.md) serviceTier, ?[Speed](api/beta/messages/create.md) speed, ?list<string> stopSequences, ?[System](api/beta/messages/create.md) system, ?float temperature, ?[BetaThinkingConfigParam](api/beta/messages.md) thinking, ?[BetaToolChoice](api/beta/messages.md) toolChoice, ?list<[BetaToolUnion](api/beta/messages.md)> tools, ?int topK, ?float topP, ?list<AnthropicBeta> betas, ?string userProfileID): [BetaMessage](api/beta/messages.md)

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

$client->beta->messages->countTokens(list<[BetaMessageParam](api/beta/messages.md)> messages, Model model, ?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl, ?[BetaContextManagementConfig](api/beta/messages.md) contextManagement, ?list<[BetaRequestMCPServerURLDefinition](api/beta/messages.md)> mcpServers, ?[BetaOutputConfig](api/beta/messages.md) outputConfig, ?[BetaJSONOutputFormat](api/beta/messages.md) outputFormat, ?[Speed](api/beta/messages/count_tokens.md) speed, ?[System](api/beta/messages/count_tokens.md) system, ?[BetaThinkingConfigParam](api/beta/messages.md) thinking, ?[BetaToolChoice](api/beta/messages.md) toolChoice, ?list<Tool> tools, ?list<AnthropicBeta> betas, ?string userProfileID): [BetaMessageTokensCount](api/beta/messages.md)

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse



[BetaAdvisorMessageIterationUsage](api/beta/messages.md)

?[BetaCacheCreation](api/beta/messages.md) cacheCreation

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

[BetaAdvisorRedactedResultBlock](api/beta/messages.md)

string encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

?string stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

"advisor\_redacted\_result" type



[BetaAdvisorRedactedResultBlockParam](api/beta/messages.md)

string encryptedContent

Opaque blob produced by a prior response; must be round-tripped verbatim.

"advisor\_redacted\_result" type

?string stopReason



[BetaAdvisorResultBlock](api/beta/messages.md)

?string stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

string text

"advisor\_result" type



[BetaAdvisorResultBlockParam](api/beta/messages.md)

string text

"advisor\_result" type

?string stopReason



[BetaAdvisorTool20260301](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCacheControlEphemeral](api/beta/messages.md) caching

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

[BetaAdvisorToolResultBlock](api/beta/messages.md)

Content content

string toolUseID

"advisor\_tool\_result" type



[BetaAdvisorToolResultBlockParam](api/beta/messages.md)

Content content

string toolUseID

"advisor\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaAdvisorToolResultError](api/beta/messages.md)

ErrorCode errorCode

"advisor\_tool\_result\_error" type



[BetaAdvisorToolResultErrorParam](api/beta/messages.md)

ErrorCode errorCode

"advisor\_tool\_result\_error" type



[BetaAllThinkingTurns](api/beta/messages.md)

"all" type



[BetaBase64ImageSource](api/beta/messages.md)

string data

MediaType mediaType

"base64" type



[BetaBase64PDFSource](api/beta/messages.md)

string data

"application/pdf" mediaType

"base64" type



[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)

string fileID

"bash\_code\_execution\_output" type



[BetaBashCodeExecutionOutputBlockParam](api/beta/messages.md)

string fileID

"bash\_code\_execution\_output" type



[BetaBashCodeExecutionResultBlock](api/beta/messages.md)

list<[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)> content

int returnCode

string stderr

string stdout

"bash\_code\_execution\_result" type



[BetaBashCodeExecutionResultBlockParam](api/beta/messages.md)

list<[BetaBashCodeExecutionOutputBlockParam](api/beta/messages.md)> content

int returnCode

string stderr

string stdout

"bash\_code\_execution\_result" type



[BetaBashCodeExecutionToolResultBlock](api/beta/messages.md)

Content content

string toolUseID

"bash\_code\_execution\_tool\_result" type



[BetaBashCodeExecutionToolResultBlockParam](api/beta/messages.md)

Content content

string toolUseID

"bash\_code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaBashCodeExecutionToolResultError](api/beta/messages.md)

ErrorCode errorCode

"bash\_code\_execution\_tool\_result\_error" type



[BetaBashCodeExecutionToolResultErrorParam](api/beta/messages.md)

ErrorCode errorCode

"bash\_code\_execution\_tool\_result\_error" type



[BetaCacheControlEphemeral](api/beta/messages.md)

"ephemeral" type



?TTL ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.



[BetaCacheCreation](api/beta/messages.md)

int ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

int ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.



[BetaCacheMissMessagesChanged](api/beta/messages.md)

int cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

"messages\_changed" type



[BetaCacheMissModelChanged](api/beta/messages.md)

int cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

"model\_changed" type



[BetaCacheMissPreviousMessageNotFound](api/beta/messages.md)

"previous\_message\_not\_found" type



[BetaCacheMissSystemChanged](api/beta/messages.md)

int cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

"system\_changed" type



[BetaCacheMissToolsChanged](api/beta/messages.md)

int cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

"tools\_changed" type



[BetaCacheMissUnavailable](api/beta/messages.md)

"unavailable" type



[BetaCitationCharLocation](api/beta/messages.md)

string citedText

int documentIndex

?string documentTitle

int endCharIndex

?string fileID

int startCharIndex

"char\_location" type



[BetaCitationCharLocationParam](api/beta/messages.md)

string citedText

int documentIndex

?string documentTitle

int endCharIndex

int startCharIndex

"char\_location" type



[BetaCitationConfig](api/beta/messages.md)

bool enabled



[BetaCitationContentBlockLocation](api/beta/messages.md)

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

[BetaCitationContentBlockLocationParam](api/beta/messages.md)

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

[BetaCitationPageLocation](api/beta/messages.md)

string citedText

int documentIndex

?string documentTitle

int endPageNumber

?string fileID

int startPageNumber

"page\_location" type



[BetaCitationPageLocationParam](api/beta/messages.md)

string citedText

int documentIndex

?string documentTitle

int endPageNumber

int startPageNumber

"page\_location" type



[BetaCitationSearchResultLocation](api/beta/messages.md)

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

[BetaCitationSearchResultLocationParam](api/beta/messages.md)

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

[BetaCitationWebSearchResultLocationParam](api/beta/messages.md)

string citedText

string encryptedIndex

?string title

"web\_search\_result\_location" type

string url



[BetaCitationsConfigParam](api/beta/messages.md)

?bool enabled



[BetaCitationsDelta](api/beta/messages.md)

Citation citation

"citations\_delta" type



[BetaCitationsWebSearchResultLocation](api/beta/messages.md)

string citedText

string encryptedIndex

?string title

"web\_search\_result\_location" type

string url



[BetaClearThinking20251015Edit](api/beta/messages.md)

"clear\_thinking\_20251015" type

?Keep keep

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.



[BetaClearThinking20251015EditResponse](api/beta/messages.md)

int clearedInputTokens

Number of input tokens cleared by this edit.

int clearedThinkingTurns

Number of thinking turns that were cleared.

"clear\_thinking\_20251015" type

The type of context management edit applied.



[BetaClearToolUses20250919Edit](api/beta/messages.md)

"clear\_tool\_uses\_20250919" type

?[BetaInputTokensClearAtLeast](api/beta/messages.md) clearAtLeast

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

?ClearToolInputs clearToolInputs

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

?list<string> excludeTools

Tool names whose uses are preserved from clearing

?[BetaToolUsesKeep](api/beta/messages.md) keep

Number of tool uses to retain in the conversation

?Trigger trigger

Condition that triggers the context management strategy



[BetaClearToolUses20250919EditResponse](api/beta/messages.md)

int clearedInputTokens

Number of input tokens cleared by this edit.

int clearedToolUses

Number of tool uses that were cleared.

"clear\_tool\_uses\_20250919" type

The type of context management edit applied.



[BetaCodeExecutionOutputBlock](api/beta/messages.md)

string fileID

"code\_execution\_output" type



[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)

string fileID

"code\_execution\_output" type



[BetaCodeExecutionResultBlock](api/beta/messages.md)

list<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

int returnCode

string stderr

string stdout

"code\_execution\_result" type



[BetaCodeExecutionResultBlockParam](api/beta/messages.md)

list<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)> content

int returnCode

string stderr

string stdout

"code\_execution\_result" type



[BetaCodeExecutionTool20250522](api/beta/messages.md)



"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250522" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaCodeExecutionTool20250825](api/beta/messages.md)



"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250825" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaCodeExecutionTool20260120](api/beta/messages.md)



"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20260120" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaCodeExecutionTool20260521](api/beta/messages.md)



"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20260521" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaCodeExecutionToolResultBlock](api/beta/messages.md)

[BetaCodeExecutionToolResultBlockContent](api/beta/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

string toolUseID

"code\_execution\_tool\_result" type



[BetaCodeExecutionToolResultBlockContent](api/beta/messages.md)

One of the following:



[BetaCodeExecutionToolResultError](api/beta/messages.md)

[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

"code\_execution\_tool\_result\_error" type



[BetaCodeExecutionResultBlock](api/beta/messages.md)

list<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

int returnCode

string stderr

string stdout

"code\_execution\_result" type



[BetaEncryptedCodeExecutionResultBlock](api/beta/messages.md)

list<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

string encryptedStdout

int returnCode

string stderr

"encrypted\_code\_execution\_result" type



[BetaCodeExecutionToolResultBlockParam](api/beta/messages.md)

[BetaCodeExecutionToolResultBlockParamContent](api/beta/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

string toolUseID

"code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaCodeExecutionToolResultBlockParamContent](api/beta/messages.md)

One of the following:



[BetaCodeExecutionToolResultErrorParam](api/beta/messages.md)

[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

"code\_execution\_tool\_result\_error" type



[BetaCodeExecutionResultBlockParam](api/beta/messages.md)

list<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)> content

int returnCode

string stderr

string stdout

"code\_execution\_result" type



[BetaEncryptedCodeExecutionResultBlockParam](api/beta/messages.md)

list<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)> content

string encryptedStdout

int returnCode

string stderr

"encrypted\_code\_execution\_result" type



[BetaCodeExecutionToolResultError](api/beta/messages.md)

[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

"code\_execution\_tool\_result\_error" type



[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"



[BetaCodeExecutionToolResultErrorParam](api/beta/messages.md)

[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

"code\_execution\_tool\_result\_error" type



[BetaCompact20260112Edit](api/beta/messages.md)

"compact\_20260112" type

?string instructions

Additional instructions for summarization.

?bool pauseAfterCompaction

Whether to pause after compaction and return the compaction block to the user.

?[BetaInputTokensTrigger](api/beta/messages.md) trigger

When to trigger compaction. Defaults to 150000 input tokens.



[BetaCompactionBlock](api/beta/messages.md)

?string content

Summary of compacted content, or null if compaction failed

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

"compaction" type



[BetaCompactionBlockParam](api/beta/messages.md)

"compaction" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?string content

Summary of previously compacted content, or null if compaction failed

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim



[BetaCompactionContentBlockDelta](api/beta/messages.md)

?string content

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

"compaction\_delta" type



[BetaCompactionIterationUsage](api/beta/messages.md)

?[BetaCacheCreation](api/beta/messages.md) cacheCreation

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

[BetaContainer](api/beta/messages.md)

string id

Identifier for the container used in this request

\Datetime expiresAt

The time at which the container will expire.

?list<[BetaSkill](api/beta/messages.md)> skills

Skills loaded in the container



[BetaContainerParams](api/beta/messages.md)

?string id

Container id

?list<[BetaSkillParams](api/beta/messages.md)> skills

List of skills to load in the container



[BetaContainerUploadBlock](api/beta/messages.md)

string fileID

"container\_upload" type



[BetaContainerUploadBlockParam](api/beta/messages.md)

string fileID

"container\_upload" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaContentBlock](api/beta/messages.md)

One of the following:



[BetaTextBlock](api/beta/messages.md)



?list<[BetaTextCitation](api/beta/messages.md)> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

string text

"text" type



[BetaThinkingBlock](api/beta/messages.md)

string signature

string thinking

"thinking" type



[BetaRedactedThinkingBlock](api/beta/messages.md)

string data

"redacted\_thinking" type



[BetaToolUseBlock](api/beta/messages.md)

string id

array<string,mixed> input

string name

"tool\_use" type

?Caller caller

Tool invocation directly from the model.



[BetaServerToolUseBlock](api/beta/messages.md)

string id

array<string,mixed> input

Name name

"server\_tool\_use" type

?Caller caller

Tool invocation directly from the model.



[BetaWebSearchToolResultBlock](api/beta/messages.md)

[BetaWebSearchToolResultBlockContent](api/beta/messages.md) content

string toolUseID

"web\_search\_tool\_result" type

?Caller caller

Tool invocation directly from the model.



[BetaWebFetchToolResultBlock](api/beta/messages.md)

Content content

string toolUseID

"web\_fetch\_tool\_result" type

?Caller caller

Tool invocation directly from the model.



[BetaAdvisorToolResultBlock](api/beta/messages.md)

Content content

string toolUseID

"advisor\_tool\_result" type



[BetaCodeExecutionToolResultBlock](api/beta/messages.md)

[BetaCodeExecutionToolResultBlockContent](api/beta/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

string toolUseID

"code\_execution\_tool\_result" type



[BetaBashCodeExecutionToolResultBlock](api/beta/messages.md)

Content content

string toolUseID

"bash\_code\_execution\_tool\_result" type



[BetaTextEditorCodeExecutionToolResultBlock](api/beta/messages.md)

Content content

string toolUseID

"text\_editor\_code\_execution\_tool\_result" type



[BetaToolSearchToolResultBlock](api/beta/messages.md)

Content content

string toolUseID

"tool\_search\_tool\_result" type



[BetaMCPToolUseBlock](api/beta/messages.md)

string id

array<string,mixed> input

string name

The name of the MCP tool

string serverName

The name of the MCP server

"mcp\_tool\_use" type



[BetaMCPToolResultBlock](api/beta/messages.md)

Content content

bool isError

string toolUseID

"mcp\_tool\_result" type



[BetaContainerUploadBlock](api/beta/messages.md)

string fileID

"container\_upload" type



[BetaCompactionBlock](api/beta/messages.md)

?string content

Summary of compacted content, or null if compaction failed

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

"compaction" type



[BetaFallbackBlock](api/beta/messages.md)

[BetaFallbackInfo](api/beta/messages.md) from

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

[BetaFallbackInfo](api/beta/messages.md) to

The fallback model producing the content that follows this block. Its `model` is always the canonical id.

[BetaFallbackRefusalTrigger](api/beta/messages.md) trigger

What caused the `from` model to hand over at this hop.

"fallback" type



[BetaContentBlockParam](api/beta/messages.md)

One of the following:



[BetaTextBlockParam](api/beta/messages.md)

string text

"text" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?list<[BetaTextCitationParam](api/beta/messages.md)> citations



[BetaImageBlockParam](api/beta/messages.md)

Source source

"image" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaRequestDocumentBlock](api/beta/messages.md)

Source source

"document" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta/messages.md) citations

?string context

?string title



[BetaSearchResultBlockParam](api/beta/messages.md)

list<[BetaTextBlockParam](api/beta/messages.md)> content

string source

string title

"search\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta/messages.md) citations



[BetaThinkingBlockParam](api/beta/messages.md)

string signature

string thinking

"thinking" type



[BetaRedactedThinkingBlockParam](api/beta/messages.md)

string data

"redacted\_thinking" type



[BetaToolUseBlockParam](api/beta/messages.md)

string id

array<string,mixed> input

string name

"tool\_use" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.



[BetaToolResultBlockParam](api/beta/messages.md)

string toolUseID

"tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Content content

?bool isError



[BetaServerToolUseBlockParam](api/beta/messages.md)

string id

array<string,mixed> input

Name name

"server\_tool\_use" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.



[BetaWebSearchToolResultBlockParam](api/beta/messages.md)

[BetaWebSearchToolResultBlockParamContent](api/beta/messages.md) content

string toolUseID

"web\_search\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.



[BetaWebFetchToolResultBlockParam](api/beta/messages.md)

Content content

string toolUseID

"web\_fetch\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.



[BetaAdvisorToolResultBlockParam](api/beta/messages.md)

Content content

string toolUseID

"advisor\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaCodeExecutionToolResultBlockParam](api/beta/messages.md)

[BetaCodeExecutionToolResultBlockParamContent](api/beta/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

string toolUseID

"code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaBashCodeExecutionToolResultBlockParam](api/beta/messages.md)

Content content

string toolUseID

"bash\_code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaTextEditorCodeExecutionToolResultBlockParam](api/beta/messages.md)

Content content

string toolUseID

"text\_editor\_code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaToolSearchToolResultBlockParam](api/beta/messages.md)

Content content

string toolUseID

"tool\_search\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaMCPToolUseBlockParam](api/beta/messages.md)

string id

array<string,mixed> input

string name

string serverName

The name of the MCP server

"mcp\_tool\_use" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaRequestMCPToolResultBlockParam](api/beta/messages.md)

string toolUseID

"mcp\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Content content

?bool isError



[BetaContainerUploadBlockParam](api/beta/messages.md)

string fileID

"container\_upload" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaCompactionBlockParam](api/beta/messages.md)

"compaction" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?string content

Summary of previously compacted content, or null if compaction failed

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim



[BetaMidConversationSystemBlockParam](api/beta/messages.md)

list<[BetaTextBlockParam](api/beta/messages.md)> content

System instruction text blocks.

"mid\_conv\_system" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaFallbackBlockParam](api/beta/messages.md)

[BetaFallbackInfoParam](api/beta/messages.md) from

Identifies one hop of a fallback transition.

[BetaFallbackInfoParam](api/beta/messages.md) to

Identifies one hop of a fallback transition.

"fallback" type

?mixed trigger

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



[BetaContentBlockSource](api/beta/messages.md)

Content content

"content" type



[BetaContentBlockSourceContent](api/beta/messages.md)

One of the following:



[BetaTextBlockParam](api/beta/messages.md)

string text

"text" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?list<[BetaTextCitationParam](api/beta/messages.md)> citations



[BetaImageBlockParam](api/beta/messages.md)

Source source

"image" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaContextManagementConfig](api/beta/messages.md)

?list<Edit> edits

List of context management edits to apply



[BetaContextManagementResponse](api/beta/messages.md)

list<AppliedEdit> appliedEdits

List of context management edits that were applied.



[BetaCountTokensContextManagementResponse](api/beta/messages.md)

int originalInputTokens

The original token count before context management was applied



[BetaDiagnostics](api/beta/messages.md)

?CacheMissReason cacheMissReason

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.



[BetaDiagnosticsParam](api/beta/messages.md)

?string previousMessageID

The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.



[BetaDirectCaller](api/beta/messages.md)

"direct" type



[BetaDocumentBlock](api/beta/messages.md)

?[BetaCitationConfig](api/beta/messages.md) citations

Citation configuration for the document

Source source

?string title

The title of the document

"document" type



[BetaEncryptedCodeExecutionResultBlock](api/beta/messages.md)

list<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

string encryptedStdout

int returnCode

string stderr

"encrypted\_code\_execution\_result" type



[BetaEncryptedCodeExecutionResultBlockParam](api/beta/messages.md)

list<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)> content

string encryptedStdout

int returnCode

string stderr

"encrypted\_code\_execution\_result" type



[BetaFallbackBlock](api/beta/messages.md)

[BetaFallbackInfo](api/beta/messages.md) from

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

[BetaFallbackInfo](api/beta/messages.md) to

The fallback model producing the content that follows this block. Its `model` is always the canonical id.

[BetaFallbackRefusalTrigger](api/beta/messages.md) trigger

What caused the `from` model to hand over at this hop.

"fallback" type



[BetaFallbackBlockParam](api/beta/messages.md)

[BetaFallbackInfoParam](api/beta/messages.md) from

Identifies one hop of a fallback transition.

[BetaFallbackInfoParam](api/beta/messages.md) to

Identifies one hop of a fallback transition.

"fallback" type

?mixed trigger

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



[BetaFallbackInfo](api/beta/messages.md)



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.



[BetaFallbackInfoParam](api/beta/messages.md)



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.



[BetaFallbackMessageIterationUsage](api/beta/messages.md)

?[BetaCacheCreation](api/beta/messages.md) cacheCreation

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

[BetaFallbackParam](api/beta/messages.md)



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

?int maxTokens

?[BetaOutputConfig](api/beta/messages.md) outputConfig

?Speed speed

?Thinking thinking



[BetaFallbackRefusalTrigger](api/beta/messages.md)

?Category category

The policy category that triggered a refusal.

"refusal" type



[BetaFileDocumentSource](api/beta/messages.md)

string fileID

"file" type



[BetaFileImageSource](api/beta/messages.md)

string fileID

"file" type



[BetaImageBlockParam](api/beta/messages.md)

Source source

"image" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaInputJSONDelta](api/beta/messages.md)

string partialJSON

"input\_json\_delta" type



[BetaInputTokensClearAtLeast](api/beta/messages.md)

"input\_tokens" type

int value



[BetaInputTokensTrigger](api/beta/messages.md)

"input\_tokens" type

int value



list<BetaIterationsUsageItem>

One of the following:



[BetaMessageIterationUsage](api/beta/messages.md)

?[BetaCacheCreation](api/beta/messages.md) cacheCreation

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

[BetaCompactionIterationUsage](api/beta/messages.md)

?[BetaCacheCreation](api/beta/messages.md) cacheCreation

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

[BetaAdvisorMessageIterationUsage](api/beta/messages.md)

?[BetaCacheCreation](api/beta/messages.md) cacheCreation

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

[BetaFallbackMessageIterationUsage](api/beta/messages.md)

?[BetaCacheCreation](api/beta/messages.md) cacheCreation

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

[BetaJSONOutputFormat](api/beta/messages.md)

array<string,mixed> schema

The JSON schema of the format

"json\_schema" type



[BetaMCPToolConfig](api/beta/messages.md)

?bool deferLoading

?bool enabled



[BetaMCPToolDefaultConfig](api/beta/messages.md)

?bool deferLoading

?bool enabled



[BetaMCPToolResultBlock](api/beta/messages.md)

Content content

bool isError

string toolUseID

"mcp\_tool\_result" type



[BetaMCPToolUseBlock](api/beta/messages.md)

string id

array<string,mixed> input

string name

The name of the MCP tool

string serverName

The name of the MCP server

"mcp\_tool\_use" type



[BetaMCPToolUseBlockParam](api/beta/messages.md)

string id

array<string,mixed> input

string name

string serverName

The name of the MCP server

"mcp\_tool\_use" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaMCPToolset](api/beta/messages.md)

string mcpServerName

Name of the MCP server to configure tools for

"mcp\_toolset" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?array<string,[BetaMCPToolConfig](api/beta/messages.md)> configs

Configuration overrides for specific tools, keyed by tool name

?[BetaMCPToolDefaultConfig](api/beta/messages.md) defaultConfig

Default configuration applied to all tools from this server



[BetaMemoryTool20250818](api/beta/messages.md)



"memory" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"memory\_20250818" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaMemoryTool20250818Command](api/beta/messages.md)

One of the following:



[BetaMemoryTool20250818ViewCommand](api/beta/messages.md)

"view" command

Command type identifier

string path

Path to directory or file to view

?list<int> viewRange

Optional line range for viewing specific lines



[BetaMemoryTool20250818CreateCommand](api/beta/messages.md)

"create" command

Command type identifier

string fileText

Content to write to the file

string path

Path where the file should be created



[BetaMemoryTool20250818StrReplaceCommand](api/beta/messages.md)

"str\_replace" command

Command type identifier

string newStr

Text to replace with

string oldStr

Text to search for and replace

string path

Path to the file where text should be replaced



[BetaMemoryTool20250818InsertCommand](api/beta/messages.md)

"insert" command

Command type identifier

int insertLine

Line number where text should be inserted

string insertText

Text to insert at the specified line

string path

Path to the file where text should be inserted



[BetaMemoryTool20250818DeleteCommand](api/beta/messages.md)

"delete" command

Command type identifier

string path

Path to the file or directory to delete



[BetaMemoryTool20250818RenameCommand](api/beta/messages.md)

"rename" command

Command type identifier

string newPath

New path for the file or directory

string oldPath

Current path of the file or directory



[BetaMemoryTool20250818CreateCommand](api/beta/messages.md)

"create" command

Command type identifier

string fileText

Content to write to the file

string path

Path where the file should be created



[BetaMemoryTool20250818DeleteCommand](api/beta/messages.md)

"delete" command

Command type identifier

string path

Path to the file or directory to delete



[BetaMemoryTool20250818InsertCommand](api/beta/messages.md)

"insert" command

Command type identifier

int insertLine

Line number where text should be inserted

string insertText

Text to insert at the specified line

string path

Path to the file where text should be inserted



[BetaMemoryTool20250818RenameCommand](api/beta/messages.md)

"rename" command

Command type identifier

string newPath

New path for the file or directory

string oldPath

Current path of the file or directory



[BetaMemoryTool20250818StrReplaceCommand](api/beta/messages.md)

"str\_replace" command

Command type identifier

string newStr

Text to replace with

string oldStr

Text to search for and replace

string path

Path to the file where text should be replaced



[BetaMemoryTool20250818ViewCommand](api/beta/messages.md)

"view" command

Command type identifier

string path

Path to directory or file to view

?list<int> viewRange

Optional line range for viewing specific lines



[BetaMessage](api/beta/messages.md)



string id

Unique object identifier.

The format and length of IDs may change over time.

?[BetaContainer](api/beta/messages.md) container

Information about the container used in the request (for the code execution tool)



list<[BetaContentBlock](api/beta/messages.md)> content

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

?[BetaContextManagementResponse](api/beta/messages.md) contextManagement

Context management response.

Information about context management strategies applied during the request.

?[BetaDiagnostics](api/beta/messages.md) diagnostics

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

?[BetaRefusalStopDetails](api/beta/messages.md) stopDetails

Structured information about a refusal.



?[BetaStopReason](api/beta/messages.md) stopReason

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

[BetaUsage](api/beta/messages.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



[BetaMessageDeltaUsage](api/beta/messages.md)

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

?[BetaOutputTokensDetails](api/beta/messages.md) outputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.

?[BetaServerToolUsage](api/beta/messages.md) serverToolUse

The number of server tool requests.



[BetaMessageIterationUsage](api/beta/messages.md)

?[BetaCacheCreation](api/beta/messages.md) cacheCreation

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

[BetaMessageParam](api/beta/messages.md)

Content content

Role role



[BetaMessageTokensCount](api/beta/messages.md)

?[BetaCountTokensContextManagementResponse](api/beta/messages.md) contextManagement

Information about context management applied to the message.

int inputTokens

The total number of tokens across the provided list of messages, system prompt, and tools.



[BetaMetadata](api/beta/messages.md)



?string userID

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.



[BetaMidConversationSystemBlockParam](api/beta/messages.md)

list<[BetaTextBlockParam](api/beta/messages.md)> content

System instruction text blocks.

"mid\_conv\_system" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaOutputConfig](api/beta/messages.md)

?Effort effort

All possible effort levels.

?[BetaJSONOutputFormat](api/beta/messages.md) format

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

?[BetaTokenTaskBudget](api/beta/messages.md) taskBudget

User-configurable total token budget across contexts.



[BetaOutputTokensDetails](api/beta/messages.md)

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

[BetaPlainTextSource](api/beta/messages.md)

string data

"text/plain" mediaType

"text" type



[BetaRawContentBlockDelta](api/beta/messages.md)

One of the following:



[BetaTextDelta](api/beta/messages.md)

string text

"text\_delta" type



[BetaInputJSONDelta](api/beta/messages.md)

string partialJSON

"input\_json\_delta" type



[BetaCitationsDelta](api/beta/messages.md)

Citation citation

"citations\_delta" type



[BetaThinkingDelta](api/beta/messages.md)

?int estimatedTokens

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

string thinking

"thinking\_delta" type



[BetaSignatureDelta](api/beta/messages.md)

string signature

"signature\_delta" type



[BetaCompactionContentBlockDelta](api/beta/messages.md)

?string content

?string encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

"compaction\_delta" type



[BetaRawContentBlockDeltaEvent](api/beta/messages.md)

[BetaRawContentBlockDelta](api/beta/messages.md) delta

int index

"content\_block\_delta" type



[BetaRawContentBlockStartEvent](api/beta/messages.md)

ContentBlock contentBlock

Response model for a file uploaded to the container.

int index

"content\_block\_start" type



[BetaRawContentBlockStopEvent](api/beta/messages.md)

int index

"content\_block\_stop" type



[BetaRawMessageDeltaEvent](api/beta/messages.md)

?[BetaContextManagementResponse](api/beta/messages.md) contextManagement

Information about context management strategies applied during the request

Delta delta

"message\_delta" type



[BetaMessageDeltaUsage](api/beta/messages.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



[BetaRawMessageStartEvent](api/beta/messages.md)

[BetaMessage](api/beta/messages.md) message

"message\_start" type



[BetaRawMessageStopEvent](api/beta/messages.md)

"message\_stop" type



[BetaRawMessageStreamEvent](api/beta/messages.md)

One of the following:



[BetaRawMessageStartEvent](api/beta/messages.md)

[BetaMessage](api/beta/messages.md) message

"message\_start" type



[BetaRawMessageDeltaEvent](api/beta/messages.md)

?[BetaContextManagementResponse](api/beta/messages.md) contextManagement

Information about context management strategies applied during the request

Delta delta

"message\_delta" type



[BetaMessageDeltaUsage](api/beta/messages.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



[BetaRawMessageStopEvent](api/beta/messages.md)

"message\_stop" type



[BetaRawContentBlockStartEvent](api/beta/messages.md)

ContentBlock contentBlock

Response model for a file uploaded to the container.

int index

"content\_block\_start" type



[BetaRawContentBlockDeltaEvent](api/beta/messages.md)

[BetaRawContentBlockDelta](api/beta/messages.md) delta

int index

"content\_block\_delta" type



[BetaRawContentBlockStopEvent](api/beta/messages.md)

int index

"content\_block\_stop" type



[BetaRedactedThinkingBlock](api/beta/messages.md)

string data

"redacted\_thinking" type



[BetaRedactedThinkingBlockParam](api/beta/messages.md)

string data

"redacted\_thinking" type



[BetaRefusalStopDetails](api/beta/messages.md)

?Category category

The policy category that triggered a refusal.

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

[BetaRequestDocumentBlock](api/beta/messages.md)

Source source

"document" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta/messages.md) citations

?string context

?string title



[BetaRequestMCPServerToolConfiguration](api/beta/messages.md)

?list<string> allowedTools

?bool enabled



[BetaRequestMCPServerURLDefinition](api/beta/messages.md)

string name

"url" type

string url

?string authorizationToken

?[BetaRequestMCPServerToolConfiguration](api/beta/messages.md) toolConfiguration



[BetaRequestMCPToolResultBlockParam](api/beta/messages.md)

string toolUseID

"mcp\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Content content

?bool isError



[BetaSearchResultBlockParam](api/beta/messages.md)

list<[BetaTextBlockParam](api/beta/messages.md)> content

string source

string title

"search\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta/messages.md) citations



[BetaServerToolCaller](api/beta/messages.md)

string toolID

"code\_execution\_20250825" type



[BetaServerToolCaller20260120](api/beta/messages.md)

string toolID

"code\_execution\_20260120" type



[BetaServerToolUsage](api/beta/messages.md)

int webFetchRequests

The number of web fetch tool requests.

int webSearchRequests

The number of web search tool requests.



[BetaServerToolUseBlock](api/beta/messages.md)

string id

array<string,mixed> input

Name name

"server\_tool\_use" type

?Caller caller

Tool invocation directly from the model.



[BetaServerToolUseBlockParam](api/beta/messages.md)

string id

array<string,mixed> input

Name name

"server\_tool\_use" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.



[BetaSignatureDelta](api/beta/messages.md)

string signature

"signature\_delta" type



[BetaSkill](api/beta/messages.md)

string skillID

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

string version

Skill version or 'latest' for most recent version



[BetaSkillParams](api/beta/messages.md)

string skillID

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

?string version

Skill version or 'latest' for most recent version



[BetaStopReason](api/beta/messages.md)

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

[BetaTextBlock](api/beta/messages.md)



?list<[BetaTextCitation](api/beta/messages.md)> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

string text

"text" type



[BetaTextBlockParam](api/beta/messages.md)

string text

"text" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?list<[BetaTextCitationParam](api/beta/messages.md)> citations



[BetaTextCitation](api/beta/messages.md)

One of the following:



[BetaCitationCharLocation](api/beta/messages.md)

string citedText

int documentIndex

?string documentTitle

int endCharIndex

?string fileID

int startCharIndex

"char\_location" type



[BetaCitationPageLocation](api/beta/messages.md)

string citedText

int documentIndex

?string documentTitle

int endPageNumber

?string fileID

int startPageNumber

"page\_location" type



[BetaCitationContentBlockLocation](api/beta/messages.md)

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

[BetaCitationsWebSearchResultLocation](api/beta/messages.md)

string citedText

string encryptedIndex

?string title

"web\_search\_result\_location" type

string url



[BetaCitationSearchResultLocation](api/beta/messages.md)

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

[BetaTextCitationParam](api/beta/messages.md)

One of the following:



[BetaCitationCharLocationParam](api/beta/messages.md)

string citedText

int documentIndex

?string documentTitle

int endCharIndex

int startCharIndex

"char\_location" type



[BetaCitationPageLocationParam](api/beta/messages.md)

string citedText

int documentIndex

?string documentTitle

int endPageNumber

int startPageNumber

"page\_location" type



[BetaCitationContentBlockLocationParam](api/beta/messages.md)

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

[BetaCitationWebSearchResultLocationParam](api/beta/messages.md)

string citedText

string encryptedIndex

?string title

"web\_search\_result\_location" type

string url



[BetaCitationSearchResultLocationParam](api/beta/messages.md)

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

[BetaTextDelta](api/beta/messages.md)

string text

"text\_delta" type



[BetaTextEditorCodeExecutionCreateResultBlock](api/beta/messages.md)

bool isFileUpdate

"text\_editor\_code\_execution\_create\_result" type



[BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta/messages.md)

bool isFileUpdate

"text\_editor\_code\_execution\_create\_result" type



[BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta/messages.md)

?list<string> lines

?int newLines

?int newStart

?int oldLines

?int oldStart

"text\_editor\_code\_execution\_str\_replace\_result" type



[BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta/messages.md)

"text\_editor\_code\_execution\_str\_replace\_result" type

?list<string> lines

?int newLines

?int newStart

?int oldLines

?int oldStart



[BetaTextEditorCodeExecutionToolResultBlock](api/beta/messages.md)

Content content

string toolUseID

"text\_editor\_code\_execution\_tool\_result" type



[BetaTextEditorCodeExecutionToolResultBlockParam](api/beta/messages.md)

Content content

string toolUseID

"text\_editor\_code\_execution\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaTextEditorCodeExecutionToolResultError](api/beta/messages.md)

ErrorCode errorCode

?string errorMessage

"text\_editor\_code\_execution\_tool\_result\_error" type



[BetaTextEditorCodeExecutionToolResultErrorParam](api/beta/messages.md)

ErrorCode errorCode

"text\_editor\_code\_execution\_tool\_result\_error" type

?string errorMessage



[BetaTextEditorCodeExecutionViewResultBlock](api/beta/messages.md)

string content

FileType fileType

?int numLines

?int startLine

?int totalLines

"text\_editor\_code\_execution\_view\_result" type



[BetaTextEditorCodeExecutionViewResultBlockParam](api/beta/messages.md)

string content

FileType fileType

"text\_editor\_code\_execution\_view\_result" type

?int numLines

?int startLine

?int totalLines



[BetaThinkingBlock](api/beta/messages.md)

string signature

string thinking

"thinking" type



[BetaThinkingBlockParam](api/beta/messages.md)

string signature

string thinking

"thinking" type



[BetaThinkingConfigAdaptive](api/beta/messages.md)

"adaptive" type

?Display display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.



[BetaThinkingConfigDisabled](api/beta/messages.md)

"disabled" type



[BetaThinkingConfigEnabled](api/beta/messages.md)



int budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

"enabled" type

?Display display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.



[BetaThinkingConfigParam](api/beta/messages.md)

One of the following:



[BetaThinkingConfigEnabled](api/beta/messages.md)



int budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

"enabled" type

?Display display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.



[BetaThinkingConfigDisabled](api/beta/messages.md)

"disabled" type



[BetaThinkingConfigAdaptive](api/beta/messages.md)

"adaptive" type

?Display display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.



[BetaThinkingDelta](api/beta/messages.md)

?int estimatedTokens

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

string thinking

"thinking\_delta" type



[BetaThinkingTurns](api/beta/messages.md)

"thinking\_turns" type

int value



[BetaTokenTaskBudget](api/beta/messages.md)

int total

Total token budget across all contexts in the session.

"tokens" type

The budget type. Currently only 'tokens' is supported.

?int remaining

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



[BetaTool](api/beta/messages.md)



InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.



string name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

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

[BetaToolBash20241022](api/beta/messages.md)



"bash" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"bash\_20241022" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolBash20250124](api/beta/messages.md)



"bash" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"bash\_20250124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolChoice](api/beta/messages.md)

One of the following:



[BetaToolChoiceAuto](api/beta/messages.md)

"auto" type



?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



[BetaToolChoiceAny](api/beta/messages.md)

"any" type



?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



[BetaToolChoiceTool](api/beta/messages.md)

string name

The name of the tool to use.

"tool" type



?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



[BetaToolChoiceNone](api/beta/messages.md)

"none" type



[BetaToolChoiceAny](api/beta/messages.md)

"any" type



?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



[BetaToolChoiceAuto](api/beta/messages.md)

"auto" type



?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



[BetaToolChoiceNone](api/beta/messages.md)

"none" type



[BetaToolChoiceTool](api/beta/messages.md)

string name

The name of the tool to use.

"tool" type



?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



[BetaToolComputerUse20241022](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int displayNumber

The X11 display number (e.g. 0, 1) for the display.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolComputerUse20250124](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int displayNumber

The X11 display number (e.g. 0, 1) for the display.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolComputerUse20251124](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

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

[BetaToolReferenceBlock](api/beta/messages.md)

string toolName

"tool\_reference" type



[BetaToolReferenceBlockParam](api/beta/messages.md)

string toolName

"tool\_reference" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaToolResultBlockParam](api/beta/messages.md)

string toolUseID

"tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Content content

?bool isError



[BetaToolSearchToolBm25\_20251119](api/beta/messages.md)



"tool\_search\_tool\_bm25" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolSearchToolRegex20251119](api/beta/messages.md)



"tool\_search\_tool\_regex" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolSearchToolResultBlock](api/beta/messages.md)

Content content

string toolUseID

"tool\_search\_tool\_result" type



[BetaToolSearchToolResultBlockParam](api/beta/messages.md)

Content content

string toolUseID

"tool\_search\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.



[BetaToolSearchToolResultError](api/beta/messages.md)

ErrorCode errorCode

?string errorMessage

"tool\_search\_tool\_result\_error" type



[BetaToolSearchToolResultErrorParam](api/beta/messages.md)

ErrorCode errorCode

"tool\_search\_tool\_result\_error" type

?string errorMessage



[BetaToolSearchToolSearchResultBlock](api/beta/messages.md)

list<[BetaToolReferenceBlock](api/beta/messages.md)> toolReferences

"tool\_search\_tool\_search\_result" type



[BetaToolSearchToolSearchResultBlockParam](api/beta/messages.md)

list<[BetaToolReferenceBlockParam](api/beta/messages.md)> toolReferences

"tool\_search\_tool\_search\_result" type



[BetaToolTextEditor20241022](api/beta/messages.md)



"str\_replace\_editor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20241022" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolTextEditor20250124](api/beta/messages.md)



"str\_replace\_editor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolTextEditor20250429](api/beta/messages.md)



"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250429" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolTextEditor20250728](api/beta/messages.md)



"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250728" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?int maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolUnion](api/beta/messages.md)

One of the following:



[BetaTool](api/beta/messages.md)



InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.



string name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

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

[BetaToolBash20241022](api/beta/messages.md)



"bash" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"bash\_20241022" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolBash20250124](api/beta/messages.md)



"bash" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"bash\_20250124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaCodeExecutionTool20250522](api/beta/messages.md)



"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250522" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaCodeExecutionTool20250825](api/beta/messages.md)



"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250825" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaCodeExecutionTool20260120](api/beta/messages.md)



"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20260120" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaCodeExecutionTool20260521](api/beta/messages.md)



"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20260521" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolComputerUse20241022](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int displayNumber

The X11 display number (e.g. 0, 1) for the display.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaMemoryTool20250818](api/beta/messages.md)



"memory" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"memory\_20250818" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolComputerUse20250124](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int displayNumber

The X11 display number (e.g. 0, 1) for the display.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolTextEditor20241022](api/beta/messages.md)



"str\_replace\_editor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20241022" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolComputerUse20251124](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

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

[BetaToolTextEditor20250124](api/beta/messages.md)



"str\_replace\_editor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250124" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolTextEditor20250429](api/beta/messages.md)



"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250429" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolTextEditor20250728](api/beta/messages.md)



"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250728" type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?int maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaWebSearchTool20250305](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[BetaUserLocation](api/beta/messages.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.



[BetaWebFetchTool20250910](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta/messages.md) citations

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

[BetaWebSearchTool20260209](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[BetaUserLocation](api/beta/messages.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.



[BetaWebFetchTool20260209](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta/messages.md) citations

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

[BetaWebFetchTool20260309](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta/messages.md) citations

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

[BetaWebSearchTool20260318](api/beta/messages.md)



"web\_search" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_search\_20260318" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

?list<string> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?ResponseInclusion responseInclusion

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[BetaUserLocation](api/beta/messages.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.



[BetaWebFetchTool20260318](api/beta/messages.md)



"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20260318" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta/messages.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?ResponseInclusion responseInclusion

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

?bool strict

When true, guarantees schema validation on tool names and inputs

?bool useCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



[BetaAdvisorTool20260301](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCacheControlEphemeral](api/beta/messages.md) caching

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

[BetaToolSearchToolBm25\_20251119](api/beta/messages.md)



"tool\_search\_tool\_bm25" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaToolSearchToolRegex20251119](api/beta/messages.md)



"tool\_search\_tool\_regex" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs



[BetaMCPToolset](api/beta/messages.md)

string mcpServerName

Name of the MCP server to configure tools for

"mcp\_toolset" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?array<string,[BetaMCPToolConfig](api/beta/messages.md)> configs

Configuration overrides for specific tools, keyed by tool name

?[BetaMCPToolDefaultConfig](api/beta/messages.md) defaultConfig

Default configuration applied to all tools from this server



[BetaToolUseBlock](api/beta/messages.md)

string id

array<string,mixed> input

string name

"tool\_use" type

?Caller caller

Tool invocation directly from the model.



[BetaToolUseBlockParam](api/beta/messages.md)

string id

array<string,mixed> input

string name

"tool\_use" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.



[BetaToolUsesKeep](api/beta/messages.md)

"tool\_uses" type

int value



[BetaToolUsesTrigger](api/beta/messages.md)

"tool\_uses" type

int value



[BetaURLImageSource](api/beta/messages.md)

"url" type

string url



[BetaURLPDFSource](api/beta/messages.md)

"url" type

string url



[BetaUsage](api/beta/messages.md)

?[BetaCacheCreation](api/beta/messages.md) cacheCreation

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

?[BetaOutputTokensDetails](api/beta/messages.md) outputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.

?[BetaServerToolUsage](api/beta/messages.md) serverToolUse

The number of server tool requests.

?ServiceTier serviceTier

If the request used the priority, standard, or batch tier.

?Speed speed

The inference speed mode used for this request.



[BetaUserLocation](api/beta/messages.md)

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

[BetaWebFetchBlock](api/beta/messages.md)

[BetaDocumentBlock](api/beta/messages.md) content

?string retrievedAt

ISO 8601 timestamp when the content was retrieved

"web\_fetch\_result" type

string url

Fetched content URL



[BetaWebFetchBlockParam](api/beta/messages.md)

[BetaRequestDocumentBlock](api/beta/messages.md) content

"web\_fetch\_result" type

string url

Fetched content URL

?string retrievedAt

ISO 8601 timestamp when the content was retrieved



[BetaWebFetchTool20250910](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta/messages.md) citations

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

[BetaWebFetchTool20260209](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta/messages.md) citations

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

[BetaWebFetchTool20260309](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta/messages.md) citations

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

[BetaWebFetchTool20260318](api/beta/messages.md)



"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20260318" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[BetaCitationsConfigParam](api/beta/messages.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?ResponseInclusion responseInclusion

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

?bool strict

When true, guarantees schema validation on tool names and inputs

?bool useCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



[BetaWebFetchToolResultBlock](api/beta/messages.md)

Content content

string toolUseID

"web\_fetch\_tool\_result" type

?Caller caller

Tool invocation directly from the model.



[BetaWebFetchToolResultBlockParam](api/beta/messages.md)

Content content

string toolUseID

"web\_fetch\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.



[BetaWebFetchToolResultErrorBlock](api/beta/messages.md)

[BetaWebFetchToolResultErrorCode](api/beta/messages.md) errorCode

"web\_fetch\_tool\_result\_error" type



[BetaWebFetchToolResultErrorBlockParam](api/beta/messages.md)

[BetaWebFetchToolResultErrorCode](api/beta/messages.md) errorCode

"web\_fetch\_tool\_result\_error" type



[BetaWebFetchToolResultErrorCode](api/beta/messages.md)

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

[BetaWebSearchResultBlock](api/beta/messages.md)

string encryptedContent

?string pageAge

string title

"web\_search\_result" type

string url



[BetaWebSearchResultBlockParam](api/beta/messages.md)

string encryptedContent

string title

"web\_search\_result" type

string url

?string pageAge



[BetaWebSearchTool20250305](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[BetaUserLocation](api/beta/messages.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.



[BetaWebSearchTool20260209](api/beta/messages.md)

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

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[BetaUserLocation](api/beta/messages.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.



[BetaWebSearchTool20260318](api/beta/messages.md)



"web\_search" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_search\_20260318" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

?list<string> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?ResponseInclusion responseInclusion

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[BetaUserLocation](api/beta/messages.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.



[BetaWebSearchToolRequestError](api/beta/messages.md)

[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

"web\_search\_tool\_result\_error" type



[BetaWebSearchToolResultBlock](api/beta/messages.md)

[BetaWebSearchToolResultBlockContent](api/beta/messages.md) content

string toolUseID

"web\_search\_tool\_result" type

?Caller caller

Tool invocation directly from the model.



[BetaWebSearchToolResultBlockContent](api/beta/messages.md)

One of the following:



[BetaWebSearchToolResultError](api/beta/messages.md)

[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

"web\_search\_tool\_result\_error" type



list<[BetaWebSearchResultBlock](api/beta/messages.md)>

string encryptedContent

?string pageAge

string title

"web\_search\_result" type

string url



[BetaWebSearchToolResultBlockParam](api/beta/messages.md)

[BetaWebSearchToolResultBlockParamContent](api/beta/messages.md) content

string toolUseID

"web\_search\_tool\_result" type

?[BetaCacheControlEphemeral](api/beta/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.



[BetaWebSearchToolResultBlockParamContent](api/beta/messages.md)

One of the following:



list<[BetaWebSearchResultBlockParam](api/beta/messages.md)>

string encryptedContent

string title

"web\_search\_result" type

string url

?string pageAge



[BetaWebSearchToolRequestError](api/beta/messages.md)

[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

"web\_search\_tool\_result\_error" type



[BetaWebSearchToolResultError](api/beta/messages.md)

[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

"web\_search\_tool\_result\_error" type



[BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

#### MessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

$client->beta->messages->batches->create(list<Request> requests, ?list<AnthropicBeta> betas, ?string userProfileID): [MessageBatch](api/beta/messages/batches.md)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

$client->beta->messages->batches->retrieve(string messageBatchID, ?list<AnthropicBeta> betas): [MessageBatch](api/beta/messages/batches.md)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

$client->beta->messages->batches->list(?string afterID, ?string beforeID, ?int limit, ?list<AnthropicBeta> betas): Page<[MessageBatch](api/beta/messages/batches.md)>

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

$client->beta->messages->batches->cancel(string messageBatchID, ?list<AnthropicBeta> betas): [MessageBatch](api/beta/messages/batches.md)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

$client->beta->messages->batches->delete(string messageBatchID, ?list<AnthropicBeta> betas): [DeletedMessageBatch](api/beta/messages/batches.md)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

$client->beta->messages->batches->results(string messageBatchID, ?list<AnthropicBeta> betas): [MessageBatchIndividualResponse](api/beta/messages/batches.md)

GET/v1/messages/batches/{message\_batch\_id}/results

---

*Copyright © Anthropic. All rights reserved.*
