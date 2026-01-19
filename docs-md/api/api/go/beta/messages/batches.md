# Batches

Copy page

Go

# Batches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

client.Beta.Messages.Batches.New(ctx, params) (\*[BetaMessageBatch](api/beta.md), error)

post/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

client.Beta.Messages.Batches.Get(ctx, messageBatchID, query) (\*[BetaMessageBatch](api/beta.md), error)

get/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

client.Beta.Messages.Batches.List(ctx, params) (\*Page[[BetaMessageBatch](api/beta.md)], error)

get/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

client.Beta.Messages.Batches.Cancel(ctx, messageBatchID, body) (\*[BetaMessageBatch](api/beta.md), error)

post/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

client.Beta.Messages.Batches.Delete(ctx, messageBatchID, body) (\*[BetaDeletedMessageBatch](api/beta.md), error)

delete/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

client.Beta.Messages.Batches.Results(ctx, messageBatchID, query) (\*[BetaMessageBatchIndividualResponse](api/beta.md), error)

get/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

type BetaDeletedMessageBatch struct{…}

ID string

ID of the Message Batch.

Type MessageBatchDeleted

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

const MessageBatchDeletedMessageBatchDeleted MessageBatchDeleted = "message\_batch\_deleted"

type BetaMessageBatch struct{…}

ID string

Unique object identifier.

The format and length of IDs may change over time.

ArchivedAt Time

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

formatdate-time

CancelInitiatedAt Time

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

formatdate-time

CreatedAt Time

RFC 3339 datetime string representing the time at which the Message Batch was created.

formatdate-time

EndedAt Time

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

ExpiresAt Time

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

formatdate-time

ProcessingStatus BetaMessageBatchProcessingStatus

Processing status of the Message Batch.

Accepts one of the following:

const BetaMessageBatchProcessingStatusInProgress BetaMessageBatchProcessingStatus = "in\_progress"

const BetaMessageBatchProcessingStatusCanceling BetaMessageBatchProcessingStatus = "canceling"

const BetaMessageBatchProcessingStatusEnded BetaMessageBatchProcessingStatus = "ended"

RequestCounts [BetaMessageBatchRequestCounts](api/beta.md)

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

Canceled int64

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

Errored int64

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

Expired int64

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

Processing int64

Number of requests in the Message Batch that are processing.

Succeeded int64

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

ResultsURL string

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Type MessageBatch

Object type.

For Message Batches, this is always `"message_batch"`.

Accepts one of the following:

const MessageBatchMessageBatch MessageBatch = "message\_batch"

type BetaMessageBatchCanceledResult struct{…}

Type Canceled

Accepts one of the following:

const CanceledCanceled Canceled = "canceled"

type BetaMessageBatchErroredResult struct{…}

Error [BetaErrorResponse](api/beta.md)

Error [BetaErrorUnion](api/beta.md)

Accepts one of the following:

type BetaInvalidRequestError struct{…}

Message string

Type InvalidRequestError

Accepts one of the following:

const InvalidRequestErrorInvalidRequestError InvalidRequestError = "invalid\_request\_error"

type BetaAuthenticationError struct{…}

Message string

Type AuthenticationError

Accepts one of the following:

const AuthenticationErrorAuthenticationError AuthenticationError = "authentication\_error"

type BetaBillingError struct{…}

Message string

Type BillingError

Accepts one of the following:

const BillingErrorBillingError BillingError = "billing\_error"

type BetaPermissionError struct{…}

Message string

Type PermissionError

Accepts one of the following:

const PermissionErrorPermissionError PermissionError = "permission\_error"

type BetaNotFoundError struct{…}

Message string

Type NotFoundError

Accepts one of the following:

const NotFoundErrorNotFoundError NotFoundError = "not\_found\_error"

type BetaRateLimitError struct{…}

Message string

Type RateLimitError

Accepts one of the following:

const RateLimitErrorRateLimitError RateLimitError = "rate\_limit\_error"

type BetaGatewayTimeoutError struct{…}

Message string

Type TimeoutError

Accepts one of the following:

const TimeoutErrorTimeoutError TimeoutError = "timeout\_error"

type BetaAPIError struct{…}

Message string

Type APIError

Accepts one of the following:

const APIErrorAPIError APIError = "api\_error"

type BetaOverloadedError struct{…}

Message string

Type OverloadedError

Accepts one of the following:

const OverloadedErrorOverloadedError OverloadedError = "overloaded\_error"

RequestID string

Type Error

Accepts one of the following:

const ErrorError Error = "error"

Type Errored

Accepts one of the following:

const ErroredErrored Errored = "errored"

type BetaMessageBatchExpiredResult struct{…}

Type Expired

Accepts one of the following:

const ExpiredExpired Expired = "expired"

type BetaMessageBatchIndividualResponse struct{…}

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

CustomID string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

