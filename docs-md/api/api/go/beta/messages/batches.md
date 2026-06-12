# Batches

Copy page

SDK language

Go

# Batches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

client.Beta.Messages.Batches.New(ctx, params) (\*[BetaMessageBatch](api/beta.md), error)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

client.Beta.Messages.Batches.Get(ctx, messageBatchID, query) (\*[BetaMessageBatch](api/beta.md), error)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

client.Beta.Messages.Batches.List(ctx, params) (\*Page[[BetaMessageBatch](api/beta.md)], error)

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

client.Beta.Messages.Batches.Cancel(ctx, messageBatchID, body) (\*[BetaMessageBatch](api/beta.md), error)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

client.Beta.Messages.Batches.Delete(ctx, messageBatchID, body) (\*[BetaDeletedMessageBatch](api/beta.md), error)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

client.Beta.Messages.Batches.Results(ctx, messageBatchID, query) (\*[BetaMessageBatchIndividualResponse](api/beta.md), error)

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse



type BetaDeletedMessageBatch struct{…}

ID string

ID of the Message Batch.



Type MessageBatchDeleted

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.



type BetaMessageBatch struct{…}



ID string

Unique object identifier.

The format and length of IDs may change over time.

ArchivedAt Time

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

CancelInitiatedAt Time

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

CreatedAt Time

RFC 3339 datetime string representing the time at which the Message Batch was created.



EndedAt Time

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

ExpiresAt Time

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.



ProcessingStatus BetaMessageBatchProcessingStatus

Processing status of the Message Batch.

One of the following:

const BetaMessageBatchProcessingStatusInProgress BetaMessageBatchProcessingStatus = "in\_progress"

const BetaMessageBatchProcessingStatusCanceling BetaMessageBatchProcessingStatus = "canceling"

const BetaMessageBatchProcessingStatusEnded BetaMessageBatchProcessingStatus = "ended"



RequestCounts [BetaMessageBatchRequestCounts](api/beta.md)

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.



Canceled int64

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



Errored int64

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



Expired int64

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

Processing int64

Number of requests in the Message Batch that are processing.



Succeeded int64

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



ResultsURL string

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.



Type MessageBatch

Object type.

For Message Batches, this is always `"message_batch"`.



type BetaMessageBatchCanceledResult struct{…}

Type Canceled



type BetaMessageBatchErroredResult struct{…}



Error [BetaErrorResponse](api/beta.md)



Error [BetaErrorUnion](api/beta.md)

One of the following:



type BetaInvalidRequestError struct{…}

Message string

Type InvalidRequestError



type BetaAuthenticationError struct{…}

Message string

Type AuthenticationError



type BetaBillingError struct{…}

Message string

Type BillingError



type BetaPermissionError struct{…}

Message string

Type PermissionError



type BetaNotFoundError struct{…}

Message string

Type NotFoundError



type BetaRateLimitError struct{…}

Message string

Type RateLimitError



type BetaGatewayTimeoutError struct{…}

Message string

Type TimeoutError



type BetaAPIError struct{…}

Message string

Type APIError



type BetaOverloadedError struct{…}

Message string

Type OverloadedError

RequestID string

Type Error

Type Errored



type BetaMessageBatchExpiredResult struct{…}

Type Expired



type BetaMessageBatchIndividualResponse struct{…}

This is a single line in the response `.jsonl` file and does not represent the response as a whole.



CustomID string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.



