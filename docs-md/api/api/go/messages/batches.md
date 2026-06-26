# Batches

Copy page



Go

# Batches

##### [Create a Message Batch](api/messages/batches/create.md)

client.Messages.Batches.New(ctx, body) (\*[MessageBatch](api/messages.md), error)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/messages/batches/retrieve.md)

client.Messages.Batches.Get(ctx, messageBatchID) (\*[MessageBatch](api/messages.md), error)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/messages/batches/list.md)

client.Messages.Batches.List(ctx, query) (\*Page[[MessageBatch](api/messages.md)], error)

GET/v1/messages/batches

##### [Cancel a Message Batch](api/messages/batches/cancel.md)

client.Messages.Batches.Cancel(ctx, messageBatchID) (\*[MessageBatch](api/messages.md), error)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/messages/batches/delete.md)

client.Messages.Batches.Delete(ctx, messageBatchID) (\*[DeletedMessageBatch](api/messages.md), error)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/messages/batches/results.md)

client.Messages.Batches.Results(ctx, messageBatchID) (\*[MessageBatchIndividualResponse](api/messages.md), error)

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse



type DeletedMessageBatch struct{…}

ID string

ID of the Message Batch.



Type MessageBatchDeleted

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.



type MessageBatch struct{…}

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

ProcessingStatus MessageBatchProcessingStatus

Processing status of the Message Batch.

One of the following:

const MessageBatchProcessingStatusInProgress MessageBatchProcessingStatus = "in\_progress"

const MessageBatchProcessingStatusCanceling MessageBatchProcessingStatus = "canceling"

const MessageBatchProcessingStatusEnded MessageBatchProcessingStatus = "ended"



RequestCounts [MessageBatchRequestCounts](api/messages.md)

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

type MessageBatchCanceledResult struct{…}

Type Canceled



type MessageBatchErroredResult struct{…}



Error [ErrorResponse](api/$shared.md)



Error [ErrorObjectUnion](api/$shared.md)

One of the following:



type InvalidRequestError struct{…}

Message string

Type InvalidRequestError



type AuthenticationError struct{…}

Message string

Type AuthenticationError



type BillingError struct{…}

Message string

Type BillingError



type PermissionError struct{…}

Message string

Type PermissionError



type NotFoundError struct{…}

Message string

Type NotFoundError



type RateLimitError struct{…}

Message string

Type RateLimitError



type GatewayTimeoutError struct{…}

Message string

Type TimeoutError



type APIErrorObject struct{…}

Message string

Type APIError



type OverloadedError struct{…}

Message string

Type OverloadedError

RequestID string

Type Error

Type Errored



type MessageBatchExpiredResult struct{…}

Type Expired



type MessageBatchIndividualResponse struct{…}

This is a single line in the response `.jsonl` file and does not represent the response as a whole.



CustomID string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.