Result [BetaMessageBatchResultUnion](api/beta.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

type BetaMessageBatchSucceededResult struct{…}

Message [BetaMessage](api/beta.md)

ID string

Unique object identifier.

The format and length of IDs may change over time.

Container [BetaContainer](api/beta.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

formatdate-time

Skills [][BetaSkill](api/beta.md)

Skills loaded in the container

SkillID string

Skill ID

maxLength64

minLength1

Type BetaSkillType

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

const BetaSkillTypeAnthropic BetaSkillType = "anthropic"

const BetaSkillTypeCustom BetaSkillType = "custom"

Version string

Skill version or 'latest' for most recent version

maxLength64

minLength1

Content [][BetaContentBlockUnion](api/beta.md)

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

type BetaTextBlock struct{…}

Citations [][BetaTextCitationUnion](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char\_location"

type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page\_location"

type BetaCitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content\_block\_location"

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web\_search\_result\_location"

URL string

type BetaCitationSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search\_result\_location"

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

type BetaThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type BetaRedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted\_thinking"

type BetaToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool\_use"

Caller BetaToolUseBlockCallerUnionoptional

Tool invocation directly from the model.

Accepts one of the following:

type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

Accepts one of the following:

const DirectDirect Direct = "direct"

type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

Accepts one of the following:

const CodeExecution20250825CodeExecution20250825 CodeExecution20250825 = "code\_execution\_20250825"

type BetaServerToolUseBlock struct{…}

ID string

Caller BetaServerToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

Accepts one of the following:

const DirectDirect Direct = "direct"

type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

Accepts one of the following:

const CodeExecution20250825CodeExecution20250825 CodeExecution20250825 = "code\_execution\_20250825"

Input map[string, any]

Name BetaServerToolUseBlockName

Accepts one of the following:

const BetaServerToolUseBlockNameWebSearch BetaServerToolUseBlockName = "web\_search"

const BetaServerToolUseBlockNameWebFetch BetaServerToolUseBlockName = "web\_fetch"

const BetaServerToolUseBlockNameCodeExecution BetaServerToolUseBlockName = "code\_execution"

const BetaServerToolUseBlockNameBashCodeExecution BetaServerToolUseBlockName = "bash\_code\_execution"

const BetaServerToolUseBlockNameTextEditorCodeExecution BetaServerToolUseBlockName = "text\_editor\_code\_execution"

const BetaServerToolUseBlockNameToolSearchToolRegex BetaServerToolUseBlockName = "tool\_search\_tool\_regex"

const BetaServerToolUseBlockNameToolSearchToolBm25 BetaServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server\_tool\_use"

type BetaWebSearchToolResultBlock struct{…}

Content [BetaWebSearchToolResultBlockContentUnion](api/beta.md)

Accepts one of the following:

type BetaWebSearchToolResultError struct{…}

ErrorCode [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta.md) = "query\_too\_long"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web\_search\_tool\_result\_error"

type BetaWebSearchToolResultBlockContentArray [][BetaWebSearchResultBlock](api/beta.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

Accepts one of the following:

const WebSearchResultWebSearchResult WebSearchResult = "web\_search\_result"

URL string

ToolUseID string

Type WebSearchToolResult

Accepts one of the following:

const WebSearchToolResultWebSearchToolResult WebSearchToolResult = "web\_search\_tool\_result"

type BetaWebFetchToolResultBlock struct{…}

Content BetaWebFetchToolResultBlockContentUnion

Accepts one of the following:

type BetaWebFetchToolResultErrorBlock struct{…}

ErrorCode [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta.md) = "unavailable"

Type WebFetchToolResultError

Accepts one of the following:

const WebFetchToolResultErrorWebFetchToolResultError WebFetchToolResultError = "web\_fetch\_tool\_result\_error"

type BetaWebFetchBlock struct{…}

Content [BetaDocumentBlock](api/beta.md)

Citations [BetaCitationConfig](api/beta.md)

Citation configuration for the document

Enabled bool

Source BetaDocumentBlockSourceUnion

Accepts one of the following:

type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Accepts one of the following:

const ApplicationPDFApplicationPDF ApplicationPDF = "application/pdf"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Accepts one of the following:

const TextPlainTextPlain TextPlain = "text/plain"

Type Text

Accepts one of the following:

const TextText Text = "text"

Title string

The title of the document

Type Document

Accepts one of the following:

const DocumentDocument Document = "document"

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

Accepts one of the following:

const WebFetchResultWebFetchResult WebFetchResult = "web\_fetch\_result"

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

Accepts one of the following:

const WebFetchToolResultWebFetchToolResult WebFetchToolResult = "web\_fetch\_tool\_result"

type BetaCodeExecutionToolResultBlock struct{…}

Content [BetaCodeExecutionToolResultBlockContentUnion](api/beta.md)

Accepts one of the following:

type BetaCodeExecutionToolResultError struct{…}

ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError

Accepts one of the following:

const CodeExecutionToolResultErrorCodeExecutionToolResultError CodeExecutionToolResultError = "code\_execution\_tool\_result\_error"

type BetaCodeExecutionResultBlock struct{…}

Content [][BetaCodeExecutionOutputBlock](api/beta.md)

FileID string

Type CodeExecutionOutput

Accepts one of the following:

const CodeExecutionOutputCodeExecutionOutput CodeExecutionOutput = "code\_execution\_output"

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

Accepts one of the following:

const CodeExecutionResultCodeExecutionResult CodeExecutionResult = "code\_execution\_result"

ToolUseID string

Type CodeExecutionToolResult

Accepts one of the following:

const CodeExecutionToolResultCodeExecutionToolResult CodeExecutionToolResult = "code\_execution\_tool\_result"

type BetaBashCodeExecutionToolResultBlock struct{…}

Content BetaBashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BetaBashCodeExecutionToolResultError struct{…}

ErrorCode BetaBashCodeExecutionToolResultErrorErrorCode

Accepts one of the following:

const BetaBashCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaBashCodeExecutionToolResultErrorErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaBashCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaBashCodeExecutionToolResultErrorErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorErrorCode = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError

Accepts one of the following:

const BashCodeExecutionToolResultErrorBashCodeExecutionToolResultError BashCodeExecutionToolResultError = "bash\_code\_execution\_tool\_result\_error"

type BetaBashCodeExecutionResultBlock struct{…}

Content [][BetaBashCodeExecutionOutputBlock](api/beta.md)

FileID string

Type BashCodeExecutionOutput

Accepts one of the following:

const BashCodeExecutionOutputBashCodeExecutionOutput BashCodeExecutionOutput = "bash\_code\_execution\_output"

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

Accepts one of the following:

const BashCodeExecutionResultBashCodeExecutionResult BashCodeExecutionResult = "bash\_code\_execution\_result"

ToolUseID string

Type BashCodeExecutionToolResult

Accepts one of the following:

const BashCodeExecutionToolResultBashCodeExecutionToolResult BashCodeExecutionToolResult = "bash\_code\_execution\_tool\_result"

type BetaTextEditorCodeExecutionToolResultBlock struct{…}

Content BetaTextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BetaTextEditorCodeExecutionToolResultError struct{…}

ErrorCode BetaTextEditorCodeExecutionToolResultErrorErrorCode

Accepts one of the following:

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorErrorCode = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorTextEditorCodeExecutionToolResultError TextEditorCodeExecutionToolResultError = "text\_editor\_code\_execution\_tool\_result\_error"

type BetaTextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType BetaTextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const BetaTextEditorCodeExecutionViewResultBlockFileTypeText BetaTextEditorCodeExecutionViewResultBlockFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockFileTypeImage BetaTextEditorCodeExecutionViewResultBlockFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockFileTypePDF BetaTextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

Accepts one of the following:

const TextEditorCodeExecutionViewResultTextEditorCodeExecutionViewResult TextEditorCodeExecutionViewResult = "text\_editor\_code\_execution\_view\_result"

type BetaTextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

Accepts one of the following:

const TextEditorCodeExecutionCreateResultTextEditorCodeExecutionCreateResult TextEditorCodeExecutionCreateResult = "text\_editor\_code\_execution\_create\_result"

type BetaTextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

Accepts one of the following:

const TextEditorCodeExecutionStrReplaceResultTextEditorCodeExecutionStrReplaceResult TextEditorCodeExecutionStrReplaceResult = "text\_editor\_code\_execution\_str\_replace\_result"

ToolUseID string

Type TextEditorCodeExecutionToolResult

Accepts one of the following:

const TextEditorCodeExecutionToolResultTextEditorCodeExecutionToolResult TextEditorCodeExecutionToolResult = "text\_editor\_code\_execution\_tool\_result"

type BetaToolSearchToolResultBlock struct{…}

Content BetaToolSearchToolResultBlockContentUnion

Accepts one of the following:

type BetaToolSearchToolResultError struct{…}

ErrorCode BetaToolSearchToolResultErrorErrorCode

Accepts one of the following:

const BetaToolSearchToolResultErrorErrorCodeInvalidToolInput BetaToolSearchToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaToolSearchToolResultErrorErrorCodeUnavailable BetaToolSearchToolResultErrorErrorCode = "unavailable"

const BetaToolSearchToolResultErrorErrorCodeTooManyRequests BetaToolSearchToolResultErrorErrorCode = "too\_many\_requests"

const BetaToolSearchToolResultErrorErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorErrorCode = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

Accepts one of the following:

const ToolSearchToolResultErrorToolSearchToolResultError ToolSearchToolResultError = "tool\_search\_tool\_result\_error"

type BetaToolSearchToolSearchResultBlock struct{…}

ToolReferences [][BetaToolReferenceBlock](api/beta.md)

ToolName string

Type ToolReference

Accepts one of the following:

const ToolReferenceToolReference ToolReference = "tool\_reference"

Type ToolSearchToolSearchResult

Accepts one of the following:

const ToolSearchToolSearchResultToolSearchToolSearchResult ToolSearchToolSearchResult = "tool\_search\_tool\_search\_result"

ToolUseID string

Type ToolSearchToolResult

Accepts one of the following:

const ToolSearchToolResultToolSearchToolResult ToolSearchToolResult = "tool\_search\_tool\_result"

type BetaMCPToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

The name of the MCP tool

ServerName string

The name of the MCP server

Type MCPToolUse

Accepts one of the following:

const MCPToolUseMCPToolUse MCPToolUse = "mcp\_tool\_use"

type BetaMCPToolResultBlock struct{…}

Content BetaMCPToolResultBlockContentUnion

Accepts one of the following:

string

type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent [][BetaTextBlock](api/beta.md)

Citations [][BetaTextCitationUnion](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char\_location"

type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page\_location"

type BetaCitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content\_block\_location"

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web\_search\_result\_location"

URL string

type BetaCitationSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search\_result\_location"

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

IsError bool

ToolUseID string

Type MCPToolResult

Accepts one of the following:

const MCPToolResultMCPToolResult MCPToolResult = "mcp\_tool\_result"

type BetaContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

Accepts one of the following:

const ContainerUploadContainerUpload ContainerUpload = "container\_upload"

ContextManagement [BetaContextManagementResponse](api/beta.md)

Context management response.

Information about context management strategies applied during the request.

AppliedEdits []BetaContextManagementResponseAppliedEditUnion

List of context management edits that were applied.

Accepts one of the following:

type BetaClearToolUses20250919EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

minimum0

ClearedToolUses int64

Number of tool uses that were cleared.

minimum0

Type ClearToolUses20250919

The type of context management edit applied.

Accepts one of the following:

const ClearToolUses20250919ClearToolUses20250919 ClearToolUses20250919 = "clear\_tool\_uses\_20250919"

type BetaClearThinking20251015EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

minimum0

ClearedThinkingTurns int64

Number of thinking turns that were cleared.

minimum0

Type ClearThinking20251015

The type of context management edit applied.

Accepts one of the following:

const ClearThinking20251015ClearThinking20251015 ClearThinking20251015 = "clear\_thinking\_20251015"

Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

const ModelClaudeOpus4\_5\_20251101 Model = "claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

const ModelClaudeOpus4\_5 Model = "claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

const ModelClaude3\_7SonnetLatest Model = "claude-3-7-sonnet-latest"

High-performance model with early extended thinking

const ModelClaude3\_7Sonnet20250219 Model = "claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

const ModelClaude3\_5HaikuLatest Model = "claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

const ModelClaude3\_5Haiku20241022 Model = "claude-3-5-haiku-20241022"

Our fastest model

const ModelClaudeHaiku4\_5 Model = "claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

const ModelClaudeHaiku4\_5\_20251001 Model = "claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaude4Sonnet20250514 Model = "claude-4-sonnet-20250514"

High-performance model with extended thinking

const ModelClaudeSonnet4\_5 Model = "claude-sonnet-4-5"

Our best model for real-world agents and coding

const ModelClaudeSonnet4\_5\_20250929 Model = "claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Our most capable model

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Our most capable model

const ModelClaude4Opus20250514 Model = "claude-4-opus-20250514"

Our most capable model

const ModelClaudeOpus4\_1\_20250805 Model = "claude-opus-4-1-20250805"

Our most capable model

const ModelClaude3OpusLatest Model = "claude-3-opus-latest"

Excels at writing and complex tasks

const ModelClaude\_3\_Opus\_20240229 Model = "claude-3-opus-20240229"

Excels at writing and complex tasks

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Our previous most fast and cost-effective

string

Role Assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

const AssistantAssistant Assistant = "assistant"

StopReason [BetaStopReason](api/beta.md)

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

const BetaStopReasonEndTurn [BetaStopReason](api/beta.md) = "end\_turn"

const BetaStopReasonMaxTokens [BetaStopReason](api/beta.md) = "max\_tokens"

const BetaStopReasonStopSequence [BetaStopReason](api/beta.md) = "stop\_sequence"

const BetaStopReasonToolUse [BetaStopReason](api/beta.md) = "tool\_use"

const BetaStopReasonPauseTurn [BetaStopReason](api/beta.md) = "pause\_turn"

const BetaStopReasonRefusal [BetaStopReason](api/beta.md) = "refusal"

const BetaStopReasonModelContextWindowExceeded [BetaStopReason](api/beta.md) = "model\_context\_window\_exceeded"

StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

Type Message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

const MessageMessage Message = "message"

Usage [BetaUsage](api/beta.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreation [BetaCacheCreation](api/beta.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

minimum0

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

minimum0

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

minimum0

CacheReadInputTokens int64

The number of input tokens read from the cache.

minimum0

InputTokens int64

The number of input tokens which were used.

minimum0

OutputTokens int64

The number of output tokens which were used.

minimum0

ServerToolUse [BetaServerToolUsage](api/beta.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

minimum0

WebSearchRequests int64

The number of web search tool requests.

minimum0

ServiceTier BetaUsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const BetaUsageServiceTierStandard BetaUsageServiceTier = "standard"

const BetaUsageServiceTierPriority BetaUsageServiceTier = "priority"

const BetaUsageServiceTierBatch BetaUsageServiceTier = "batch"

Type Succeeded

Accepts one of the following:

const SucceededSucceeded Succeeded = "succeeded"

type BetaMessageBatchErroredResult struct{…}

Error [BetaErrorResponse](api/beta.md)

Error [BetaErrorUnion](api/beta.md)

Accepts one of the following:

type BetaInvalidRequestError struct{…}

Message string

Type InvalidRequestError

Accepts one of the following:

const InvalidRequestErrorInvalidRequestError InvalidRequestError = "invalid\_request\_error"

type BetaAuthenticationError struct{…}

Message string

Type AuthenticationError

Accepts one of the following:

const AuthenticationErrorAuthenticationError AuthenticationError = "authentication\_error"

type BetaBillingError struct{…}

Message string

Type BillingError

Accepts one of the following:

const BillingErrorBillingError BillingError = "billing\_error"

type BetaPermissionError struct{…}

Message string

Type PermissionError

Accepts one of the following:

const PermissionErrorPermissionError PermissionError = "permission\_error"

type BetaNotFoundError struct{…}

Message string

Type NotFoundError

Accepts one of the following:

const NotFoundErrorNotFoundError NotFoundError = "not\_found\_error"

type BetaRateLimitError struct{…}

Message string

Type RateLimitError

Accepts one of the following:

const RateLimitErrorRateLimitError RateLimitError = "rate\_limit\_error"

type BetaGatewayTimeoutError struct{…}

Message string

Type TimeoutError

Accepts one of the following:

const TimeoutErrorTimeoutError TimeoutError = "timeout\_error"

type BetaAPIError struct{…}

Message string

Type APIError

Accepts one of the following:

const APIErrorAPIError APIError = "api\_error"

type BetaOverloadedError struct{…}

Message string

Type OverloadedError

Accepts one of the following:

const OverloadedErrorOverloadedError OverloadedError = "overloaded\_error"

RequestID string

Type Error

Accepts one of the following:

const ErrorError Error = "error"

Type Errored

Accepts one of the following:

const ErroredErrored Errored = "errored"

type BetaMessageBatchCanceledResult struct{…}

Type Canceled

Accepts one of the following:

const CanceledCanceled Canceled = "canceled"

type BetaMessageBatchExpiredResult struct{…}

Type Expired

Accepts one of the following:

const ExpiredExpired Expired = "expired"

type BetaMessageBatchRequestCounts struct{…}

Canceled int64

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

Errored int64

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

Expired int64

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

Processing int64

Number of requests in the Message Batch that are processing.

Succeeded int64

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

type BetaMessageBatchResultUnion interface{…}

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

type BetaMessageBatchSucceededResult struct{…}

Message [BetaMessage](api/beta.md)

ID string

Unique object identifier.

The format and length of IDs may change over time.

Container [BetaContainer](api/beta.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

formatdate-time

Skills [][BetaSkill](api/beta.md)

Skills loaded in the container

SkillID string

Skill ID

maxLength64

minLength1

Type BetaSkillType

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

const BetaSkillTypeAnthropic BetaSkillType = "anthropic"

const BetaSkillTypeCustom BetaSkillType = "custom"

Version string

Skill version or 'latest' for most recent version

maxLength64

minLength1

Content [][BetaContentBlockUnion](api/beta.md)

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

type BetaTextBlock struct{…}

Citations [][BetaTextCitationUnion](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char\_location"

type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page\_location"

type BetaCitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content\_block\_location"

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web\_search\_result\_location"

URL string

type BetaCitationSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search\_result\_location"

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

type BetaThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type BetaRedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted\_thinking"

type BetaToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool\_use"

Caller BetaToolUseBlockCallerUnionoptional

Tool invocation directly from the model.

Accepts one of the following:

type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

Accepts one of the following:

const DirectDirect Direct = "direct"

type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

Accepts one of the following:

const CodeExecution20250825CodeExecution20250825 CodeExecution20250825 = "code\_execution\_20250825"

type BetaServerToolUseBlock struct{…}

ID string

Caller BetaServerToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

Accepts one of the following:

const DirectDirect Direct = "direct"

type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

Accepts one of the following:

const CodeExecution20250825CodeExecution20250825 CodeExecution20250825 = "code\_execution\_20250825"

Input map[string, any]

Name BetaServerToolUseBlockName

Accepts one of the following:

const BetaServerToolUseBlockNameWebSearch BetaServerToolUseBlockName = "web\_search"

const BetaServerToolUseBlockNameWebFetch BetaServerToolUseBlockName = "web\_fetch"

const BetaServerToolUseBlockNameCodeExecution BetaServerToolUseBlockName = "code\_execution"

const BetaServerToolUseBlockNameBashCodeExecution BetaServerToolUseBlockName = "bash\_code\_execution"

const BetaServerToolUseBlockNameTextEditorCodeExecution BetaServerToolUseBlockName = "text\_editor\_code\_execution"

const BetaServerToolUseBlockNameToolSearchToolRegex BetaServerToolUseBlockName = "tool\_search\_tool\_regex"

const BetaServerToolUseBlockNameToolSearchToolBm25 BetaServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server\_tool\_use"

type BetaWebSearchToolResultBlock struct{…}

Content [BetaWebSearchToolResultBlockContentUnion](api/beta.md)

Accepts one of the following:

type BetaWebSearchToolResultError struct{…}

ErrorCode [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta.md) = "query\_too\_long"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web\_search\_tool\_result\_error"

type BetaWebSearchToolResultBlockContentArray [][BetaWebSearchResultBlock](api/beta.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

Accepts one of the following:

const WebSearchResultWebSearchResult WebSearchResult = "web\_search\_result"

URL string

ToolUseID string

Type WebSearchToolResult

Accepts one of the following:

const WebSearchToolResultWebSearchToolResult WebSearchToolResult = "web\_search\_tool\_result"

type BetaWebFetchToolResultBlock struct{…}

Content BetaWebFetchToolResultBlockContentUnion

Accepts one of the following:

type BetaWebFetchToolResultErrorBlock struct{…}

ErrorCode [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta.md) = "unavailable"

Type WebFetchToolResultError

Accepts one of the following:

const WebFetchToolResultErrorWebFetchToolResultError WebFetchToolResultError = "web\_fetch\_tool\_result\_error"

type BetaWebFetchBlock struct{…}

Content [BetaDocumentBlock](api/beta.md)

Citations [BetaCitationConfig](api/beta.md)

Citation configuration for the document

Enabled bool

Source BetaDocumentBlockSourceUnion

Accepts one of the following:

type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Accepts one of the following:

const ApplicationPDFApplicationPDF ApplicationPDF = "application/pdf"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Accepts one of the following:

const TextPlainTextPlain TextPlain = "text/plain"

Type Text

Accepts one of the following:

const TextText Text = "text"

Title string

The title of the document

Type Document

Accepts one of the following:

const DocumentDocument Document = "document"

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

Accepts one of the following:

const WebFetchResultWebFetchResult WebFetchResult = "web\_fetch\_result"

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

Accepts one of the following:

const WebFetchToolResultWebFetchToolResult WebFetchToolResult = "web\_fetch\_tool\_result"

type BetaCodeExecutionToolResultBlock struct{…}

Content [BetaCodeExecutionToolResultBlockContentUnion](api/beta.md)

Accepts one of the following:

type BetaCodeExecutionToolResultError struct{…}

ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError

Accepts one of the following:

const CodeExecutionToolResultErrorCodeExecutionToolResultError CodeExecutionToolResultError = "code\_execution\_tool\_result\_error"

type BetaCodeExecutionResultBlock struct{…}

Content [][BetaCodeExecutionOutputBlock](api/beta.md)

FileID string

Type CodeExecutionOutput

Accepts one of the following:

const CodeExecutionOutputCodeExecutionOutput CodeExecutionOutput = "code\_execution\_output"

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

Accepts one of the following:

const CodeExecutionResultCodeExecutionResult CodeExecutionResult = "code\_execution\_result"

ToolUseID string

Type CodeExecutionToolResult

Accepts one of the following:

const CodeExecutionToolResultCodeExecutionToolResult CodeExecutionToolResult = "code\_execution\_tool\_result"

type BetaBashCodeExecutionToolResultBlock struct{…}

Content BetaBashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BetaBashCodeExecutionToolResultError struct{…}

ErrorCode BetaBashCodeExecutionToolResultErrorErrorCode

Accepts one of the following:

const BetaBashCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaBashCodeExecutionToolResultErrorErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaBashCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaBashCodeExecutionToolResultErrorErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorErrorCode = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError

Accepts one of the following:

const BashCodeExecutionToolResultErrorBashCodeExecutionToolResultError BashCodeExecutionToolResultError = "bash\_code\_execution\_tool\_result\_error"

type BetaBashCodeExecutionResultBlock struct{…}

Content [][BetaBashCodeExecutionOutputBlock](api/beta.md)

FileID string

Type BashCodeExecutionOutput

Accepts one of the following:

const BashCodeExecutionOutputBashCodeExecutionOutput BashCodeExecutionOutput = "bash\_code\_execution\_output"

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

Accepts one of the following:

const BashCodeExecutionResultBashCodeExecutionResult BashCodeExecutionResult = "bash\_code\_execution\_result"

ToolUseID string

Type BashCodeExecutionToolResult

Accepts one of the following:

const BashCodeExecutionToolResultBashCodeExecutionToolResult BashCodeExecutionToolResult = "bash\_code\_execution\_tool\_result"

type BetaTextEditorCodeExecutionToolResultBlock struct{…}

Content BetaTextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BetaTextEditorCodeExecutionToolResultError struct{…}

ErrorCode BetaTextEditorCodeExecutionToolResultErrorErrorCode

Accepts one of the following:

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorErrorCode = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorTextEditorCodeExecutionToolResultError TextEditorCodeExecutionToolResultError = "text\_editor\_code\_execution\_tool\_result\_error"

type BetaTextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType BetaTextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const BetaTextEditorCodeExecutionViewResultBlockFileTypeText BetaTextEditorCodeExecutionViewResultBlockFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockFileTypeImage BetaTextEditorCodeExecutionViewResultBlockFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockFileTypePDF BetaTextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

Accepts one of the following:

const TextEditorCodeExecutionViewResultTextEditorCodeExecutionViewResult TextEditorCodeExecutionViewResult = "text\_editor\_code\_execution\_view\_result"

type BetaTextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

Accepts one of the following:

const TextEditorCodeExecutionCreateResultTextEditorCodeExecutionCreateResult TextEditorCodeExecutionCreateResult = "text\_editor\_code\_execution\_create\_result"

type BetaTextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

Accepts one of the following:

const TextEditorCodeExecutionStrReplaceResultTextEditorCodeExecutionStrReplaceResult TextEditorCodeExecutionStrReplaceResult = "text\_editor\_code\_execution\_str\_replace\_result"

ToolUseID string

Type TextEditorCodeExecutionToolResult

Accepts one of the following:

const TextEditorCodeExecutionToolResultTextEditorCodeExecutionToolResult TextEditorCodeExecutionToolResult = "text\_editor\_code\_execution\_tool\_result"

type BetaToolSearchToolResultBlock struct{…}

Content BetaToolSearchToolResultBlockContentUnion

Accepts one of the following:

type BetaToolSearchToolResultError struct{…}

ErrorCode BetaToolSearchToolResultErrorErrorCode

Accepts one of the following:

const BetaToolSearchToolResultErrorErrorCodeInvalidToolInput BetaToolSearchToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaToolSearchToolResultErrorErrorCodeUnavailable BetaToolSearchToolResultErrorErrorCode = "unavailable"

const BetaToolSearchToolResultErrorErrorCodeTooManyRequests BetaToolSearchToolResultErrorErrorCode = "too\_many\_requests"

const BetaToolSearchToolResultErrorErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorErrorCode = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

Accepts one of the following:

const ToolSearchToolResultErrorToolSearchToolResultError ToolSearchToolResultError = "tool\_search\_tool\_result\_error"

type BetaToolSearchToolSearchResultBlock struct{…}

ToolReferences [][BetaToolReferenceBlock](api/beta.md)

ToolName string

Type ToolReference

Accepts one of the following:

const ToolReferenceToolReference ToolReference = "tool\_reference"

Type ToolSearchToolSearchResult

Accepts one of the following:

const ToolSearchToolSearchResultToolSearchToolSearchResult ToolSearchToolSearchResult = "tool\_search\_tool\_search\_result"

ToolUseID string

Type ToolSearchToolResult

Accepts one of the following:

const ToolSearchToolResultToolSearchToolResult ToolSearchToolResult = "tool\_search\_tool\_result"

type BetaMCPToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

The name of the MCP tool

ServerName string

The name of the MCP server

Type MCPToolUse

Accepts one of the following:

const MCPToolUseMCPToolUse MCPToolUse = "mcp\_tool\_use"

type BetaMCPToolResultBlock struct{…}

Content BetaMCPToolResultBlockContentUnion

Accepts one of the following:

string

type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent [][BetaTextBlock](api/beta.md)

Citations [][BetaTextCitationUnion](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char\_location"

type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page\_location"

type BetaCitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content\_block\_location"

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web\_search\_result\_location"

URL string

type BetaCitationSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search\_result\_location"

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

IsError bool

ToolUseID string

Type MCPToolResult

Accepts one of the following:

const MCPToolResultMCPToolResult MCPToolResult = "mcp\_tool\_result"

type BetaContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

Accepts one of the following:

const ContainerUploadContainerUpload ContainerUpload = "container\_upload"

ContextManagement [BetaContextManagementResponse](api/beta.md)

Context management response.

Information about context management strategies applied during the request.

AppliedEdits []BetaContextManagementResponseAppliedEditUnion

List of context management edits that were applied.

Accepts one of the following:

type BetaClearToolUses20250919EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

minimum0

ClearedToolUses int64

Number of tool uses that were cleared.

minimum0

Type ClearToolUses20250919

The type of context management edit applied.

Accepts one of the following:

const ClearToolUses20250919ClearToolUses20250919 ClearToolUses20250919 = "clear\_tool\_uses\_20250919"

type BetaClearThinking20251015EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

minimum0

ClearedThinkingTurns int64

Number of thinking turns that were cleared.

minimum0

Type ClearThinking20251015

The type of context management edit applied.

Accepts one of the following:

const ClearThinking20251015ClearThinking20251015 ClearThinking20251015 = "clear\_thinking\_20251015"

Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

const ModelClaudeOpus4\_5\_20251101 Model = "claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

const ModelClaudeOpus4\_5 Model = "claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

const ModelClaude3\_7SonnetLatest Model = "claude-3-7-sonnet-latest"

High-performance model with early extended thinking

const ModelClaude3\_7Sonnet20250219 Model = "claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

const ModelClaude3\_5HaikuLatest Model = "claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

const ModelClaude3\_5Haiku20241022 Model = "claude-3-5-haiku-20241022"

Our fastest model

const ModelClaudeHaiku4\_5 Model = "claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

const ModelClaudeHaiku4\_5\_20251001 Model = "claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaude4Sonnet20250514 Model = "claude-4-sonnet-20250514"

High-performance model with extended thinking

const ModelClaudeSonnet4\_5 Model = "claude-sonnet-4-5"

Our best model for real-world agents and coding

const ModelClaudeSonnet4\_5\_20250929 Model = "claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Our most capable model

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Our most capable model

const ModelClaude4Opus20250514 Model = "claude-4-opus-20250514"

Our most capable model

const ModelClaudeOpus4\_1\_20250805 Model = "claude-opus-4-1-20250805"

Our most capable model

const ModelClaude3OpusLatest Model = "claude-3-opus-latest"

Excels at writing and complex tasks

const ModelClaude\_3\_Opus\_20240229 Model = "claude-3-opus-20240229"

Excels at writing and complex tasks

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Our previous most fast and cost-effective

string

Role Assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

const AssistantAssistant Assistant = "assistant"

StopReason [BetaStopReason](api/beta.md)

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

const BetaStopReasonEndTurn [BetaStopReason](api/beta.md) = "end\_turn"

const BetaStopReasonMaxTokens [BetaStopReason](api/beta.md) = "max\_tokens"

const BetaStopReasonStopSequence [BetaStopReason](api/beta.md) = "stop\_sequence"

const BetaStopReasonToolUse [BetaStopReason](api/beta.md) = "tool\_use"

const BetaStopReasonPauseTurn [BetaStopReason](api/beta.md) = "pause\_turn"

const BetaStopReasonRefusal [BetaStopReason](api/beta.md) = "refusal"

const BetaStopReasonModelContextWindowExceeded [BetaStopReason](api/beta.md) = "model\_context\_window\_exceeded"

StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

Type Message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

const MessageMessage Message = "message"

Usage [BetaUsage](api/beta.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreation [BetaCacheCreation](api/beta.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

minimum0

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

minimum0

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

minimum0

CacheReadInputTokens int64

The number of input tokens read from the cache.

minimum0

InputTokens int64

The number of input tokens which were used.

minimum0

OutputTokens int64

The number of output tokens which were used.

minimum0

ServerToolUse [BetaServerToolUsage](api/beta.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

minimum0

WebSearchRequests int64

The number of web search tool requests.

minimum0

ServiceTier BetaUsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const BetaUsageServiceTierStandard BetaUsageServiceTier = "standard"

const BetaUsageServiceTierPriority BetaUsageServiceTier = "priority"

const BetaUsageServiceTierBatch BetaUsageServiceTier = "batch"

Type Succeeded

Accepts one of the following:

const SucceededSucceeded Succeeded = "succeeded"

type BetaMessageBatchErroredResult struct{…}

Error [BetaErrorResponse](api/beta.md)

Error [BetaErrorUnion](api/beta.md)

Accepts one of the following:

type BetaInvalidRequestError struct{…}

Message string

Type InvalidRequestError

Accepts one of the following:

const InvalidRequestErrorInvalidRequestError InvalidRequestError = "invalid\_request\_error"

type BetaAuthenticationError struct{…}

Message string

Type AuthenticationError

Accepts one of the following:

const AuthenticationErrorAuthenticationError AuthenticationError = "authentication\_error"

type BetaBillingError struct{…}

Message string

Type BillingError

Accepts one of the following:

const BillingErrorBillingError BillingError = "billing\_error"

type BetaPermissionError struct{…}

Message string

Type PermissionError

Accepts one of the following:

const PermissionErrorPermissionError PermissionError = "permission\_error"

type BetaNotFoundError struct{…}

Message string

Type NotFoundError

Accepts one of the following:

const NotFoundErrorNotFoundError NotFoundError = "not\_found\_error"

type BetaRateLimitError struct{…}

Message string

Type RateLimitError

Accepts one of the following:

const RateLimitErrorRateLimitError RateLimitError = "rate\_limit\_error"

type BetaGatewayTimeoutError struct{…}

Message string

Type TimeoutError

Accepts one of the following:

const TimeoutErrorTimeoutError TimeoutError = "timeout\_error"

type BetaAPIError struct{…}

Message string

Type APIError

Accepts one of the following:

const APIErrorAPIError APIError = "api\_error"

type BetaOverloadedError struct{…}

Message string

Type OverloadedError

Accepts one of the following:

const OverloadedErrorOverloadedError OverloadedError = "overloaded\_error"

RequestID string

Type Error

Accepts one of the following:

const ErrorError Error = "error"

Type Errored

Accepts one of the following:

const ErroredErrored Errored = "errored"

type BetaMessageBatchCanceledResult struct{…}

Type Canceled

Accepts one of the following:

const CanceledCanceled Canceled = "canceled"

type BetaMessageBatchExpiredResult struct{…}

Type Expired

Accepts one of the following:

const ExpiredExpired Expired = "expired"

type BetaMessageBatchSucceededResult struct{…}

Message [BetaMessage](api/beta.md)

ID string

Unique object identifier.

The format and length of IDs may change over time.

Container [BetaContainer](api/beta.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

formatdate-time

Skills [][BetaSkill](api/beta.md)

Skills loaded in the container

SkillID string

Skill ID

maxLength64

minLength1

Type BetaSkillType

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

const BetaSkillTypeAnthropic BetaSkillType = "anthropic"

const BetaSkillTypeCustom BetaSkillType = "custom"

Version string

Skill version or 'latest' for most recent version

maxLength64

minLength1

Content [][BetaContentBlockUnion](api/beta.md)

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

type BetaTextBlock struct{…}

Citations [][BetaTextCitationUnion](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char\_location"

type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page\_location"

type BetaCitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content\_block\_location"

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web\_search\_result\_location"

URL string

type BetaCitationSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search\_result\_location"

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

type BetaThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type BetaRedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted\_thinking"

type BetaToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool\_use"

Caller BetaToolUseBlockCallerUnionoptional

Tool invocation directly from the model.

Accepts one of the following:

type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

Accepts one of the following:

const DirectDirect Direct = "direct"

type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

Accepts one of the following:

const CodeExecution20250825CodeExecution20250825 CodeExecution20250825 = "code\_execution\_20250825"

type BetaServerToolUseBlock struct{…}

ID string

Caller BetaServerToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

Accepts one of the following:

const DirectDirect Direct = "direct"

type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

Accepts one of the following:

const CodeExecution20250825CodeExecution20250825 CodeExecution20250825 = "code\_execution\_20250825"

Input map[string, any]

Name BetaServerToolUseBlockName

Accepts one of the following:

const BetaServerToolUseBlockNameWebSearch BetaServerToolUseBlockName = "web\_search"

const BetaServerToolUseBlockNameWebFetch BetaServerToolUseBlockName = "web\_fetch"

const BetaServerToolUseBlockNameCodeExecution BetaServerToolUseBlockName = "code\_execution"

const BetaServerToolUseBlockNameBashCodeExecution BetaServerToolUseBlockName = "bash\_code\_execution"

const BetaServerToolUseBlockNameTextEditorCodeExecution BetaServerToolUseBlockName = "text\_editor\_code\_execution"

const BetaServerToolUseBlockNameToolSearchToolRegex BetaServerToolUseBlockName = "tool\_search\_tool\_regex"

const BetaServerToolUseBlockNameToolSearchToolBm25 BetaServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server\_tool\_use"

type BetaWebSearchToolResultBlock struct{…}

Content [BetaWebSearchToolResultBlockContentUnion](api/beta.md)

Accepts one of the following:

type BetaWebSearchToolResultError struct{…}

ErrorCode [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta.md) = "query\_too\_long"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web\_search\_tool\_result\_error"

type BetaWebSearchToolResultBlockContentArray [][BetaWebSearchResultBlock](api/beta.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

Accepts one of the following:

const WebSearchResultWebSearchResult WebSearchResult = "web\_search\_result"

URL string

ToolUseID string

Type WebSearchToolResult

Accepts one of the following:

const WebSearchToolResultWebSearchToolResult WebSearchToolResult = "web\_search\_tool\_result"

type BetaWebFetchToolResultBlock struct{…}

Content BetaWebFetchToolResultBlockContentUnion

Accepts one of the following:

type BetaWebFetchToolResultErrorBlock struct{…}

ErrorCode [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta.md) = "unavailable"

Type WebFetchToolResultError

Accepts one of the following:

const WebFetchToolResultErrorWebFetchToolResultError WebFetchToolResultError = "web\_fetch\_tool\_result\_error"

type BetaWebFetchBlock struct{…}

Content [BetaDocumentBlock](api/beta.md)

Citations [BetaCitationConfig](api/beta.md)

Citation configuration for the document

Enabled bool

Source BetaDocumentBlockSourceUnion

Accepts one of the following:

type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Accepts one of the following:

const ApplicationPDFApplicationPDF ApplicationPDF = "application/pdf"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Accepts one of the following:

const TextPlainTextPlain TextPlain = "text/plain"

Type Text

Accepts one of the following:

const TextText Text = "text"

Title string

The title of the document

Type Document

Accepts one of the following:

const DocumentDocument Document = "document"

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

Accepts one of the following:

const WebFetchResultWebFetchResult WebFetchResult = "web\_fetch\_result"

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

Accepts one of the following:

const WebFetchToolResultWebFetchToolResult WebFetchToolResult = "web\_fetch\_tool\_result"

type BetaCodeExecutionToolResultBlock struct{…}

Content [BetaCodeExecutionToolResultBlockContentUnion](api/beta.md)

Accepts one of the following:

type BetaCodeExecutionToolResultError struct{…}

ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError

Accepts one of the following:

const CodeExecutionToolResultErrorCodeExecutionToolResultError CodeExecutionToolResultError = "code\_execution\_tool\_result\_error"

type BetaCodeExecutionResultBlock struct{…}

Content [][BetaCodeExecutionOutputBlock](api/beta.md)

FileID string

Type CodeExecutionOutput

Accepts one of the following:

const CodeExecutionOutputCodeExecutionOutput CodeExecutionOutput = "code\_execution\_output"

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

Accepts one of the following:

const CodeExecutionResultCodeExecutionResult CodeExecutionResult = "code\_execution\_result"

ToolUseID string

Type CodeExecutionToolResult

Accepts one of the following:

const CodeExecutionToolResultCodeExecutionToolResult CodeExecutionToolResult = "code\_execution\_tool\_result"

type BetaBashCodeExecutionToolResultBlock struct{…}

Content BetaBashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BetaBashCodeExecutionToolResultError struct{…}

ErrorCode BetaBashCodeExecutionToolResultErrorErrorCode

Accepts one of the following:

const BetaBashCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaBashCodeExecutionToolResultErrorErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaBashCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaBashCodeExecutionToolResultErrorErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorErrorCode = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError

Accepts one of the following:

const BashCodeExecutionToolResultErrorBashCodeExecutionToolResultError BashCodeExecutionToolResultError = "bash\_code\_execution\_tool\_result\_error"

type BetaBashCodeExecutionResultBlock struct{…}

Content [][BetaBashCodeExecutionOutputBlock](api/beta.md)

FileID string

Type BashCodeExecutionOutput

Accepts one of the following:

const BashCodeExecutionOutputBashCodeExecutionOutput BashCodeExecutionOutput = "bash\_code\_execution\_output"

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

Accepts one of the following:

const BashCodeExecutionResultBashCodeExecutionResult BashCodeExecutionResult = "bash\_code\_execution\_result"

ToolUseID string

Type BashCodeExecutionToolResult

Accepts one of the following:

const BashCodeExecutionToolResultBashCodeExecutionToolResult BashCodeExecutionToolResult = "bash\_code\_execution\_tool\_result"

type BetaTextEditorCodeExecutionToolResultBlock struct{…}

Content BetaTextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BetaTextEditorCodeExecutionToolResultError struct{…}

ErrorCode BetaTextEditorCodeExecutionToolResultErrorErrorCode

Accepts one of the following:

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorErrorCode = "too\_many\_requests"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorErrorCode = "execution\_time\_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorErrorCode = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorTextEditorCodeExecutionToolResultError TextEditorCodeExecutionToolResultError = "text\_editor\_code\_execution\_tool\_result\_error"

type BetaTextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType BetaTextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const BetaTextEditorCodeExecutionViewResultBlockFileTypeText BetaTextEditorCodeExecutionViewResultBlockFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockFileTypeImage BetaTextEditorCodeExecutionViewResultBlockFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockFileTypePDF BetaTextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

Accepts one of the following:

const TextEditorCodeExecutionViewResultTextEditorCodeExecutionViewResult TextEditorCodeExecutionViewResult = "text\_editor\_code\_execution\_view\_result"

type BetaTextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

Accepts one of the following:

const TextEditorCodeExecutionCreateResultTextEditorCodeExecutionCreateResult TextEditorCodeExecutionCreateResult = "text\_editor\_code\_execution\_create\_result"

type BetaTextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

Accepts one of the following:

const TextEditorCodeExecutionStrReplaceResultTextEditorCodeExecutionStrReplaceResult TextEditorCodeExecutionStrReplaceResult = "text\_editor\_code\_execution\_str\_replace\_result"

ToolUseID string

Type TextEditorCodeExecutionToolResult

Accepts one of the following:

const TextEditorCodeExecutionToolResultTextEditorCodeExecutionToolResult TextEditorCodeExecutionToolResult = "text\_editor\_code\_execution\_tool\_result"

type BetaToolSearchToolResultBlock struct{…}

Content BetaToolSearchToolResultBlockContentUnion

Accepts one of the following:

type BetaToolSearchToolResultError struct{…}

ErrorCode BetaToolSearchToolResultErrorErrorCode

Accepts one of the following:

const BetaToolSearchToolResultErrorErrorCodeInvalidToolInput BetaToolSearchToolResultErrorErrorCode = "invalid\_tool\_input"

const BetaToolSearchToolResultErrorErrorCodeUnavailable BetaToolSearchToolResultErrorErrorCode = "unavailable"

const BetaToolSearchToolResultErrorErrorCodeTooManyRequests BetaToolSearchToolResultErrorErrorCode = "too\_many\_requests"

const BetaToolSearchToolResultErrorErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorErrorCode = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

Accepts one of the following:

const ToolSearchToolResultErrorToolSearchToolResultError ToolSearchToolResultError = "tool\_search\_tool\_result\_error"

type BetaToolSearchToolSearchResultBlock struct{…}

ToolReferences [][BetaToolReferenceBlock](api/beta.md)

ToolName string

Type ToolReference

Accepts one of the following:

const ToolReferenceToolReference ToolReference = "tool\_reference"

Type ToolSearchToolSearchResult

Accepts one of the following:

const ToolSearchToolSearchResultToolSearchToolSearchResult ToolSearchToolSearchResult = "tool\_search\_tool\_search\_result"

ToolUseID string

Type ToolSearchToolResult

Accepts one of the following:

const ToolSearchToolResultToolSearchToolResult ToolSearchToolResult = "tool\_search\_tool\_result"

type BetaMCPToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

The name of the MCP tool

ServerName string

The name of the MCP server

Type MCPToolUse

Accepts one of the following:

const MCPToolUseMCPToolUse MCPToolUse = "mcp\_tool\_use"

type BetaMCPToolResultBlock struct{…}

Content BetaMCPToolResultBlockContentUnion

Accepts one of the following:

string

type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent [][BetaTextBlock](api/beta.md)

Citations [][BetaTextCitationUnion](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char\_location"

type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page\_location"

type BetaCitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content\_block\_location"

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web\_search\_result\_location"

URL string

type BetaCitationSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search\_result\_location"

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

IsError bool

ToolUseID string

Type MCPToolResult

Accepts one of the following:

const MCPToolResultMCPToolResult MCPToolResult = "mcp\_tool\_result"

type BetaContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

Accepts one of the following:

const ContainerUploadContainerUpload ContainerUpload = "container\_upload"

ContextManagement [BetaContextManagementResponse](api/beta.md)

Context management response.

Information about context management strategies applied during the request.

AppliedEdits []BetaContextManagementResponseAppliedEditUnion

List of context management edits that were applied.

Accepts one of the following:

type BetaClearToolUses20250919EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

minimum0

ClearedToolUses int64

Number of tool uses that were cleared.

minimum0

Type ClearToolUses20250919

The type of context management edit applied.

Accepts one of the following:

const ClearToolUses20250919ClearToolUses20250919 ClearToolUses20250919 = "clear\_tool\_uses\_20250919"

type BetaClearThinking20251015EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

minimum0

ClearedThinkingTurns int64

Number of thinking turns that were cleared.

minimum0

Type ClearThinking20251015

The type of context management edit applied.

Accepts one of the following:

const ClearThinking20251015ClearThinking20251015 ClearThinking20251015 = "clear\_thinking\_20251015"

Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

const ModelClaudeOpus4\_5\_20251101 Model = "claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

const ModelClaudeOpus4\_5 Model = "claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

const ModelClaude3\_7SonnetLatest Model = "claude-3-7-sonnet-latest"

High-performance model with early extended thinking

const ModelClaude3\_7Sonnet20250219 Model = "claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

const ModelClaude3\_5HaikuLatest Model = "claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

const ModelClaude3\_5Haiku20241022 Model = "claude-3-5-haiku-20241022"

Our fastest model

const ModelClaudeHaiku4\_5 Model = "claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

const ModelClaudeHaiku4\_5\_20251001 Model = "claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaude4Sonnet20250514 Model = "claude-4-sonnet-20250514"

High-performance model with extended thinking

const ModelClaudeSonnet4\_5 Model = "claude-sonnet-4-5"

Our best model for real-world agents and coding

const ModelClaudeSonnet4\_5\_20250929 Model = "claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Our most capable model

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Our most capable model

const ModelClaude4Opus20250514 Model = "claude-4-opus-20250514"

Our most capable model

const ModelClaudeOpus4\_1\_20250805 Model = "claude-opus-4-1-20250805"

Our most capable model

const ModelClaude3OpusLatest Model = "claude-3-opus-latest"

Excels at writing and complex tasks

const ModelClaude\_3\_Opus\_20240229 Model = "claude-3-opus-20240229"

Excels at writing and complex tasks

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Our previous most fast and cost-effective

string

Role Assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

const AssistantAssistant Assistant = "assistant"

StopReason [BetaStopReason](api/beta.md)

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

const BetaStopReasonEndTurn [BetaStopReason](api/beta.md) = "end\_turn"

const BetaStopReasonMaxTokens [BetaStopReason](api/beta.md) = "max\_tokens"

const BetaStopReasonStopSequence [BetaStopReason](api/beta.md) = "stop\_sequence"

const BetaStopReasonToolUse [BetaStopReason](api/beta.md) = "tool\_use"

const BetaStopReasonPauseTurn [BetaStopReason](api/beta.md) = "pause\_turn"

const BetaStopReasonRefusal [BetaStopReason](api/beta.md) = "refusal"

const BetaStopReasonModelContextWindowExceeded [BetaStopReason](api/beta.md) = "model\_context\_window\_exceeded"

StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

Type Message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

const MessageMessage Message = "message"

Usage [BetaUsage](api/beta.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreation [BetaCacheCreation](api/beta.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

minimum0

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

minimum0

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

minimum0

CacheReadInputTokens int64

The number of input tokens read from the cache.

minimum0

InputTokens int64

The number of input tokens which were used.

minimum0

OutputTokens int64

The number of output tokens which were used.

minimum0

ServerToolUse [BetaServerToolUsage](api/beta.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

minimum0

WebSearchRequests int64

The number of web search tool requests.

minimum0

ServiceTier BetaUsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const BetaUsageServiceTierStandard BetaUsageServiceTier = "standard"

const BetaUsageServiceTierPriority BetaUsageServiceTier = "priority"

const BetaUsageServiceTierBatch BetaUsageServiceTier = "batch"

Type Succeeded

Accepts one of the following:

const SucceededSucceeded Succeeded = "succeeded"

---

*Copyright © Anthropic. All rights reserved.*
