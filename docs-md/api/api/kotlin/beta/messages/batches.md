# Batches

Copy page

Kotlin

# Batches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

beta().messages().batches().create(BatchCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none()) : [BetaMessageBatch](api/beta.md)

post/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

beta().messages().batches().retrieve(BatchRetrieveParamsparams = BatchRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [BetaMessageBatch](api/beta.md)

get/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

beta().messages().batches().list(BatchListParamsparams = BatchListParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : BatchListPage

get/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

beta().messages().batches().cancel(BatchCancelParamsparams = BatchCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [BetaMessageBatch](api/beta.md)

post/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

beta().messages().batches().delete(BatchDeleteParamsparams = BatchDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [BetaDeletedMessageBatch](api/beta.md)

delete/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

beta().messages().batches().resultsStreaming(BatchResultsParamsparams = BatchResultsParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [BetaMessageBatchIndividualResponse](api/beta.md)

get/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

class BetaDeletedMessageBatch:

id: String

ID of the Message Batch.

type: JsonValue; "message\_batch\_deleted"constant"message\_batch\_deleted"constant

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

MESSAGE\_BATCH\_DELETED("message\_batch\_deleted")

class BetaMessageBatch:

id: String

Unique object identifier.

The format and length of IDs may change over time.

archivedAt: Optional<LocalDateTime>

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

formatdate-time

cancelInitiatedAt: Optional<LocalDateTime>

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

formatdate-time

createdAt: LocalDateTime

RFC 3339 datetime string representing the time at which the Message Batch was created.

formatdate-time

endedAt: Optional<LocalDateTime>

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expiresAt: LocalDateTime

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

formatdate-time

processingStatus: ProcessingStatus

Processing status of the Message Batch.

Accepts one of the following:

IN\_PROGRESS("in\_progress")

CANCELING("canceling")

ENDED("ended")

requestCounts: [BetaMessageBatchRequestCounts](api/beta.md)

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

canceled: Long

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: Long

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: Long

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Long

Number of requests in the Message Batch that are processing.

succeeded: Long

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

resultsUrl: Optional<String>

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: JsonValue; "message\_batch"constant"message\_batch"constant

Object type.

For Message Batches, this is always `"message_batch"`.

Accepts one of the following:

MESSAGE\_BATCH("message\_batch")

class BetaMessageBatchCanceledResult:

type: JsonValue; "canceled"constant"canceled"constant

Accepts one of the following:

CANCELED("canceled")

class BetaMessageBatchErroredResult:

error: [BetaErrorResponse](api/beta.md)

error: [BetaError](api/beta.md)

Accepts one of the following:

class BetaInvalidRequestError:

message: String

type: JsonValue; "invalid\_request\_error"constant"invalid\_request\_error"constant

Accepts one of the following:

INVALID\_REQUEST\_ERROR("invalid\_request\_error")

class BetaAuthenticationError:

message: String

type: JsonValue; "authentication\_error"constant"authentication\_error"constant

Accepts one of the following:

AUTHENTICATION\_ERROR("authentication\_error")

class BetaBillingError:

message: String

type: JsonValue; "billing\_error"constant"billing\_error"constant

Accepts one of the following:

BILLING\_ERROR("billing\_error")

class BetaPermissionError:

message: String

type: JsonValue; "permission\_error"constant"permission\_error"constant

Accepts one of the following:

PERMISSION\_ERROR("permission\_error")

class BetaNotFoundError:

message: String

type: JsonValue; "not\_found\_error"constant"not\_found\_error"constant

Accepts one of the following:

NOT\_FOUND\_ERROR("not\_found\_error")

class BetaRateLimitError:

message: String

type: JsonValue; "rate\_limit\_error"constant"rate\_limit\_error"constant

Accepts one of the following:

RATE\_LIMIT\_ERROR("rate\_limit\_error")

class BetaGatewayTimeoutError:

message: String

type: JsonValue; "timeout\_error"constant"timeout\_error"constant

Accepts one of the following:

TIMEOUT\_ERROR("timeout\_error")

class BetaApiError:

message: String

type: JsonValue; "api\_error"constant"api\_error"constant

Accepts one of the following:

API\_ERROR("api\_error")

class BetaOverloadedError:

message: String

type: JsonValue; "overloaded\_error"constant"overloaded\_error"constant

Accepts one of the following:

OVERLOADED\_ERROR("overloaded\_error")

requestId: Optional<String>

type: JsonValue; "error"constant"error"constant

Accepts one of the following:

ERROR("error")

type: JsonValue; "errored"constant"errored"constant

Accepts one of the following:

ERRORED("errored")

class BetaMessageBatchExpiredResult:

type: JsonValue; "expired"constant"expired"constant

Accepts one of the following:

EXPIRED("expired")

class BetaMessageBatchIndividualResponse:

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

customId: String

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [BetaMessageBatchResult](api/beta.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class BetaMessageBatchSucceededResult:

message: [BetaMessage](api/beta.md)

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: Optional<[BetaContainer](api/beta.md)>

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expiresAt: LocalDateTime

The time at which the container will expire.

formatdate-time

skills: Optional<List<[BetaSkill](api/beta.md)>>

Skills loaded in the container

skillId: String

Skill ID

maxLength64

minLength1

type: Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: List<[BetaContentBlock](api/beta.md)>

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

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaThinkingBlock:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlock:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class BetaToolUseBlock:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaServerToolUseBlock:

id: String

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

input: Input

name: Name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

class BetaWebSearchToolResultBlock:

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

List<[BetaWebSearchResultBlock](api/beta.md)>

encryptedContent: String

pageAge: Optional<String>

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

class BetaWebFetchToolResultBlock:

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchBlock:

content: [BetaDocumentBlock](api/beta.md)

citations: Optional<[BetaCitationConfig](api/beta.md)>

Citation configuration for the document

enabled: Boolean

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

title: Optional<String>

The title of the document

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

toolUseId: String

type: JsonValue; "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT("web\_fetch\_tool\_result")

class BetaCodeExecutionToolResultBlock:

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlock:

content: List<[BetaCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

toolUseId: String

type: JsonValue; "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT("code\_execution\_tool\_result")

class BetaBashCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionResultBlock:

content: List<[BetaBashCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

toolUseId: String

type: JsonValue; "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT("bash\_code\_execution\_tool\_result")

class BetaTextEditorCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

errorMessage: Optional<String>

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

class BetaTextEditorCodeExecutionViewResultBlock:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

class BetaTextEditorCodeExecutionCreateResultBlock:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

toolUseId: String

type: JsonValue; "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT("text\_editor\_code\_execution\_tool\_result")

class BetaToolSearchToolResultBlock:

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

errorMessage: Optional<String>

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlock:

toolReferences: List<[BetaToolReferenceBlock](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

toolUseId: String

type: JsonValue; "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT("tool\_search\_tool\_result")

class BetaMcpToolUseBlock:

id: String

input: Input

name: String

The name of the MCP tool

serverName: String

The name of the MCP server

type: JsonValue; "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Accepts one of the following:

MCP\_TOOL\_USE("mcp\_tool\_use")

class BetaMcpToolResultBlock:

content: Content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

isError: Boolean

toolUseId: String

type: JsonValue; "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Accepts one of the following:

MCP\_TOOL\_RESULT("mcp\_tool\_result")

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

fileId: String

type: JsonValue; "container\_upload"constant"container\_upload"constant

Accepts one of the following:

CONTAINER\_UPLOAD("container\_upload")

contextManagement: Optional<[BetaContextManagementResponse](api/beta.md)>

Context management response.

Information about context management strategies applied during the request.

appliedEdits: List<AppliedEdit>

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedToolUses: Long

Number of tool uses that were cleared.

minimum0

type: JsonValue; "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_TOOL\_USES\_20250919("clear\_tool\_uses\_20250919")

class BetaClearThinking20251015EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedThinkingTurns: Long

Number of thinking turns that were cleared.

minimum0

type: JsonValue; "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_THINKING\_20251015("clear\_thinking\_20251015")

model: Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_3\_7\_SONNET\_LATEST("claude-3-7-sonnet-latest")

High-performance model with early extended thinking

CLAUDE\_3\_7\_SONNET\_20250219("claude-3-7-sonnet-20250219")

High-performance model with early extended thinking

CLAUDE\_3\_5\_HAIKU\_LATEST("claude-3-5-haiku-latest")

Fastest and most compact model for near-instant responsiveness

CLAUDE\_3\_5\_HAIKU\_20241022("claude-3-5-haiku-20241022")

Our fastest model

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_4\_SONNET\_20250514("claude-4-sonnet-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

Our best model for real-world agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

Our best model for real-world agents and coding

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Our most capable model

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Our most capable model

CLAUDE\_4\_OPUS\_20250514("claude-4-opus-20250514")

Our most capable model

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Our most capable model

CLAUDE\_3\_OPUS\_LATEST("claude-3-opus-latest")

Excels at writing and complex tasks

CLAUDE\_3\_OPUS\_20240229("claude-3-opus-20240229")

Excels at writing and complex tasks

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Our previous most fast and cost-effective

role: JsonValue; "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

ASSISTANT("assistant")

stopReason: Optional<[BetaStopReason](api/beta.md)>

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

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

stopSequence: Optional<String>

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: JsonValue; "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

usage: [BetaUsage](api/beta.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cacheCreation: Optional<[BetaCacheCreation](api/beta.md)>

Breakdown of cached tokens by TTL

ephemeral1hInputTokens: Long

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral5mInputTokens: Long

The number of input tokens used to create the 5 minute cache entry.

minimum0

cacheCreationInputTokens: Optional<Long>

The number of input tokens used to create the cache entry.

minimum0

cacheReadInputTokens: Optional<Long>

The number of input tokens read from the cache.

minimum0

inputTokens: Long

The number of input tokens which were used.

minimum0

outputTokens: Long

The number of output tokens which were used.

minimum0

serverToolUse: Optional<[BetaServerToolUsage](api/beta.md)>

The number of server tool requests.

webFetchRequests: Long

The number of web fetch tool requests.

minimum0

webSearchRequests: Long

The number of web search tool requests.

minimum0

serviceTier: Optional<ServiceTier>

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

type: JsonValue; "succeeded"constant"succeeded"constant

Accepts one of the following:

SUCCEEDED("succeeded")

class BetaMessageBatchErroredResult:

error: [BetaErrorResponse](api/beta.md)

error: [BetaError](api/beta.md)

Accepts one of the following:

class BetaInvalidRequestError:

message: String

type: JsonValue; "invalid\_request\_error"constant"invalid\_request\_error"constant

Accepts one of the following:

INVALID\_REQUEST\_ERROR("invalid\_request\_error")

class BetaAuthenticationError:

message: String

type: JsonValue; "authentication\_error"constant"authentication\_error"constant

Accepts one of the following:

AUTHENTICATION\_ERROR("authentication\_error")

class BetaBillingError:

message: String

type: JsonValue; "billing\_error"constant"billing\_error"constant

Accepts one of the following:

BILLING\_ERROR("billing\_error")

class BetaPermissionError:

message: String

type: JsonValue; "permission\_error"constant"permission\_error"constant

Accepts one of the following:

PERMISSION\_ERROR("permission\_error")

class BetaNotFoundError:

message: String

type: JsonValue; "not\_found\_error"constant"not\_found\_error"constant

Accepts one of the following:

NOT\_FOUND\_ERROR("not\_found\_error")

class BetaRateLimitError:

message: String

type: JsonValue; "rate\_limit\_error"constant"rate\_limit\_error"constant

Accepts one of the following:

RATE\_LIMIT\_ERROR("rate\_limit\_error")

class BetaGatewayTimeoutError:

message: String

type: JsonValue; "timeout\_error"constant"timeout\_error"constant

Accepts one of the following:

TIMEOUT\_ERROR("timeout\_error")

class BetaApiError:

message: String

type: JsonValue; "api\_error"constant"api\_error"constant

Accepts one of the following:

API\_ERROR("api\_error")

class BetaOverloadedError:

message: String

type: JsonValue; "overloaded\_error"constant"overloaded\_error"constant

Accepts one of the following:

OVERLOADED\_ERROR("overloaded\_error")

requestId: Optional<String>

type: JsonValue; "error"constant"error"constant

Accepts one of the following:

ERROR("error")

type: JsonValue; "errored"constant"errored"constant

Accepts one of the following:

ERRORED("errored")

class BetaMessageBatchCanceledResult:

type: JsonValue; "canceled"constant"canceled"constant

Accepts one of the following:

CANCELED("canceled")

class BetaMessageBatchExpiredResult:

type: JsonValue; "expired"constant"expired"constant

Accepts one of the following:

EXPIRED("expired")

class BetaMessageBatchRequestCounts:

canceled: Long

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: Long

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: Long

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Long

Number of requests in the Message Batch that are processing.

succeeded: Long

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

class BetaMessageBatchResult: A class that can be one of several variants.union

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

class BetaMessageBatchSucceededResult:

message: [BetaMessage](api/beta.md)

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: Optional<[BetaContainer](api/beta.md)>

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expiresAt: LocalDateTime

The time at which the container will expire.

formatdate-time

skills: Optional<List<[BetaSkill](api/beta.md)>>

Skills loaded in the container

skillId: String

Skill ID

maxLength64

minLength1

type: Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: List<[BetaContentBlock](api/beta.md)>

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

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaThinkingBlock:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlock:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class BetaToolUseBlock:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaServerToolUseBlock:

id: String

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

input: Input

name: Name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

class BetaWebSearchToolResultBlock:

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

List<[BetaWebSearchResultBlock](api/beta.md)>

encryptedContent: String

pageAge: Optional<String>

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

class BetaWebFetchToolResultBlock:

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchBlock:

content: [BetaDocumentBlock](api/beta.md)

citations: Optional<[BetaCitationConfig](api/beta.md)>

Citation configuration for the document

enabled: Boolean

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

title: Optional<String>

The title of the document

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

toolUseId: String

type: JsonValue; "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT("web\_fetch\_tool\_result")

class BetaCodeExecutionToolResultBlock:

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlock:

content: List<[BetaCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

toolUseId: String

type: JsonValue; "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT("code\_execution\_tool\_result")

class BetaBashCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionResultBlock:

content: List<[BetaBashCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

toolUseId: String

type: JsonValue; "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT("bash\_code\_execution\_tool\_result")

class BetaTextEditorCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

errorMessage: Optional<String>

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

class BetaTextEditorCodeExecutionViewResultBlock:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

class BetaTextEditorCodeExecutionCreateResultBlock:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

toolUseId: String

type: JsonValue; "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT("text\_editor\_code\_execution\_tool\_result")

class BetaToolSearchToolResultBlock:

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

errorMessage: Optional<String>

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlock:

toolReferences: List<[BetaToolReferenceBlock](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

toolUseId: String

type: JsonValue; "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT("tool\_search\_tool\_result")

class BetaMcpToolUseBlock:

id: String

input: Input

name: String

The name of the MCP tool

serverName: String

The name of the MCP server

type: JsonValue; "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Accepts one of the following:

MCP\_TOOL\_USE("mcp\_tool\_use")

class BetaMcpToolResultBlock:

content: Content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

isError: Boolean

toolUseId: String

type: JsonValue; "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Accepts one of the following:

MCP\_TOOL\_RESULT("mcp\_tool\_result")

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

fileId: String

type: JsonValue; "container\_upload"constant"container\_upload"constant

Accepts one of the following:

CONTAINER\_UPLOAD("container\_upload")

contextManagement: Optional<[BetaContextManagementResponse](api/beta.md)>

Context management response.

Information about context management strategies applied during the request.

appliedEdits: List<AppliedEdit>

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedToolUses: Long

Number of tool uses that were cleared.

minimum0

type: JsonValue; "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_TOOL\_USES\_20250919("clear\_tool\_uses\_20250919")

class BetaClearThinking20251015EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedThinkingTurns: Long

Number of thinking turns that were cleared.

minimum0

type: JsonValue; "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_THINKING\_20251015("clear\_thinking\_20251015")

model: Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_3\_7\_SONNET\_LATEST("claude-3-7-sonnet-latest")

High-performance model with early extended thinking

CLAUDE\_3\_7\_SONNET\_20250219("claude-3-7-sonnet-20250219")

High-performance model with early extended thinking

CLAUDE\_3\_5\_HAIKU\_LATEST("claude-3-5-haiku-latest")

Fastest and most compact model for near-instant responsiveness

CLAUDE\_3\_5\_HAIKU\_20241022("claude-3-5-haiku-20241022")

Our fastest model

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_4\_SONNET\_20250514("claude-4-sonnet-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

Our best model for real-world agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

Our best model for real-world agents and coding

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Our most capable model

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Our most capable model

CLAUDE\_4\_OPUS\_20250514("claude-4-opus-20250514")

Our most capable model

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Our most capable model

CLAUDE\_3\_OPUS\_LATEST("claude-3-opus-latest")

Excels at writing and complex tasks

CLAUDE\_3\_OPUS\_20240229("claude-3-opus-20240229")

Excels at writing and complex tasks

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Our previous most fast and cost-effective

role: JsonValue; "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

ASSISTANT("assistant")

stopReason: Optional<[BetaStopReason](api/beta.md)>

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

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

stopSequence: Optional<String>

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: JsonValue; "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

usage: [BetaUsage](api/beta.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cacheCreation: Optional<[BetaCacheCreation](api/beta.md)>

Breakdown of cached tokens by TTL

ephemeral1hInputTokens: Long

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral5mInputTokens: Long

The number of input tokens used to create the 5 minute cache entry.

minimum0

cacheCreationInputTokens: Optional<Long>

The number of input tokens used to create the cache entry.

minimum0

cacheReadInputTokens: Optional<Long>

The number of input tokens read from the cache.

minimum0

inputTokens: Long

The number of input tokens which were used.

minimum0

outputTokens: Long

The number of output tokens which were used.

minimum0

serverToolUse: Optional<[BetaServerToolUsage](api/beta.md)>

The number of server tool requests.

webFetchRequests: Long

The number of web fetch tool requests.

minimum0

webSearchRequests: Long

The number of web search tool requests.

minimum0

serviceTier: Optional<ServiceTier>

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

type: JsonValue; "succeeded"constant"succeeded"constant

Accepts one of the following:

SUCCEEDED("succeeded")

class BetaMessageBatchErroredResult:

error: [BetaErrorResponse](api/beta.md)

error: [BetaError](api/beta.md)

Accepts one of the following:

class BetaInvalidRequestError:

message: String

type: JsonValue; "invalid\_request\_error"constant"invalid\_request\_error"constant

Accepts one of the following:

INVALID\_REQUEST\_ERROR("invalid\_request\_error")

class BetaAuthenticationError:

message: String

type: JsonValue; "authentication\_error"constant"authentication\_error"constant

Accepts one of the following:

AUTHENTICATION\_ERROR("authentication\_error")

class BetaBillingError:

message: String

type: JsonValue; "billing\_error"constant"billing\_error"constant

Accepts one of the following:

BILLING\_ERROR("billing\_error")

class BetaPermissionError:

message: String

type: JsonValue; "permission\_error"constant"permission\_error"constant

Accepts one of the following:

PERMISSION\_ERROR("permission\_error")

class BetaNotFoundError:

message: String

type: JsonValue; "not\_found\_error"constant"not\_found\_error"constant

Accepts one of the following:

NOT\_FOUND\_ERROR("not\_found\_error")

class BetaRateLimitError:

message: String

type: JsonValue; "rate\_limit\_error"constant"rate\_limit\_error"constant

Accepts one of the following:

RATE\_LIMIT\_ERROR("rate\_limit\_error")

class BetaGatewayTimeoutError:

message: String

type: JsonValue; "timeout\_error"constant"timeout\_error"constant

Accepts one of the following:

TIMEOUT\_ERROR("timeout\_error")

class BetaApiError:

message: String

type: JsonValue; "api\_error"constant"api\_error"constant

Accepts one of the following:

API\_ERROR("api\_error")

class BetaOverloadedError:

message: String

type: JsonValue; "overloaded\_error"constant"overloaded\_error"constant

Accepts one of the following:

OVERLOADED\_ERROR("overloaded\_error")

requestId: Optional<String>

type: JsonValue; "error"constant"error"constant

Accepts one of the following:

ERROR("error")

type: JsonValue; "errored"constant"errored"constant

Accepts one of the following:

ERRORED("errored")

class BetaMessageBatchCanceledResult:

type: JsonValue; "canceled"constant"canceled"constant

Accepts one of the following:

CANCELED("canceled")

class BetaMessageBatchExpiredResult:

type: JsonValue; "expired"constant"expired"constant

Accepts one of the following:

EXPIRED("expired")

class BetaMessageBatchSucceededResult:

message: [BetaMessage](api/beta.md)

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: Optional<[BetaContainer](api/beta.md)>

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expiresAt: LocalDateTime

The time at which the container will expire.

formatdate-time

skills: Optional<List<[BetaSkill](api/beta.md)>>

Skills loaded in the container

skillId: String

Skill ID

maxLength64

minLength1

type: Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: List<[BetaContentBlock](api/beta.md)>

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

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaThinkingBlock:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlock:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class BetaToolUseBlock:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaServerToolUseBlock:

id: String

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

input: Input

name: Name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

class BetaWebSearchToolResultBlock:

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

List<[BetaWebSearchResultBlock](api/beta.md)>

encryptedContent: String

pageAge: Optional<String>

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

class BetaWebFetchToolResultBlock:

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchBlock:

content: [BetaDocumentBlock](api/beta.md)

citations: Optional<[BetaCitationConfig](api/beta.md)>

Citation configuration for the document

enabled: Boolean

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

title: Optional<String>

The title of the document

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

toolUseId: String

type: JsonValue; "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT("web\_fetch\_tool\_result")

class BetaCodeExecutionToolResultBlock:

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlock:

content: List<[BetaCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

toolUseId: String

type: JsonValue; "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT("code\_execution\_tool\_result")

class BetaBashCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionResultBlock:

content: List<[BetaBashCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

toolUseId: String

type: JsonValue; "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT("bash\_code\_execution\_tool\_result")

class BetaTextEditorCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

errorMessage: Optional<String>

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

class BetaTextEditorCodeExecutionViewResultBlock:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

class BetaTextEditorCodeExecutionCreateResultBlock:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

toolUseId: String

type: JsonValue; "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT("text\_editor\_code\_execution\_tool\_result")

class BetaToolSearchToolResultBlock:

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

errorMessage: Optional<String>

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlock:

toolReferences: List<[BetaToolReferenceBlock](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

toolUseId: String

type: JsonValue; "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT("tool\_search\_tool\_result")

class BetaMcpToolUseBlock:

id: String

input: Input

name: String

The name of the MCP tool

serverName: String

The name of the MCP server

type: JsonValue; "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Accepts one of the following:

MCP\_TOOL\_USE("mcp\_tool\_use")

class BetaMcpToolResultBlock:

content: Content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

isError: Boolean

toolUseId: String

type: JsonValue; "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Accepts one of the following:

MCP\_TOOL\_RESULT("mcp\_tool\_result")

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

fileId: String

type: JsonValue; "container\_upload"constant"container\_upload"constant

Accepts one of the following:

CONTAINER\_UPLOAD("container\_upload")

contextManagement: Optional<[BetaContextManagementResponse](api/beta.md)>

Context management response.

Information about context management strategies applied during the request.

appliedEdits: List<AppliedEdit>

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedToolUses: Long

Number of tool uses that were cleared.

minimum0

type: JsonValue; "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_TOOL\_USES\_20250919("clear\_tool\_uses\_20250919")

class BetaClearThinking20251015EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedThinkingTurns: Long

Number of thinking turns that were cleared.

minimum0

type: JsonValue; "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_THINKING\_20251015("clear\_thinking\_20251015")

model: Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_3\_7\_SONNET\_LATEST("claude-3-7-sonnet-latest")

High-performance model with early extended thinking

CLAUDE\_3\_7\_SONNET\_20250219("claude-3-7-sonnet-20250219")

High-performance model with early extended thinking

CLAUDE\_3\_5\_HAIKU\_LATEST("claude-3-5-haiku-latest")

Fastest and most compact model for near-instant responsiveness

CLAUDE\_3\_5\_HAIKU\_20241022("claude-3-5-haiku-20241022")

Our fastest model

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_4\_SONNET\_20250514("claude-4-sonnet-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

Our best model for real-world agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

Our best model for real-world agents and coding

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Our most capable model

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Our most capable model

CLAUDE\_4\_OPUS\_20250514("claude-4-opus-20250514")

Our most capable model

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Our most capable model

CLAUDE\_3\_OPUS\_LATEST("claude-3-opus-latest")

Excels at writing and complex tasks

CLAUDE\_3\_OPUS\_20240229("claude-3-opus-20240229")

Excels at writing and complex tasks

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Our previous most fast and cost-effective

role: JsonValue; "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

ASSISTANT("assistant")

stopReason: Optional<[BetaStopReason](api/beta.md)>

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

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

stopSequence: Optional<String>

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: JsonValue; "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

usage: [BetaUsage](api/beta.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cacheCreation: Optional<[BetaCacheCreation](api/beta.md)>

Breakdown of cached tokens by TTL

ephemeral1hInputTokens: Long

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral5mInputTokens: Long

The number of input tokens used to create the 5 minute cache entry.

minimum0

cacheCreationInputTokens: Optional<Long>

The number of input tokens used to create the cache entry.

minimum0

cacheReadInputTokens: Optional<Long>

The number of input tokens read from the cache.

minimum0

inputTokens: Long

The number of input tokens which were used.

minimum0

outputTokens: Long

The number of output tokens which were used.

minimum0

serverToolUse: Optional<[BetaServerToolUsage](api/beta.md)>

The number of server tool requests.

webFetchRequests: Long

The number of web fetch tool requests.

minimum0

webSearchRequests: Long

The number of web search tool requests.

minimum0

serviceTier: Optional<ServiceTier>

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

type: JsonValue; "succeeded"constant"succeeded"constant

Accepts one of the following:

SUCCEEDED("succeeded")