Result [MessageBatchResultUnion](api/messages.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



type MessageBatchSucceededResult struct{…}



Message [Message](api/messages.md)



ID string

Unique object identifier.

The format and length of IDs may change over time.



Container [Container](api/messages.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



Content [][ContentBlockUnion](api/messages.md)

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

type TextBlock struct{…}



Citations [][TextCitationUnion](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocation struct{…}

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

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationsSearchResultLocation struct{…}

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

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking



type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking



type ToolUseBlock struct{…}

ID string



Caller ToolUseBlockCallerUnion

Tool invocation directly from the model.

One of the following:



type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map[string, any]

Name string

Type ToolUse



type ServerToolUseBlock struct{…}

ID string



Caller ServerToolUseBlockCallerUnion

Tool invocation directly from the model.

One of the following:



type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map[string, any]



Name ServerToolUseBlockName

One of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web\_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web\_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code\_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash\_code\_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text\_editor\_code\_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool\_search\_tool\_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse



type WebSearchToolResultBlock struct{…}



Caller WebSearchToolResultBlockCallerUnion

Tool invocation directly from the model.

One of the following:



type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



Content [WebSearchToolResultBlockContentUnion](api/messages.md)

One of the following:



type WebSearchToolResultError struct{…}



ErrorCode [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](api/messages.md) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](api/messages.md) = "max\_uses\_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](api/messages.md) = "query\_too\_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](api/messages.md) = "request\_too\_large"

Type WebSearchToolResultError



type WebSearchToolResultBlockContentArray [][WebSearchResultBlock](api/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult



type WebFetchToolResultBlock struct{…}



Caller WebFetchToolResultBlockCallerUnion

Tool invocation directly from the model.

One of the following:



type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



Content WebFetchToolResultBlockContentUnion

One of the following:



type WebFetchToolResultErrorBlock struct{…}



ErrorCode [WebFetchToolResultErrorCode](api/messages.md)

One of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](api/messages.md) = "url\_too\_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_allowed"

const WebFetchToolResultErrorCodeURLNotInPriorContext [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_in\_prior\_context"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](api/messages.md) = "unsupported\_content\_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](api/messages.md) = "max\_uses\_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](api/messages.md) = "unavailable"

Type WebFetchToolResultError



type WebFetchBlock struct{…}



Content [DocumentBlock](api/messages.md)



Citations [CitationsConfig](api/messages.md)

Citation configuration for the document

Enabled bool



Source DocumentBlockSourceUnion

One of the following:



type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type PlainTextSource struct{…}

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

type CodeExecutionToolResultBlock struct{…}



Content [CodeExecutionToolResultBlockContentUnion](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type CodeExecutionToolResultError struct{…}



ErrorCode [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type CodeExecutionResultBlock struct{…}



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



type BashCodeExecutionToolResultBlock struct{…}



Content BashCodeExecutionToolResultBlockContentUnion

One of the following:



type BashCodeExecutionToolResultError struct{…}



ErrorCode [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](api/messages.md) = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError



type BashCodeExecutionResultBlock struct{…}



Content [][BashCodeExecutionOutputBlock](api/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



type TextEditorCodeExecutionToolResultBlock struct{…}



Content TextEditorCodeExecutionToolResultBlockContentUnion

One of the following:



type TextEditorCodeExecutionToolResultError struct{…}



ErrorCode [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type TextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType TextEditorCodeExecutionViewResultBlockFileType

One of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult



type ToolSearchToolResultBlock struct{…}



Content ToolSearchToolResultBlockContentUnion

One of the following:



type ToolSearchToolResultError struct{…}



ErrorCode [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](api/messages.md) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type ToolSearchToolSearchResultBlock struct{…}



ToolReferences [][ToolReferenceBlock](api/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

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

string



Role Assistant

Conversational role of the generated message.

This will always be `"assistant"`.



StopDetails [RefusalStopDetails](api/messages.md)

Structured information about a refusal.



Category RefusalStopDetailsCategory

The policy category that triggered a refusal.

One of the following:

const RefusalStopDetailsCategoryCyber RefusalStopDetailsCategory = "cyber"

const RefusalStopDetailsCategoryBio RefusalStopDetailsCategory = "bio"

const RefusalStopDetailsCategoryFrontierLLM RefusalStopDetailsCategory = "frontier\_llm"

const RefusalStopDetailsCategoryReasoningExtraction RefusalStopDetailsCategory = "reasoning\_extraction"



Explanation string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

Type Refusal



StopReason [StopReason](api/messages.md)

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

const StopReasonEndTurn [StopReason](api/messages.md) = "end\_turn"

const StopReasonMaxTokens [StopReason](api/messages.md) = "max\_tokens"

const StopReasonStopSequence [StopReason](api/messages.md) = "stop\_sequence"

const StopReasonToolUse [StopReason](api/messages.md) = "tool\_use"

const StopReasonPauseTurn [StopReason](api/messages.md) = "pause\_turn"

const StopReasonRefusal [StopReason](api/messages.md) = "refusal"



StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



Type Message

Object type.

For Messages, this is always `"message"`.



Usage [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



CacheCreation [CacheCreation](api/messages.md)

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

OutputTokens int64

The number of output tokens which were used.



OutputTokensDetails [OutputTokensDetails](api/messages.md)

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

ServerToolUse [ServerToolUsage](api/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

One of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type Succeeded



type MessageBatchErroredResult struct{…}



Error [ErrorResponse](api/$shared.md)



Error [ErrorObjectUnion](api/$shared.md)

One of the following:



type InvalidRequestError struct{…}

Message string

Type InvalidRequestError



type AuthenticationError struct{…}

Message string

Type AuthenticationError



type BillingError struct{…}

Message string

Type BillingError



type PermissionError struct{…}

Message string

Type PermissionError



type NotFoundError struct{…}

Message string

Type NotFoundError



type RateLimitError struct{…}

Message string

Type RateLimitError



type GatewayTimeoutError struct{…}

Message string

Type TimeoutError



type APIErrorObject struct{…}

Message string

Type APIError



type OverloadedError struct{…}

Message string

Type OverloadedError

RequestID string

Type Error

Type Errored



type MessageBatchCanceledResult struct{…}

Type Canceled



type MessageBatchExpiredResult struct{…}

Type Expired



type MessageBatchRequestCounts struct{…}

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

type MessageBatchResultUnion interface{…}

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



type MessageBatchSucceededResult struct{…}



Message [Message](api/messages.md)



ID string

Unique object identifier.

The format and length of IDs may change over time.



Container [Container](api/messages.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



Content [][ContentBlockUnion](api/messages.md)

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

type TextBlock struct{…}



Citations [][TextCitationUnion](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocation struct{…}

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

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationsSearchResultLocation struct{…}

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

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking



type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking



type ToolUseBlock struct{…}

ID string



Caller ToolUseBlockCallerUnion

Tool invocation directly from the model.

One of the following:



type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map[string, any]

Name string

Type ToolUse



type ServerToolUseBlock struct{…}

ID string



Caller ServerToolUseBlockCallerUnion

Tool invocation directly from the model.

One of the following:



type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map[string, any]



Name ServerToolUseBlockName

One of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web\_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web\_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code\_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash\_code\_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text\_editor\_code\_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool\_search\_tool\_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse



type WebSearchToolResultBlock struct{…}



Caller WebSearchToolResultBlockCallerUnion

Tool invocation directly from the model.

One of the following:



type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



Content [WebSearchToolResultBlockContentUnion](api/messages.md)

One of the following:



type WebSearchToolResultError struct{…}



ErrorCode [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](api/messages.md) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](api/messages.md) = "max\_uses\_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](api/messages.md) = "query\_too\_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](api/messages.md) = "request\_too\_large"

Type WebSearchToolResultError



type WebSearchToolResultBlockContentArray [][WebSearchResultBlock](api/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult



type WebFetchToolResultBlock struct{…}



Caller WebFetchToolResultBlockCallerUnion

Tool invocation directly from the model.

One of the following:



type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



Content WebFetchToolResultBlockContentUnion

One of the following:



type WebFetchToolResultErrorBlock struct{…}



ErrorCode [WebFetchToolResultErrorCode](api/messages.md)

One of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](api/messages.md) = "url\_too\_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_allowed"

const WebFetchToolResultErrorCodeURLNotInPriorContext [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_in\_prior\_context"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](api/messages.md) = "unsupported\_content\_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](api/messages.md) = "max\_uses\_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](api/messages.md) = "unavailable"

Type WebFetchToolResultError



type WebFetchBlock struct{…}



Content [DocumentBlock](api/messages.md)



Citations [CitationsConfig](api/messages.md)

Citation configuration for the document

Enabled bool



Source DocumentBlockSourceUnion

One of the following:



type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type PlainTextSource struct{…}

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

type CodeExecutionToolResultBlock struct{…}



Content [CodeExecutionToolResultBlockContentUnion](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type CodeExecutionToolResultError struct{…}



ErrorCode [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type CodeExecutionResultBlock struct{…}



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



type BashCodeExecutionToolResultBlock struct{…}



Content BashCodeExecutionToolResultBlockContentUnion

One of the following:



type BashCodeExecutionToolResultError struct{…}



ErrorCode [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](api/messages.md) = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError



type BashCodeExecutionResultBlock struct{…}



Content [][BashCodeExecutionOutputBlock](api/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



type TextEditorCodeExecutionToolResultBlock struct{…}



Content TextEditorCodeExecutionToolResultBlockContentUnion

One of the following:



type TextEditorCodeExecutionToolResultError struct{…}



ErrorCode [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type TextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType TextEditorCodeExecutionViewResultBlockFileType

One of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult



type ToolSearchToolResultBlock struct{…}



Content ToolSearchToolResultBlockContentUnion

One of the following:



type ToolSearchToolResultError struct{…}



ErrorCode [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](api/messages.md) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type ToolSearchToolSearchResultBlock struct{…}



ToolReferences [][ToolReferenceBlock](api/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

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

string



Role Assistant

Conversational role of the generated message.

This will always be `"assistant"`.



StopDetails [RefusalStopDetails](api/messages.md)

Structured information about a refusal.



Category RefusalStopDetailsCategory

The policy category that triggered a refusal.

One of the following:

const RefusalStopDetailsCategoryCyber RefusalStopDetailsCategory = "cyber"

const RefusalStopDetailsCategoryBio RefusalStopDetailsCategory = "bio"

const RefusalStopDetailsCategoryFrontierLLM RefusalStopDetailsCategory = "frontier\_llm"

const RefusalStopDetailsCategoryReasoningExtraction RefusalStopDetailsCategory = "reasoning\_extraction"



Explanation string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

Type Refusal



StopReason [StopReason](api/messages.md)

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

const StopReasonEndTurn [StopReason](api/messages.md) = "end\_turn"

const StopReasonMaxTokens [StopReason](api/messages.md) = "max\_tokens"

const StopReasonStopSequence [StopReason](api/messages.md) = "stop\_sequence"

const StopReasonToolUse [StopReason](api/messages.md) = "tool\_use"

const StopReasonPauseTurn [StopReason](api/messages.md) = "pause\_turn"

const StopReasonRefusal [StopReason](api/messages.md) = "refusal"



StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



Type Message

Object type.

For Messages, this is always `"message"`.



Usage [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



CacheCreation [CacheCreation](api/messages.md)

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

OutputTokens int64

The number of output tokens which were used.



OutputTokensDetails [OutputTokensDetails](api/messages.md)

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

ServerToolUse [ServerToolUsage](api/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

One of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type Succeeded



type MessageBatchErroredResult struct{…}



Error [ErrorResponse](api/$shared.md)



Error [ErrorObjectUnion](api/$shared.md)

One of the following:



type InvalidRequestError struct{…}

Message string

Type InvalidRequestError



type AuthenticationError struct{…}

Message string

Type AuthenticationError



type BillingError struct{…}

Message string

Type BillingError



type PermissionError struct{…}

Message string

Type PermissionError



type NotFoundError struct{…}

Message string

Type NotFoundError



type RateLimitError struct{…}

Message string

Type RateLimitError



type GatewayTimeoutError struct{…}

Message string

Type TimeoutError



type APIErrorObject struct{…}

Message string

Type APIError



type OverloadedError struct{…}

Message string

Type OverloadedError

RequestID string

Type Error

Type Errored



type MessageBatchCanceledResult struct{…}

Type Canceled



type MessageBatchExpiredResult struct{…}

Type Expired



type MessageBatchSucceededResult struct{…}



Message [Message](api/messages.md)



ID string

Unique object identifier.

The format and length of IDs may change over time.



Container [Container](api/messages.md)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.



Content [][ContentBlockUnion](api/messages.md)

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

type TextBlock struct{…}



Citations [][TextCitationUnion](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation



type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation



type CitationContentBlockLocation struct{…}

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

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string



type CitationsSearchResultLocation struct{…}

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

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking



type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking



type ToolUseBlock struct{…}

ID string



Caller ToolUseBlockCallerUnion

Tool invocation directly from the model.

One of the following:



type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map[string, any]

Name string

Type ToolUse



type ServerToolUseBlock struct{…}

ID string



Caller ServerToolUseBlockCallerUnion

Tool invocation directly from the model.

One of the following:



type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map[string, any]



Name ServerToolUseBlockName

One of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web\_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web\_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code\_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash\_code\_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text\_editor\_code\_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool\_search\_tool\_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool\_search\_tool\_bm25"

Type ServerToolUse



type WebSearchToolResultBlock struct{…}



Caller WebSearchToolResultBlockCallerUnion

Tool invocation directly from the model.

One of the following:



type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



Content [WebSearchToolResultBlockContentUnion](api/messages.md)

One of the following:



type WebSearchToolResultError struct{…}



ErrorCode [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](api/messages.md) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](api/messages.md) = "max\_uses\_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](api/messages.md) = "query\_too\_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](api/messages.md) = "request\_too\_large"

Type WebSearchToolResultError



type WebSearchToolResultBlockContentArray [][WebSearchResultBlock](api/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult



type WebFetchToolResultBlock struct{…}



Caller WebFetchToolResultBlockCallerUnion

Tool invocation directly from the model.

One of the following:



type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct



type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825



type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120



Content WebFetchToolResultBlockContentUnion

One of the following:



type WebFetchToolResultErrorBlock struct{…}



ErrorCode [WebFetchToolResultErrorCode](api/messages.md)

One of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](api/messages.md) = "url\_too\_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_allowed"

const WebFetchToolResultErrorCodeURLNotInPriorContext [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_in\_prior\_context"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](api/messages.md) = "url\_not\_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](api/messages.md) = "unsupported\_content\_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](api/messages.md) = "max\_uses\_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](api/messages.md) = "unavailable"

Type WebFetchToolResultError



type WebFetchBlock struct{…}



Content [DocumentBlock](api/messages.md)



Citations [CitationsConfig](api/messages.md)

Citation configuration for the document

Enabled bool



Source DocumentBlockSourceUnion

One of the following:



type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64



type PlainTextSource struct{…}

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

type CodeExecutionToolResultBlock struct{…}



Content [CodeExecutionToolResultBlockContentUnion](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



type CodeExecutionToolResultError struct{…}



ErrorCode [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

Type CodeExecutionToolResultError



type CodeExecutionResultBlock struct{…}



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult



type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web\_search results.



Content [][CodeExecutionOutputBlock](api/messages.md)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult



type BashCodeExecutionToolResultBlock struct{…}



Content BashCodeExecutionToolResultBlockContentUnion

One of the following:



type BashCodeExecutionToolResultError struct{…}



ErrorCode [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](api/messages.md) = "output\_file\_too\_large"

Type BashCodeExecutionToolResultError



type BashCodeExecutionResultBlock struct{…}



Content [][BashCodeExecutionOutputBlock](api/messages.md)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult



type TextEditorCodeExecutionToolResultBlock struct{…}



Content TextEditorCodeExecutionToolResultBlockContentUnion

One of the following:



type TextEditorCodeExecutionToolResultError struct{…}



ErrorCode [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) = "file\_not\_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError



type TextEditorCodeExecutionViewResultBlock struct{…}

Content string



FileType TextEditorCodeExecutionViewResultBlockFileType

One of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult



type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult



type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines []string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult



type ToolSearchToolResultBlock struct{…}



Content ToolSearchToolResultBlockContentUnion

One of the following:



type ToolSearchToolResultError struct{…}



ErrorCode [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](api/messages.md) = "invalid\_tool\_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](api/messages.md) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](api/messages.md) = "too\_many\_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](api/messages.md) = "execution\_time\_exceeded"

ErrorMessage string

Type ToolSearchToolResultError



type ToolSearchToolSearchResultBlock struct{…}



ToolReferences [][ToolReferenceBlock](api/messages.md)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult



type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

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

string



Role Assistant

Conversational role of the generated message.

This will always be `"assistant"`.



StopDetails [RefusalStopDetails](api/messages.md)

Structured information about a refusal.



Category RefusalStopDetailsCategory

The policy category that triggered a refusal.

One of the following:

const RefusalStopDetailsCategoryCyber RefusalStopDetailsCategory = "cyber"

const RefusalStopDetailsCategoryBio RefusalStopDetailsCategory = "bio"

const RefusalStopDetailsCategoryFrontierLLM RefusalStopDetailsCategory = "frontier\_llm"

const RefusalStopDetailsCategoryReasoningExtraction RefusalStopDetailsCategory = "reasoning\_extraction"



Explanation string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

Type Refusal



StopReason [StopReason](api/messages.md)

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

const StopReasonEndTurn [StopReason](api/messages.md) = "end\_turn"

const StopReasonMaxTokens [StopReason](api/messages.md) = "max\_tokens"

const StopReasonStopSequence [StopReason](api/messages.md) = "stop\_sequence"

const StopReasonToolUse [StopReason](api/messages.md) = "tool\_use"

const StopReasonPauseTurn [StopReason](api/messages.md) = "pause\_turn"

const StopReasonRefusal [StopReason](api/messages.md) = "refusal"



StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



Type Message

Object type.

For Messages, this is always `"message"`.



Usage [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



CacheCreation [CacheCreation](api/messages.md)

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

OutputTokens int64

The number of output tokens which were used.



OutputTokensDetails [OutputTokensDetails](api/messages.md)

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

ServerToolUse [ServerToolUsage](api/messages.md)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.



ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

One of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type Succeeded

---

*Copyright © Anthropic. All rights reserved.*
