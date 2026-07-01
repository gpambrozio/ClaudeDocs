# Messages

Copy page



C#

# Messages

##### [Create a Message](api/messages/create.md)

[Message](api/messages.md) Messages.Create(MessageCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages

##### [Count tokens in a Message](api/messages/count_tokens.md)

[MessageTokensCount](api/messages.md) Messages.CountTokens(MessageCountTokensParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class BashCodeExecutionOutputBlock:

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant



class BashCodeExecutionOutputBlockParam:

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant



class BashCodeExecutionResultBlock:



required IReadOnlyList<[BashCodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant



class BashCodeExecutionResultBlockParam:



required IReadOnlyList<[BashCodeExecutionOutputBlockParam](api/messages.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant



class BashCodeExecutionToolResultBlock:



required Content Content

One of the following:



class BashCodeExecutionToolResultError:



required [BashCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant



class BashCodeExecutionResultBlock:



required IReadOnlyList<[BashCodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant



class BashCodeExecutionToolResultBlockParam:



required Content Content

One of the following:



class BashCodeExecutionToolResultErrorParam:



required [BashCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant



class BashCodeExecutionResultBlockParam:



required IReadOnlyList<[BashCodeExecutionOutputBlockParam](api/messages.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class BashCodeExecutionToolResultError:



required [BashCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant



enum BashCodeExecutionToolResultErrorCode:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge



class BashCodeExecutionToolResultErrorParam:



required [BashCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant



class CacheControlEphemeral:

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class CacheCreation:

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.



class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationContentBlockLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required string? FileID

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationsConfig:

required Boolean Enabled



class CitationsConfigParam:

Boolean Enabled



class CitationsDelta:



required Citation Citation

One of the following:



class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required string? FileID

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationsSearchResultLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

JsonElement Type "citations\_delta"constant



class CitationsSearchResultLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CodeExecutionOutputBlock:

required string FileID

JsonElement Type "code\_execution\_output"constant



class CodeExecutionOutputBlockParam:

required string FileID

JsonElement Type "code\_execution\_output"constant



class CodeExecutionResultBlock:



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant



class CodeExecutionResultBlockParam:



required IReadOnlyList<[CodeExecutionOutputBlockParam](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant



class CodeExecutionTool20250522:



JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20250522"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20250825:



JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20250825"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20260120:

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20260120"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20260521:

Code execution tool with REPL state persistence.



JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20260521"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class CodeExecutionToolResultBlock:



required [CodeExecutionToolResultBlockContent](api/messages.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultError:



required [CodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant



class CodeExecutionResultBlock:



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant



class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant



class CodeExecutionToolResultBlockContent: A class that can be one of several variants.union 

Code execution result with encrypted stdout for PFC + web\_search results.



class CodeExecutionToolResultError:



required [CodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant



class CodeExecutionResultBlock:



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant



class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant



class CodeExecutionToolResultBlockParam:



required [CodeExecutionToolResultBlockParamContent](api/messages.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultErrorParam:



required [CodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant



class CodeExecutionResultBlockParam:



required IReadOnlyList<[CodeExecutionOutputBlockParam](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant



class EncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.



required IReadOnlyList<[CodeExecutionOutputBlockParam](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class CodeExecutionToolResultBlockParamContent: A class that can be one of several variants.union 

Code execution result with encrypted stdout for PFC + web\_search results.



class CodeExecutionToolResultErrorParam:



required [CodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant



class CodeExecutionResultBlockParam:



required IReadOnlyList<[CodeExecutionOutputBlockParam](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant



class EncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.



required IReadOnlyList<[CodeExecutionOutputBlockParam](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant



class CodeExecutionToolResultError:



required [CodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant



enum CodeExecutionToolResultErrorCode:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded



class CodeExecutionToolResultErrorParam:



required [CodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant



class Container:

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.



class ContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container\_upload"constant



class ContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

required string FileID

JsonElement Type "container\_upload"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class ContentBlock: A class that can be one of several variants.union 

Response model for a file uploaded to the container.



class TextBlock:



required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required string? FileID

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationsSearchResultLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant



class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant



class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant



class ToolUseBlock:

required string ID



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant



class ServerToolUseBlock:

required string ID



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

required IReadOnlyDictionary<string, JsonElement> Input



required Name Name

One of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant



class WebSearchToolResultBlock:



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



required [WebSearchToolResultBlockContent](api/messages.md) Content

One of the following:



class WebSearchToolResultError:



required [WebSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant



IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant



class WebFetchToolResultBlock:



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



required Content Content

One of the following:



class WebFetchToolResultErrorBlock:



required [WebFetchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_in\_prior\_context"UrlNotInPriorContext

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant



class WebFetchBlock:



required [DocumentBlock](api/messages.md) Content



required [CitationsConfig](api/messages.md)? Citations

Citation configuration for the document

required Boolean Enabled



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant



class CodeExecutionToolResultBlock:



required [CodeExecutionToolResultBlockContent](api/messages.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultError:



required [CodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant



class CodeExecutionResultBlock:



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant



class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant



class BashCodeExecutionToolResultBlock:



required Content Content

One of the following:



class BashCodeExecutionToolResultError:



required [BashCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant



class BashCodeExecutionResultBlock:



required IReadOnlyList<[BashCodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant



class TextEditorCodeExecutionToolResultBlock:



required Content Content

One of the following:



class TextEditorCodeExecutionToolResultError:



required [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant



class TextEditorCodeExecutionViewResultBlock:

required string Content



required FileType FileType

One of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant



class TextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant



class TextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant



class ToolSearchToolResultBlock:



required Content Content

One of the following:



class ToolSearchToolResultError:



required [ToolSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant



class ToolSearchToolSearchResultBlock:



required IReadOnlyList<[ToolReferenceBlock](api/messages.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant



class ContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container\_upload"constant



class ContentBlockParam: A class that can be one of several variants.union 

Regular text content.



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class DocumentBlockParam:



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant



class ContentBlockSource:



required Content Content

One of the following:

string



IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant



class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title



class SearchResultBlockParam:



required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md) Citations

Boolean Enabled



class ThinkingBlockParam:

required string Signature

required string Thinking

JsonElement Type "thinking"constant



class RedactedThinkingBlockParam:

required string Data

JsonElement Type "redacted\_thinking"constant



class ToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class ToolResultBlockParam:

required string ToolUseID

JsonElement Type "tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Content Content

One of the following:

string



IReadOnlyList<Block>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class SearchResultBlockParam:



required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md) Citations

Boolean Enabled



class DocumentBlockParam:



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant



class ContentBlockSource:



required Content Content

One of the following:

string



IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant



class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title



class ToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

required string ToolName

JsonElement Type "tool\_reference"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean IsError



class ServerToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input



required Name Name

One of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class WebSearchToolResultBlockParam:



required [WebSearchToolResultBlockParamContent](api/messages.md) Content

One of the following:



IReadOnlyList<[WebSearchResultBlockParam](api/messages.md)>

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge



class WebSearchToolRequestError:



required [WebSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class WebFetchToolResultBlockParam:



required Content Content

One of the following:



class WebFetchToolResultErrorBlockParam:



required [WebFetchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_in\_prior\_context"UrlNotInPriorContext

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant



class WebFetchBlockParam:



required [DocumentBlockParam](api/messages.md) Content



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant



class ContentBlockSource:



required Content Content

One of the following:

string



IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant



class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class CodeExecutionToolResultBlockParam:



required [CodeExecutionToolResultBlockParamContent](api/messages.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultErrorParam:



required [CodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant



class CodeExecutionResultBlockParam:



required IReadOnlyList<[CodeExecutionOutputBlockParam](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant



class EncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.



required IReadOnlyList<[CodeExecutionOutputBlockParam](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class BashCodeExecutionToolResultBlockParam:



required Content Content

One of the following:



class BashCodeExecutionToolResultErrorParam:



required [BashCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant



class BashCodeExecutionResultBlockParam:



required IReadOnlyList<[BashCodeExecutionOutputBlockParam](api/messages.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class TextEditorCodeExecutionToolResultBlockParam:



required Content Content

One of the following:



class TextEditorCodeExecutionToolResultErrorParam:



required [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

string? ErrorMessage



class TextEditorCodeExecutionViewResultBlockParam:

required string Content



required FileType FileType

One of the following:

"text"Text

"image"Image

"pdf"Pdf

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

Long? NumLines

Long? StartLine

Long? TotalLines



class TextEditorCodeExecutionCreateResultBlockParam:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant



class TextEditorCodeExecutionStrReplaceResultBlockParam:

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

IReadOnlyList<string>? Lines

Long? NewLines

Long? NewStart

Long? OldLines

Long? OldStart

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class ToolSearchToolResultBlockParam:



required Content Content

One of the following:



class ToolSearchToolResultErrorParam:



required [ToolSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "tool\_search\_tool\_result\_error"constant

string? ErrorMessage



class ToolSearchToolSearchResultBlockParam:



required IReadOnlyList<[ToolReferenceBlockParam](api/messages.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class ContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

required string FileID

JsonElement Type "container\_upload"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class MidConversationSystemBlockParam:

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

System instruction text blocks.

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

JsonElement Type "mid\_conv\_system"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class ContentBlockSource:



required Content Content

One of the following:

string



IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant



class ContentBlockSourceContent: A class that can be one of several variants.union 



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class DocumentBlock:



required [CitationsConfig](api/messages.md)? Citations

Citation configuration for the document

required Boolean Enabled



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant



class DocumentBlockParam:



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant



class ContentBlockSource:



required Content Content

One of the following:

string



IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant



class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title



class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant



class EncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.



required IReadOnlyList<[CodeExecutionOutputBlockParam](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class InputJsonDelta:

required string PartialJson

JsonElement Type "input\_json\_delta"constant



class JsonOutputFormat:

required IReadOnlyDictionary<string, JsonElement> Schema

The JSON schema of the format

JsonElement Type "json\_schema"constant



class MemoryTool20250818:



JsonElement Name "memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "memory\_20250818"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class Message:



required string ID

Unique object identifier.

The format and length of IDs may change over time.



required [Container](api/messages.md)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.



required IReadOnlyList<[ContentBlock](api/messages.md)> Content

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

class TextBlock:



required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required string? FileID

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationsSearchResultLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant



class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant



class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant



class ToolUseBlock:

required string ID



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant



class ServerToolUseBlock:

required string ID



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

required IReadOnlyDictionary<string, JsonElement> Input



required Name Name

One of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant



class WebSearchToolResultBlock:



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



required [WebSearchToolResultBlockContent](api/messages.md) Content

One of the following:



class WebSearchToolResultError:



required [WebSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant



IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant



class WebFetchToolResultBlock:



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



required Content Content

One of the following:



class WebFetchToolResultErrorBlock:



required [WebFetchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_in\_prior\_context"UrlNotInPriorContext

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant



class WebFetchBlock:



required [DocumentBlock](api/messages.md) Content



required [CitationsConfig](api/messages.md)? Citations

Citation configuration for the document

required Boolean Enabled



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant



class CodeExecutionToolResultBlock:



required [CodeExecutionToolResultBlockContent](api/messages.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultError:



required [CodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant



class CodeExecutionResultBlock:



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant



class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant



class BashCodeExecutionToolResultBlock:



required Content Content

One of the following:



class BashCodeExecutionToolResultError:



required [BashCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant



class BashCodeExecutionResultBlock:



required IReadOnlyList<[BashCodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant



class TextEditorCodeExecutionToolResultBlock:



required Content Content

One of the following:



class TextEditorCodeExecutionToolResultError:



required [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant



class TextEditorCodeExecutionViewResultBlock:

required string Content



required FileType FileType

One of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant



class TextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant



class TextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant



class ToolSearchToolResultBlock:



required Content Content

One of the following:



class ToolSearchToolResultError:



required [ToolSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant



class ToolSearchToolSearchResultBlock:



required IReadOnlyList<[ToolReferenceBlock](api/messages.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant



class ContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container\_upload"constant



required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-fable-5"ClaudeFable5

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"ClaudeMythos5

Most capable model for cybersecurity and biology research

"claude-opus-4-8"ClaudeOpus4\_8

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"ClaudeMythosPreview

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"ClaudeOpus4\_6

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

"claude-opus-4-1"ClaudeOpus4\_1

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Exceptional model for specialized complex tasks



JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.



required [RefusalStopDetails](api/messages.md)? StopDetails

Structured information about a refusal.



required Category? Category

The policy category that triggered a refusal.

One of the following:

"cyber"Cyber

"bio"Bio

"frontier\_llm"FrontierLlm

"reasoning\_extraction"ReasoningExtraction

"military\_weapons"MilitaryWeapons



required string? Explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonElement Type "refusal"constant



required [StopReason](api/messages.md)? StopReason

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

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal



required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.



required [Usage](api/messages.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



required [CacheCreation](api/messages.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.



required [OutputTokensDetails](api/messages.md)? OutputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



required Long ThinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.



required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

One of the following:

"standard"Standard

"priority"Priority

"batch"Batch



class MessageCountTokensTool: A class that can be one of several variants.union 

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



class Tool:



required InputSchema InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required



required string Name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



string Description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Boolean? EagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Type? Type



class ToolBash20250124:



JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash\_20250124"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20250522:



JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20250522"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20250825:



JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20250825"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20260120:

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20260120"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20260521:

Code execution tool with REPL state persistence.



JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20260521"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class MemoryTool20250818:



JsonElement Name "memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "memory\_20250818"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolTextEditor20250124:



JsonElement Name "str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250124"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolTextEditor20250429:



JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250429"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolTextEditor20250728:



JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250728"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Long? MaxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class WebSearchTool20250305:



JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20250305"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



[UserLocation](api/messages.md)? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class WebFetchTool20250910:



JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20250910"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class WebSearchTool20260209:



JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20260209"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



[UserLocation](api/messages.md)? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class WebFetchTool20260209:



JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20260209"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class WebFetchTool20260309:

Web fetch tool with use\_cache parameter for bypassing cached content.



JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20260309"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Boolean UseCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class WebSearchTool20260318:



JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20260318"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.



ResponseInclusion ResponseInclusion

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"Full

"excluded"Excluded

Boolean Strict

When true, guarantees schema validation on tool names and inputs



[UserLocation](api/messages.md)? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class WebFetchTool20260318:



JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20260318"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.



ResponseInclusion ResponseInclusion

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"Full

"excluded"Excluded

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Boolean UseCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class ToolSearchToolBm25\_20251119:



JsonElement Name "tool\_search\_tool\_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



required Type Type

One of the following:

"tool\_search\_tool\_bm25\_20251119"ToolSearchToolBm25\_20251119

"tool\_search\_tool\_bm25"ToolSearchToolBm25



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolSearchToolRegex20251119:



JsonElement Name "tool\_search\_tool\_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



required Type Type

One of the following:

"tool\_search\_tool\_regex\_20251119"ToolSearchToolRegex20251119

"tool\_search\_tool\_regex"ToolSearchToolRegex



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class MessageDeltaUsage:

required Long? CacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The cumulative number of input tokens read from the cache.

required Long? InputTokens

The cumulative number of input tokens which were used.

required Long OutputTokens

The cumulative number of output tokens which were used.



required [OutputTokensDetails](api/messages.md)? OutputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



required Long ThinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.



class MessageParam:



required Content Content

One of the following:

string



IReadOnlyList<[ContentBlockParam](api/messages.md)>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class DocumentBlockParam:



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant



class ContentBlockSource:



required Content Content

One of the following:

string



IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant



class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title



class SearchResultBlockParam:



required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md) Citations

Boolean Enabled



class ThinkingBlockParam:

required string Signature

required string Thinking

JsonElement Type "thinking"constant



class RedactedThinkingBlockParam:

required string Data

JsonElement Type "redacted\_thinking"constant



class ToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class ToolResultBlockParam:

required string ToolUseID

JsonElement Type "tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Content Content

One of the following:

string



IReadOnlyList<Block>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class SearchResultBlockParam:



required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md) Citations

Boolean Enabled



class DocumentBlockParam:



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant



class ContentBlockSource:



required Content Content

One of the following:

string



IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant



class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title



class ToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

required string ToolName

JsonElement Type "tool\_reference"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean IsError



class ServerToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input



required Name Name

One of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class WebSearchToolResultBlockParam:



required [WebSearchToolResultBlockParamContent](api/messages.md) Content

One of the following:



IReadOnlyList<[WebSearchResultBlockParam](api/messages.md)>

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge



class WebSearchToolRequestError:



required [WebSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class WebFetchToolResultBlockParam:



required Content Content

One of the following:



class WebFetchToolResultErrorBlockParam:



required [WebFetchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_in\_prior\_context"UrlNotInPriorContext

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant



class WebFetchBlockParam:



required [DocumentBlockParam](api/messages.md) Content



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant



class ContentBlockSource:



required Content Content

One of the following:

string



IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant



class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class CodeExecutionToolResultBlockParam:



required [CodeExecutionToolResultBlockParamContent](api/messages.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultErrorParam:



required [CodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant



class CodeExecutionResultBlockParam:



required IReadOnlyList<[CodeExecutionOutputBlockParam](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant



class EncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.



required IReadOnlyList<[CodeExecutionOutputBlockParam](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class BashCodeExecutionToolResultBlockParam:



required Content Content

One of the following:



class BashCodeExecutionToolResultErrorParam:



required [BashCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant



class BashCodeExecutionResultBlockParam:



required IReadOnlyList<[BashCodeExecutionOutputBlockParam](api/messages.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class TextEditorCodeExecutionToolResultBlockParam:



required Content Content

One of the following:



class TextEditorCodeExecutionToolResultErrorParam:



required [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

string? ErrorMessage



class TextEditorCodeExecutionViewResultBlockParam:

required string Content



required FileType FileType

One of the following:

"text"Text

"image"Image

"pdf"Pdf

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

Long? NumLines

Long? StartLine

Long? TotalLines



class TextEditorCodeExecutionCreateResultBlockParam:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant



class TextEditorCodeExecutionStrReplaceResultBlockParam:

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

IReadOnlyList<string>? Lines

Long? NewLines

Long? NewStart

Long? OldLines

Long? OldStart

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class ToolSearchToolResultBlockParam:



required Content Content

One of the following:



class ToolSearchToolResultErrorParam:



required [ToolSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "tool\_search\_tool\_result\_error"constant

string? ErrorMessage



class ToolSearchToolSearchResultBlockParam:



required IReadOnlyList<[ToolReferenceBlockParam](api/messages.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class ContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

required string FileID

JsonElement Type "container\_upload"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class MidConversationSystemBlockParam:

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

System instruction text blocks.

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

JsonElement Type "mid\_conv\_system"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



required Role Role

One of the following:

"user"User

"assistant"Assistant

"system"System



class MessageTokensCount:

required Long InputTokens

The total number of tokens across the provided list of messages, system prompt, and tools.



class Metadata:



string? UserID

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



class MidConversationSystemBlockParam:

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

System instruction text blocks.

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

JsonElement Type "mid\_conv\_system"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class OutputConfig:



Effort? Effort

All possible effort levels.

One of the following:

"low"Low

"medium"Medium

"high"High

"xhigh"Xhigh

"max"Max



[JsonOutputFormat](api/messages.md)? Format

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

required IReadOnlyDictionary<string, JsonElement> Schema

The JSON schema of the format

JsonElement Type "json\_schema"constant



class OutputTokensDetails:



required Long ThinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant



class RawContentBlockDelta: A class that can be one of several variants.union 



class TextDelta:

required string Text

JsonElement Type "text\_delta"constant



class InputJsonDelta:

required string PartialJson

JsonElement Type "input\_json\_delta"constant



class CitationsDelta:



required Citation Citation

One of the following:



class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required string? FileID

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationsSearchResultLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

JsonElement Type "citations\_delta"constant



class ThinkingDelta:

required string Thinking

JsonElement Type "thinking\_delta"constant



class SignatureDelta:

required string Signature

JsonElement Type "signature\_delta"constant



class RawContentBlockDeltaEvent:



required [RawContentBlockDelta](api/messages.md) Delta

One of the following:



class TextDelta:

required string Text

JsonElement Type "text\_delta"constant



class InputJsonDelta:

required string PartialJson

JsonElement Type "input\_json\_delta"constant



class CitationsDelta:



required Citation Citation

One of the following:



class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required string? FileID

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationsSearchResultLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

JsonElement Type "citations\_delta"constant



class ThinkingDelta:

required string Thinking

JsonElement Type "thinking\_delta"constant



class SignatureDelta:

required string Signature

JsonElement Type "signature\_delta"constant

required Long Index

JsonElement Type "content\_block\_delta"constant



class RawContentBlockStartEvent:



required ContentBlock ContentBlock

Response model for a file uploaded to the container.

One of the following:



class TextBlock:



required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required string? FileID

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationsSearchResultLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant



class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant



class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant



class ToolUseBlock:

required string ID



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant



class ServerToolUseBlock:

required string ID



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

required IReadOnlyDictionary<string, JsonElement> Input



required Name Name

One of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant



class WebSearchToolResultBlock:



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



required [WebSearchToolResultBlockContent](api/messages.md) Content

One of the following:



class WebSearchToolResultError:



required [WebSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant



IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant



class WebFetchToolResultBlock:



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



required Content Content

One of the following:



class WebFetchToolResultErrorBlock:



required [WebFetchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_in\_prior\_context"UrlNotInPriorContext

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant



class WebFetchBlock:



required [DocumentBlock](api/messages.md) Content



required [CitationsConfig](api/messages.md)? Citations

Citation configuration for the document

required Boolean Enabled



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant



class CodeExecutionToolResultBlock:



required [CodeExecutionToolResultBlockContent](api/messages.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultError:



required [CodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant



class CodeExecutionResultBlock:



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant



class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant



class BashCodeExecutionToolResultBlock:



required Content Content

One of the following:



class BashCodeExecutionToolResultError:



required [BashCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant



class BashCodeExecutionResultBlock:



required IReadOnlyList<[BashCodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant



class TextEditorCodeExecutionToolResultBlock:



required Content Content

One of the following:



class TextEditorCodeExecutionToolResultError:



required [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant



class TextEditorCodeExecutionViewResultBlock:

required string Content



required FileType FileType

One of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant



class TextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant



class TextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant



class ToolSearchToolResultBlock:



required Content Content

One of the following:



class ToolSearchToolResultError:



required [ToolSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant



class ToolSearchToolSearchResultBlock:



required IReadOnlyList<[ToolReferenceBlock](api/messages.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant



class ContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container\_upload"constant

required Long Index

JsonElement Type "content\_block\_start"constant



class RawContentBlockStopEvent:

required Long Index

JsonElement Type "content\_block\_stop"constant



class RawMessageDeltaEvent:



required Delta Delta



required [Container](api/messages.md)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.



required [RefusalStopDetails](api/messages.md)? StopDetails

Structured information about a refusal.



required Category? Category

The policy category that triggered a refusal.

One of the following:

"cyber"Cyber

"bio"Bio

"frontier\_llm"FrontierLlm

"reasoning\_extraction"ReasoningExtraction

"military\_weapons"MilitaryWeapons



required string? Explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonElement Type "refusal"constant



required [StopReason](api/messages.md)? StopReason

One of the following:

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal

required string? StopSequence

JsonElement Type "message\_delta"constant



required [MessageDeltaUsage](api/messages.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required Long? CacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The cumulative number of input tokens read from the cache.

required Long? InputTokens

The cumulative number of input tokens which were used.

required Long OutputTokens

The cumulative number of output tokens which were used.



required [OutputTokensDetails](api/messages.md)? OutputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



required Long ThinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.



class RawMessageStartEvent:



required [Message](api/messages.md) Message



required string ID

Unique object identifier.

The format and length of IDs may change over time.



required [Container](api/messages.md)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.



required IReadOnlyList<[ContentBlock](api/messages.md)> Content

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

class TextBlock:



required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required string? FileID

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationsSearchResultLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant



class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant



class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant



class ToolUseBlock:

required string ID



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant



class ServerToolUseBlock:

required string ID



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

required IReadOnlyDictionary<string, JsonElement> Input



required Name Name

One of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant



class WebSearchToolResultBlock:



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



required [WebSearchToolResultBlockContent](api/messages.md) Content

One of the following:



class WebSearchToolResultError:



required [WebSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant



IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant



class WebFetchToolResultBlock:



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



required Content Content

One of the following:



class WebFetchToolResultErrorBlock:



required [WebFetchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_in\_prior\_context"UrlNotInPriorContext

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant



class WebFetchBlock:



required [DocumentBlock](api/messages.md) Content



required [CitationsConfig](api/messages.md)? Citations

Citation configuration for the document

required Boolean Enabled



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant



class CodeExecutionToolResultBlock:



required [CodeExecutionToolResultBlockContent](api/messages.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultError:



required [CodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant



class CodeExecutionResultBlock:



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant



class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant



class BashCodeExecutionToolResultBlock:



required Content Content

One of the following:



class BashCodeExecutionToolResultError:



required [BashCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant



class BashCodeExecutionResultBlock:



required IReadOnlyList<[BashCodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant



class TextEditorCodeExecutionToolResultBlock:



required Content Content

One of the following:



class TextEditorCodeExecutionToolResultError:



required [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant



class TextEditorCodeExecutionViewResultBlock:

required string Content



required FileType FileType

One of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant



class TextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant



class TextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant



class ToolSearchToolResultBlock:



required Content Content

One of the following:



class ToolSearchToolResultError:



required [ToolSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant



class ToolSearchToolSearchResultBlock:



required IReadOnlyList<[ToolReferenceBlock](api/messages.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant



class ContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container\_upload"constant



required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-fable-5"ClaudeFable5

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"ClaudeMythos5

Most capable model for cybersecurity and biology research

"claude-opus-4-8"ClaudeOpus4\_8

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"ClaudeMythosPreview

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"ClaudeOpus4\_6

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

"claude-opus-4-1"ClaudeOpus4\_1

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Exceptional model for specialized complex tasks



JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.



required [RefusalStopDetails](api/messages.md)? StopDetails

Structured information about a refusal.



required Category? Category

The policy category that triggered a refusal.

One of the following:

"cyber"Cyber

"bio"Bio

"frontier\_llm"FrontierLlm

"reasoning\_extraction"ReasoningExtraction

"military\_weapons"MilitaryWeapons



required string? Explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonElement Type "refusal"constant



required [StopReason](api/messages.md)? StopReason

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

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal



required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.



required [Usage](api/messages.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



required [CacheCreation](api/messages.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.



required [OutputTokensDetails](api/messages.md)? OutputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



required Long ThinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.



required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

One of the following:

"standard"Standard

"priority"Priority

"batch"Batch

JsonElement Type "message\_start"constant



class RawMessageStopEvent:

JsonElement Type "message\_stop"constant



class RawMessageStreamEvent: A class that can be one of several variants.union 



class RawMessageStartEvent:



required [Message](api/messages.md) Message



required string ID

Unique object identifier.

The format and length of IDs may change over time.



required [Container](api/messages.md)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.



required IReadOnlyList<[ContentBlock](api/messages.md)> Content

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

class TextBlock:



required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required string? FileID

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationsSearchResultLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant



class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant



class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant



class ToolUseBlock:

required string ID



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant



class ServerToolUseBlock:

required string ID



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

required IReadOnlyDictionary<string, JsonElement> Input



required Name Name

One of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant



class WebSearchToolResultBlock:



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



required [WebSearchToolResultBlockContent](api/messages.md) Content

One of the following:



class WebSearchToolResultError:



required [WebSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant



IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant



class WebFetchToolResultBlock:



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



required Content Content

One of the following:



class WebFetchToolResultErrorBlock:



required [WebFetchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_in\_prior\_context"UrlNotInPriorContext

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant



class WebFetchBlock:



required [DocumentBlock](api/messages.md) Content



required [CitationsConfig](api/messages.md)? Citations

Citation configuration for the document

required Boolean Enabled



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant



class CodeExecutionToolResultBlock:



required [CodeExecutionToolResultBlockContent](api/messages.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultError:



required [CodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant



class CodeExecutionResultBlock:



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant



class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant



class BashCodeExecutionToolResultBlock:



required Content Content

One of the following:



class BashCodeExecutionToolResultError:



required [BashCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant



class BashCodeExecutionResultBlock:



required IReadOnlyList<[BashCodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant



class TextEditorCodeExecutionToolResultBlock:



required Content Content

One of the following:



class TextEditorCodeExecutionToolResultError:



required [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant



class TextEditorCodeExecutionViewResultBlock:

required string Content



required FileType FileType

One of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant



class TextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant



class TextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant



class ToolSearchToolResultBlock:



required Content Content

One of the following:



class ToolSearchToolResultError:



required [ToolSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant



class ToolSearchToolSearchResultBlock:



required IReadOnlyList<[ToolReferenceBlock](api/messages.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant



class ContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container\_upload"constant



required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-fable-5"ClaudeFable5

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"ClaudeMythos5

Most capable model for cybersecurity and biology research

"claude-opus-4-8"ClaudeOpus4\_8

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"ClaudeMythosPreview

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"ClaudeOpus4\_6

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

"claude-opus-4-1"ClaudeOpus4\_1

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Exceptional model for specialized complex tasks



JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.



required [RefusalStopDetails](api/messages.md)? StopDetails

Structured information about a refusal.



required Category? Category

The policy category that triggered a refusal.

One of the following:

"cyber"Cyber

"bio"Bio

"frontier\_llm"FrontierLlm

"reasoning\_extraction"ReasoningExtraction

"military\_weapons"MilitaryWeapons



required string? Explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonElement Type "refusal"constant



required [StopReason](api/messages.md)? StopReason

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

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal



required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.



required [Usage](api/messages.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



required [CacheCreation](api/messages.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.



required [OutputTokensDetails](api/messages.md)? OutputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



required Long ThinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.



required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

One of the following:

"standard"Standard

"priority"Priority

"batch"Batch

JsonElement Type "message\_start"constant



class RawMessageDeltaEvent:



required Delta Delta



required [Container](api/messages.md)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.



required [RefusalStopDetails](api/messages.md)? StopDetails

Structured information about a refusal.



required Category? Category

The policy category that triggered a refusal.

One of the following:

"cyber"Cyber

"bio"Bio

"frontier\_llm"FrontierLlm

"reasoning\_extraction"ReasoningExtraction

"military\_weapons"MilitaryWeapons



required string? Explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonElement Type "refusal"constant



required [StopReason](api/messages.md)? StopReason

One of the following:

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal

required string? StopSequence

JsonElement Type "message\_delta"constant



required [MessageDeltaUsage](api/messages.md) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required Long? CacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The cumulative number of input tokens read from the cache.

required Long? InputTokens

The cumulative number of input tokens which were used.

required Long OutputTokens

The cumulative number of output tokens which were used.



required [OutputTokensDetails](api/messages.md)? OutputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



required Long ThinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.



class RawMessageStopEvent:

JsonElement Type "message\_stop"constant



class RawContentBlockStartEvent:



required ContentBlock ContentBlock

Response model for a file uploaded to the container.

One of the following:



class TextBlock:



required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required string? FileID

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationsSearchResultLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant



class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant



class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant



class ToolUseBlock:

required string ID



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant



class ServerToolUseBlock:

required string ID



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

required IReadOnlyDictionary<string, JsonElement> Input



required Name Name

One of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant



class WebSearchToolResultBlock:



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



required [WebSearchToolResultBlockContent](api/messages.md) Content

One of the following:



class WebSearchToolResultError:



required [WebSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant



IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant



class WebFetchToolResultBlock:



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



required Content Content

One of the following:



class WebFetchToolResultErrorBlock:



required [WebFetchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_in\_prior\_context"UrlNotInPriorContext

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant



class WebFetchBlock:



required [DocumentBlock](api/messages.md) Content



required [CitationsConfig](api/messages.md)? Citations

Citation configuration for the document

required Boolean Enabled



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant



class CodeExecutionToolResultBlock:



required [CodeExecutionToolResultBlockContent](api/messages.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultError:



required [CodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant



class CodeExecutionResultBlock:



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant



class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



required IReadOnlyList<[CodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant



class BashCodeExecutionToolResultBlock:



required Content Content

One of the following:



class BashCodeExecutionToolResultError:



required [BashCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant



class BashCodeExecutionResultBlock:



required IReadOnlyList<[BashCodeExecutionOutputBlock](api/messages.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant



class TextEditorCodeExecutionToolResultBlock:



required Content Content

One of the following:



class TextEditorCodeExecutionToolResultError:



required [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant



class TextEditorCodeExecutionViewResultBlock:

required string Content



required FileType FileType

One of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant



class TextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant



class TextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant



class ToolSearchToolResultBlock:



required Content Content

One of the following:



class ToolSearchToolResultError:



required [ToolSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant



class ToolSearchToolSearchResultBlock:



required IReadOnlyList<[ToolReferenceBlock](api/messages.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant



class ContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container\_upload"constant

required Long Index

JsonElement Type "content\_block\_start"constant



class RawContentBlockDeltaEvent:



required [RawContentBlockDelta](api/messages.md) Delta

One of the following:



class TextDelta:

required string Text

JsonElement Type "text\_delta"constant



class InputJsonDelta:

required string PartialJson

JsonElement Type "input\_json\_delta"constant



class CitationsDelta:



required Citation Citation

One of the following:



class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required string? FileID

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationsSearchResultLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

JsonElement Type "citations\_delta"constant



class ThinkingDelta:

required string Thinking

JsonElement Type "thinking\_delta"constant



class SignatureDelta:

required string Signature

JsonElement Type "signature\_delta"constant

required Long Index

JsonElement Type "content\_block\_delta"constant



class RawContentBlockStopEvent:

required Long Index

JsonElement Type "content\_block\_stop"constant



class RedactedThinkingBlock:

required string Data

JsonElement Type "redacted\_thinking"constant



class RedactedThinkingBlockParam:

required string Data

JsonElement Type "redacted\_thinking"constant



class RefusalStopDetails:

Structured information about a refusal.



required Category? Category

The policy category that triggered a refusal.

One of the following:

"cyber"Cyber

"bio"Bio

"frontier\_llm"FrontierLlm

"reasoning\_extraction"ReasoningExtraction

"military\_weapons"MilitaryWeapons



required string? Explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonElement Type "refusal"constant



class SearchResultBlockParam:



required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md) Citations

Boolean Enabled



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class ServerToolUsage:

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.



class ServerToolUseBlock:

required string ID



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

required IReadOnlyDictionary<string, JsonElement> Input



required Name Name

One of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant



class ServerToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input



required Name Name

One of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class SignatureDelta:

required string Signature

JsonElement Type "signature\_delta"constant



enum StopReason:

"end\_turn"EndTurn

"max\_tokens"MaxTokens

"stop\_sequence"StopSequence

"tool\_use"ToolUse

"pause\_turn"PauseTurn

"refusal"Refusal



class TextBlock:



required IReadOnlyList<[TextCitation](api/messages.md)>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required string? FileID

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationsSearchResultLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

required string Text

JsonElement Type "text"constant



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class TextCitation: A class that can be one of several variants.union 



class CitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required string? FileID

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationsSearchResultLocation:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class TextCitationParam: A class that can be one of several variants.union 



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class TextDelta:

required string Text

JsonElement Type "text\_delta"constant



class TextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant



class TextEditorCodeExecutionCreateResultBlockParam:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant



class TextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant



class TextEditorCodeExecutionStrReplaceResultBlockParam:

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

IReadOnlyList<string>? Lines

Long? NewLines

Long? NewStart

Long? OldLines

Long? OldStart



class TextEditorCodeExecutionToolResultBlock:



required Content Content

One of the following:



class TextEditorCodeExecutionToolResultError:



required [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant



class TextEditorCodeExecutionViewResultBlock:

required string Content



required FileType FileType

One of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant



class TextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant



class TextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList<string>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant



class TextEditorCodeExecutionToolResultBlockParam:



required Content Content

One of the following:



class TextEditorCodeExecutionToolResultErrorParam:



required [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

string? ErrorMessage



class TextEditorCodeExecutionViewResultBlockParam:

required string Content



required FileType FileType

One of the following:

"text"Text

"image"Image

"pdf"Pdf

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

Long? NumLines

Long? StartLine

Long? TotalLines



class TextEditorCodeExecutionCreateResultBlockParam:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant



class TextEditorCodeExecutionStrReplaceResultBlockParam:

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

IReadOnlyList<string>? Lines

Long? NewLines

Long? NewStart

Long? OldLines

Long? OldStart

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class TextEditorCodeExecutionToolResultError:



required [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant



enum TextEditorCodeExecutionToolResultErrorCode:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound



class TextEditorCodeExecutionToolResultErrorParam:



required [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

string? ErrorMessage



class TextEditorCodeExecutionViewResultBlock:

required string Content



required FileType FileType

One of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant



class TextEditorCodeExecutionViewResultBlockParam:

required string Content



required FileType FileType

One of the following:

"text"Text

"image"Image

"pdf"Pdf

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

Long? NumLines

Long? StartLine

Long? TotalLines



class ThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant



class ThinkingBlockParam:

required string Signature

required string Thinking

JsonElement Type "thinking"constant



class ThinkingConfigAdaptive:

JsonElement Type "adaptive"constant



Display? Display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"Summarized

"omitted"Omitted



class ThinkingConfigDisabled:

JsonElement Type "disabled"constant



class ThinkingConfigEnabled:



required Long BudgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

JsonElement Type "enabled"constant



Display? Display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"Summarized

"omitted"Omitted



class ThinkingConfigParam: A class that can be one of several variants.union 

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](build-with-claude/extended-thinking.md) for details.



class ThinkingConfigEnabled:



required Long BudgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

JsonElement Type "enabled"constant



Display? Display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"Summarized

"omitted"Omitted



class ThinkingConfigDisabled:

JsonElement Type "disabled"constant



class ThinkingConfigAdaptive:

JsonElement Type "adaptive"constant



Display? Display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"Summarized

"omitted"Omitted



class ThinkingDelta:

required string Thinking

JsonElement Type "thinking\_delta"constant



class Tool:



required InputSchema InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required



required string Name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



string Description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Boolean? EagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Type? Type



class ToolBash20250124:



JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash\_20250124"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolChoice: A class that can be one of several variants.union 

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.



class ToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonElement Type "auto"constant



Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



class ToolChoiceAny:

The model will use any available tools.

JsonElement Type "any"constant



Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class ToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

required string Name

The name of the tool to use.

JsonElement Type "tool"constant



Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class ToolChoiceNone:

The model will not be allowed to use tools.

JsonElement Type "none"constant



class ToolChoiceAny:

The model will use any available tools.

JsonElement Type "any"constant



Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class ToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonElement Type "auto"constant



Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



class ToolChoiceNone:

The model will not be allowed to use tools.

JsonElement Type "none"constant



class ToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

required string Name

The name of the tool to use.

JsonElement Type "tool"constant



Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class ToolReferenceBlock:

required string ToolName

JsonElement Type "tool\_reference"constant



class ToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

required string ToolName

JsonElement Type "tool\_reference"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class ToolResultBlockParam:

required string ToolUseID

JsonElement Type "tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Content Content

One of the following:

string



IReadOnlyList<Block>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class SearchResultBlockParam:



required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md) Citations

Boolean Enabled



class DocumentBlockParam:



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant



class ContentBlockSource:



required Content Content

One of the following:

string



IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant



class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title



class ToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

required string ToolName

JsonElement Type "tool\_reference"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean IsError



class ToolSearchToolBm25\_20251119:



JsonElement Name "tool\_search\_tool\_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



required Type Type

One of the following:

"tool\_search\_tool\_bm25\_20251119"ToolSearchToolBm25\_20251119

"tool\_search\_tool\_bm25"ToolSearchToolBm25



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolSearchToolRegex20251119:



JsonElement Name "tool\_search\_tool\_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



required Type Type

One of the following:

"tool\_search\_tool\_regex\_20251119"ToolSearchToolRegex20251119

"tool\_search\_tool\_regex"ToolSearchToolRegex



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolSearchToolResultBlock:



required Content Content

One of the following:



class ToolSearchToolResultError:



required [ToolSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant



class ToolSearchToolSearchResultBlock:



required IReadOnlyList<[ToolReferenceBlock](api/messages.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant



class ToolSearchToolResultBlockParam:



required Content Content

One of the following:



class ToolSearchToolResultErrorParam:



required [ToolSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "tool\_search\_tool\_result\_error"constant

string? ErrorMessage



class ToolSearchToolSearchResultBlockParam:



required IReadOnlyList<[ToolReferenceBlockParam](api/messages.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class ToolSearchToolResultError:



required [ToolSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool\_search\_tool\_result\_error"constant



enum ToolSearchToolResultErrorCode:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded



class ToolSearchToolResultErrorParam:



required [ToolSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "tool\_search\_tool\_result\_error"constant

string? ErrorMessage



class ToolSearchToolSearchResultBlock:



required IReadOnlyList<[ToolReferenceBlock](api/messages.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

JsonElement Type "tool\_search\_tool\_search\_result"constant



class ToolSearchToolSearchResultBlockParam:



required IReadOnlyList<[ToolReferenceBlockParam](api/messages.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "tool\_search\_tool\_search\_result"constant



class ToolTextEditor20250124:



JsonElement Name "str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250124"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolTextEditor20250429:



JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250429"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolTextEditor20250728:



JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250728"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Long? MaxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolUnion: A class that can be one of several variants.union 

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



class Tool:



required InputSchema InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required



required string Name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



string Description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Boolean? EagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Type? Type



class ToolBash20250124:



JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash\_20250124"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20250522:



JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20250522"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20250825:



JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20250825"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20260120:

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20260120"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20260521:

Code execution tool with REPL state persistence.



JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20260521"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class MemoryTool20250818:



JsonElement Name "memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "memory\_20250818"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolTextEditor20250124:



JsonElement Name "str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250124"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolTextEditor20250429:



JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250429"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolTextEditor20250728:



JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250728"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Long? MaxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class WebSearchTool20250305:



JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20250305"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



[UserLocation](api/messages.md)? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class WebFetchTool20250910:



JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20250910"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class WebSearchTool20260209:



JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20260209"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



[UserLocation](api/messages.md)? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class WebFetchTool20260209:



JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20260209"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class WebFetchTool20260309:

Web fetch tool with use\_cache parameter for bypassing cached content.



JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20260309"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Boolean UseCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class WebSearchTool20260318:



JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20260318"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.



ResponseInclusion ResponseInclusion

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"Full

"excluded"Excluded

Boolean Strict

When true, guarantees schema validation on tool names and inputs



[UserLocation](api/messages.md)? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class WebFetchTool20260318:



JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20260318"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.



ResponseInclusion ResponseInclusion

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"Full

"excluded"Excluded

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Boolean UseCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class ToolSearchToolBm25\_20251119:



JsonElement Name "tool\_search\_tool\_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



required Type Type

One of the following:

"tool\_search\_tool\_bm25\_20251119"ToolSearchToolBm25\_20251119

"tool\_search\_tool\_bm25"ToolSearchToolBm25



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolSearchToolRegex20251119:



JsonElement Name "tool\_search\_tool\_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



required Type Type

One of the following:

"tool\_search\_tool\_regex\_20251119"ToolSearchToolRegex20251119

"tool\_search\_tool\_regex"ToolSearchToolRegex



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolUseBlock:

required string ID



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant



class ToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url



class UrlPdfSource:

JsonElement Type "url"constant

required string Url



class Usage:



required [CacheCreation](api/messages.md)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.



required [OutputTokensDetails](api/messages.md)? OutputTokensDetails

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



required Long ThinkingTokens

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



required [ServerToolUsage](api/messages.md)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.



required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

One of the following:

"standard"Standard

"priority"Priority

"batch"Batch



class UserLocation:

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class WebFetchBlock:



required [DocumentBlock](api/messages.md) Content



required [CitationsConfig](api/messages.md)? Citations

Citation configuration for the document

required Boolean Enabled



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL



class WebFetchBlockParam:



required [DocumentBlockParam](api/messages.md) Content



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant



class ContentBlockSource:



required Content Content

One of the following:

string



IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant



class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

string? RetrievedAt

ISO 8601 timestamp when the content was retrieved



class WebFetchTool20250910:



JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20250910"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class WebFetchTool20260209:



JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20260209"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class WebFetchTool20260309:

Web fetch tool with use\_cache parameter for bypassing cached content.



JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20260309"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Boolean UseCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class WebFetchTool20260318:



JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20260318"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.



ResponseInclusion ResponseInclusion

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"Full

"excluded"Excluded

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Boolean UseCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class WebFetchToolResultBlock:



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



required Content Content

One of the following:



class WebFetchToolResultErrorBlock:



required [WebFetchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_in\_prior\_context"UrlNotInPriorContext

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant



class WebFetchBlock:



required [DocumentBlock](api/messages.md) Content



required [CitationsConfig](api/messages.md)? Citations

Citation configuration for the document

required Boolean Enabled



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant



class WebFetchToolResultBlockParam:



required Content Content

One of the following:



class WebFetchToolResultErrorBlockParam:



required [WebFetchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_in\_prior\_context"UrlNotInPriorContext

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant



class WebFetchBlockParam:



required [DocumentBlockParam](api/messages.md) Content



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant



class ContentBlockSource:



required Content Content

One of the following:

string



IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant



class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class WebFetchToolResultErrorBlock:



required [WebFetchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_in\_prior\_context"UrlNotInPriorContext

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant



class WebFetchToolResultErrorBlockParam:



required [WebFetchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_in\_prior\_context"UrlNotInPriorContext

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant



enum WebFetchToolResultErrorCode:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_in\_prior\_context"UrlNotInPriorContext

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable



class WebSearchResultBlock:

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url



class WebSearchResultBlockParam:

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge



class WebSearchTool20250305:



JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20250305"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



[UserLocation](api/messages.md)? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class WebSearchTool20260209:



JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20260209"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



[UserLocation](api/messages.md)? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class WebSearchTool20260318:



JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20260318"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.



ResponseInclusion ResponseInclusion

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"Full

"excluded"Excluded

Boolean Strict

When true, guarantees schema validation on tool names and inputs



[UserLocation](api/messages.md)? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class WebSearchToolRequestError:



required [WebSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant



class WebSearchToolResultBlock:



required Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



required [WebSearchToolResultBlockContent](api/messages.md) Content

One of the following:



class WebSearchToolResultError:



required [WebSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant



IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant



class WebSearchToolResultBlockContent: A class that can be one of several variants.union 



class WebSearchToolResultError:



required [WebSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant



IReadOnlyList<[WebSearchResultBlock](api/messages.md)>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web\_search\_result"constant

required string Url



class WebSearchToolResultBlockParam:



required [WebSearchToolResultBlockParamContent](api/messages.md) Content

One of the following:



IReadOnlyList<[WebSearchResultBlockParam](api/messages.md)>

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge



class WebSearchToolRequestError:



required [WebSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class WebSearchToolResultBlockParamContent: A class that can be one of several variants.union 



IReadOnlyList<[WebSearchResultBlockParam](api/messages.md)>

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge



class WebSearchToolRequestError:



required [WebSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant



class WebSearchToolResultError:



required [WebSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant



enum WebSearchToolResultErrorCode:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

#### MessagesBatches

##### [Create a Message Batch](api/messages/batches/create.md)

[MessageBatch](api/messages/batches.md) Messages.Batches.Create(BatchCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/messages/batches/retrieve.md)

[MessageBatch](api/messages/batches.md) Messages.Batches.Retrieve(BatchRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/messages/batches/list.md)

[BatchListPageResponse](api/messages/batches.md) Messages.Batches.List(BatchListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/messages/batches

##### [Cancel a Message Batch](api/messages/batches/cancel.md)

[MessageBatch](api/messages/batches.md) Messages.Batches.Cancel(BatchCancelParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/messages/batches/delete.md)

[DeletedMessageBatch](api/messages/batches.md) Messages.Batches.Delete(BatchDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/messages/batches/results.md)

[MessageBatchIndividualResponse](api/messages/batches.md) Messages.Batches.ResultsStreaming(BatchResultsParamsparameters, CancellationTokencancellationToken = default)

GET/v1/messages/batches/{message\_batch\_id}/results

---

*Copyright © Anthropic. All rights reserved.*
