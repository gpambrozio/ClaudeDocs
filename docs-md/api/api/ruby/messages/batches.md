# Batches

Copy page

SDK language

Ruby

# Batches

##### [Create a Message Batch](api/messages/batches/create.md)

messages.batches.create(\*\*kwargs) -> [MessageBatch](api/messages.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/messages/batches/retrieve.md)

messages.batches.retrieve(message\_batch\_id) -> [MessageBatch](api/messages.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/messages/batches/list.md)

messages.batches.list(\*\*kwargs) -> Page<[MessageBatch](api/messages.md) { id, archived\_at, cancel\_initiated\_at, 7 more } >

GET/v1/messages/batches

##### [Cancel a Message Batch](api/messages/batches/cancel.md)

messages.batches.cancel(message\_batch\_id) -> [MessageBatch](api/messages.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/messages/batches/delete.md)

messages.batches.delete(message\_batch\_id) -> [DeletedMessageBatch](api/messages.md) { id, type }

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/messages/batches/results.md)

messages.batches.results(message\_batch\_id) -> [MessageBatchIndividualResponse](api/messages.md) { custom\_id, result }

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse



class DeletedMessageBatch { id, type } 

id: String

ID of the Message Batch.



type: :message\_batch\_deleted

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.



class MessageBatch { id, archived\_at, cancel\_initiated\_at, 7 more } 



id: String

Unique object identifier.

The format and length of IDs may change over time.

archived\_at: Time

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

cancel\_initiated\_at: Time

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

created\_at: Time

RFC 3339 datetime string representing the time at which the Message Batch was created.



ended\_at: Time

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires\_at: Time

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.



processing\_status: :in\_progress | :canceling | :ended

Processing status of the Message Batch.

One of the following:

:in\_progress

:canceling

:ended



request\_counts: [MessageBatchRequestCounts](api/messages.md) { canceled, errored, expired, 2 more } 

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.



canceled: Integer

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



errored: Integer

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



expired: Integer

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Integer

Number of requests in the Message Batch that are processing.



succeeded: Integer

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



results\_url: String

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.



type: :message\_batch

Object type.

For Message Batches, this is always `"message_batch"`.



class MessageBatchCanceledResult { type } 

type: :canceled



class MessageBatchErroredResult { error, type } 



error: [ErrorResponse](api/$shared.md) { error, request\_id, type } 



error: [ErrorObject](api/$shared.md)

One of the following:



class InvalidRequestError { message, type } 

message: String

type: :invalid\_request\_error



class AuthenticationError { message, type } 

message: String

type: :authentication\_error



class BillingError { message, type } 

message: String

type: :billing\_error



class PermissionError { message, type } 

message: String

type: :permission\_error



class NotFoundError { message, type } 

message: String

type: :not\_found\_error



class RateLimitError { message, type } 

message: String

type: :rate\_limit\_error



class GatewayTimeoutError { message, type } 

message: String

type: :timeout\_error



class APIErrorObject { message, type } 

message: String

type: :api\_error



class OverloadedError { message, type } 

message: String

type: :overloaded\_error

request\_id: String

type: :error

type: :errored



class MessageBatchExpiredResult { type } 

type: :expired



class MessageBatchIndividualResponse { custom\_id, result } 

This is a single line in the response `.jsonl` file and does not represent the response as a whole.



custom\_id: String

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.



