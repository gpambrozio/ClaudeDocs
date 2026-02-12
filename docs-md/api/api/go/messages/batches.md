# Batches

Copy page

Go

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

type DeletedMessageBatch struct{…}

ID string

ID of the Message Batch.

Type MessageBatchDeleted

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

type MessageBatch struct{…}

ID string

Unique object identifier.

The format and length of IDs may change over time.

ArchivedAt Time

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

CancelInitiatedAt Time

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

CreatedAt Time

RFC 3339 datetime string representing the time at which the Message Batch was created.

EndedAt Time

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

ExpiresAt Time

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

ProcessingStatus MessageBatchProcessingStatus

Processing status of the Message Batch.

Accepts one of the following:

const MessageBatchProcessingStatusInProgress MessageBatchProcessingStatus = "in\_progress"

const MessageBatchProcessingStatusCanceling MessageBatchProcessingStatus = "canceling"

const MessageBatchProcessingStatusEnded MessageBatchProcessingStatus = "ended"

RequestCounts [MessageBatchRequestCounts](api/messages.md)

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

type MessageBatchCanceledResult struct{…}

Type Canceled

type MessageBatchErroredResult struct{…}

Error [ErrorResponse](api/$shared.md)

Error [ErrorObjectUnion](api/$shared.md)

Accepts one of the following:

type InvalidRequestError struct{…}

Message string

Type InvalidRequestError

type AuthenticationError struct{…}

Message string

Type AuthenticationError

type BillingError struct{…}

Message string

Type BillingError

type PermissionError struct{…}

Message string

Type PermissionError

type NotFoundError struct{…}

Message string

Type NotFoundError

type RateLimitError struct{…}

Message string

Type RateLimitError

type GatewayTimeoutError struct{…}

Message string

Type TimeoutError

type APIErrorObject struct{…}

Message string

Type APIError

type OverloadedError struct{…}

Message string

Type OverloadedError

RequestID string

Type Error

Type Errored

type MessageBatchExpiredResult struct{…}

Type Expired

type MessageBatchIndividualResponse struct{…}

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

CustomID string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

