# Batches

Copy page



Java

# Batches

##### [Create a Message Batch](api/messages/batches/create.md)

[MessageBatch](api/messages/batches.md) messages().batches().create(BatchCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/messages/batches/retrieve.md)

[MessageBatch](api/messages/batches.md) messages().batches().retrieve(BatchRetrieveParamsparams = BatchRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/messages/batches/list.md)

BatchListPage messages().batches().list(BatchListParamsparams = BatchListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches

##### [Cancel a Message Batch](api/messages/batches/cancel.md)

[MessageBatch](api/messages/batches.md) messages().batches().cancel(BatchCancelParamsparams = BatchCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/messages/batches/delete.md)

[DeletedMessageBatch](api/messages/batches.md) messages().batches().delete(BatchDeleteParamsparams = BatchDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/messages/batches/results.md)

[MessageBatchIndividualResponse](api/messages/batches.md) messages().batches().resultsStreaming(BatchResultsParamsparams = BatchResultsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse



class DeletedMessageBatch:

String id

ID of the Message Batch.



JsonValue; type "message\_batch\_deleted"constant"message\_batch\_deleted"constant

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.



class MessageBatch:



String id

Unique object identifier.

The format and length of IDs may change over time.

Optional<LocalDateTime> archivedAt

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

Optional<LocalDateTime> cancelInitiatedAt

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

LocalDateTime createdAt

RFC 3339 datetime string representing the time at which the Message Batch was created.



Optional<LocalDateTime> endedAt

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

LocalDateTime expiresAt

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.



ProcessingStatus processingStatus

Processing status of the Message Batch.

One of the following:

IN\_PROGRESS("in\_progress")

CANCELING("canceling")

ENDED("ended")



[MessageBatchRequestCounts](api/messages/batches.md) requestCounts

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.



long canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



long errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



long expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

long processing

Number of requests in the Message Batch that are processing.



long succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



Optional<String> resultsUrl

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.



JsonValue; type "message\_batch"constant"message\_batch"constant

Object type.

For Message Batches, this is always `"message_batch"`.



class MessageBatchCanceledResult:

JsonValue; type "canceled"constant"canceled"constant



class MessageBatchErroredResult:



[ErrorResponse](api/$shared.md) error



[ErrorObject](api/$shared.md) error

One of the following:



class InvalidRequestError:

String message

JsonValue; type "invalid\_request\_error"constant"invalid\_request\_error"constant



class AuthenticationError:

String message

JsonValue; type "authentication\_error"constant"authentication\_error"constant



class BillingError:

String message

JsonValue; type "billing\_error"constant"billing\_error"constant



class PermissionError:

String message

JsonValue; type "permission\_error"constant"permission\_error"constant



class NotFoundError:

String message

JsonValue; type "not\_found\_error"constant"not\_found\_error"constant



class RateLimitError:

String message

JsonValue; type "rate\_limit\_error"constant"rate\_limit\_error"constant



class GatewayTimeoutError:

String message

JsonValue; type "timeout\_error"constant"timeout\_error"constant



class ApiErrorObject:

String message

JsonValue; type "api\_error"constant"api\_error"constant



class OverloadedError:

String message

JsonValue; type "overloaded\_error"constant"overloaded\_error"constant

Optional<String> requestId

JsonValue; type "error"constant"error"constant

JsonValue; type "errored"constant"errored"constant



class MessageBatchExpiredResult:

JsonValue; type "expired"constant"expired"constant



class MessageBatchIndividualResponse:

This is a single line in the response `.jsonl` file and does not represent the response as a whole.



String customId

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.



[MessageBatchResult](api/messages/batches.md) result

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



class MessageBatchSucceededResult:



[Message](api/messages.md) message



String id

Unique object identifier.

The format and length of IDs may change over time.



Optional<[Container](api/messages.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.



List<[ContentBlock](api/messages.md)> content

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

Optional<List<[TextCitation](api/messages.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class CitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class CitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class CitationContentBlockLocation:

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

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class CitationsSearchResultLocation:

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

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant



class RedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant



class ToolUseBlock:

String id



Caller caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class ServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant



class ServerToolUseBlock:

String id



Caller caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class ServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

Input input



Name name

One of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant



class WebSearchToolResultBlock:



Caller caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class ServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



[WebSearchToolResultBlockContent](api/messages.md) content

One of the following:



class WebSearchToolResultError:



[WebSearchToolResultErrorCode](api/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant



List<[WebSearchResultBlock](api/messages.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant



class WebFetchToolResultBlock:



Caller caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class ServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



Content content

One of the following:



class WebFetchToolResultErrorBlock:



[WebFetchToolResultErrorCode](api/messages.md) errorCode

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

class WebFetchBlock:



[DocumentBlock](api/messages.md) content



Optional<[CitationsConfig](api/messages.md)> citations

Citation configuration for the document

boolean enabled



Source source

One of the following:



class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class PlainTextSource:

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

class CodeExecutionToolResultBlock:



[CodeExecutionToolResultBlockContent](api/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultError:



[CodeExecutionToolResultErrorCode](api/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



class CodeExecutionResultBlock:



List<[CodeExecutionOutputBlock](api/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[CodeExecutionOutputBlock](api/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant



class BashCodeExecutionToolResultBlock:



Content content

One of the following:



class BashCodeExecutionToolResultError:



[BashCodeExecutionToolResultErrorCode](api/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant



class BashCodeExecutionResultBlock:



List<[BashCodeExecutionOutputBlock](api/messages.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant



class TextEditorCodeExecutionToolResultBlock:



Content content

One of the following:



class TextEditorCodeExecutionToolResultError:



[TextEditorCodeExecutionToolResultErrorCode](api/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant



class TextEditorCodeExecutionViewResultBlock:

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

class TextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant



class TextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant



class ToolSearchToolResultBlock:



Content content

One of the following:



class ToolSearchToolResultError:



[ToolSearchToolResultErrorCode](api/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant



class ToolSearchToolSearchResultBlock:



List<[ToolReferenceBlock](api/messages.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant



class ContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

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

Optional<[RefusalStopDetails](api/messages.md)> stopDetails

Structured information about a refusal.



Optional<Category> category

The policy category that triggered a refusal.

One of the following:

CYBER("cyber")

BIO("bio")

FRONTIER\_LLM("frontier\_llm")

REASONING\_EXTRACTION("reasoning\_extraction")

MILITARY\_WEAPONS("military\_weapons")



Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonValue; type "refusal"constant"refusal"constant



Optional<[StopReason](api/messages.md)> stopReason

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

REFUSAL("refusal")



Optional<String> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.



[Usage](api/messages.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



Optional<[CacheCreation](api/messages.md)> cacheCreation

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

long outputTokens

The number of output tokens which were used.



Optional<[OutputTokensDetails](api/messages.md)> outputTokensDetails

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

Optional<[ServerToolUsage](api/messages.md)> serverToolUse

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

JsonValue; type "succeeded"constant"succeeded"constant



class MessageBatchErroredResult:



[ErrorResponse](api/$shared.md) error



[ErrorObject](api/$shared.md) error

One of the following:



class InvalidRequestError:

String message

JsonValue; type "invalid\_request\_error"constant"invalid\_request\_error"constant



class AuthenticationError:

String message

JsonValue; type "authentication\_error"constant"authentication\_error"constant



class BillingError:

String message

JsonValue; type "billing\_error"constant"billing\_error"constant



class PermissionError:

String message

JsonValue; type "permission\_error"constant"permission\_error"constant



class NotFoundError:

String message

JsonValue; type "not\_found\_error"constant"not\_found\_error"constant



class RateLimitError:

String message

JsonValue; type "rate\_limit\_error"constant"rate\_limit\_error"constant



class GatewayTimeoutError:

String message

JsonValue; type "timeout\_error"constant"timeout\_error"constant



class ApiErrorObject:

String message

JsonValue; type "api\_error"constant"api\_error"constant



class OverloadedError:

String message

JsonValue; type "overloaded\_error"constant"overloaded\_error"constant

Optional<String> requestId

JsonValue; type "error"constant"error"constant

JsonValue; type "errored"constant"errored"constant



class MessageBatchCanceledResult:

JsonValue; type "canceled"constant"canceled"constant



class MessageBatchExpiredResult:

JsonValue; type "expired"constant"expired"constant



class MessageBatchRequestCounts:



long canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



long errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



long expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

long processing

Number of requests in the Message Batch that are processing.



long succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



class MessageBatchResult: A class that can be one of several variants.union 

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.



class MessageBatchSucceededResult:



[Message](api/messages.md) message



String id

Unique object identifier.

The format and length of IDs may change over time.



Optional<[Container](api/messages.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.



List<[ContentBlock](api/messages.md)> content

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

Optional<List<[TextCitation](api/messages.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class CitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class CitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class CitationContentBlockLocation:

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

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class CitationsSearchResultLocation:

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

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant



class RedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant



class ToolUseBlock:

String id



Caller caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class ServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant



class ServerToolUseBlock:

String id



Caller caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class ServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

Input input



Name name

One of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant



class WebSearchToolResultBlock:



Caller caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class ServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



[WebSearchToolResultBlockContent](api/messages.md) content

One of the following:



class WebSearchToolResultError:



[WebSearchToolResultErrorCode](api/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant



List<[WebSearchResultBlock](api/messages.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant



class WebFetchToolResultBlock:



Caller caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class ServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



Content content

One of the following:



class WebFetchToolResultErrorBlock:



[WebFetchToolResultErrorCode](api/messages.md) errorCode

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

class WebFetchBlock:



[DocumentBlock](api/messages.md) content



Optional<[CitationsConfig](api/messages.md)> citations

Citation configuration for the document

boolean enabled



Source source

One of the following:



class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class PlainTextSource:

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

class CodeExecutionToolResultBlock:



[CodeExecutionToolResultBlockContent](api/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultError:



[CodeExecutionToolResultErrorCode](api/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



class CodeExecutionResultBlock:



List<[CodeExecutionOutputBlock](api/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[CodeExecutionOutputBlock](api/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant



class BashCodeExecutionToolResultBlock:



Content content

One of the following:



class BashCodeExecutionToolResultError:



[BashCodeExecutionToolResultErrorCode](api/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant



class BashCodeExecutionResultBlock:



List<[BashCodeExecutionOutputBlock](api/messages.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant



class TextEditorCodeExecutionToolResultBlock:



Content content

One of the following:



class TextEditorCodeExecutionToolResultError:



[TextEditorCodeExecutionToolResultErrorCode](api/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant



class TextEditorCodeExecutionViewResultBlock:

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

class TextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant



class TextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant



class ToolSearchToolResultBlock:



Content content

One of the following:



class ToolSearchToolResultError:



[ToolSearchToolResultErrorCode](api/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant



class ToolSearchToolSearchResultBlock:



List<[ToolReferenceBlock](api/messages.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant



class ContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

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

Optional<[RefusalStopDetails](api/messages.md)> stopDetails

Structured information about a refusal.



Optional<Category> category

The policy category that triggered a refusal.

One of the following:

CYBER("cyber")

BIO("bio")

FRONTIER\_LLM("frontier\_llm")

REASONING\_EXTRACTION("reasoning\_extraction")

MILITARY\_WEAPONS("military\_weapons")



Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonValue; type "refusal"constant"refusal"constant



Optional<[StopReason](api/messages.md)> stopReason

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

REFUSAL("refusal")



Optional<String> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.



[Usage](api/messages.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



Optional<[CacheCreation](api/messages.md)> cacheCreation

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

long outputTokens

The number of output tokens which were used.



Optional<[OutputTokensDetails](api/messages.md)> outputTokensDetails

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

Optional<[ServerToolUsage](api/messages.md)> serverToolUse

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

JsonValue; type "succeeded"constant"succeeded"constant



class MessageBatchErroredResult:



[ErrorResponse](api/$shared.md) error



[ErrorObject](api/$shared.md) error

One of the following:



class InvalidRequestError:

String message

JsonValue; type "invalid\_request\_error"constant"invalid\_request\_error"constant



class AuthenticationError:

String message

JsonValue; type "authentication\_error"constant"authentication\_error"constant



class BillingError:

String message

JsonValue; type "billing\_error"constant"billing\_error"constant



class PermissionError:

String message

JsonValue; type "permission\_error"constant"permission\_error"constant



class NotFoundError:

String message

JsonValue; type "not\_found\_error"constant"not\_found\_error"constant



class RateLimitError:

String message

JsonValue; type "rate\_limit\_error"constant"rate\_limit\_error"constant



class GatewayTimeoutError:

String message

JsonValue; type "timeout\_error"constant"timeout\_error"constant



class ApiErrorObject:

String message

JsonValue; type "api\_error"constant"api\_error"constant



class OverloadedError:

String message

JsonValue; type "overloaded\_error"constant"overloaded\_error"constant

Optional<String> requestId

JsonValue; type "error"constant"error"constant

JsonValue; type "errored"constant"errored"constant



class MessageBatchCanceledResult:

JsonValue; type "canceled"constant"canceled"constant



class MessageBatchExpiredResult:

JsonValue; type "expired"constant"expired"constant



class MessageBatchSucceededResult:



[Message](api/messages.md) message



String id

Unique object identifier.

The format and length of IDs may change over time.



Optional<[Container](api/messages.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.



List<[ContentBlock](api/messages.md)> content

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

Optional<List<[TextCitation](api/messages.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class CitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class CitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class CitationContentBlockLocation:

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

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class CitationsSearchResultLocation:

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

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant



class RedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant



class ToolUseBlock:

String id



Caller caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class ServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant



class ServerToolUseBlock:

String id



Caller caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class ServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

Input input



Name name

One of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant



class WebSearchToolResultBlock:



Caller caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class ServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



[WebSearchToolResultBlockContent](api/messages.md) content

One of the following:



class WebSearchToolResultError:



[WebSearchToolResultErrorCode](api/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant



List<[WebSearchResultBlock](api/messages.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant



class WebFetchToolResultBlock:



Caller caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class ServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



Content content

One of the following:



class WebFetchToolResultErrorBlock:



[WebFetchToolResultErrorCode](api/messages.md) errorCode

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

class WebFetchBlock:



[DocumentBlock](api/messages.md) content



Optional<[CitationsConfig](api/messages.md)> citations

Citation configuration for the document

boolean enabled



Source source

One of the following:



class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class PlainTextSource:

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

class CodeExecutionToolResultBlock:



[CodeExecutionToolResultBlockContent](api/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultError:



[CodeExecutionToolResultErrorCode](api/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



class CodeExecutionResultBlock:



List<[CodeExecutionOutputBlock](api/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[CodeExecutionOutputBlock](api/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant



class BashCodeExecutionToolResultBlock:



Content content

One of the following:



class BashCodeExecutionToolResultError:



[BashCodeExecutionToolResultErrorCode](api/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant



class BashCodeExecutionResultBlock:



List<[BashCodeExecutionOutputBlock](api/messages.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant



class TextEditorCodeExecutionToolResultBlock:



Content content

One of the following:



class TextEditorCodeExecutionToolResultError:



[TextEditorCodeExecutionToolResultErrorCode](api/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant



class TextEditorCodeExecutionViewResultBlock:

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

class TextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant



class TextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant



class ToolSearchToolResultBlock:



Content content

One of the following:



class ToolSearchToolResultError:



[ToolSearchToolResultErrorCode](api/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant



class ToolSearchToolSearchResultBlock:



List<[ToolReferenceBlock](api/messages.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant



class ContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

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

Optional<[RefusalStopDetails](api/messages.md)> stopDetails

Structured information about a refusal.



Optional<Category> category

The policy category that triggered a refusal.

One of the following:

CYBER("cyber")

BIO("bio")

FRONTIER\_LLM("frontier\_llm")

REASONING\_EXTRACTION("reasoning\_extraction")

MILITARY\_WEAPONS("military\_weapons")



Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonValue; type "refusal"constant"refusal"constant



Optional<[StopReason](api/messages.md)> stopReason

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

REFUSAL("refusal")



Optional<String> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.



[Usage](api/messages.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



Optional<[CacheCreation](api/messages.md)> cacheCreation

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

long outputTokens

The number of output tokens which were used.



Optional<[OutputTokensDetails](api/messages.md)> outputTokensDetails

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

Optional<[ServerToolUsage](api/messages.md)> serverToolUse

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

JsonValue; type "succeeded"constant"succeeded"constant

---

*Copyright © Anthropic. All rights reserved.*
