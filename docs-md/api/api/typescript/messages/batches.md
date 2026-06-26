# Batches

Copy page



TypeScript

# Batches

##### [Create a Message Batch](api/messages/batches/create.md)

client.messages.batches.create(BatchCreateParams { requests } body, RequestOptionsoptions?): [MessageBatch](api/messages.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/messages/batches/retrieve.md)

client.messages.batches.retrieve(stringmessageBatchID, RequestOptionsoptions?): [MessageBatch](api/messages.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/messages/batches/list.md)

client.messages.batches.list(BatchListParams { after\_id, before\_id, limit } query?, RequestOptionsoptions?): Page<[MessageBatch](api/messages.md) { id, archived\_at, cancel\_initiated\_at, 7 more } >

GET/v1/messages/batches

##### [Cancel a Message Batch](api/messages/batches/cancel.md)

client.messages.batches.cancel(stringmessageBatchID, RequestOptionsoptions?): [MessageBatch](api/messages.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/messages/batches/delete.md)

client.messages.batches.delete(stringmessageBatchID, RequestOptionsoptions?): [DeletedMessageBatch](api/messages.md) { id, type }

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/messages/batches/results.md)

client.messages.batches.results(stringmessageBatchID, RequestOptionsoptions?): [MessageBatchIndividualResponse](api/messages.md) { custom\_id, result }  | Stream<[MessageBatchIndividualResponse](api/messages.md) { custom\_id, result } >

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse



DeletedMessageBatch { id, type } 

id: string

ID of the Message Batch.



type: "message\_batch\_deleted"

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.



