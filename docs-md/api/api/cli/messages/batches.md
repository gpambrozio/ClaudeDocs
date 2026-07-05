# Batches

Copy page



CLI

# Batches

##### [Create a Message Batch](api/messages/batches/create.md)

$ ant messages:batches create

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/messages/batches/retrieve.md)

$ ant messages:batches retrieve

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/messages/batches/list.md)

$ ant messages:batches list

GET/v1/messages/batches

##### [Cancel a Message Batch](api/messages/batches/cancel.md)

$ ant messages:batches cancel

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/messages/batches/delete.md)

$ ant messages:batches delete

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/messages/batches/results.md)

$ ant messages:batches results

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse



deleted\_message\_batch: object { id, type } 

id: string

ID of the Message Batch.



type: "message\_batch\_deleted"

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.



message\_batch: object { id, archived\_at, cancel\_initiated\_at, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.

archived\_at: string

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

cancel\_initiated\_at: string

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

created\_at: string

RFC 3339 datetime string representing the time at which the Message Batch was created.



ended\_at: string

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

expires\_at: string

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.



processing\_status: "in\_progress" or "canceling" or "ended"

Processing status of the Message Batch.

"in\_progress"

"canceling"

"ended"



request\_counts: object { canceled, errored, expired, 2 more } 

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

results\_url: string

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.



type: "message\_batch"

Object type.

For Message Batches, this is always `"message_batch"`.



message\_batch\_canceled\_result: object { type } 

type: "canceled"



message\_batch\_errored\_result: object { error, type } 



error: object { error, request\_id, type } 



error: [InvalidRequestError](api/$shared.md) { message, type }  or [AuthenticationError](api/$shared.md) { message, type }  or [BillingError](api/$shared.md) { message, type }  or 6 more



invalid\_request\_error: object { message, type } 

message: string

type: "invalid\_request\_error"



authentication\_error: object { message, type } 

message: string

type: "authentication\_error"



billing\_error: object { message, type } 

message: string

type: "billing\_error"



permission\_error: object { message, type } 

message: string

type: "permission\_error"



not\_found\_error: object { message, type } 

message: string

type: "not\_found\_error"



rate\_limit\_error: object { message, type } 

message: string

type: "rate\_limit\_error"



gateway\_timeout\_error: object { message, type } 

message: string

type: "timeout\_error"



api\_error\_object: object { message, type } 

message: string

type: "api\_error"



overloaded\_error: object { message, type } 

message: string

type: "overloaded\_error"

request\_id: string

type: "error"

type: "errored"



message\_batch\_expired\_result: object { type } 

type: "expired"



message\_batch\_individual\_response: object { custom\_id, result } 

This is a single line in the response `.jsonl` file and does not represent the response as a whole.



custom\_id: string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.



result: [MessageBatchSucceededResult](api/messages/batches.md) { message, type }  or [MessageBatchErroredResult](api/messages/batches.md) { error, type }  or [MessageBatchCanceledResult](api/messages/batches.md) { type }  or [MessageBatchExpiredResult](api/messages/batches.md) { type } 

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.



message\_batch\_succeeded\_result: object { message, type } 



message: object { id, container, content, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: object { id, expires\_at } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



content: array of [ContentBlock](api/messages.md)

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



text\_block: object { citations, text, type } 



citations: array of [TextCitation](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



citations\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



thinking\_block: object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



redacted\_thinking\_block: object { data, type } 

data: string

type: "redacted\_thinking"



tool\_use\_block: object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.



direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"



server\_tool\_use\_block: object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.



direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



web\_search\_tool\_result\_block: object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.



direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultError](api/messages.md) { error\_code, type }  or array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 



web\_search\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



union\_member\_1: array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



web\_fetch\_tool\_result\_block: object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.



direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  or [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 



web\_fetch\_tool\_result\_error\_block: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

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

web\_fetch\_block: object { content, retrieved\_at, type, url } 



content: object { citations, source, title, type } 



citations: object { enabled } 

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 



base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [CodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more }  or [EncryptedCodeExecutionResultBlock](api/messages.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 



bash\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 



text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 



tool\_search\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



tool\_search\_tool\_search\_result\_block: object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlock](api/messages.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



container\_upload\_block: object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



model: "claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 13 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-sonnet-5"

High-performance model for coding and agents

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



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: object { category, explanation, type } 

Structured information about a refusal.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 3 more

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"



stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 6 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: object { thinking\_tokens } 

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



server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"

type: "succeeded"



message\_batch\_errored\_result: object { error, type } 



error: object { error, request\_id, type } 



error: [InvalidRequestError](api/$shared.md) { message, type }  or [AuthenticationError](api/$shared.md) { message, type }  or [BillingError](api/$shared.md) { message, type }  or 6 more



invalid\_request\_error: object { message, type } 

message: string

type: "invalid\_request\_error"



authentication\_error: object { message, type } 

message: string

type: "authentication\_error"



billing\_error: object { message, type } 

message: string

type: "billing\_error"



permission\_error: object { message, type } 

message: string

type: "permission\_error"



not\_found\_error: object { message, type } 

message: string

type: "not\_found\_error"



rate\_limit\_error: object { message, type } 

message: string

type: "rate\_limit\_error"



gateway\_timeout\_error: object { message, type } 

message: string

type: "timeout\_error"



api\_error\_object: object { message, type } 

message: string

type: "api\_error"



overloaded\_error: object { message, type } 

message: string

type: "overloaded\_error"

request\_id: string

type: "error"

type: "errored"



message\_batch\_canceled\_result: object { type } 

type: "canceled"



message\_batch\_expired\_result: object { type } 

type: "expired"



message\_batch\_request\_counts: object { canceled, errored, expired, 2 more } 

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

message\_batch\_result: [MessageBatchSucceededResult](api/messages/batches.md) { message, type }  or [MessageBatchErroredResult](api/messages/batches.md) { error, type }  or [MessageBatchCanceledResult](api/messages/batches.md) { type }  or [MessageBatchExpiredResult](api/messages/batches.md) { type } 

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.



message\_batch\_succeeded\_result: object { message, type } 



message: object { id, container, content, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: object { id, expires\_at } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



content: array of [ContentBlock](api/messages.md)

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



text\_block: object { citations, text, type } 



citations: array of [TextCitation](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



citations\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



thinking\_block: object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



redacted\_thinking\_block: object { data, type } 

data: string

type: "redacted\_thinking"



tool\_use\_block: object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.



direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"



server\_tool\_use\_block: object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.



direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



web\_search\_tool\_result\_block: object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.



direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultError](api/messages.md) { error\_code, type }  or array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 



web\_search\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



union\_member\_1: array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



web\_fetch\_tool\_result\_block: object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.



direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  or [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 



web\_fetch\_tool\_result\_error\_block: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

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

web\_fetch\_block: object { content, retrieved\_at, type, url } 



content: object { citations, source, title, type } 



citations: object { enabled } 

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 



base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [CodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more }  or [EncryptedCodeExecutionResultBlock](api/messages.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 



bash\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 



text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 



tool\_search\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



tool\_search\_tool\_search\_result\_block: object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlock](api/messages.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



container\_upload\_block: object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



model: "claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 13 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-sonnet-5"

High-performance model for coding and agents

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



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: object { category, explanation, type } 

Structured information about a refusal.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 3 more

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"



stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 6 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: object { thinking\_tokens } 

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



server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"

type: "succeeded"



message\_batch\_errored\_result: object { error, type } 



error: object { error, request\_id, type } 



error: [InvalidRequestError](api/$shared.md) { message, type }  or [AuthenticationError](api/$shared.md) { message, type }  or [BillingError](api/$shared.md) { message, type }  or 6 more



invalid\_request\_error: object { message, type } 

message: string

type: "invalid\_request\_error"



authentication\_error: object { message, type } 

message: string

type: "authentication\_error"



billing\_error: object { message, type } 

message: string

type: "billing\_error"



permission\_error: object { message, type } 

message: string

type: "permission\_error"



not\_found\_error: object { message, type } 

message: string

type: "not\_found\_error"



rate\_limit\_error: object { message, type } 

message: string

type: "rate\_limit\_error"



gateway\_timeout\_error: object { message, type } 

message: string

type: "timeout\_error"



api\_error\_object: object { message, type } 

message: string

type: "api\_error"



overloaded\_error: object { message, type } 

message: string

type: "overloaded\_error"

request\_id: string

type: "error"

type: "errored"



message\_batch\_canceled\_result: object { type } 

type: "canceled"



message\_batch\_expired\_result: object { type } 

type: "expired"



message\_batch\_succeeded\_result: object { message, type } 



message: object { id, container, content, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: object { id, expires\_at } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



content: array of [ContentBlock](api/messages.md)

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



text\_block: object { citations, text, type } 



citations: array of [TextCitation](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



citations\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



thinking\_block: object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



redacted\_thinking\_block: object { data, type } 

data: string

type: "redacted\_thinking"



tool\_use\_block: object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.



direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"



server\_tool\_use\_block: object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.



direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



web\_search\_tool\_result\_block: object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.



direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultError](api/messages.md) { error\_code, type }  or array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 



web\_search\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



union\_member\_1: array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



web\_fetch\_tool\_result\_block: object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.



direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  or [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 



web\_fetch\_tool\_result\_error\_block: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

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

web\_fetch\_block: object { content, retrieved\_at, type, url } 



content: object { citations, source, title, type } 



citations: object { enabled } 

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 



base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [CodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more }  or [EncryptedCodeExecutionResultBlock](api/messages.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 



bash\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 



text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 



tool\_search\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



tool\_search\_tool\_search\_result\_block: object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlock](api/messages.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



container\_upload\_block: object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



model: "claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 13 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-sonnet-5"

High-performance model for coding and agents

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



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: object { category, explanation, type } 

Structured information about a refusal.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 3 more

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"



stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 6 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: object { thinking\_tokens } 

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



server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"

type: "succeeded"

---

*Copyright © Anthropic. All rights reserved.*