Result [MessageBatchResultUnion](api/messages.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

type MessageBatchSucceededResult struct{…}

Message [Message](api/messages.md)

ID string

Unique object identifier.

The format and length of IDs may change over time.

Content [][ContentBlockUnion](api/messages.md)

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

type TextBlock struct{…}

Citations [][TextCitationUnion](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Text string

Type Text

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

type ToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse

type ServerToolUseBlock struct{…}

ID string

Input map[string, any]

Name WebSearch

Type ServerToolUse

type WebSearchToolResultBlock struct{…}

Content [WebSearchToolResultBlockContentUnion](api/messages.md)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode WebSearchToolResultErrorErrorCode

Accepts one of the following:

const WebSearchToolResultErrorErrorCodeInvalidToolInput WebSearchToolResultErrorErrorCode = "invalid\_tool\_input"

const WebSearchToolResultErrorErrorCodeUnavailable WebSearchToolResultErrorErrorCode = "unavailable"

const WebSearchToolResultErrorErrorCodeMaxUsesExceeded WebSearchToolResultErrorErrorCode = "max\_uses\_exceeded"

const WebSearchToolResultErrorErrorCodeTooManyRequests WebSearchToolResultErrorErrorCode = "too\_many\_requests"

const WebSearchToolResultErrorErrorCodeQueryTooLong WebSearchToolResultErrorErrorCode = "query\_too\_long"

const WebSearchToolResultErrorErrorCodeRequestTooLarge WebSearchToolResultErrorErrorCode = "request\_too\_large"

Type WebSearchToolResultError

type WebSearchToolResultBlockContentArray [][WebSearchResultBlock](api/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult

Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

const ModelClaudeOpus4\_6 Model = "claude-opus-4-6"

Most intelligent model for building agents and coding

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

StopReason [StopReason](api/messages.md)

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

const StopReasonEndTurn [StopReason](api/messages.md) = "end\_turn"

const StopReasonMaxTokens [StopReason](api/messages.md) = "max\_tokens"

const StopReasonStopSequence [StopReason](api/messages.md) = "stop\_sequence"

const StopReasonToolUse [StopReason](api/messages.md) = "tool\_use"

const StopReasonPauseTurn [StopReason](api/messages.md) = "pause\_turn"

const StopReasonRefusal [StopReason](api/messages.md) = "refusal"

StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

Type Message

Object type.

For Messages, this is always `"message"`.

Usage [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreation [CacheCreation](api/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

ServerToolUse [ServerToolUsage](api/messages.md)

The number of server tool requests.

WebSearchRequests int64

The number of web search tool requests.

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type Succeeded

type MessageBatchErroredResult struct{…}

Error [ErrorResponse](api/$shared.md)

Error [ErrorObjectUnion](api/$shared.md)

Accepts one of the following:

type InvalidRequestError struct{…}

Message string

Type InvalidRequestError

type AuthenticationError struct{…}

Message string

Type AuthenticationError

type BillingError struct{…}

Message string

Type BillingError

type PermissionError struct{…}

Message string

Type PermissionError

type NotFoundError struct{…}

Message string

Type NotFoundError

type RateLimitError struct{…}

Message string

Type RateLimitError

type GatewayTimeoutError struct{…}

Message string

Type TimeoutError

type APIErrorObject struct{…}

Message string

Type APIError

type OverloadedError struct{…}

Message string

Type OverloadedError

RequestID string

Type Error

Type Errored

type MessageBatchCanceledResult struct{…}

Type Canceled

type MessageBatchExpiredResult struct{…}

Type Expired

type MessageBatchRequestCounts struct{…}

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

type MessageBatchResultUnion interface{…}

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

type MessageBatchSucceededResult struct{…}

Message [Message](api/messages.md)

ID string

Unique object identifier.

The format and length of IDs may change over time.

Content [][ContentBlockUnion](api/messages.md)

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

type TextBlock struct{…}

Citations [][TextCitationUnion](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Text string

Type Text

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

type ToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse

type ServerToolUseBlock struct{…}

ID string

Input map[string, any]

Name WebSearch

Type ServerToolUse

type WebSearchToolResultBlock struct{…}

Content [WebSearchToolResultBlockContentUnion](api/messages.md)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode WebSearchToolResultErrorErrorCode

Accepts one of the following:

const WebSearchToolResultErrorErrorCodeInvalidToolInput WebSearchToolResultErrorErrorCode = "invalid\_tool\_input"

const WebSearchToolResultErrorErrorCodeUnavailable WebSearchToolResultErrorErrorCode = "unavailable"

const WebSearchToolResultErrorErrorCodeMaxUsesExceeded WebSearchToolResultErrorErrorCode = "max\_uses\_exceeded"

const WebSearchToolResultErrorErrorCodeTooManyRequests WebSearchToolResultErrorErrorCode = "too\_many\_requests"

const WebSearchToolResultErrorErrorCodeQueryTooLong WebSearchToolResultErrorErrorCode = "query\_too\_long"

const WebSearchToolResultErrorErrorCodeRequestTooLarge WebSearchToolResultErrorErrorCode = "request\_too\_large"

Type WebSearchToolResultError

type WebSearchToolResultBlockContentArray [][WebSearchResultBlock](api/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult

Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

const ModelClaudeOpus4\_6 Model = "claude-opus-4-6"

Most intelligent model for building agents and coding

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

StopReason [StopReason](api/messages.md)

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

const StopReasonEndTurn [StopReason](api/messages.md) = "end\_turn"

const StopReasonMaxTokens [StopReason](api/messages.md) = "max\_tokens"

const StopReasonStopSequence [StopReason](api/messages.md) = "stop\_sequence"

const StopReasonToolUse [StopReason](api/messages.md) = "tool\_use"

const StopReasonPauseTurn [StopReason](api/messages.md) = "pause\_turn"

const StopReasonRefusal [StopReason](api/messages.md) = "refusal"

StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

Type Message

Object type.

For Messages, this is always `"message"`.

Usage [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreation [CacheCreation](api/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

ServerToolUse [ServerToolUsage](api/messages.md)

The number of server tool requests.

WebSearchRequests int64

The number of web search tool requests.

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type Succeeded

type MessageBatchErroredResult struct{…}

Error [ErrorResponse](api/$shared.md)

Error [ErrorObjectUnion](api/$shared.md)

Accepts one of the following:

type InvalidRequestError struct{…}

Message string

Type InvalidRequestError

type AuthenticationError struct{…}

Message string

Type AuthenticationError

type BillingError struct{…}

Message string

Type BillingError

type PermissionError struct{…}

Message string

Type PermissionError

type NotFoundError struct{…}

Message string

Type NotFoundError

type RateLimitError struct{…}

Message string

Type RateLimitError

type GatewayTimeoutError struct{…}

Message string

Type TimeoutError

type APIErrorObject struct{…}

Message string

Type APIError

type OverloadedError struct{…}

Message string

Type OverloadedError

RequestID string

Type Error

Type Errored

type MessageBatchCanceledResult struct{…}

Type Canceled

type MessageBatchExpiredResult struct{…}

Type Expired

type MessageBatchSucceededResult struct{…}

Message [Message](api/messages.md)

ID string

Unique object identifier.

The format and length of IDs may change over time.

Content [][ContentBlockUnion](api/messages.md)

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

type TextBlock struct{…}

Citations [][TextCitationUnion](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Text string

Type Text

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

type ToolUseBlock struct{…}

ID string

Input map[string, any]

Name string

Type ToolUse

type ServerToolUseBlock struct{…}

ID string

Input map[string, any]

Name WebSearch

Type ServerToolUse

type WebSearchToolResultBlock struct{…}

Content [WebSearchToolResultBlockContentUnion](api/messages.md)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode WebSearchToolResultErrorErrorCode

Accepts one of the following:

const WebSearchToolResultErrorErrorCodeInvalidToolInput WebSearchToolResultErrorErrorCode = "invalid\_tool\_input"

const WebSearchToolResultErrorErrorCodeUnavailable WebSearchToolResultErrorErrorCode = "unavailable"

const WebSearchToolResultErrorErrorCodeMaxUsesExceeded WebSearchToolResultErrorErrorCode = "max\_uses\_exceeded"

const WebSearchToolResultErrorErrorCodeTooManyRequests WebSearchToolResultErrorErrorCode = "too\_many\_requests"

const WebSearchToolResultErrorErrorCodeQueryTooLong WebSearchToolResultErrorErrorCode = "query\_too\_long"

const WebSearchToolResultErrorErrorCodeRequestTooLarge WebSearchToolResultErrorErrorCode = "request\_too\_large"

Type WebSearchToolResultError

type WebSearchToolResultBlockContentArray [][WebSearchResultBlock](api/messages.md)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult

Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

const ModelClaudeOpus4\_6 Model = "claude-opus-4-6"

Most intelligent model for building agents and coding

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

StopReason [StopReason](api/messages.md)

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

const StopReasonEndTurn [StopReason](api/messages.md) = "end\_turn"

const StopReasonMaxTokens [StopReason](api/messages.md) = "max\_tokens"

const StopReasonStopSequence [StopReason](api/messages.md) = "stop\_sequence"

const StopReasonToolUse [StopReason](api/messages.md) = "tool\_use"

const StopReasonPauseTurn [StopReason](api/messages.md) = "pause\_turn"

const StopReasonRefusal [StopReason](api/messages.md) = "refusal"

StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

Type Message

Object type.

For Messages, this is always `"message"`.

Usage [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreation [CacheCreation](api/messages.md)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

ServerToolUse [ServerToolUsage](api/messages.md)

The number of server tool requests.

WebSearchRequests int64

The number of web search tool requests.

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type Succeeded

---

*Copyright © Anthropic. All rights reserved.*
