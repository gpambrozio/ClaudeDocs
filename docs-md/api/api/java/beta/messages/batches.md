# Batches

Copy page

Java

# Batches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

[BetaMessageBatch](api/beta.md) beta().messages().batches().create(BatchCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

[BetaMessageBatch](api/beta.md) beta().messages().batches().retrieve(BatchRetrieveParamsparams = BatchRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

BatchListPage beta().messages().batches().list(BatchListParamsparams = BatchListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

[BetaMessageBatch](api/beta.md) beta().messages().batches().cancel(BatchCancelParamsparams = BatchCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

[BetaDeletedMessageBatch](api/beta.md) beta().messages().batches().delete(BatchDeleteParamsparams = BatchDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

[BetaMessageBatchIndividualResponse](api/beta.md) beta().messages().batches().resultsStreaming(BatchResultsParamsparams = BatchResultsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

class BetaDeletedMessageBatch:

String id

ID of the Message Batch.

JsonValue; type "message\_batch\_deleted"constant"message\_batch\_deleted"constant

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

class BetaMessageBatch:

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional<LocalDateTime> archivedAt

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

Optional<LocalDateTime> cancelInitiatedAt

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

LocalDateTime createdAt

RFC 3339 datetime string representing the time at which the Message Batch was created.

Optional<LocalDateTime> endedAt

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

LocalDateTime expiresAt

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

ProcessingStatus processingStatus

Processing status of the Message Batch.

Accepts one of the following:

IN\_PROGRESS("in\_progress")

CANCELING("canceling")

ENDED("ended")

[BetaMessageBatchRequestCounts](api/beta.md) requestCounts

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

long canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

long errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

long expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

long processing

Number of requests in the Message Batch that are processing.

long succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

Optional<String> resultsUrl

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

JsonValue; type "message\_batch"constant"message\_batch"constant

Object type.

For Message Batches, this is always `"message_batch"`.

class BetaMessageBatchCanceledResult:

JsonValue; type "canceled"constant"canceled"constant

class BetaMessageBatchErroredResult:

[BetaErrorResponse](api/beta.md) error

[BetaError](api/beta.md) error

Accepts one of the following:

class BetaInvalidRequestError:

String message

JsonValue; type "invalid\_request\_error"constant"invalid\_request\_error"constant

class BetaAuthenticationError:

String message

JsonValue; type "authentication\_error"constant"authentication\_error"constant

class BetaBillingError:

String message

JsonValue; type "billing\_error"constant"billing\_error"constant

class BetaPermissionError:

String message

JsonValue; type "permission\_error"constant"permission\_error"constant

class BetaNotFoundError:

String message

JsonValue; type "not\_found\_error"constant"not\_found\_error"constant

class BetaRateLimitError:

String message

JsonValue; type "rate\_limit\_error"constant"rate\_limit\_error"constant

class BetaGatewayTimeoutError:

String message

JsonValue; type "timeout\_error"constant"timeout\_error"constant

class BetaApiError:

String message

JsonValue; type "api\_error"constant"api\_error"constant

class BetaOverloadedError:

String message

JsonValue; type "overloaded\_error"constant"overloaded\_error"constant

Optional<String> requestId

JsonValue; type "error"constant"error"constant

JsonValue; type "errored"constant"errored"constant

class BetaMessageBatchExpiredResult:

JsonValue; type "expired"constant"expired"constant

class BetaMessageBatchIndividualResponse:

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

String customId

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

[BetaMessageBatchResult](api/beta.md) result

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class BetaMessageBatchSucceededResult:

[BetaMessage](api/beta.md) message

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional<[BetaContainer](api/beta.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

Optional<List<[BetaSkill](api/beta.md)>> skills

Skills loaded in the container

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

List<[BetaContentBlock](api/beta.md)> content

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

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolUseBlock:

String id

Input input

Name name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaWebSearchToolResultBlock:

[BetaWebSearchToolResultBlockContent](api/beta.md) content

Accepts one of the following:

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

List<[BetaWebSearchResultBlock](api/beta.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

class BetaWebFetchToolResultBlock:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

[BetaDocumentBlock](api/beta.md) content

Optional<[BetaCitationConfig](api/beta.md)> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](api/beta.md) content

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

List<[BetaBashCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

Content content

Accepts one of the following:

class BetaToolSearchToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

List<[BetaToolReferenceBlock](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

Content content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

JsonValue; type "compaction"constant"compaction"constant

Optional<[BetaContextManagementResponse](api/beta.md)> contextManagement

Context management response.

Information about context management strategies applied during the request.

List<AppliedEdit> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

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

JsonValue; role "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Optional<[BetaStopReason](api/beta.md)> stopReason

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

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

Optional<String> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

[BetaUsage](api/beta.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional<Long> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The number of input tokens read from the cache.

Optional<String> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration

long outputTokens

The number of output tokens which were used.

Optional<[BetaServerToolUsage](api/beta.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

Optional<ServiceTier> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

Optional<Speed> speed

The inference speed mode used for this request.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

JsonValue; type "succeeded"constant"succeeded"constant

class BetaMessageBatchErroredResult:

[BetaErrorResponse](api/beta.md) error

[BetaError](api/beta.md) error

Accepts one of the following:

class BetaInvalidRequestError:

String message

JsonValue; type "invalid\_request\_error"constant"invalid\_request\_error"constant

class BetaAuthenticationError:

String message

JsonValue; type "authentication\_error"constant"authentication\_error"constant

class BetaBillingError:

String message

JsonValue; type "billing\_error"constant"billing\_error"constant

class BetaPermissionError:

String message

JsonValue; type "permission\_error"constant"permission\_error"constant

class BetaNotFoundError:

String message

JsonValue; type "not\_found\_error"constant"not\_found\_error"constant

class BetaRateLimitError:

String message

JsonValue; type "rate\_limit\_error"constant"rate\_limit\_error"constant

class BetaGatewayTimeoutError:

String message

JsonValue; type "timeout\_error"constant"timeout\_error"constant

class BetaApiError:

String message

JsonValue; type "api\_error"constant"api\_error"constant

class BetaOverloadedError:

String message

JsonValue; type "overloaded\_error"constant"overloaded\_error"constant

Optional<String> requestId

JsonValue; type "error"constant"error"constant

JsonValue; type "errored"constant"errored"constant

class BetaMessageBatchCanceledResult:

JsonValue; type "canceled"constant"canceled"constant

class BetaMessageBatchExpiredResult:

JsonValue; type "expired"constant"expired"constant

class BetaMessageBatchRequestCounts:

long canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

long errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

long expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

long processing

Number of requests in the Message Batch that are processing.

long succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

class BetaMessageBatchResult: A class that can be one of several variants.union

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

class BetaMessageBatchSucceededResult:

[BetaMessage](api/beta.md) message

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional<[BetaContainer](api/beta.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

Optional<List<[BetaSkill](api/beta.md)>> skills

Skills loaded in the container

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

List<[BetaContentBlock](api/beta.md)> content

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

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolUseBlock:

String id

Input input

Name name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaWebSearchToolResultBlock:

[BetaWebSearchToolResultBlockContent](api/beta.md) content

Accepts one of the following:

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

List<[BetaWebSearchResultBlock](api/beta.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

class BetaWebFetchToolResultBlock:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

[BetaDocumentBlock](api/beta.md) content

Optional<[BetaCitationConfig](api/beta.md)> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](api/beta.md) content

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

List<[BetaBashCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

Content content

Accepts one of the following:

class BetaToolSearchToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

List<[BetaToolReferenceBlock](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

Content content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

JsonValue; type "compaction"constant"compaction"constant

Optional<[BetaContextManagementResponse](api/beta.md)> contextManagement

Context management response.

Information about context management strategies applied during the request.

List<AppliedEdit> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

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

JsonValue; role "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Optional<[BetaStopReason](api/beta.md)> stopReason

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

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

Optional<String> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

[BetaUsage](api/beta.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional<Long> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The number of input tokens read from the cache.

Optional<String> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration

long outputTokens

The number of output tokens which were used.

Optional<[BetaServerToolUsage](api/beta.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

Optional<ServiceTier> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

Optional<Speed> speed

The inference speed mode used for this request.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

JsonValue; type "succeeded"constant"succeeded"constant

class BetaMessageBatchErroredResult:

[BetaErrorResponse](api/beta.md) error

[BetaError](api/beta.md) error

Accepts one of the following:

class BetaInvalidRequestError:

String message

JsonValue; type "invalid\_request\_error"constant"invalid\_request\_error"constant

class BetaAuthenticationError:

String message

JsonValue; type "authentication\_error"constant"authentication\_error"constant

class BetaBillingError:

String message

JsonValue; type "billing\_error"constant"billing\_error"constant

class BetaPermissionError:

String message

JsonValue; type "permission\_error"constant"permission\_error"constant

class BetaNotFoundError:

String message

JsonValue; type "not\_found\_error"constant"not\_found\_error"constant

class BetaRateLimitError:

String message

JsonValue; type "rate\_limit\_error"constant"rate\_limit\_error"constant

class BetaGatewayTimeoutError:

String message

JsonValue; type "timeout\_error"constant"timeout\_error"constant

class BetaApiError:

String message

JsonValue; type "api\_error"constant"api\_error"constant

class BetaOverloadedError:

String message

JsonValue; type "overloaded\_error"constant"overloaded\_error"constant

Optional<String> requestId

JsonValue; type "error"constant"error"constant

JsonValue; type "errored"constant"errored"constant

class BetaMessageBatchCanceledResult:

JsonValue; type "canceled"constant"canceled"constant

class BetaMessageBatchExpiredResult:

JsonValue; type "expired"constant"expired"constant

class BetaMessageBatchSucceededResult:

[BetaMessage](api/beta.md) message

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional<[BetaContainer](api/beta.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

Optional<List<[BetaSkill](api/beta.md)>> skills

Skills loaded in the container

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

List<[BetaContentBlock](api/beta.md)> content

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

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolUseBlock:

String id

Input input

Name name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaWebSearchToolResultBlock:

[BetaWebSearchToolResultBlockContent](api/beta.md) content

Accepts one of the following:

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

List<[BetaWebSearchResultBlock](api/beta.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

class BetaWebFetchToolResultBlock:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

[BetaDocumentBlock](api/beta.md) content

Optional<[BetaCitationConfig](api/beta.md)> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](api/beta.md) content

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

List<[BetaBashCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

Content content

Accepts one of the following:

class BetaToolSearchToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

List<[BetaToolReferenceBlock](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

Content content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

JsonValue; type "compaction"constant"compaction"constant

Optional<[BetaContextManagementResponse](api/beta.md)> contextManagement

Context management response.

Information about context management strategies applied during the request.

List<AppliedEdit> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

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

JsonValue; role "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Optional<[BetaStopReason](api/beta.md)> stopReason

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

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

Optional<String> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

[BetaUsage](api/beta.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional<Long> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The number of input tokens read from the cache.

Optional<String> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration

long outputTokens

The number of output tokens which were used.

Optional<[BetaServerToolUsage](api/beta.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

Optional<ServiceTier> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

Optional<Speed> speed

The inference speed mode used for this request.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

JsonValue; type "succeeded"constant"succeeded"constant

---

*Copyright © Anthropic. All rights reserved.*
