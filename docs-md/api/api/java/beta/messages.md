# Messages

Copy page



Java

# Messages

##### [Create a Message](api/beta/messages/create.md)

[BetaMessage](api/beta/messages.md) beta().messages().create(MessageCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

[BetaMessageTokensCount](api/beta/messages.md) beta().messages().countTokens(MessageCountTokensParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse



class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration



class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

Optional<String> stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant



class BetaAdvisorRedactedResultBlockParam:

String encryptedContent

Opaque blob produced by a prior response; must be round-tripped verbatim.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

Optional<String> stopReason



class BetaAdvisorResultBlock:

Optional<String> stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant



class BetaAdvisorResultBlockParam:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

Optional<String> stopReason



class BetaAdvisorTool20260301:



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



JsonValue; name "advisor"constant"advisor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "advisor\_20260301"constant"advisor\_20260301"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> caching

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxTokens

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaAdvisorToolResultBlock:



Content content

One of the following:



class BetaAdvisorToolResultError:



ErrorCode errorCode

One of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

MODEL\_NOT\_FOUND("model\_not\_found")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant



class BetaAdvisorResultBlock:

Optional<String> stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant



class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

Optional<String> stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant



class BetaAdvisorToolResultBlockParam:



Content content

One of the following:



class BetaAdvisorToolResultErrorParam:



ErrorCode errorCode

One of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

MODEL\_NOT\_FOUND("model\_not\_found")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant



class BetaAdvisorResultBlockParam:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

Optional<String> stopReason



class BetaAdvisorRedactedResultBlockParam:

String encryptedContent

Opaque blob produced by a prior response; must be round-tripped verbatim.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

Optional<String> stopReason

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaAdvisorToolResultError:



ErrorCode errorCode

One of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

MODEL\_NOT\_FOUND("model\_not\_found")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant



class BetaAdvisorToolResultErrorParam:



ErrorCode errorCode

One of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

MODEL\_NOT\_FOUND("model\_not\_found")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant



class BetaAllThinkingTurns:

JsonValue; type "all"constant"all"constant



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaBashCodeExecutionOutputBlock:

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant



class BetaBashCodeExecutionOutputBlockParam:

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant



class BetaBashCodeExecutionResultBlock:



List<[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant



class BetaBashCodeExecutionResultBlockParam:



List<[BetaBashCodeExecutionOutputBlockParam](api/beta/messages.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant



class BetaBashCodeExecutionToolResultBlock:



Content content

One of the following:



class BetaBashCodeExecutionToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant



class BetaBashCodeExecutionResultBlock:



List<[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant



class BetaBashCodeExecutionToolResultBlockParam:



Content content

One of the following:



class BetaBashCodeExecutionToolResultErrorParam:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant



class BetaBashCodeExecutionResultBlockParam:



List<[BetaBashCodeExecutionOutputBlockParam](api/beta/messages.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaBashCodeExecutionToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant



class BetaBashCodeExecutionToolResultErrorParam:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant



class BetaCacheControlEphemeral:

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaCacheCreation:

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.



class BetaCacheMissMessagesChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "messages\_changed"constant"messages\_changed"constant



class BetaCacheMissModelChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "model\_changed"constant"model\_changed"constant



class BetaCacheMissPreviousMessageNotFound:

JsonValue; type "previous\_message\_not\_found"constant"previous\_message\_not\_found"constant



class BetaCacheMissSystemChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "system\_changed"constant"system\_changed"constant



class BetaCacheMissToolsChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "tools\_changed"constant"tools\_changed"constant



class BetaCacheMissUnavailable:

JsonValue; type "unavailable"constant"unavailable"constant



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationConfig:

boolean enabled



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationsConfigParam:

Optional<Boolean> enabled



class BetaCitationsDelta:



Citation citation

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

JsonValue; type "citations\_delta"constant"citations\_delta"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaClearThinking20251015Edit:

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant



Optional<Keep> keep

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

One of the following:



class BetaThinkingTurns:

JsonValue; type "thinking\_turns"constant"thinking\_turns"constant

long value



class BetaAllThinkingTurns:

JsonValue; type "all"constant"all"constant

JsonValue;



class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.



class BetaClearToolUses20250919Edit:

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant



Optional<[BetaInputTokensClearAtLeast](api/beta/messages.md)> clearAtLeast

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value



Optional<ClearToolInputs> clearToolInputs

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

One of the following:

boolean

List<String>

Optional<List<String>> excludeTools

Tool names whose uses are preserved from clearing



Optional<[BetaToolUsesKeep](api/beta/messages.md)> keep

Number of tool uses to retain in the conversation

JsonValue; type "tool\_uses"constant"tool\_uses"constant

long value



Optional<Trigger> trigger

Condition that triggers the context management strategy

One of the following:



class BetaInputTokensTrigger:

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value



class BetaToolUsesTrigger:

JsonValue; type "tool\_uses"constant"tool\_uses"constant

long value



class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.



class BetaCodeExecutionOutputBlock:

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant



class BetaCodeExecutionOutputBlockParam:

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant



class BetaCodeExecutionResultBlock:



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class BetaCodeExecutionResultBlockParam:



List<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class BetaCodeExecutionTool20250522:



JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20250522"constant"code\_execution\_20250522"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20250825:



JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20260120:

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20260521:

Code execution tool with REPL state persistence.



JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20260521"constant"code\_execution\_20260521"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionToolResultBlock:



[BetaCodeExecutionToolResultBlockContent](api/beta/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError:



[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



class BetaCodeExecutionResultBlock:



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant



class BetaCodeExecutionToolResultBlockContent: A class that can be one of several variants.union 

Code execution result with encrypted stdout for PFC + web\_search results.



class BetaCodeExecutionToolResultError:



[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



class BetaCodeExecutionResultBlock:



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant



class BetaCodeExecutionToolResultBlockParam:



[BetaCodeExecutionToolResultBlockParamContent](api/beta/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultErrorParam:



[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



class BetaCodeExecutionResultBlockParam:



List<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaCodeExecutionToolResultBlockParamContent: A class that can be one of several variants.union 

Code execution result with encrypted stdout for PFC + web\_search results.



class BetaCodeExecutionToolResultErrorParam:



[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



class BetaCodeExecutionResultBlockParam:



List<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant



class BetaCodeExecutionToolResultError:



[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



enum BetaCodeExecutionToolResultErrorCode:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")



class BetaCodeExecutionToolResultErrorParam:



[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



class BetaCompact20260112Edit:

Automatically compact older context when reaching the configured trigger threshold.

JsonValue; type "compact\_20260112"constant"compact\_20260112"constant

Optional<String> instructions

Additional instructions for summarization.

Optional<Boolean> pauseAfterCompaction

Whether to pause after compaction and return the compaction block to the user.



Optional<[BetaInputTokensTrigger](api/beta/messages.md)> trigger

When to trigger compaction. Defaults to 150000 input tokens.

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value



class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction"constant"compaction"constant



class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

JsonValue; type "compaction"constant"compaction"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<String> content

Summary of previously compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim



class BetaCompactionContentBlockDelta:

Optional<String> content

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction\_delta"constant"compaction\_delta"constant



class BetaCompactionIterationUsage:

Token usage for a compaction iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration



class BetaContainer:

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.



Optional<List<[BetaSkill](api/beta/messages.md)>> skills

Skills loaded in the container

String skillId

Skill ID



Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version



class BetaContainerParams:

Container parameters with skills to be loaded.

Optional<String> id

Container id



Optional<List<[BetaSkillParams](api/beta/messages.md)>> skills

List of skills to load in the container

String skillId

Skill ID



Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

Optional<String> version

Skill version or 'latest' for most recent version



class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant



class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaContentBlock: A class that can be one of several variants.union 

Response model for a file uploaded to the container.



class BetaTextBlock:



Optional<List<[BetaTextCitation](api/beta/messages.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant



class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant



class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant



class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaServerToolUseBlock:

String id

Input input



Name name

One of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebSearchToolResultBlock:



[BetaWebSearchToolResultBlockContent](api/beta/messages.md) content

One of the following:



class BetaWebSearchToolResultError:



[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant



List<[BetaWebSearchResultBlock](api/beta/messages.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebFetchToolResultBlock:



Content content

One of the following:



class BetaWebFetchToolResultErrorBlock:



[BetaWebFetchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_IN\_PRIOR\_CONTEXT("url\_not\_in\_prior\_context")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant



class BetaWebFetchBlock:



[BetaDocumentBlock](api/beta/messages.md) content



Optional<[BetaCitationConfig](api/beta/messages.md)> citations

Citation configuration for the document

boolean enabled



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaAdvisorToolResultBlock:



Content content

One of the following:



class BetaAdvisorToolResultError:



ErrorCode errorCode

One of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

MODEL\_NOT\_FOUND("model\_not\_found")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant



class BetaAdvisorResultBlock:

Optional<String> stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant



class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

Optional<String> stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant



class BetaCodeExecutionToolResultBlock:



[BetaCodeExecutionToolResultBlockContent](api/beta/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError:



[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



class BetaCodeExecutionResultBlock:



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant



class BetaBashCodeExecutionToolResultBlock:



Content content

One of the following:



class BetaBashCodeExecutionToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant



class BetaBashCodeExecutionResultBlock:



List<[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant



class BetaTextEditorCodeExecutionToolResultBlock:



Content content

One of the following:



class BetaTextEditorCodeExecutionToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant



class BetaTextEditorCodeExecutionViewResultBlock:

String content



FileType fileType

One of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant



class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant



class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant



class BetaToolSearchToolResultBlock:



Content content

One of the following:



class BetaToolSearchToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant



class BetaToolSearchToolSearchResultBlock:



List<[BetaToolReferenceBlock](api/beta/messages.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant



class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant



class BetaMcpToolResultBlock:



Content content

One of the following:

String



List<[BetaTextBlock](api/beta/messages.md)>



Optional<List<[BetaTextCitation](api/beta/messages.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant



class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant



class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction"constant"compaction"constant



class BetaFallbackBlock:

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

[BetaFallbackInfo](api/beta/messages.md) from

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackInfo](api/beta/messages.md) to

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackRefusalTrigger](api/beta/messages.md) trigger

What caused the `from` model to hand over at this hop.



Optional<Category> category

The policy category that triggered a refusal.

One of the following:

CYBER("cyber")

BIO("bio")

FRONTIER\_LLM("frontier\_llm")

REASONING\_EXTRACTION("reasoning\_extraction")

JsonValue; type "refusal"constant"refusal"constant

JsonValue; type "fallback"constant"fallback"constant



class BetaContentBlockParam: A class that can be one of several variants.union 

Regular text content.



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaRequestDocumentBlock:



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant



class BetaContentBlockSource:



Content content

One of the following:

String



List<[BetaContentBlockSourceContent](api/beta/messages.md)>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant



class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title



class BetaSearchResultBlockParam:



List<[BetaTextBlockParam](api/beta/messages.md)> content

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String source

String title

JsonValue; type "search\_result"constant"search\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled



class BetaThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant



class BetaRedactedThinkingBlockParam:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant



class BetaToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaToolResultBlockParam:

String toolUseId

JsonValue; type "tool\_result"constant"tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Content> content

One of the following:

String



List<Block>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaSearchResultBlockParam:



List<[BetaTextBlockParam](api/beta/messages.md)> content

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String source

String title

JsonValue; type "search\_result"constant"search\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled



class BetaRequestDocumentBlock:



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant



class BetaContentBlockSource:



Content content

One of the following:

String



List<[BetaContentBlockSourceContent](api/beta/messages.md)>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant



class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title



class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> isError



class BetaServerToolUseBlockParam:

String id

Input input



Name name

One of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebSearchToolResultBlockParam:



[BetaWebSearchToolResultBlockParamContent](api/beta/messages.md) content

One of the following:



List<[BetaWebSearchResultBlockParam](api/beta/messages.md)>

String encryptedContent

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

Optional<String> pageAge



class BetaWebSearchToolRequestError:



[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebFetchToolResultBlockParam:



Content content

One of the following:



class BetaWebFetchToolResultErrorBlockParam:



[BetaWebFetchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_IN\_PRIOR\_CONTEXT("url\_not\_in\_prior\_context")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant



class BetaWebFetchBlockParam:



[BetaRequestDocumentBlock](api/beta/messages.md) content



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant



class BetaContentBlockSource:



Content content

One of the following:

String



List<[BetaContentBlockSourceContent](api/beta/messages.md)>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant



class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaAdvisorToolResultBlockParam:



Content content

One of the following:



class BetaAdvisorToolResultErrorParam:



ErrorCode errorCode

One of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

MODEL\_NOT\_FOUND("model\_not\_found")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant



class BetaAdvisorResultBlockParam:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

Optional<String> stopReason



class BetaAdvisorRedactedResultBlockParam:

String encryptedContent

Opaque blob produced by a prior response; must be round-tripped verbatim.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

Optional<String> stopReason

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaCodeExecutionToolResultBlockParam:



[BetaCodeExecutionToolResultBlockParamContent](api/beta/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultErrorParam:



[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



class BetaCodeExecutionResultBlockParam:



List<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaBashCodeExecutionToolResultBlockParam:



Content content

One of the following:



class BetaBashCodeExecutionToolResultErrorParam:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant



class BetaBashCodeExecutionResultBlockParam:



List<[BetaBashCodeExecutionOutputBlockParam](api/beta/messages.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaTextEditorCodeExecutionToolResultBlockParam:



Content content

One of the following:



class BetaTextEditorCodeExecutionToolResultErrorParam:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Optional<String> errorMessage



class BetaTextEditorCodeExecutionViewResultBlockParam:

String content



FileType fileType

One of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines



class BetaTextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant



class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaToolSearchToolResultBlockParam:



Content content

One of the following:



class BetaToolSearchToolResultErrorParam:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Optional<String> errorMessage



class BetaToolSearchToolSearchResultBlockParam:



List<[BetaToolReferenceBlockParam](api/beta/messages.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaMcpToolUseBlockParam:

String id

Input input

String name

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaRequestMcpToolResultBlockParam:

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Content> content

One of the following:

String



List<[BetaTextBlockParam](api/beta/messages.md)>

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

Optional<Boolean> isError



class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

JsonValue; type "compaction"constant"compaction"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<String> content

Summary of previously compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim



class BetaMidConversationSystemBlockParam:

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



List<[BetaTextBlockParam](api/beta/messages.md)> content

System instruction text blocks.

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

JsonValue; type "mid\_conv\_system"constant"mid\_conv\_system"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaFallbackBlockParam:

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

[BetaFallbackInfoParam](api/beta/messages.md) from

Identifies one hop of a fallback transition.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackInfoParam](api/beta/messages.md) to

Identifies one hop of a fallback transition.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

JsonValue; type "fallback"constant"fallback"constant

Optional<JsonValue> trigger

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



class BetaContentBlockSource:



Content content

One of the following:

String



List<[BetaContentBlockSourceContent](api/beta/messages.md)>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant



class BetaContentBlockSourceContent: A class that can be one of several variants.union 



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaContextManagementConfig:



Optional<List<Edit>> edits

List of context management edits to apply

One of the following:



class BetaClearToolUses20250919Edit:

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant



Optional<[BetaInputTokensClearAtLeast](api/beta/messages.md)> clearAtLeast

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value



Optional<ClearToolInputs> clearToolInputs

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

One of the following:

boolean

List<String>

Optional<List<String>> excludeTools

Tool names whose uses are preserved from clearing



Optional<[BetaToolUsesKeep](api/beta/messages.md)> keep

Number of tool uses to retain in the conversation

JsonValue; type "tool\_uses"constant"tool\_uses"constant

long value



Optional<Trigger> trigger

Condition that triggers the context management strategy

One of the following:



class BetaInputTokensTrigger:

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value



class BetaToolUsesTrigger:

JsonValue; type "tool\_uses"constant"tool\_uses"constant

long value



class BetaClearThinking20251015Edit:

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant



Optional<Keep> keep

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

One of the following:



class BetaThinkingTurns:

JsonValue; type "thinking\_turns"constant"thinking\_turns"constant

long value



class BetaAllThinkingTurns:

JsonValue; type "all"constant"all"constant

JsonValue;



class BetaCompact20260112Edit:

Automatically compact older context when reaching the configured trigger threshold.

JsonValue; type "compact\_20260112"constant"compact\_20260112"constant

Optional<String> instructions

Additional instructions for summarization.

Optional<Boolean> pauseAfterCompaction

Whether to pause after compaction and return the compaction block to the user.



Optional<[BetaInputTokensTrigger](api/beta/messages.md)> trigger

When to trigger compaction. Defaults to 150000 input tokens.

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value



class BetaContextManagementResponse:



List<AppliedEdit> appliedEdits

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.



class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.



class BetaCountTokensContextManagementResponse:

long originalInputTokens

The original token count before context management was applied



class BetaDiagnostics:

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



Optional<CacheMissReason> cacheMissReason

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



class BetaCacheMissModelChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "model\_changed"constant"model\_changed"constant



class BetaCacheMissSystemChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "system\_changed"constant"system\_changed"constant



class BetaCacheMissToolsChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "tools\_changed"constant"tools\_changed"constant



class BetaCacheMissMessagesChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "messages\_changed"constant"messages\_changed"constant



class BetaCacheMissPreviousMessageNotFound:

JsonValue; type "previous\_message\_not\_found"constant"previous\_message\_not\_found"constant



class BetaCacheMissUnavailable:

JsonValue; type "unavailable"constant"unavailable"constant



class BetaDiagnosticsParam:

Request-level diagnostics. Currently carries the previous response
id for prompt-cache divergence reporting.

Optional<String> previousMessageId

The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaDocumentBlock:



Optional<[BetaCitationConfig](api/beta/messages.md)> citations

Citation configuration for the document

boolean enabled



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant



class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant



class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant



class BetaFallbackBlock:

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

[BetaFallbackInfo](api/beta/messages.md) from

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackInfo](api/beta/messages.md) to

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackRefusalTrigger](api/beta/messages.md) trigger

What caused the `from` model to hand over at this hop.



Optional<Category> category

The policy category that triggered a refusal.

One of the following:

CYBER("cyber")

BIO("bio")

FRONTIER\_LLM("frontier\_llm")

REASONING\_EXTRACTION("reasoning\_extraction")

JsonValue; type "refusal"constant"refusal"constant

JsonValue; type "fallback"constant"fallback"constant



class BetaFallbackBlockParam:

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

[BetaFallbackInfoParam](api/beta/messages.md) from

Identifies one hop of a fallback transition.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackInfoParam](api/beta/messages.md) to

Identifies one hop of a fallback transition.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

JsonValue; type "fallback"constant"fallback"constant

Optional<JsonValue> trigger

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



class BetaFallbackInfo:

Identifies one hop of a fallback transition.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



class BetaFallbackInfoParam:

Identifies one hop of a fallback transition.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



class BetaFallbackMessageIterationUsage:

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "fallback\_message"constant"fallback\_message"constant

Usage for the fallback-model attempt that served the response



class BetaFallbackParam:

One entry in the `fallbacks` chain on a `/v1/messages` request.

`model` is required. The four override fields (`max_tokens`, `thinking`,
`output_config`, and `speed`) replace the corresponding top-level field
for this attempt only and are validated as if the request were made to
`model`. Any other key is rejected at parse time.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

Optional<Long> maxTokens



Optional<[BetaOutputConfig](api/beta/messages.md)> outputConfig



Optional<Effort> effort

All possible effort levels.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

XHIGH("xhigh")

MAX("max")



Optional<[BetaJsonOutputFormat](api/beta/messages.md)> format

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

Schema schema

The JSON schema of the format

JsonValue; type "json\_schema"constant"json\_schema"constant



Optional<[BetaTokenTaskBudget](api/beta/messages.md)> taskBudget

User-configurable total token budget across contexts.

long total

Total token budget across all contexts in the session.

JsonValue; type "tokens"constant"tokens"constant

The budget type. Currently only 'tokens' is supported.

Optional<Long> remaining

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



Optional<Speed> speed

One of the following:

STANDARD("standard")

FAST("fast")



Optional<Thinking> thinking

One of the following:



class BetaThinkingConfigEnabled:



long budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

JsonValue; type "enabled"constant"enabled"constant



Optional<Display> display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

SUMMARIZED("summarized")

OMITTED("omitted")



class BetaThinkingConfigDisabled:

JsonValue; type "disabled"constant"disabled"constant



class BetaThinkingConfigAdaptive:

JsonValue; type "adaptive"constant"adaptive"constant



Optional<Display> display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

SUMMARIZED("summarized")

OMITTED("omitted")



class BetaFallbackRefusalTrigger:

The `from` model declined for policy reasons.



Optional<Category> category

The policy category that triggered a refusal.

One of the following:

CYBER("cyber")

BIO("bio")

FRONTIER\_LLM("frontier\_llm")

REASONING\_EXTRACTION("reasoning\_extraction")

JsonValue; type "refusal"constant"refusal"constant



class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaInputJsonDelta:

String partialJson

JsonValue; type "input\_json\_delta"constant"input\_json\_delta"constant



class BetaInputTokensClearAtLeast:

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value



class BetaInputTokensTrigger:

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value



class BetaJsonOutputFormat:

Schema schema

The JSON schema of the format

JsonValue; type "json\_schema"constant"json\_schema"constant



class BetaMcpToolConfig:

Configuration for a specific tool in an MCP toolset.

Optional<Boolean> deferLoading

Optional<Boolean> enabled



class BetaMcpToolDefaultConfig:

Default configuration for tools in an MCP toolset.

Optional<Boolean> deferLoading

Optional<Boolean> enabled



class BetaMcpToolResultBlock:



Content content

One of the following:

String



List<[BetaTextBlock](api/beta/messages.md)>



Optional<List<[BetaTextCitation](api/beta/messages.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant



class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant



class BetaMcpToolUseBlockParam:

String id

Input input

String name

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaMcpToolset:

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

String mcpServerName

Name of the MCP server to configure tools for

JsonValue; type "mcp\_toolset"constant"mcp\_toolset"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Configs> configs

Configuration overrides for specific tools, keyed by tool name

Optional<Boolean> deferLoading

Optional<Boolean> enabled



Optional<[BetaMcpToolDefaultConfig](api/beta/messages.md)> defaultConfig

Default configuration applied to all tools from this server

Optional<Boolean> deferLoading

Optional<Boolean> enabled



class BetaMemoryTool20250818:



JsonValue; name "memory"constant"memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "memory\_20250818"constant"memory\_20250818"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaMemoryTool20250818Command: A class that can be one of several variants.union 



class BetaMemoryTool20250818ViewCommand:

JsonValue; command "view"constant"view"constant

Command type identifier

String path

Path to directory or file to view

Optional<List<Long>> viewRange

Optional line range for viewing specific lines



class BetaMemoryTool20250818CreateCommand:

JsonValue; command "create"constant"create"constant

Command type identifier

String fileText

Content to write to the file

String path

Path where the file should be created



class BetaMemoryTool20250818StrReplaceCommand:

JsonValue; command "str\_replace"constant"str\_replace"constant

Command type identifier

String newStr

Text to replace with

String oldStr

Text to search for and replace

String path

Path to the file where text should be replaced



class BetaMemoryTool20250818InsertCommand:

JsonValue; command "insert"constant"insert"constant

Command type identifier

long insertLine

Line number where text should be inserted

String insertText

Text to insert at the specified line

String path

Path to the file where text should be inserted



class BetaMemoryTool20250818DeleteCommand:

JsonValue; command "delete"constant"delete"constant

Command type identifier

String path

Path to the file or directory to delete



class BetaMemoryTool20250818RenameCommand:

JsonValue; command "rename"constant"rename"constant

Command type identifier

String newPath

New path for the file or directory

String oldPath

Current path of the file or directory



class BetaMemoryTool20250818CreateCommand:

JsonValue; command "create"constant"create"constant

Command type identifier

String fileText

Content to write to the file

String path

Path where the file should be created



class BetaMemoryTool20250818DeleteCommand:

JsonValue; command "delete"constant"delete"constant

Command type identifier

String path

Path to the file or directory to delete



class BetaMemoryTool20250818InsertCommand:

JsonValue; command "insert"constant"insert"constant

Command type identifier

long insertLine

Line number where text should be inserted

String insertText

Text to insert at the specified line

String path

Path to the file where text should be inserted



class BetaMemoryTool20250818RenameCommand:

JsonValue; command "rename"constant"rename"constant

Command type identifier

String newPath

New path for the file or directory

String oldPath

Current path of the file or directory



class BetaMemoryTool20250818StrReplaceCommand:

JsonValue; command "str\_replace"constant"str\_replace"constant

Command type identifier

String newStr

Text to replace with

String oldStr

Text to search for and replace

String path

Path to the file where text should be replaced



class BetaMemoryTool20250818ViewCommand:

JsonValue; command "view"constant"view"constant

Command type identifier

String path

Path to directory or file to view

Optional<List<Long>> viewRange

Optional line range for viewing specific lines



class BetaMessage:



String id

Unique object identifier.

The format and length of IDs may change over time.



Optional<[BetaContainer](api/beta/messages.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.



Optional<List<[BetaSkill](api/beta/messages.md)>> skills

Skills loaded in the container

String skillId

Skill ID



Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version



List<[BetaContentBlock](api/beta/messages.md)> content

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

class BetaTextBlock:



Optional<List<[BetaTextCitation](api/beta/messages.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant



class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant



class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant



class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaServerToolUseBlock:

String id

Input input



Name name

One of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebSearchToolResultBlock:



[BetaWebSearchToolResultBlockContent](api/beta/messages.md) content

One of the following:



class BetaWebSearchToolResultError:



[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant



List<[BetaWebSearchResultBlock](api/beta/messages.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebFetchToolResultBlock:



Content content

One of the following:



class BetaWebFetchToolResultErrorBlock:



[BetaWebFetchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_IN\_PRIOR\_CONTEXT("url\_not\_in\_prior\_context")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant



class BetaWebFetchBlock:



[BetaDocumentBlock](api/beta/messages.md) content



Optional<[BetaCitationConfig](api/beta/messages.md)> citations

Citation configuration for the document

boolean enabled



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaAdvisorToolResultBlock:



Content content

One of the following:



class BetaAdvisorToolResultError:



ErrorCode errorCode

One of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

MODEL\_NOT\_FOUND("model\_not\_found")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant



class BetaAdvisorResultBlock:

Optional<String> stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant



class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

Optional<String> stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant



class BetaCodeExecutionToolResultBlock:



[BetaCodeExecutionToolResultBlockContent](api/beta/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError:



[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



class BetaCodeExecutionResultBlock:



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant



class BetaBashCodeExecutionToolResultBlock:



Content content

One of the following:



class BetaBashCodeExecutionToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant



class BetaBashCodeExecutionResultBlock:



List<[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant



class BetaTextEditorCodeExecutionToolResultBlock:



Content content

One of the following:



class BetaTextEditorCodeExecutionToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant



class BetaTextEditorCodeExecutionViewResultBlock:

String content



FileType fileType

One of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant



class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant



class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant



class BetaToolSearchToolResultBlock:



Content content

One of the following:



class BetaToolSearchToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant



class BetaToolSearchToolSearchResultBlock:



List<[BetaToolReferenceBlock](api/beta/messages.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant



class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant



class BetaMcpToolResultBlock:



Content content

One of the following:

String



List<[BetaTextBlock](api/beta/messages.md)>



Optional<List<[BetaTextCitation](api/beta/messages.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant



class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant



class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction"constant"compaction"constant



class BetaFallbackBlock:

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

[BetaFallbackInfo](api/beta/messages.md) from

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackInfo](api/beta/messages.md) to

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackRefusalTrigger](api/beta/messages.md) trigger

What caused the `from` model to hand over at this hop.



Optional<Category> category

The policy category that triggered a refusal.

One of the following:

CYBER("cyber")

BIO("bio")

FRONTIER\_LLM("frontier\_llm")

REASONING\_EXTRACTION("reasoning\_extraction")

JsonValue; type "refusal"constant"refusal"constant

JsonValue; type "fallback"constant"fallback"constant



Optional<[BetaContextManagementResponse](api/beta/messages.md)> contextManagement

Context management response.

Information about context management strategies applied during the request.



List<AppliedEdit> appliedEdits

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.



class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.



Optional<[BetaDiagnostics](api/beta/messages.md)> diagnostics

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



Optional<CacheMissReason> cacheMissReason

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



class BetaCacheMissModelChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "model\_changed"constant"model\_changed"constant



class BetaCacheMissSystemChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "system\_changed"constant"system\_changed"constant



class BetaCacheMissToolsChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "tools\_changed"constant"tools\_changed"constant



class BetaCacheMissMessagesChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "messages\_changed"constant"messages\_changed"constant



class BetaCacheMissPreviousMessageNotFound:

JsonValue; type "previous\_message\_not\_found"constant"previous\_message\_not\_found"constant



class BetaCacheMissUnavailable:

JsonValue; type "unavailable"constant"unavailable"constant



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



JsonValue; role "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.



Optional<[BetaRefusalStopDetails](api/beta/messages.md)> stopDetails

Structured information about a refusal.



Optional<Category> category

The policy category that triggered a refusal.

One of the following:

CYBER("cyber")

BIO("bio")

FRONTIER\_LLM("frontier\_llm")

REASONING\_EXTRACTION("reasoning\_extraction")



Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



Optional<String> fallbackCreditToken

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

Optional<Boolean> fallbackHasPrefillClaim

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

Optional<String> recommendedModel

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

JsonValue; type "refusal"constant"refusal"constant



Optional<[BetaStopReason](api/beta/messages.md)> stopReason

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

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")



Optional<String> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



JsonValue; type "message"constant"message"constant

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

Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional<Long> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The number of input tokens read from the cache.

Optional<String> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.



Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage:

Token usage for a sampling iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration



class BetaCompactionIterationUsage:

Token usage for a compaction iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage:

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "fallback\_message"constant"fallback\_message"constant

Usage for the fallback-model attempt that served the response

long outputTokens

The number of output tokens which were used.



Optional<[BetaOutputTokensDetails](api/beta/messages.md)> outputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



long thinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



Optional<[BetaServerToolUsage](api/beta/messages.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.



Optional<ServiceTier> serviceTier

If the request used the priority, standard, or batch tier.

One of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")



Optional<Speed> speed

The inference speed mode used for this request.

One of the following:

STANDARD("standard")

FAST("fast")



class BetaMessageDeltaUsage:

Optional<Long> cacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The cumulative number of input tokens read from the cache.

Optional<Long> inputTokens

The cumulative number of input tokens which were used.



Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage:

Token usage for a sampling iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration



class BetaCompactionIterationUsage:

Token usage for a compaction iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage:

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "fallback\_message"constant"fallback\_message"constant

Usage for the fallback-model attempt that served the response

long outputTokens

The cumulative number of output tokens which were used.



Optional<[BetaOutputTokensDetails](api/beta/messages.md)> outputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



long thinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



Optional<[BetaServerToolUsage](api/beta/messages.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.



class BetaMessageIterationUsage:

Token usage for a sampling iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration



class BetaMessageParam:



Content content

One of the following:

String



List<[BetaContentBlockParam](api/beta/messages.md)>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaRequestDocumentBlock:



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant



class BetaContentBlockSource:



Content content

One of the following:

String



List<[BetaContentBlockSourceContent](api/beta/messages.md)>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant



class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title



class BetaSearchResultBlockParam:



List<[BetaTextBlockParam](api/beta/messages.md)> content

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String source

String title

JsonValue; type "search\_result"constant"search\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled



class BetaThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant



class BetaRedactedThinkingBlockParam:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant



class BetaToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaToolResultBlockParam:

String toolUseId

JsonValue; type "tool\_result"constant"tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Content> content

One of the following:

String



List<Block>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaSearchResultBlockParam:



List<[BetaTextBlockParam](api/beta/messages.md)> content

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String source

String title

JsonValue; type "search\_result"constant"search\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled



class BetaRequestDocumentBlock:



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant



class BetaContentBlockSource:



Content content

One of the following:

String



List<[BetaContentBlockSourceContent](api/beta/messages.md)>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant



class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title



class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> isError



class BetaServerToolUseBlockParam:

String id

Input input



Name name

One of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebSearchToolResultBlockParam:



[BetaWebSearchToolResultBlockParamContent](api/beta/messages.md) content

One of the following:



List<[BetaWebSearchResultBlockParam](api/beta/messages.md)>

String encryptedContent

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

Optional<String> pageAge



class BetaWebSearchToolRequestError:



[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebFetchToolResultBlockParam:



Content content

One of the following:



class BetaWebFetchToolResultErrorBlockParam:



[BetaWebFetchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_IN\_PRIOR\_CONTEXT("url\_not\_in\_prior\_context")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant



class BetaWebFetchBlockParam:



[BetaRequestDocumentBlock](api/beta/messages.md) content



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant



class BetaContentBlockSource:



Content content

One of the following:

String



List<[BetaContentBlockSourceContent](api/beta/messages.md)>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant



class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaAdvisorToolResultBlockParam:



Content content

One of the following:



class BetaAdvisorToolResultErrorParam:



ErrorCode errorCode

One of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

MODEL\_NOT\_FOUND("model\_not\_found")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant



class BetaAdvisorResultBlockParam:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

Optional<String> stopReason



class BetaAdvisorRedactedResultBlockParam:

String encryptedContent

Opaque blob produced by a prior response; must be round-tripped verbatim.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

Optional<String> stopReason

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaCodeExecutionToolResultBlockParam:



[BetaCodeExecutionToolResultBlockParamContent](api/beta/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultErrorParam:



[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



class BetaCodeExecutionResultBlockParam:



List<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaBashCodeExecutionToolResultBlockParam:



Content content

One of the following:



class BetaBashCodeExecutionToolResultErrorParam:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant



class BetaBashCodeExecutionResultBlockParam:



List<[BetaBashCodeExecutionOutputBlockParam](api/beta/messages.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaTextEditorCodeExecutionToolResultBlockParam:



Content content

One of the following:



class BetaTextEditorCodeExecutionToolResultErrorParam:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Optional<String> errorMessage



class BetaTextEditorCodeExecutionViewResultBlockParam:

String content



FileType fileType

One of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines



class BetaTextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant



class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaToolSearchToolResultBlockParam:



Content content

One of the following:



class BetaToolSearchToolResultErrorParam:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Optional<String> errorMessage



class BetaToolSearchToolSearchResultBlockParam:



List<[BetaToolReferenceBlockParam](api/beta/messages.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaMcpToolUseBlockParam:

String id

Input input

String name

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaRequestMcpToolResultBlockParam:

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Content> content

One of the following:

String



List<[BetaTextBlockParam](api/beta/messages.md)>

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

Optional<Boolean> isError



class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

JsonValue; type "compaction"constant"compaction"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<String> content

Summary of previously compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim



class BetaMidConversationSystemBlockParam:

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



List<[BetaTextBlockParam](api/beta/messages.md)> content

System instruction text blocks.

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

JsonValue; type "mid\_conv\_system"constant"mid\_conv\_system"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaFallbackBlockParam:

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

[BetaFallbackInfoParam](api/beta/messages.md) from

Identifies one hop of a fallback transition.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackInfoParam](api/beta/messages.md) to

Identifies one hop of a fallback transition.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

JsonValue; type "fallback"constant"fallback"constant

Optional<JsonValue> trigger

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



Role role

One of the following:

USER("user")

ASSISTANT("assistant")

SYSTEM("system")



class BetaMessageTokensCount:



Optional<[BetaCountTokensContextManagementResponse](api/beta/messages.md)> contextManagement

Information about context management applied to the message.

long originalInputTokens

The original token count before context management was applied

long inputTokens

The total number of tokens across the provided list of messages, system prompt, and tools.



class BetaMetadata:



Optional<String> userId

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



class BetaMidConversationSystemBlockParam:

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



List<[BetaTextBlockParam](api/beta/messages.md)> content

System instruction text blocks.

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

JsonValue; type "mid\_conv\_system"constant"mid\_conv\_system"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaOutputConfig:



Optional<Effort> effort

All possible effort levels.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

XHIGH("xhigh")

MAX("max")



Optional<[BetaJsonOutputFormat](api/beta/messages.md)> format

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

Schema schema

The JSON schema of the format

JsonValue; type "json\_schema"constant"json\_schema"constant



Optional<[BetaTokenTaskBudget](api/beta/messages.md)> taskBudget

User-configurable total token budget across contexts.

long total

Total token budget across all contexts in the session.

JsonValue; type "tokens"constant"tokens"constant

The budget type. Currently only 'tokens' is supported.

Optional<Long> remaining

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



class BetaOutputTokensDetails:



long thinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant



class BetaRawContentBlockDelta: A class that can be one of several variants.union 



class BetaTextDelta:

String text

JsonValue; type "text\_delta"constant"text\_delta"constant



class BetaInputJsonDelta:

String partialJson

JsonValue; type "input\_json\_delta"constant"input\_json\_delta"constant



class BetaCitationsDelta:



Citation citation

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

JsonValue; type "citations\_delta"constant"citations\_delta"constant



class BetaThinkingDelta:

Optional<Long> estimatedTokens

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

String thinking

JsonValue; type "thinking\_delta"constant"thinking\_delta"constant



class BetaSignatureDelta:

String signature

JsonValue; type "signature\_delta"constant"signature\_delta"constant



class BetaCompactionContentBlockDelta:

Optional<String> content

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction\_delta"constant"compaction\_delta"constant



class BetaRawContentBlockDeltaEvent:



[BetaRawContentBlockDelta](api/beta/messages.md) delta

One of the following:



class BetaTextDelta:

String text

JsonValue; type "text\_delta"constant"text\_delta"constant



class BetaInputJsonDelta:

String partialJson

JsonValue; type "input\_json\_delta"constant"input\_json\_delta"constant



class BetaCitationsDelta:



Citation citation

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

JsonValue; type "citations\_delta"constant"citations\_delta"constant



class BetaThinkingDelta:

Optional<Long> estimatedTokens

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

String thinking

JsonValue; type "thinking\_delta"constant"thinking\_delta"constant



class BetaSignatureDelta:

String signature

JsonValue; type "signature\_delta"constant"signature\_delta"constant



class BetaCompactionContentBlockDelta:

Optional<String> content

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction\_delta"constant"compaction\_delta"constant

long index

JsonValue; type "content\_block\_delta"constant"content\_block\_delta"constant



class BetaRawContentBlockStartEvent:



ContentBlock contentBlock

Response model for a file uploaded to the container.

One of the following:



class BetaTextBlock:



Optional<List<[BetaTextCitation](api/beta/messages.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant



class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant



class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant



class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaServerToolUseBlock:

String id

Input input



Name name

One of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebSearchToolResultBlock:



[BetaWebSearchToolResultBlockContent](api/beta/messages.md) content

One of the following:



class BetaWebSearchToolResultError:



[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant



List<[BetaWebSearchResultBlock](api/beta/messages.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebFetchToolResultBlock:



Content content

One of the following:



class BetaWebFetchToolResultErrorBlock:



[BetaWebFetchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_IN\_PRIOR\_CONTEXT("url\_not\_in\_prior\_context")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant



class BetaWebFetchBlock:



[BetaDocumentBlock](api/beta/messages.md) content



Optional<[BetaCitationConfig](api/beta/messages.md)> citations

Citation configuration for the document

boolean enabled



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaAdvisorToolResultBlock:



Content content

One of the following:



class BetaAdvisorToolResultError:



ErrorCode errorCode

One of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

MODEL\_NOT\_FOUND("model\_not\_found")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant



class BetaAdvisorResultBlock:

Optional<String> stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant



class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

Optional<String> stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant



class BetaCodeExecutionToolResultBlock:



[BetaCodeExecutionToolResultBlockContent](api/beta/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError:



[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



class BetaCodeExecutionResultBlock:



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant



class BetaBashCodeExecutionToolResultBlock:



Content content

One of the following:



class BetaBashCodeExecutionToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant



class BetaBashCodeExecutionResultBlock:



List<[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant



class BetaTextEditorCodeExecutionToolResultBlock:



Content content

One of the following:



class BetaTextEditorCodeExecutionToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant



class BetaTextEditorCodeExecutionViewResultBlock:

String content



FileType fileType

One of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant



class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant



class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant



class BetaToolSearchToolResultBlock:



Content content

One of the following:



class BetaToolSearchToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant



class BetaToolSearchToolSearchResultBlock:



List<[BetaToolReferenceBlock](api/beta/messages.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant



class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant



class BetaMcpToolResultBlock:



Content content

One of the following:

String



List<[BetaTextBlock](api/beta/messages.md)>



Optional<List<[BetaTextCitation](api/beta/messages.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant



class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant



class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction"constant"compaction"constant



class BetaFallbackBlock:

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

[BetaFallbackInfo](api/beta/messages.md) from

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackInfo](api/beta/messages.md) to

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackRefusalTrigger](api/beta/messages.md) trigger

What caused the `from` model to hand over at this hop.



Optional<Category> category

The policy category that triggered a refusal.

One of the following:

CYBER("cyber")

BIO("bio")

FRONTIER\_LLM("frontier\_llm")

REASONING\_EXTRACTION("reasoning\_extraction")

JsonValue; type "refusal"constant"refusal"constant

JsonValue; type "fallback"constant"fallback"constant

long index

JsonValue; type "content\_block\_start"constant"content\_block\_start"constant



class BetaRawContentBlockStopEvent:

long index

JsonValue; type "content\_block\_stop"constant"content\_block\_stop"constant



class BetaRawMessageDeltaEvent:



Optional<[BetaContextManagementResponse](api/beta/messages.md)> contextManagement

Information about context management strategies applied during the request



List<AppliedEdit> appliedEdits

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.



class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.



Delta delta



Optional<[BetaContainer](api/beta/messages.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.



Optional<List<[BetaSkill](api/beta/messages.md)>> skills

Skills loaded in the container

String skillId

Skill ID



Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version



Optional<[BetaRefusalStopDetails](api/beta/messages.md)> stopDetails

Structured information about a refusal.



Optional<Category> category

The policy category that triggered a refusal.

One of the following:

CYBER("cyber")

BIO("bio")

FRONTIER\_LLM("frontier\_llm")

REASONING\_EXTRACTION("reasoning\_extraction")



Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



Optional<String> fallbackCreditToken

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

Optional<Boolean> fallbackHasPrefillClaim

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

Optional<String> recommendedModel

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

JsonValue; type "refusal"constant"refusal"constant



Optional<[BetaStopReason](api/beta/messages.md)> stopReason

One of the following:

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

Optional<String> stopSequence

JsonValue; type "message\_delta"constant"message\_delta"constant



[BetaMessageDeltaUsage](api/beta/messages.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional<Long> cacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The cumulative number of input tokens read from the cache.

Optional<Long> inputTokens

The cumulative number of input tokens which were used.



Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage:

Token usage for a sampling iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration



class BetaCompactionIterationUsage:

Token usage for a compaction iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage:

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "fallback\_message"constant"fallback\_message"constant

Usage for the fallback-model attempt that served the response

long outputTokens

The cumulative number of output tokens which were used.



Optional<[BetaOutputTokensDetails](api/beta/messages.md)> outputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



long thinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



Optional<[BetaServerToolUsage](api/beta/messages.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.



class BetaRawMessageStartEvent:



[BetaMessage](api/beta/messages.md) message



String id

Unique object identifier.

The format and length of IDs may change over time.



Optional<[BetaContainer](api/beta/messages.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.



Optional<List<[BetaSkill](api/beta/messages.md)>> skills

Skills loaded in the container

String skillId

Skill ID



Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version



List<[BetaContentBlock](api/beta/messages.md)> content

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

class BetaTextBlock:



Optional<List<[BetaTextCitation](api/beta/messages.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant



class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant



class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant



class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaServerToolUseBlock:

String id

Input input



Name name

One of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebSearchToolResultBlock:



[BetaWebSearchToolResultBlockContent](api/beta/messages.md) content

One of the following:



class BetaWebSearchToolResultError:



[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant



List<[BetaWebSearchResultBlock](api/beta/messages.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebFetchToolResultBlock:



Content content

One of the following:



class BetaWebFetchToolResultErrorBlock:



[BetaWebFetchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_IN\_PRIOR\_CONTEXT("url\_not\_in\_prior\_context")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant



class BetaWebFetchBlock:



[BetaDocumentBlock](api/beta/messages.md) content



Optional<[BetaCitationConfig](api/beta/messages.md)> citations

Citation configuration for the document

boolean enabled



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaAdvisorToolResultBlock:



Content content

One of the following:



class BetaAdvisorToolResultError:



ErrorCode errorCode

One of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

MODEL\_NOT\_FOUND("model\_not\_found")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant



class BetaAdvisorResultBlock:

Optional<String> stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant



class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

Optional<String> stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant



class BetaCodeExecutionToolResultBlock:



[BetaCodeExecutionToolResultBlockContent](api/beta/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError:



[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



class BetaCodeExecutionResultBlock:



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant



class BetaBashCodeExecutionToolResultBlock:



Content content

One of the following:



class BetaBashCodeExecutionToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant



class BetaBashCodeExecutionResultBlock:



List<[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant



class BetaTextEditorCodeExecutionToolResultBlock:



Content content

One of the following:



class BetaTextEditorCodeExecutionToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant



class BetaTextEditorCodeExecutionViewResultBlock:

String content



FileType fileType

One of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant



class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant



class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant



class BetaToolSearchToolResultBlock:



Content content

One of the following:



class BetaToolSearchToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant



class BetaToolSearchToolSearchResultBlock:



List<[BetaToolReferenceBlock](api/beta/messages.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant



class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant



class BetaMcpToolResultBlock:



Content content

One of the following:

String



List<[BetaTextBlock](api/beta/messages.md)>



Optional<List<[BetaTextCitation](api/beta/messages.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant



class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant



class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction"constant"compaction"constant



class BetaFallbackBlock:

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

[BetaFallbackInfo](api/beta/messages.md) from

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackInfo](api/beta/messages.md) to

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackRefusalTrigger](api/beta/messages.md) trigger

What caused the `from` model to hand over at this hop.



Optional<Category> category

The policy category that triggered a refusal.

One of the following:

CYBER("cyber")

BIO("bio")

FRONTIER\_LLM("frontier\_llm")

REASONING\_EXTRACTION("reasoning\_extraction")

JsonValue; type "refusal"constant"refusal"constant

JsonValue; type "fallback"constant"fallback"constant



Optional<[BetaContextManagementResponse](api/beta/messages.md)> contextManagement

Context management response.

Information about context management strategies applied during the request.



List<AppliedEdit> appliedEdits

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.



class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.



Optional<[BetaDiagnostics](api/beta/messages.md)> diagnostics

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



Optional<CacheMissReason> cacheMissReason

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



class BetaCacheMissModelChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "model\_changed"constant"model\_changed"constant



class BetaCacheMissSystemChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "system\_changed"constant"system\_changed"constant



class BetaCacheMissToolsChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "tools\_changed"constant"tools\_changed"constant



class BetaCacheMissMessagesChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "messages\_changed"constant"messages\_changed"constant



class BetaCacheMissPreviousMessageNotFound:

JsonValue; type "previous\_message\_not\_found"constant"previous\_message\_not\_found"constant



class BetaCacheMissUnavailable:

JsonValue; type "unavailable"constant"unavailable"constant



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



JsonValue; role "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.



Optional<[BetaRefusalStopDetails](api/beta/messages.md)> stopDetails

Structured information about a refusal.



Optional<Category> category

The policy category that triggered a refusal.

One of the following:

CYBER("cyber")

BIO("bio")

FRONTIER\_LLM("frontier\_llm")

REASONING\_EXTRACTION("reasoning\_extraction")



Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



Optional<String> fallbackCreditToken

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

Optional<Boolean> fallbackHasPrefillClaim

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

Optional<String> recommendedModel

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

JsonValue; type "refusal"constant"refusal"constant



Optional<[BetaStopReason](api/beta/messages.md)> stopReason

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

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")



Optional<String> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



JsonValue; type "message"constant"message"constant

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

Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional<Long> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The number of input tokens read from the cache.

Optional<String> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.



Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage:

Token usage for a sampling iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration



class BetaCompactionIterationUsage:

Token usage for a compaction iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage:

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "fallback\_message"constant"fallback\_message"constant

Usage for the fallback-model attempt that served the response

long outputTokens

The number of output tokens which were used.



Optional<[BetaOutputTokensDetails](api/beta/messages.md)> outputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



long thinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



Optional<[BetaServerToolUsage](api/beta/messages.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.



Optional<ServiceTier> serviceTier

If the request used the priority, standard, or batch tier.

One of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")



Optional<Speed> speed

The inference speed mode used for this request.

One of the following:

STANDARD("standard")

FAST("fast")

JsonValue; type "message\_start"constant"message\_start"constant



class BetaRawMessageStopEvent:

JsonValue; type "message\_stop"constant"message\_stop"constant



class BetaRawMessageStreamEvent: A class that can be one of several variants.union 



class BetaRawMessageStartEvent:



[BetaMessage](api/beta/messages.md) message



String id

Unique object identifier.

The format and length of IDs may change over time.



Optional<[BetaContainer](api/beta/messages.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.



Optional<List<[BetaSkill](api/beta/messages.md)>> skills

Skills loaded in the container

String skillId

Skill ID



Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version



List<[BetaContentBlock](api/beta/messages.md)> content

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

class BetaTextBlock:



Optional<List<[BetaTextCitation](api/beta/messages.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant



class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant



class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant



class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaServerToolUseBlock:

String id

Input input



Name name

One of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebSearchToolResultBlock:



[BetaWebSearchToolResultBlockContent](api/beta/messages.md) content

One of the following:



class BetaWebSearchToolResultError:



[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant



List<[BetaWebSearchResultBlock](api/beta/messages.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebFetchToolResultBlock:



Content content

One of the following:



class BetaWebFetchToolResultErrorBlock:



[BetaWebFetchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_IN\_PRIOR\_CONTEXT("url\_not\_in\_prior\_context")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant



class BetaWebFetchBlock:



[BetaDocumentBlock](api/beta/messages.md) content



Optional<[BetaCitationConfig](api/beta/messages.md)> citations

Citation configuration for the document

boolean enabled



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaAdvisorToolResultBlock:



Content content

One of the following:



class BetaAdvisorToolResultError:



ErrorCode errorCode

One of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

MODEL\_NOT\_FOUND("model\_not\_found")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant



class BetaAdvisorResultBlock:

Optional<String> stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant



class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

Optional<String> stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant



class BetaCodeExecutionToolResultBlock:



[BetaCodeExecutionToolResultBlockContent](api/beta/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError:



[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



class BetaCodeExecutionResultBlock:



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant



class BetaBashCodeExecutionToolResultBlock:



Content content

One of the following:



class BetaBashCodeExecutionToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant



class BetaBashCodeExecutionResultBlock:



List<[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant



class BetaTextEditorCodeExecutionToolResultBlock:



Content content

One of the following:



class BetaTextEditorCodeExecutionToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant



class BetaTextEditorCodeExecutionViewResultBlock:

String content



FileType fileType

One of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant



class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant



class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant



class BetaToolSearchToolResultBlock:



Content content

One of the following:



class BetaToolSearchToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant



class BetaToolSearchToolSearchResultBlock:



List<[BetaToolReferenceBlock](api/beta/messages.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant



class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant



class BetaMcpToolResultBlock:



Content content

One of the following:

String



List<[BetaTextBlock](api/beta/messages.md)>



Optional<List<[BetaTextCitation](api/beta/messages.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant



class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant



class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction"constant"compaction"constant



class BetaFallbackBlock:

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

[BetaFallbackInfo](api/beta/messages.md) from

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackInfo](api/beta/messages.md) to

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackRefusalTrigger](api/beta/messages.md) trigger

What caused the `from` model to hand over at this hop.



Optional<Category> category

The policy category that triggered a refusal.

One of the following:

CYBER("cyber")

BIO("bio")

FRONTIER\_LLM("frontier\_llm")

REASONING\_EXTRACTION("reasoning\_extraction")

JsonValue; type "refusal"constant"refusal"constant

JsonValue; type "fallback"constant"fallback"constant



Optional<[BetaContextManagementResponse](api/beta/messages.md)> contextManagement

Context management response.

Information about context management strategies applied during the request.



List<AppliedEdit> appliedEdits

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.



class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.



Optional<[BetaDiagnostics](api/beta/messages.md)> diagnostics

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



Optional<CacheMissReason> cacheMissReason

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



class BetaCacheMissModelChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "model\_changed"constant"model\_changed"constant



class BetaCacheMissSystemChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "system\_changed"constant"system\_changed"constant



class BetaCacheMissToolsChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "tools\_changed"constant"tools\_changed"constant



class BetaCacheMissMessagesChanged:

long cacheMissedInputTokens

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

JsonValue; type "messages\_changed"constant"messages\_changed"constant



class BetaCacheMissPreviousMessageNotFound:

JsonValue; type "previous\_message\_not\_found"constant"previous\_message\_not\_found"constant



class BetaCacheMissUnavailable:

JsonValue; type "unavailable"constant"unavailable"constant



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



JsonValue; role "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.



Optional<[BetaRefusalStopDetails](api/beta/messages.md)> stopDetails

Structured information about a refusal.



Optional<Category> category

The policy category that triggered a refusal.

One of the following:

CYBER("cyber")

BIO("bio")

FRONTIER\_LLM("frontier\_llm")

REASONING\_EXTRACTION("reasoning\_extraction")



Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



Optional<String> fallbackCreditToken

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

Optional<Boolean> fallbackHasPrefillClaim

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

Optional<String> recommendedModel

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

JsonValue; type "refusal"constant"refusal"constant



Optional<[BetaStopReason](api/beta/messages.md)> stopReason

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

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")



Optional<String> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



JsonValue; type "message"constant"message"constant

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

Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional<Long> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The number of input tokens read from the cache.

Optional<String> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.



Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage:

Token usage for a sampling iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration



class BetaCompactionIterationUsage:

Token usage for a compaction iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage:

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "fallback\_message"constant"fallback\_message"constant

Usage for the fallback-model attempt that served the response

long outputTokens

The number of output tokens which were used.



Optional<[BetaOutputTokensDetails](api/beta/messages.md)> outputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



long thinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



Optional<[BetaServerToolUsage](api/beta/messages.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.



Optional<ServiceTier> serviceTier

If the request used the priority, standard, or batch tier.

One of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")



Optional<Speed> speed

The inference speed mode used for this request.

One of the following:

STANDARD("standard")

FAST("fast")

JsonValue; type "message\_start"constant"message\_start"constant



class BetaRawMessageDeltaEvent:



Optional<[BetaContextManagementResponse](api/beta/messages.md)> contextManagement

Information about context management strategies applied during the request



List<AppliedEdit> appliedEdits

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.



class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.



Delta delta



Optional<[BetaContainer](api/beta/messages.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.



Optional<List<[BetaSkill](api/beta/messages.md)>> skills

Skills loaded in the container

String skillId

Skill ID



Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version



Optional<[BetaRefusalStopDetails](api/beta/messages.md)> stopDetails

Structured information about a refusal.



Optional<Category> category

The policy category that triggered a refusal.

One of the following:

CYBER("cyber")

BIO("bio")

FRONTIER\_LLM("frontier\_llm")

REASONING\_EXTRACTION("reasoning\_extraction")



Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



Optional<String> fallbackCreditToken

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

Optional<Boolean> fallbackHasPrefillClaim

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

Optional<String> recommendedModel

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

JsonValue; type "refusal"constant"refusal"constant



Optional<[BetaStopReason](api/beta/messages.md)> stopReason

One of the following:

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

Optional<String> stopSequence

JsonValue; type "message\_delta"constant"message\_delta"constant



[BetaMessageDeltaUsage](api/beta/messages.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional<Long> cacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The cumulative number of input tokens read from the cache.

Optional<Long> inputTokens

The cumulative number of input tokens which were used.



Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage:

Token usage for a sampling iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration



class BetaCompactionIterationUsage:

Token usage for a compaction iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage:

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "fallback\_message"constant"fallback\_message"constant

Usage for the fallback-model attempt that served the response

long outputTokens

The cumulative number of output tokens which were used.



Optional<[BetaOutputTokensDetails](api/beta/messages.md)> outputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



long thinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



Optional<[BetaServerToolUsage](api/beta/messages.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.



class BetaRawMessageStopEvent:

JsonValue; type "message\_stop"constant"message\_stop"constant



class BetaRawContentBlockStartEvent:



ContentBlock contentBlock

Response model for a file uploaded to the container.

One of the following:



class BetaTextBlock:



Optional<List<[BetaTextCitation](api/beta/messages.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant



class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant



class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant



class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaServerToolUseBlock:

String id

Input input



Name name

One of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebSearchToolResultBlock:



[BetaWebSearchToolResultBlockContent](api/beta/messages.md) content

One of the following:



class BetaWebSearchToolResultError:



[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant



List<[BetaWebSearchResultBlock](api/beta/messages.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebFetchToolResultBlock:



Content content

One of the following:



class BetaWebFetchToolResultErrorBlock:



[BetaWebFetchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_IN\_PRIOR\_CONTEXT("url\_not\_in\_prior\_context")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant



class BetaWebFetchBlock:



[BetaDocumentBlock](api/beta/messages.md) content



Optional<[BetaCitationConfig](api/beta/messages.md)> citations

Citation configuration for the document

boolean enabled



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaAdvisorToolResultBlock:



Content content

One of the following:



class BetaAdvisorToolResultError:



ErrorCode errorCode

One of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

MODEL\_NOT\_FOUND("model\_not\_found")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant



class BetaAdvisorResultBlock:

Optional<String> stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant



class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

Optional<String> stopReason

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant



class BetaCodeExecutionToolResultBlock:



[BetaCodeExecutionToolResultBlockContent](api/beta/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError:



[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



class BetaCodeExecutionResultBlock:



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[BetaCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant



class BetaBashCodeExecutionToolResultBlock:



Content content

One of the following:



class BetaBashCodeExecutionToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant



class BetaBashCodeExecutionResultBlock:



List<[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant



class BetaTextEditorCodeExecutionToolResultBlock:



Content content

One of the following:



class BetaTextEditorCodeExecutionToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant



class BetaTextEditorCodeExecutionViewResultBlock:

String content



FileType fileType

One of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant



class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant



class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant



class BetaToolSearchToolResultBlock:



Content content

One of the following:



class BetaToolSearchToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant



class BetaToolSearchToolSearchResultBlock:



List<[BetaToolReferenceBlock](api/beta/messages.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant



class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant



class BetaMcpToolResultBlock:



Content content

One of the following:

String



List<[BetaTextBlock](api/beta/messages.md)>



Optional<List<[BetaTextCitation](api/beta/messages.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant



class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant



class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction"constant"compaction"constant



class BetaFallbackBlock:

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

[BetaFallbackInfo](api/beta/messages.md) from

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackInfo](api/beta/messages.md) to

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackRefusalTrigger](api/beta/messages.md) trigger

What caused the `from` model to hand over at this hop.



Optional<Category> category

The policy category that triggered a refusal.

One of the following:

CYBER("cyber")

BIO("bio")

FRONTIER\_LLM("frontier\_llm")

REASONING\_EXTRACTION("reasoning\_extraction")

JsonValue; type "refusal"constant"refusal"constant

JsonValue; type "fallback"constant"fallback"constant

long index

JsonValue; type "content\_block\_start"constant"content\_block\_start"constant



class BetaRawContentBlockDeltaEvent:



[BetaRawContentBlockDelta](api/beta/messages.md) delta

One of the following:



class BetaTextDelta:

String text

JsonValue; type "text\_delta"constant"text\_delta"constant



class BetaInputJsonDelta:

String partialJson

JsonValue; type "input\_json\_delta"constant"input\_json\_delta"constant



class BetaCitationsDelta:



Citation citation

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

JsonValue; type "citations\_delta"constant"citations\_delta"constant



class BetaThinkingDelta:

Optional<Long> estimatedTokens

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

String thinking

JsonValue; type "thinking\_delta"constant"thinking\_delta"constant



class BetaSignatureDelta:

String signature

JsonValue; type "signature\_delta"constant"signature\_delta"constant



class BetaCompactionContentBlockDelta:

Optional<String> content

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction\_delta"constant"compaction\_delta"constant

long index

JsonValue; type "content\_block\_delta"constant"content\_block\_delta"constant



class BetaRawContentBlockStopEvent:

long index

JsonValue; type "content\_block\_stop"constant"content\_block\_stop"constant



class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant



class BetaRedactedThinkingBlockParam:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant



class BetaRefusalStopDetails:

Structured information about a refusal.



Optional<Category> category

The policy category that triggered a refusal.

One of the following:

CYBER("cyber")

BIO("bio")

FRONTIER\_LLM("frontier\_llm")

REASONING\_EXTRACTION("reasoning\_extraction")



Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



Optional<String> fallbackCreditToken

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

Optional<Boolean> fallbackHasPrefillClaim

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

Optional<String> recommendedModel

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

JsonValue; type "refusal"constant"refusal"constant



class BetaRequestDocumentBlock:



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant



class BetaContentBlockSource:



Content content

One of the following:

String



List<[BetaContentBlockSourceContent](api/beta/messages.md)>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant



class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title



class BetaRequestMcpServerToolConfiguration:

Optional<List<String>> allowedTools

Optional<Boolean> enabled



class BetaRequestMcpServerUrlDefinition:

String name

JsonValue; type "url"constant"url"constant

String url

Optional<String> authorizationToken



Optional<[BetaRequestMcpServerToolConfiguration](api/beta/messages.md)> toolConfiguration

Optional<List<String>> allowedTools

Optional<Boolean> enabled



class BetaRequestMcpToolResultBlockParam:

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Content> content

One of the following:

String



List<[BetaTextBlockParam](api/beta/messages.md)>

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

Optional<Boolean> isError



class BetaSearchResultBlockParam:



List<[BetaTextBlockParam](api/beta/messages.md)> content

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String source

String title

JsonValue; type "search\_result"constant"search\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaServerToolUsage:

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.



class BetaServerToolUseBlock:

String id

Input input



Name name

One of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaServerToolUseBlockParam:

String id

Input input



Name name

One of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaSignatureDelta:

String signature

JsonValue; type "signature\_delta"constant"signature\_delta"constant



class BetaSkill:

A skill that was loaded in a container (response model).

String skillId

Skill ID



Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version



class BetaSkillParams:

Specification for a skill to be loaded in a container (request model).

String skillId

Skill ID



Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

Optional<String> version

Skill version or 'latest' for most recent version



enum BetaStopReason:

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")



class BetaTextBlock:



Optional<List<[BetaTextCitation](api/beta/messages.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaTextCitation: A class that can be one of several variants.union 



class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

Optional<String> fileId

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocation:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaTextCitationParam: A class that can be one of several variants.union 



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaTextDelta:

String text

JsonValue; type "text\_delta"constant"text\_delta"constant



class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant



class BetaTextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant



class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant



class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart



class BetaTextEditorCodeExecutionToolResultBlock:



Content content

One of the following:



class BetaTextEditorCodeExecutionToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant



class BetaTextEditorCodeExecutionViewResultBlock:

String content



FileType fileType

One of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant



class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant



class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant



class BetaTextEditorCodeExecutionToolResultBlockParam:



Content content

One of the following:



class BetaTextEditorCodeExecutionToolResultErrorParam:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Optional<String> errorMessage



class BetaTextEditorCodeExecutionViewResultBlockParam:

String content



FileType fileType

One of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines



class BetaTextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant



class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaTextEditorCodeExecutionToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant



class BetaTextEditorCodeExecutionToolResultErrorParam:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Optional<String> errorMessage



class BetaTextEditorCodeExecutionViewResultBlock:

String content



FileType fileType

One of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant



class BetaTextEditorCodeExecutionViewResultBlockParam:

String content



FileType fileType

One of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines



class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant



class BetaThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant



class BetaThinkingConfigAdaptive:

JsonValue; type "adaptive"constant"adaptive"constant



Optional<Display> display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

SUMMARIZED("summarized")

OMITTED("omitted")



class BetaThinkingConfigDisabled:

JsonValue; type "disabled"constant"disabled"constant



class BetaThinkingConfigEnabled:



long budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

JsonValue; type "enabled"constant"enabled"constant



Optional<Display> display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

SUMMARIZED("summarized")

OMITTED("omitted")



class BetaThinkingConfigParam: A class that can be one of several variants.union 

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](build-with-claude/extended-thinking.md) for details.



class BetaThinkingConfigEnabled:



long budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

JsonValue; type "enabled"constant"enabled"constant



Optional<Display> display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

SUMMARIZED("summarized")

OMITTED("omitted")



class BetaThinkingConfigDisabled:

JsonValue; type "disabled"constant"disabled"constant



class BetaThinkingConfigAdaptive:

JsonValue; type "adaptive"constant"adaptive"constant



Optional<Display> display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

SUMMARIZED("summarized")

OMITTED("omitted")



class BetaThinkingDelta:

Optional<Long> estimatedTokens

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

String thinking

JsonValue; type "thinking\_delta"constant"thinking\_delta"constant



class BetaThinkingTurns:

JsonValue; type "thinking\_turns"constant"thinking\_turns"constant

long value



class BetaTokenTaskBudget:

User-configurable total token budget across contexts.

long total

Total token budget across all contexts in the session.

JsonValue; type "tokens"constant"tokens"constant

The budget type. Currently only 'tokens' is supported.

Optional<Long> remaining

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



class BetaTool:



InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required



String name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



Optional<String> description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Optional<Boolean> eagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

Optional<Type> type



class BetaToolBash20241022:



JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "bash\_20241022"constant"bash\_20241022"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolBash20250124:



JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "bash\_20250124"constant"bash\_20250124"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolChoice: A class that can be one of several variants.union 

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.



class BetaToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonValue; type "auto"constant"auto"constant



Optional<Boolean> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



class BetaToolChoiceAny:

The model will use any available tools.

JsonValue; type "any"constant"any"constant



Optional<Boolean> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class BetaToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

String name

The name of the tool to use.

JsonValue; type "tool"constant"tool"constant



Optional<Boolean> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class BetaToolChoiceNone:

The model will not be allowed to use tools.

JsonValue; type "none"constant"none"constant



class BetaToolChoiceAny:

The model will use any available tools.

JsonValue; type "any"constant"any"constant



Optional<Boolean> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class BetaToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonValue; type "auto"constant"auto"constant



Optional<Boolean> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



class BetaToolChoiceNone:

The model will not be allowed to use tools.

JsonValue; type "none"constant"none"constant



class BetaToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

String name

The name of the tool to use.

JsonValue; type "tool"constant"tool"constant



Optional<Boolean> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class BetaToolComputerUse20241022:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.



JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer\_20241022"constant"computer\_20241022"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20250124:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.



JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer\_20250124"constant"computer\_20250124"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20251124:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.



JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer\_20251124"constant"computer\_20251124"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional<Boolean> enableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolReferenceBlock:

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant



class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaToolResultBlockParam:

String toolUseId

JsonValue; type "tool\_result"constant"tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Content> content

One of the following:

String



List<Block>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaSearchResultBlockParam:



List<[BetaTextBlockParam](api/beta/messages.md)> content

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String source

String title

JsonValue; type "search\_result"constant"search\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled



class BetaRequestDocumentBlock:



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant



class BetaContentBlockSource:



Content content

One of the following:

String



List<[BetaContentBlockSourceContent](api/beta/messages.md)>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant



class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title



class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> isError



class BetaToolSearchToolBm25\_20251119:



JsonValue; name "tool\_search\_tool\_bm25"constant"tool\_search\_tool\_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



Type type

One of the following:

TOOL\_SEARCH\_TOOL\_BM25\_20251119("tool\_search\_tool\_bm25\_20251119")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolSearchToolRegex20251119:



JsonValue; name "tool\_search\_tool\_regex"constant"tool\_search\_tool\_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



Type type

One of the following:

TOOL\_SEARCH\_TOOL\_REGEX\_20251119("tool\_search\_tool\_regex\_20251119")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolSearchToolResultBlock:



Content content

One of the following:



class BetaToolSearchToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant



class BetaToolSearchToolSearchResultBlock:



List<[BetaToolReferenceBlock](api/beta/messages.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant



class BetaToolSearchToolResultBlockParam:



Content content

One of the following:



class BetaToolSearchToolResultErrorParam:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Optional<String> errorMessage



class BetaToolSearchToolSearchResultBlockParam:



List<[BetaToolReferenceBlockParam](api/beta/messages.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaToolSearchToolResultError:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant



class BetaToolSearchToolResultErrorParam:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Optional<String> errorMessage



class BetaToolSearchToolSearchResultBlock:



List<[BetaToolReferenceBlock](api/beta/messages.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant



class BetaToolSearchToolSearchResultBlockParam:



List<[BetaToolReferenceBlockParam](api/beta/messages.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant



class BetaToolTextEditor20241022:



JsonValue; name "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20241022"constant"text\_editor\_20241022"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250124:



JsonValue; name "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20250124"constant"text\_editor\_20250124"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250429:



JsonValue; name "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20250429"constant"text\_editor\_20250429"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250728:



JsonValue; name "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20250728"constant"text\_editor\_20250728"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Long> maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolUnion: A class that can be one of several variants.union 

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



class BetaTool:



InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required



String name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



Optional<String> description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Optional<Boolean> eagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

Optional<Type> type



class BetaToolBash20241022:



JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "bash\_20241022"constant"bash\_20241022"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolBash20250124:



JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "bash\_20250124"constant"bash\_20250124"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20250522:



JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20250522"constant"code\_execution\_20250522"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20250825:



JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20260120:

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20260521:

Code execution tool with REPL state persistence.



JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20260521"constant"code\_execution\_20260521"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20241022:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.



JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer\_20241022"constant"computer\_20241022"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaMemoryTool20250818:



JsonValue; name "memory"constant"memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "memory\_20250818"constant"memory\_20250818"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20250124:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.



JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer\_20250124"constant"computer\_20250124"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20241022:



JsonValue; name "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20241022"constant"text\_editor\_20241022"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20251124:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.



JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer\_20251124"constant"computer\_20251124"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional<Boolean> enableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250124:



JsonValue; name "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20250124"constant"text\_editor\_20250124"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250429:



JsonValue; name "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20250429"constant"text\_editor\_20250429"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250728:



JsonValue; name "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20250728"constant"text\_editor\_20250728"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Long> maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaWebSearchTool20250305:



JsonValue; name "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_search\_20250305"constant"web\_search\_20250305"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional<List<String>> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



Optional<[BetaUserLocation](api/beta/messages.md)> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

The city of the user.

Optional<String> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional<String> region

The region of the user.

Optional<String> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebFetchTool20250910:



JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20250910"constant"web\_fetch\_20250910"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaWebSearchTool20260209:



JsonValue; name "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_search\_20260209"constant"web\_search\_20260209"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional<List<String>> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



Optional<[BetaUserLocation](api/beta/messages.md)> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

The city of the user.

Optional<String> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional<String> region

The region of the user.

Optional<String> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebFetchTool20260209:



JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20260209"constant"web\_fetch\_20260209"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaWebFetchTool20260309:

Web fetch tool with use\_cache parameter for bypassing cached content.



JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20260309"constant"web\_fetch\_20260309"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

Optional<Boolean> useCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class BetaWebSearchTool20260318:



JsonValue; name "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_search\_20260318"constant"web\_search\_20260318"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional<List<String>> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.



Optional<ResponseInclusion> responseInclusion

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

FULL("full")

EXCLUDED("excluded")

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



Optional<[BetaUserLocation](api/beta/messages.md)> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

The city of the user.

Optional<String> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional<String> region

The region of the user.

Optional<String> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebFetchTool20260318:



JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20260318"constant"web\_fetch\_20260318"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.



Optional<ResponseInclusion> responseInclusion

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

FULL("full")

EXCLUDED("excluded")

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

Optional<Boolean> useCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class BetaAdvisorTool20260301:



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



JsonValue; name "advisor"constant"advisor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "advisor\_20260301"constant"advisor\_20260301"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> caching

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxTokens

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolSearchToolBm25\_20251119:



JsonValue; name "tool\_search\_tool\_bm25"constant"tool\_search\_tool\_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



Type type

One of the following:

TOOL\_SEARCH\_TOOL\_BM25\_20251119("tool\_search\_tool\_bm25\_20251119")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolSearchToolRegex20251119:



JsonValue; name "tool\_search\_tool\_regex"constant"tool\_search\_tool\_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



Type type

One of the following:

TOOL\_SEARCH\_TOOL\_REGEX\_20251119("tool\_search\_tool\_regex\_20251119")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaMcpToolset:

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

String mcpServerName

Name of the MCP server to configure tools for

JsonValue; type "mcp\_toolset"constant"mcp\_toolset"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Configs> configs

Configuration overrides for specific tools, keyed by tool name

Optional<Boolean> deferLoading

Optional<Boolean> enabled



Optional<[BetaMcpToolDefaultConfig](api/beta/messages.md)> defaultConfig

Default configuration applied to all tools from this server

Optional<Boolean> deferLoading

Optional<Boolean> enabled



class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaToolUsesKeep:

JsonValue; type "tool\_uses"constant"tool\_uses"constant

long value



class BetaToolUsesTrigger:

JsonValue; type "tool\_uses"constant"tool\_uses"constant

long value



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url



class BetaUsage:



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional<Long> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The number of input tokens read from the cache.

Optional<String> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.



Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage:

Token usage for a sampling iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration



class BetaCompactionIterationUsage:

Token usage for a compaction iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage:

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



Optional<[BetaCacheCreation](api/beta/messages.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

long outputTokens

The number of output tokens which were used.

JsonValue; type "fallback\_message"constant"fallback\_message"constant

Usage for the fallback-model attempt that served the response

long outputTokens

The number of output tokens which were used.



Optional<[BetaOutputTokensDetails](api/beta/messages.md)> outputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



long thinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



Optional<[BetaServerToolUsage](api/beta/messages.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.



Optional<ServiceTier> serviceTier

If the request used the priority, standard, or batch tier.

One of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")



Optional<Speed> speed

The inference speed mode used for this request.

One of the following:

STANDARD("standard")

FAST("fast")



class BetaUserLocation:

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

The city of the user.

Optional<String> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional<String> region

The region of the user.

Optional<String> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebFetchBlock:



[BetaDocumentBlock](api/beta/messages.md) content



Optional<[BetaCitationConfig](api/beta/messages.md)> citations

Citation configuration for the document

boolean enabled



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL



class BetaWebFetchBlockParam:



[BetaRequestDocumentBlock](api/beta/messages.md) content



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant



class BetaContentBlockSource:



Content content

One of the following:

String



List<[BetaContentBlockSourceContent](api/beta/messages.md)>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant



class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved



class BetaWebFetchTool20250910:



JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20250910"constant"web\_fetch\_20250910"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaWebFetchTool20260209:



JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20260209"constant"web\_fetch\_20260209"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaWebFetchTool20260309:

Web fetch tool with use\_cache parameter for bypassing cached content.



JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20260309"constant"web\_fetch\_20260309"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

Optional<Boolean> useCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class BetaWebFetchTool20260318:



JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20260318"constant"web\_fetch\_20260318"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.



Optional<ResponseInclusion> responseInclusion

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

FULL("full")

EXCLUDED("excluded")

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

Optional<Boolean> useCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class BetaWebFetchToolResultBlock:



Content content

One of the following:



class BetaWebFetchToolResultErrorBlock:



[BetaWebFetchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_IN\_PRIOR\_CONTEXT("url\_not\_in\_prior\_context")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant



class BetaWebFetchBlock:



[BetaDocumentBlock](api/beta/messages.md) content



Optional<[BetaCitationConfig](api/beta/messages.md)> citations

Citation configuration for the document

boolean enabled



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebFetchToolResultBlockParam:



Content content

One of the following:



class BetaWebFetchToolResultErrorBlockParam:



[BetaWebFetchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_IN\_PRIOR\_CONTEXT("url\_not\_in\_prior\_context")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant



class BetaWebFetchBlockParam:



[BetaRequestDocumentBlock](api/beta/messages.md) content



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant



class BetaContentBlockSource:



Content content

One of the following:

String



List<[BetaContentBlockSourceContent](api/beta/messages.md)>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant



class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebFetchToolResultErrorBlock:



[BetaWebFetchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_IN\_PRIOR\_CONTEXT("url\_not\_in\_prior\_context")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant



class BetaWebFetchToolResultErrorBlockParam:



[BetaWebFetchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_IN\_PRIOR\_CONTEXT("url\_not\_in\_prior\_context")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant



enum BetaWebFetchToolResultErrorCode:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_IN\_PRIOR\_CONTEXT("url\_not\_in\_prior\_context")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")



class BetaWebSearchResultBlock:

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url



class BetaWebSearchResultBlockParam:

String encryptedContent

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

Optional<String> pageAge



class BetaWebSearchTool20250305:



JsonValue; name "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_search\_20250305"constant"web\_search\_20250305"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional<List<String>> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



Optional<[BetaUserLocation](api/beta/messages.md)> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

The city of the user.

Optional<String> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional<String> region

The region of the user.

Optional<String> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebSearchTool20260209:



JsonValue; name "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_search\_20260209"constant"web\_search\_20260209"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional<List<String>> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



Optional<[BetaUserLocation](api/beta/messages.md)> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

The city of the user.

Optional<String> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional<String> region

The region of the user.

Optional<String> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebSearchTool20260318:



JsonValue; name "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_search\_20260318"constant"web\_search\_20260318"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional<List<String>> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.



Optional<ResponseInclusion> responseInclusion

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

FULL("full")

EXCLUDED("excluded")

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



Optional<[BetaUserLocation](api/beta/messages.md)> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

The city of the user.

Optional<String> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional<String> region

The region of the user.

Optional<String> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebSearchToolRequestError:



[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant



class BetaWebSearchToolResultBlock:



[BetaWebSearchToolResultBlockContent](api/beta/messages.md) content

One of the following:



class BetaWebSearchToolResultError:



[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant



List<[BetaWebSearchResultBlock](api/beta/messages.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebSearchToolResultBlockContent: A class that can be one of several variants.union 



class BetaWebSearchToolResultError:



[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant



List<[BetaWebSearchResultBlock](api/beta/messages.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url



class BetaWebSearchToolResultBlockParam:



[BetaWebSearchToolResultBlockParamContent](api/beta/messages.md) content

One of the following:



List<[BetaWebSearchResultBlockParam](api/beta/messages.md)>

String encryptedContent

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

Optional<String> pageAge



class BetaWebSearchToolRequestError:



[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebSearchToolResultBlockParamContent: A class that can be one of several variants.union 



List<[BetaWebSearchResultBlockParam](api/beta/messages.md)>

String encryptedContent

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

Optional<String> pageAge



class BetaWebSearchToolRequestError:



[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant



class BetaWebSearchToolResultError:



[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant



enum BetaWebSearchToolResultErrorCode:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

#### MessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

[BetaMessageBatch](api/beta/messages/batches.md) beta().messages().batches().create(BatchCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

[BetaMessageBatch](api/beta/messages/batches.md) beta().messages().batches().retrieve(BatchRetrieveParamsparams = BatchRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

BatchListPage beta().messages().batches().list(BatchListParamsparams = BatchListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

[BetaMessageBatch](api/beta/messages/batches.md) beta().messages().batches().cancel(BatchCancelParamsparams = BatchCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

[BetaDeletedMessageBatch](api/beta/messages/batches.md) beta().messages().batches().delete(BatchDeleteParamsparams = BatchDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

[BetaMessageBatchIndividualResponse](api/beta/messages/batches.md) beta().messages().batches().resultsStreaming(BatchResultsParamsparams = BatchResultsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches/{message\_batch\_id}/results

---

*Copyright © Anthropic. All rights reserved.*