MessageBatch { id, archived\_at, cancel\_initiated\_at, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.

archived\_at: string | null

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

cancel\_initiated\_at: string | null

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

created\_at: string

RFC 3339 datetime string representing the time at which the Message Batch was created.



ended\_at: string | null

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires\_at: string

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.



processing\_status: "in\_progress" | "canceling" | "ended"

Processing status of the Message Batch.

One of the following:

"in\_progress"

"canceling"

"ended"



request\_counts: [MessageBatchRequestCounts](api/messages.md) { canceled, errored, expired, 2 more } 

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.



canceled: number

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



errored: number

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



expired: number

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: number

Number of requests in the Message Batch that are processing.



succeeded: number

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



results\_url: string | null

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.



type: "message\_batch"

Object type.

For Message Batches, this is always `"message_batch"`.



MessageBatchCanceledResult { type } 

type: "canceled"



MessageBatchErroredResult { error, type } 



error: [ErrorResponse](api/$shared.md) { error, request\_id, type } 



error: [ErrorObject](api/$shared.md)

One of the following:



InvalidRequestError { message, type } 

message: string

type: "invalid\_request\_error"



AuthenticationError { message, type } 

message: string

type: "authentication\_error"



BillingError { message, type } 

message: string

type: "billing\_error"



PermissionError { message, type } 

message: string

type: "permission\_error"



NotFoundError { message, type } 

message: string

type: "not\_found\_error"



RateLimitError { message, type } 

message: string

type: "rate\_limit\_error"



GatewayTimeoutError { message, type } 

message: string

type: "timeout\_error"



APIErrorObject { message, type } 

message: string

type: "api\_error"



OverloadedError { message, type } 

message: string

type: "overloaded\_error"

request\_id: string | null

type: "error"

type: "errored"



MessageBatchExpiredResult { type } 

type: "expired"



MessageBatchIndividualResponse { custom\_id, result } 

This is a single line in the response `.jsonl` file and does not represent the response as a whole.



custom\_id: string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.



result: [MessageBatchResult](api/messages.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



MessageBatchSucceededResult { message, type } 



message: [Message](api/messages.md) { id, container, content, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: [Container](api/messages.md) { id, expires\_at }  | null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



content: Array<[ContentBlock](api/messages.md)>

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

TextBlock { citations, text, type } 



citations: Array<[TextCitation](api/messages.md)> | null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

file\_id: string | null

start\_char\_index: number

type: "char\_location"



CitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

file\_id: string | null

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string | null

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"

text: string

type: "text"



ThinkingBlock { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



RedactedThinkingBlock { data, type } 

data: string

type: "redacted\_thinking"



ToolUseBlock { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: Record<string, unknown>

name: string

type: "tool\_use"



ServerToolUseBlock { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: Record<string, unknown>



name: "web\_search" | "web\_fetch" | "code\_execution" | 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



WebSearchToolResultBlock { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



WebSearchToolResultError { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



Array<[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } >

encrypted\_content: string

page\_age: string | null

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



WebFetchToolResultBlock { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  | [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



WebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



WebFetchBlock { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled }  | null

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string | null

The title of the document

type: "document"

retrieved\_at: string | null

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



CodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultError { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array<[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } >

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array<[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } >

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  | [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultError { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array<[BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } >

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



TextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  | [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  | [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  | [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string | null

type: "text\_editor\_code\_execution\_tool\_result\_error"



TextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" | "image" | "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number | null

start\_line: number | null

total\_lines: number | null

type: "text\_editor\_code\_execution\_view\_result"



TextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array<string> | null

new\_lines: number | null

new\_start: number | null

old\_lines: number | null

old\_start: number | null

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



ToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  | [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string | null

type: "tool\_search\_tool\_result\_error"



ToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array<[ToolReferenceBlock](api/messages.md) { tool\_name, type } >

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



ContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-fable-5" | "claude-mythos-5" | "claude-opus-4-8" | 12 more

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type }  | null

Structured information about a refusal.



category: "cyber" | "bio" | "frontier\_llm" | "reasoning\_extraction" | null

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string | null

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



stop\_reason: [StopReason](api/messages.md) | null

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

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"



stop\_sequence: string | null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 6 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number | null

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number | null

The number of input tokens read from the cache.

inference\_geo: string | null

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens }  | null

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests }  | null

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" | "priority" | "batch" | null

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"

type: "succeeded"



MessageBatchErroredResult { error, type } 



error: [ErrorResponse](api/$shared.md) { error, request\_id, type } 



error: [ErrorObject](api/$shared.md)

One of the following:



InvalidRequestError { message, type } 

message: string

type: "invalid\_request\_error"



AuthenticationError { message, type } 

message: string

type: "authentication\_error"



BillingError { message, type } 

message: string

type: "billing\_error"



PermissionError { message, type } 

message: string

type: "permission\_error"



NotFoundError { message, type } 

message: string

type: "not\_found\_error"



RateLimitError { message, type } 

message: string

type: "rate\_limit\_error"



GatewayTimeoutError { message, type } 

message: string

type: "timeout\_error"



APIErrorObject { message, type } 

message: string

type: "api\_error"



OverloadedError { message, type } 

message: string

type: "overloaded\_error"

request\_id: string | null

type: "error"

type: "errored"



MessageBatchCanceledResult { type } 

type: "canceled"



MessageBatchExpiredResult { type } 

type: "expired"



MessageBatchRequestCounts { canceled, errored, expired, 2 more } 



canceled: number

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



errored: number

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



expired: number

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: number

Number of requests in the Message Batch that are processing.



succeeded: number

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



MessageBatchResult = [MessageBatchSucceededResult](api/messages.md) { message, type }  | [MessageBatchErroredResult](api/messages.md) { error, type }  | [MessageBatchCanceledResult](api/messages.md) { type }  | [MessageBatchExpiredResult](api/messages.md) { type } 

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



MessageBatchSucceededResult { message, type } 



message: [Message](api/messages.md) { id, container, content, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: [Container](api/messages.md) { id, expires\_at }  | null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



content: Array<[ContentBlock](api/messages.md)>

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

TextBlock { citations, text, type } 



citations: Array<[TextCitation](api/messages.md)> | null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

file\_id: string | null

start\_char\_index: number

type: "char\_location"



CitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

file\_id: string | null

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string | null

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"

text: string

type: "text"



ThinkingBlock { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



RedactedThinkingBlock { data, type } 

data: string

type: "redacted\_thinking"



ToolUseBlock { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: Record<string, unknown>

name: string

type: "tool\_use"



ServerToolUseBlock { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: Record<string, unknown>



name: "web\_search" | "web\_fetch" | "code\_execution" | 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



WebSearchToolResultBlock { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



WebSearchToolResultError { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



Array<[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } >

encrypted\_content: string

page\_age: string | null

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



WebFetchToolResultBlock { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  | [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



WebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



WebFetchBlock { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled }  | null

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string | null

The title of the document

type: "document"

retrieved\_at: string | null

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



CodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultError { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array<[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } >

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array<[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } >

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  | [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultError { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array<[BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } >

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



TextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  | [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  | [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  | [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string | null

type: "text\_editor\_code\_execution\_tool\_result\_error"



TextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" | "image" | "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number | null

start\_line: number | null

total\_lines: number | null

type: "text\_editor\_code\_execution\_view\_result"



TextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array<string> | null

new\_lines: number | null

new\_start: number | null

old\_lines: number | null

old\_start: number | null

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



ToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  | [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string | null

type: "tool\_search\_tool\_result\_error"



ToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array<[ToolReferenceBlock](api/messages.md) { tool\_name, type } >

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



ContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-fable-5" | "claude-mythos-5" | "claude-opus-4-8" | 12 more

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type }  | null

Structured information about a refusal.



category: "cyber" | "bio" | "frontier\_llm" | "reasoning\_extraction" | null

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string | null

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



stop\_reason: [StopReason](api/messages.md) | null

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

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"



stop\_sequence: string | null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 6 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number | null

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number | null

The number of input tokens read from the cache.

inference\_geo: string | null

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens }  | null

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests }  | null

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" | "priority" | "batch" | null

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"

type: "succeeded"



MessageBatchErroredResult { error, type } 



error: [ErrorResponse](api/$shared.md) { error, request\_id, type } 



error: [ErrorObject](api/$shared.md)

One of the following:



InvalidRequestError { message, type } 

message: string

type: "invalid\_request\_error"



AuthenticationError { message, type } 

message: string

type: "authentication\_error"



BillingError { message, type } 

message: string

type: "billing\_error"



PermissionError { message, type } 

message: string

type: "permission\_error"



NotFoundError { message, type } 

message: string

type: "not\_found\_error"



RateLimitError { message, type } 

message: string

type: "rate\_limit\_error"



GatewayTimeoutError { message, type } 

message: string

type: "timeout\_error"



APIErrorObject { message, type } 

message: string

type: "api\_error"



OverloadedError { message, type } 

message: string

type: "overloaded\_error"

request\_id: string | null

type: "error"

type: "errored"



MessageBatchCanceledResult { type } 

type: "canceled"



MessageBatchExpiredResult { type } 

type: "expired"



MessageBatchSucceededResult { message, type } 



message: [Message](api/messages.md) { id, container, content, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: [Container](api/messages.md) { id, expires\_at }  | null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



content: Array<[ContentBlock](api/messages.md)>

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

TextBlock { citations, text, type } 



citations: Array<[TextCitation](api/messages.md)> | null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

file\_id: string | null

start\_char\_index: number

type: "char\_location"



CitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

file\_id: string | null

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string | null



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string | null

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string | null

type: "search\_result\_location"

text: string

type: "text"



ThinkingBlock { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



RedactedThinkingBlock { data, type } 

data: string

type: "redacted\_thinking"



ToolUseBlock { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: Record<string, unknown>

name: string

type: "tool\_use"



ServerToolUseBlock { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: Record<string, unknown>



name: "web\_search" | "web\_fetch" | "code\_execution" | 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



WebSearchToolResultBlock { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



WebSearchToolResultError { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



Array<[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } >

encrypted\_content: string

page\_age: string | null

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



WebFetchToolResultBlock { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  | [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



WebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



WebFetchBlock { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled }  | null

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string | null

The title of the document

type: "document"

retrieved\_at: string | null

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



CodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultError { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array<[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } >

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array<[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } >

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  | [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultError { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array<[BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } >

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



TextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  | [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  | [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  | [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string | null

type: "text\_editor\_code\_execution\_tool\_result\_error"



TextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" | "image" | "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number | null

start\_line: number | null

total\_lines: number | null

type: "text\_editor\_code\_execution\_view\_result"



TextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array<string> | null

new\_lines: number | null

new\_start: number | null

old\_lines: number | null

old\_start: number | null

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



ToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  | [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string | null

type: "tool\_search\_tool\_result\_error"



ToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array<[ToolReferenceBlock](api/messages.md) { tool\_name, type } >

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



ContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-fable-5" | "claude-mythos-5" | "claude-opus-4-8" | 12 more

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type }  | null

Structured information about a refusal.



category: "cyber" | "bio" | "frontier\_llm" | "reasoning\_extraction" | null

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string | null

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



stop\_reason: [StopReason](api/messages.md) | null

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

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"



stop\_sequence: string | null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 6 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number | null

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number | null

The number of input tokens read from the cache.

inference\_geo: string | null

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens }  | null

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests }  | null

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" | "priority" | "batch" | null

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"

type: "succeeded"

---

*Copyright © Anthropic. All rights reserved.*
