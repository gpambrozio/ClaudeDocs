# Messages

Copy page

C#

# Messages

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

class UnionMember2:

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

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant

class BetaCodeExecutionToolResultBlockContent: A class that can be one of several variants.union

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

class BetaCodeExecutionToolResultBlockParam:

required [BetaCodeExecutionToolResultBlockParamContent](api/beta.md) Content

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

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

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

class BetaCodeExecutionToolResultBlockParam:

required [BetaCodeExecutionToolResultBlockParamContent](api/beta.md) Content

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

class UnionMember2:

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

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

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

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3\_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3\_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3\_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3\_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4\_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4\_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4\_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude\_3\_Opus\_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

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

required IReadOnlyList<UnnamedSchemaWithArrayParent1>? Iterations

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

required IReadOnlyList<UnnamedSchemaWithArrayParent1>? Iterations

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

class BetaCodeExecutionToolResultBlockParam:

required [BetaCodeExecutionToolResultBlockParamContent](api/beta.md) Content

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

maxLength256

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

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

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

required IReadOnlyList<UnnamedSchemaWithArrayParent1>? Iterations

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

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

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

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3\_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3\_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3\_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3\_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4\_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4\_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4\_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude\_3\_Opus\_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

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

required IReadOnlyList<UnnamedSchemaWithArrayParent1>? Iterations

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

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

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

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3\_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3\_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3\_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3\_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4\_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4\_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4\_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude\_3\_Opus\_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

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

required IReadOnlyList<UnnamedSchemaWithArrayParent1>? Iterations

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

required IReadOnlyList<UnnamedSchemaWithArrayParent1>? Iterations

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

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

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

class BetaThinkingConfigDisabled:

JsonElement Type "disabled"constant

class BetaThinkingConfigEnabled:

required Long BudgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

JsonElement Type "enabled"constant

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

class BetaThinkingConfigDisabled:

JsonElement Type "disabled"constant

class BetaThinkingConfigAdaptive:

JsonElement Type "adaptive"constant

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

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

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

UserLocation? UserLocation

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

required IReadOnlyList<UnnamedSchemaWithArrayParent1>? Iterations

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

UserLocation? UserLocation

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

#### MessagesBatches

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

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

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

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3\_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3\_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3\_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3\_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4\_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4\_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4\_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude\_3\_Opus\_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

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

required IReadOnlyList<UnnamedSchemaWithArrayParent1>? Iterations

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

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

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

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3\_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3\_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3\_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3\_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4\_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4\_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4\_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude\_3\_Opus\_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

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

required IReadOnlyList<UnnamedSchemaWithArrayParent1>? Iterations

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

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](api/beta.md) Content

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

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3\_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3\_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3\_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3\_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4\_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4\_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4\_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude\_3\_Opus\_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

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

required IReadOnlyList<UnnamedSchemaWithArrayParent1>? Iterations

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

---

*Copyright © Anthropic. All rights reserved.*