result: [MessageBatchResult](api/messages.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



class MessageBatchSucceededResult { message, type } 



message: [Message](api/messages.md) { id, container, content, 7 more } 



id: String

Unique object identifier.

The format and length of IDs may change over time.



container: [Container](api/messages.md) { id, expires\_at } 

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.



content: Array[[ContentBlock](api/messages.md)]

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

class TextBlock { citations, text, type } 



citations: Array[[TextCitation](api/messages.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text



class ThinkingBlock { signature, thinking, type } 

signature: String

thinking: String

type: :thinking



class RedactedThinkingBlock { data, type } 

data: String

type: :redacted\_thinking



class ToolUseBlock { id, caller\_, input, 2 more } 

id: String



caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class DirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class ServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120

input: Hash[Symbol, untyped]

name: String

type: :tool\_use



class ServerToolUseBlock { id, caller\_, input, 2 more } 

id: String



caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class DirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class ServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120

input: Hash[Symbol, untyped]



name: :web\_search | :web\_fetch | :code\_execution | 4 more

One of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use



class WebSearchToolResultBlock { caller\_, content, tool\_use\_id, type } 



caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class DirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class ServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



class WebSearchToolResultError { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error



UnionMember1 = Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result



class WebFetchToolResultBlock { caller\_, content, tool\_use\_id, type } 



caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class DirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class ServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  | [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



class WebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class WebFetchBlock { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled } 

Citation configuration for the document

enabled: bool



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



class Base64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class PlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result



class CodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultError { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class CodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class EncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result



class BashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  | [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



class BashCodeExecutionToolResultError { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result



class TextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  | [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  | [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  | [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



class TextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error



class TextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result



class TextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class TextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result



class ToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  | [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



class ToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error



class ToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array[[ToolReferenceBlock](api/messages.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result



class ContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

:"claude-opus-4-0"

Powerful model for complex tasks

:"claude-opus-4-20250514"

Powerful model for complex tasks

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-3-haiku-20240307"

Fast and cost-effective model

String = String



role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type } 

Structured information about a refusal.



category: :cyber | :bio | :reasoning\_extraction

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

:cyber

:bio

:reasoning\_extraction



explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: :refusal



stop\_reason: [StopReason](api/messages.md)

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

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:refusal



stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: :message

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

cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: Integer

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.



service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

One of the following:

:standard

:priority

:batch

type: :succeeded



class MessageBatchErroredResult { error, type } 



error: [ErrorResponse](api/$shared.md) { error, request\_id, type } 



error: [ErrorObject](api/$shared.md)

One of the following:



class InvalidRequestError { message, type } 

message: String

type: :invalid\_request\_error



class AuthenticationError { message, type } 

message: String

type: :authentication\_error



class BillingError { message, type } 

message: String

type: :billing\_error



class PermissionError { message, type } 

message: String

type: :permission\_error



class NotFoundError { message, type } 

message: String

type: :not\_found\_error



class RateLimitError { message, type } 

message: String

type: :rate\_limit\_error



class GatewayTimeoutError { message, type } 

message: String

type: :timeout\_error



class APIErrorObject { message, type } 

message: String

type: :api\_error



class OverloadedError { message, type } 

message: String

type: :overloaded\_error

request\_id: String

type: :error

type: :errored



class MessageBatchCanceledResult { type } 

type: :canceled



class MessageBatchExpiredResult { type } 

type: :expired



class MessageBatchRequestCounts { canceled, errored, expired, 2 more } 



canceled: Integer

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



errored: Integer

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



expired: Integer

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Integer

Number of requests in the Message Batch that are processing.



succeeded: Integer

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



MessageBatchResult = [MessageBatchSucceededResult](api/messages.md) { message, type }  | [MessageBatchErroredResult](api/messages.md) { error, type }  | [MessageBatchCanceledResult](api/messages.md) { type }  | [MessageBatchExpiredResult](api/messages.md) { type } 

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



class MessageBatchSucceededResult { message, type } 



message: [Message](api/messages.md) { id, container, content, 7 more } 



id: String

Unique object identifier.

The format and length of IDs may change over time.



container: [Container](api/messages.md) { id, expires\_at } 

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.



content: Array[[ContentBlock](api/messages.md)]

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

class TextBlock { citations, text, type } 



citations: Array[[TextCitation](api/messages.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text



class ThinkingBlock { signature, thinking, type } 

signature: String

thinking: String

type: :thinking



class RedactedThinkingBlock { data, type } 

data: String

type: :redacted\_thinking



class ToolUseBlock { id, caller\_, input, 2 more } 

id: String



caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class DirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class ServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120

input: Hash[Symbol, untyped]

name: String

type: :tool\_use



class ServerToolUseBlock { id, caller\_, input, 2 more } 

id: String



caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class DirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class ServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120

input: Hash[Symbol, untyped]



name: :web\_search | :web\_fetch | :code\_execution | 4 more

One of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use



class WebSearchToolResultBlock { caller\_, content, tool\_use\_id, type } 



caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class DirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class ServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



class WebSearchToolResultError { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error



UnionMember1 = Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result



class WebFetchToolResultBlock { caller\_, content, tool\_use\_id, type } 



caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class DirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class ServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  | [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



class WebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class WebFetchBlock { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled } 

Citation configuration for the document

enabled: bool



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



class Base64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class PlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result



class CodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultError { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class CodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class EncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result



class BashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  | [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



class BashCodeExecutionToolResultError { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result



class TextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  | [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  | [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  | [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



class TextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error



class TextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result



class TextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class TextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result



class ToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  | [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



class ToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error



class ToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array[[ToolReferenceBlock](api/messages.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result



class ContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

:"claude-opus-4-0"

Powerful model for complex tasks

:"claude-opus-4-20250514"

Powerful model for complex tasks

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-3-haiku-20240307"

Fast and cost-effective model

String = String



role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type } 

Structured information about a refusal.



category: :cyber | :bio | :reasoning\_extraction

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

:cyber

:bio

:reasoning\_extraction



explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: :refusal



stop\_reason: [StopReason](api/messages.md)

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

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:refusal



stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: :message

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

cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: Integer

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.



service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

One of the following:

:standard

:priority

:batch

type: :succeeded



class MessageBatchErroredResult { error, type } 



error: [ErrorResponse](api/$shared.md) { error, request\_id, type } 



error: [ErrorObject](api/$shared.md)

One of the following:



class InvalidRequestError { message, type } 

message: String

type: :invalid\_request\_error



class AuthenticationError { message, type } 

message: String

type: :authentication\_error



class BillingError { message, type } 

message: String

type: :billing\_error



class PermissionError { message, type } 

message: String

type: :permission\_error



class NotFoundError { message, type } 

message: String

type: :not\_found\_error



class RateLimitError { message, type } 

message: String

type: :rate\_limit\_error



class GatewayTimeoutError { message, type } 

message: String

type: :timeout\_error



class APIErrorObject { message, type } 

message: String

type: :api\_error



class OverloadedError { message, type } 

message: String

type: :overloaded\_error

request\_id: String

type: :error

type: :errored



class MessageBatchCanceledResult { type } 

type: :canceled



class MessageBatchExpiredResult { type } 

type: :expired



class MessageBatchSucceededResult { message, type } 



message: [Message](api/messages.md) { id, container, content, 7 more } 



id: String

Unique object identifier.

The format and length of IDs may change over time.



container: [Container](api/messages.md) { id, expires\_at } 

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.



content: Array[[ContentBlock](api/messages.md)]

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

class TextBlock { citations, text, type } 



citations: Array[[TextCitation](api/messages.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text



class ThinkingBlock { signature, thinking, type } 

signature: String

thinking: String

type: :thinking



class RedactedThinkingBlock { data, type } 

data: String

type: :redacted\_thinking



class ToolUseBlock { id, caller\_, input, 2 more } 

id: String



caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class DirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class ServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120

input: Hash[Symbol, untyped]

name: String

type: :tool\_use



class ServerToolUseBlock { id, caller\_, input, 2 more } 

id: String



caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class DirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class ServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120

input: Hash[Symbol, untyped]



name: :web\_search | :web\_fetch | :code\_execution | 4 more

One of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use



class WebSearchToolResultBlock { caller\_, content, tool\_use\_id, type } 



caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class DirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class ServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



class WebSearchToolResultError { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error



UnionMember1 = Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result



class WebFetchToolResultBlock { caller\_, content, tool\_use\_id, type } 



caller\_: [DirectCaller](api/messages.md) { type }  | [ServerToolCaller](api/messages.md) { tool\_id, type }  | [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class DirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class ServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class ServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  | [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



class WebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class WebFetchBlock { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled } 

Citation configuration for the document

enabled: bool



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



class Base64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class PlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result



class CodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultError { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class CodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class EncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[CodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result



class BashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  | [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



class BashCodeExecutionToolResultError { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result



class TextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  | [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  | [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  | [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



class TextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error



class TextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result



class TextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class TextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result



class ToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  | [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



class ToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error



class ToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array[[ToolReferenceBlock](api/messages.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result



class ContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

:"claude-opus-4-0"

Powerful model for complex tasks

:"claude-opus-4-20250514"

Powerful model for complex tasks

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-3-haiku-20240307"

Fast and cost-effective model

String = String



role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type } 

Structured information about a refusal.



category: :cyber | :bio | :reasoning\_extraction

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

:cyber

:bio

:reasoning\_extraction



explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: :refusal



stop\_reason: [StopReason](api/messages.md)

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

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:refusal



stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: :message

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

cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: Integer

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.



service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

One of the following:

:standard

:priority

:batch

type: :succeeded

---

*Copyright © Anthropic. All rights reserved.*