Result [BetaMessageBatchResultUnion](api/beta.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



type BetaMessageBatchSucceededResult struct{…}



Message [BetaMessage](api/beta.md)



ID string

Unique object identifier.

The format and length of IDs may change over time.



Container [BetaContainer](api/beta.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



Skills [][BetaSkill](api/beta.md)

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

Content [][BetaContentBlockUnion](api/beta.md)

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

Citations [][BetaTextCitationUnion](api/beta.md)

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

Content [BetaWebSearchToolResultBlockContentUnion](api/beta.md)

One of the following:



type BetaWebSearchToolResultError struct{…}



ErrorCode [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta.md) = "request\_too\_large"

Type WebSearchToolResultError



type BetaWebSearchToolResultBlockContentArray [][BetaWebSearchResultBlock](api/beta.md)

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

ErrorCode [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotInPriorContext [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_in\_prior\_context"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta.md) = "unavailable"

Type WebFetchToolResultError



type BetaWebFetchBlock struct{…}



Content [BetaDocumentBlock](api/beta.md)



Citations [BetaCitationConfig](api/beta.md)

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

Content [BetaCodeExecutionToolResultBlockContentUnion](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type BetaCodeExecutionToolResultError struct{…}



ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type BetaCodeExecutionResultBlock struct{…}



Content [][BetaCodeExecutionOutputBlock](api/beta.md)

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

Content [][BetaCodeExecutionOutputBlock](api/beta.md)

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

Content [][BetaBashCodeExecutionOutputBlock](api/beta.md)

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

ToolReferences [][BetaToolReferenceBlock](api/beta.md)

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

type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent [][BetaTextBlock](api/beta.md)



Citations [][BetaTextCitationUnion](api/beta.md)

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
declined. A turn routed directly by the sticky decision has no such boundary
and carries no block — the signal for whether a fallback model served the
response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



From [BetaFallbackInfo](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

string



To [BetaFallbackInfo](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

string

Type Fallback



ContextManagement [BetaContextManagementResponse](api/beta.md)

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

Diagnostics [BetaDiagnostics](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

string



Role Assistant

Conversational role of the generated message.

This will always be `"assistant"`.



StopDetails [BetaRefusalStopDetails](api/beta.md)

Structured information about a refusal.



Category BetaRefusalStopDetailsCategory

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

const BetaRefusalStopDetailsCategoryCyber BetaRefusalStopDetailsCategory = "cyber"

const BetaRefusalStopDetailsCategoryBio BetaRefusalStopDetailsCategory = "bio"

const BetaRefusalStopDetailsCategoryReasoningExtraction BetaRefusalStopDetailsCategory = "reasoning\_extraction"

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

StopReason [BetaStopReason](api/beta.md)

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

const BetaStopReasonEndTurn [BetaStopReason](api/beta.md) = "end\_turn"

const BetaStopReasonMaxTokens [BetaStopReason](api/beta.md) = "max\_tokens"

const BetaStopReasonStopSequence [BetaStopReason](api/beta.md) = "stop\_sequence"

const BetaStopReasonToolUse [BetaStopReason](api/beta.md) = "tool\_use"

const BetaStopReasonPauseTurn [BetaStopReason](api/beta.md) = "pause\_turn"

const BetaStopReasonCompaction [BetaStopReason](api/beta.md) = "compaction"

const BetaStopReasonRefusal [BetaStopReason](api/beta.md) = "refusal"

const BetaStopReasonModelContextWindowExceeded [BetaStopReason](api/beta.md) = "model\_context\_window\_exceeded"



StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



Type Message

Object type.

For Messages, this is always `"message"`.



Usage [BetaUsage](api/beta.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



CacheCreation [BetaCacheCreation](api/beta.md)

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

Iterations [BetaIterationsUsage](api/beta.md)

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

CacheCreation [BetaCacheCreation](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

string

OutputTokens int64

The number of output tokens which were used.

Type Message

Usage for a sampling iteration



type BetaCompactionIterationUsage struct{…}

Token usage for a compaction iteration.



CacheCreation [BetaCacheCreation](api/beta.md)

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

CacheCreation [BetaCacheCreation](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

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

CacheCreation [BetaCacheCreation](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

string

OutputTokens int64

The number of output tokens which were used.

Type FallbackMessage

Usage for the fallback-model attempt that served the response

OutputTokens int64

The number of output tokens which were used.



OutputTokensDetails [BetaOutputTokensDetails](api/beta.md)

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

ServerToolUse [BetaServerToolUsage](api/beta.md)

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

Type Succeeded



type BetaMessageBatchErroredResult struct{…}



Error [BetaErrorResponse](api/beta.md)



Error [BetaErrorUnion](api/beta.md)

One of the following:



type BetaInvalidRequestError struct{…}

Message string

Type InvalidRequestError



type BetaAuthenticationError struct{…}

Message string

Type AuthenticationError



type BetaBillingError struct{…}

Message string

Type BillingError



type BetaPermissionError struct{…}

Message string

Type PermissionError



type BetaNotFoundError struct{…}

Message string

Type NotFoundError



type BetaRateLimitError struct{…}

Message string

Type RateLimitError



type BetaGatewayTimeoutError struct{…}

Message string

Type TimeoutError



type BetaAPIError struct{…}

Message string

Type APIError



type BetaOverloadedError struct{…}

Message string

Type OverloadedError

RequestID string

Type Error

Type Errored



type BetaMessageBatchCanceledResult struct{…}

Type Canceled



type BetaMessageBatchExpiredResult struct{…}

Type Expired



type BetaMessageBatchRequestCounts struct{…}



Canceled int64

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



Errored int64

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



Expired int64

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

Processing int64

Number of requests in the Message Batch that are processing.



Succeeded int64

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



type BetaMessageBatchResultUnion interface{…}

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



type BetaMessageBatchSucceededResult struct{…}



Message [BetaMessage](api/beta.md)



ID string

Unique object identifier.

The format and length of IDs may change over time.



Container [BetaContainer](api/beta.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



Skills [][BetaSkill](api/beta.md)

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

Content [][BetaContentBlockUnion](api/beta.md)

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

Citations [][BetaTextCitationUnion](api/beta.md)

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

Content [BetaWebSearchToolResultBlockContentUnion](api/beta.md)

One of the following:



type BetaWebSearchToolResultError struct{…}



ErrorCode [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta.md) = "request\_too\_large"

Type WebSearchToolResultError



type BetaWebSearchToolResultBlockContentArray [][BetaWebSearchResultBlock](api/beta.md)

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

ErrorCode [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotInPriorContext [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_in\_prior\_context"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta.md) = "unavailable"

Type WebFetchToolResultError



type BetaWebFetchBlock struct{…}



Content [BetaDocumentBlock](api/beta.md)



Citations [BetaCitationConfig](api/beta.md)

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

Content [BetaCodeExecutionToolResultBlockContentUnion](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type BetaCodeExecutionToolResultError struct{…}



ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type BetaCodeExecutionResultBlock struct{…}



Content [][BetaCodeExecutionOutputBlock](api/beta.md)

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

Content [][BetaCodeExecutionOutputBlock](api/beta.md)

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

Content [][BetaBashCodeExecutionOutputBlock](api/beta.md)

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

ToolReferences [][BetaToolReferenceBlock](api/beta.md)

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

type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent [][BetaTextBlock](api/beta.md)



Citations [][BetaTextCitationUnion](api/beta.md)

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
declined. A turn routed directly by the sticky decision has no such boundary
and carries no block — the signal for whether a fallback model served the
response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



From [BetaFallbackInfo](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

string



To [BetaFallbackInfo](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

string

Type Fallback



ContextManagement [BetaContextManagementResponse](api/beta.md)

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

Diagnostics [BetaDiagnostics](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

string



Role Assistant

Conversational role of the generated message.

This will always be `"assistant"`.



StopDetails [BetaRefusalStopDetails](api/beta.md)

Structured information about a refusal.



Category BetaRefusalStopDetailsCategory

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

const BetaRefusalStopDetailsCategoryCyber BetaRefusalStopDetailsCategory = "cyber"

const BetaRefusalStopDetailsCategoryBio BetaRefusalStopDetailsCategory = "bio"

const BetaRefusalStopDetailsCategoryReasoningExtraction BetaRefusalStopDetailsCategory = "reasoning\_extraction"

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

StopReason [BetaStopReason](api/beta.md)

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

const BetaStopReasonEndTurn [BetaStopReason](api/beta.md) = "end\_turn"

const BetaStopReasonMaxTokens [BetaStopReason](api/beta.md) = "max\_tokens"

const BetaStopReasonStopSequence [BetaStopReason](api/beta.md) = "stop\_sequence"

const BetaStopReasonToolUse [BetaStopReason](api/beta.md) = "tool\_use"

const BetaStopReasonPauseTurn [BetaStopReason](api/beta.md) = "pause\_turn"

const BetaStopReasonCompaction [BetaStopReason](api/beta.md) = "compaction"

const BetaStopReasonRefusal [BetaStopReason](api/beta.md) = "refusal"

const BetaStopReasonModelContextWindowExceeded [BetaStopReason](api/beta.md) = "model\_context\_window\_exceeded"



StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



Type Message

Object type.

For Messages, this is always `"message"`.



Usage [BetaUsage](api/beta.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



CacheCreation [BetaCacheCreation](api/beta.md)

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

Iterations [BetaIterationsUsage](api/beta.md)

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

CacheCreation [BetaCacheCreation](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

string

OutputTokens int64

The number of output tokens which were used.

Type Message

Usage for a sampling iteration



type BetaCompactionIterationUsage struct{…}

Token usage for a compaction iteration.



CacheCreation [BetaCacheCreation](api/beta.md)

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

CacheCreation [BetaCacheCreation](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

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

CacheCreation [BetaCacheCreation](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

string

OutputTokens int64

The number of output tokens which were used.

Type FallbackMessage

Usage for the fallback-model attempt that served the response

OutputTokens int64

The number of output tokens which were used.



OutputTokensDetails [BetaOutputTokensDetails](api/beta.md)

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

ServerToolUse [BetaServerToolUsage](api/beta.md)

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

Type Succeeded



type BetaMessageBatchErroredResult struct{…}



Error [BetaErrorResponse](api/beta.md)



Error [BetaErrorUnion](api/beta.md)

One of the following:



type BetaInvalidRequestError struct{…}

Message string

Type InvalidRequestError



type BetaAuthenticationError struct{…}

Message string

Type AuthenticationError



type BetaBillingError struct{…}

Message string

Type BillingError



type BetaPermissionError struct{…}

Message string

Type PermissionError



type BetaNotFoundError struct{…}

Message string

Type NotFoundError



type BetaRateLimitError struct{…}

Message string

Type RateLimitError



type BetaGatewayTimeoutError struct{…}

Message string

Type TimeoutError



type BetaAPIError struct{…}

Message string

Type APIError



type BetaOverloadedError struct{…}

Message string

Type OverloadedError

RequestID string

Type Error

Type Errored



type BetaMessageBatchCanceledResult struct{…}

Type Canceled



type BetaMessageBatchExpiredResult struct{…}

Type Expired



type BetaMessageBatchSucceededResult struct{…}



Message [BetaMessage](api/beta.md)



ID string

Unique object identifier.

The format and length of IDs may change over time.



Container [BetaContainer](api/beta.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



Skills [][BetaSkill](api/beta.md)

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

Content [][BetaContentBlockUnion](api/beta.md)

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

Citations [][BetaTextCitationUnion](api/beta.md)

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

Content [BetaWebSearchToolResultBlockContentUnion](api/beta.md)

One of the following:



type BetaWebSearchToolResultError struct{…}



ErrorCode [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](api/beta.md) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](api/beta.md) = "max\_uses\_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](api/beta.md) = "query\_too\_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](api/beta.md) = "request\_too\_large"

Type WebSearchToolResultError



type BetaWebSearchToolResultBlockContentArray [][BetaWebSearchResultBlock](api/beta.md)

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

ErrorCode [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_too\_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_allowed"

const BetaWebFetchToolResultErrorCodeURLNotInPriorContext [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_in\_prior\_context"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](api/beta.md) = "url\_not\_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](api/beta.md) = "unsupported\_content\_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](api/beta.md) = "max\_uses\_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](api/beta.md) = "unavailable"

Type WebFetchToolResultError



type BetaWebFetchBlock struct{…}



Content [BetaDocumentBlock](api/beta.md)



Citations [BetaCitationConfig](api/beta.md)

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

Content [BetaCodeExecutionToolResultBlockContentUnion](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type BetaCodeExecutionToolResultError struct{…}



ErrorCode [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "invalid\_tool\_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "too\_many\_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](api/beta.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type BetaCodeExecutionResultBlock struct{…}



Content [][BetaCodeExecutionOutputBlock](api/beta.md)

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

Content [][BetaCodeExecutionOutputBlock](api/beta.md)

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

Content [][BetaBashCodeExecutionOutputBlock](api/beta.md)

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

ToolReferences [][BetaToolReferenceBlock](api/beta.md)

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

type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent [][BetaTextBlock](api/beta.md)



Citations [][BetaTextCitationUnion](api/beta.md)

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
declined. A turn routed directly by the sticky decision has no such boundary
and carries no block — the signal for whether a fallback model served the
response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



From [BetaFallbackInfo](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

string



To [BetaFallbackInfo](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

string

Type Fallback



ContextManagement [BetaContextManagementResponse](api/beta.md)

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

Diagnostics [BetaDiagnostics](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

string



Role Assistant

Conversational role of the generated message.

This will always be `"assistant"`.



StopDetails [BetaRefusalStopDetails](api/beta.md)

Structured information about a refusal.



Category BetaRefusalStopDetailsCategory

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

const BetaRefusalStopDetailsCategoryCyber BetaRefusalStopDetailsCategory = "cyber"

const BetaRefusalStopDetailsCategoryBio BetaRefusalStopDetailsCategory = "bio"

const BetaRefusalStopDetailsCategoryReasoningExtraction BetaRefusalStopDetailsCategory = "reasoning\_extraction"

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

StopReason [BetaStopReason](api/beta.md)

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

const BetaStopReasonEndTurn [BetaStopReason](api/beta.md) = "end\_turn"

const BetaStopReasonMaxTokens [BetaStopReason](api/beta.md) = "max\_tokens"

const BetaStopReasonStopSequence [BetaStopReason](api/beta.md) = "stop\_sequence"

const BetaStopReasonToolUse [BetaStopReason](api/beta.md) = "tool\_use"

const BetaStopReasonPauseTurn [BetaStopReason](api/beta.md) = "pause\_turn"

const BetaStopReasonCompaction [BetaStopReason](api/beta.md) = "compaction"

const BetaStopReasonRefusal [BetaStopReason](api/beta.md) = "refusal"

const BetaStopReasonModelContextWindowExceeded [BetaStopReason](api/beta.md) = "model\_context\_window\_exceeded"



StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



Type Message

Object type.

For Messages, this is always `"message"`.



Usage [BetaUsage](api/beta.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



CacheCreation [BetaCacheCreation](api/beta.md)

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

Iterations [BetaIterationsUsage](api/beta.md)

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

CacheCreation [BetaCacheCreation](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

string

OutputTokens int64

The number of output tokens which were used.

Type Message

Usage for a sampling iteration



type BetaCompactionIterationUsage struct{…}

Token usage for a compaction iteration.



CacheCreation [BetaCacheCreation](api/beta.md)

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

CacheCreation [BetaCacheCreation](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

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

CacheCreation [BetaCacheCreation](api/beta.md)

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

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Powerful model for complex tasks

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Powerful model for complex tasks

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Fast and cost-effective model

string

OutputTokens int64

The number of output tokens which were used.

Type FallbackMessage

Usage for the fallback-model attempt that served the response

OutputTokens int64

The number of output tokens which were used.



OutputTokensDetails [BetaOutputTokensDetails](api/beta.md)

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

ServerToolUse [BetaServerToolUsage](api/beta.md)

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

Type Succeeded

---

*Copyright © Anthropic. All rights reserved.*
