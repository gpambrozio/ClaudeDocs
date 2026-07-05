# Batches

Copy page



Python

# Batches

##### [Create a Message Batch](api/messages/batches/create.md)

messages.batches.create(BatchCreateParams\*\*kwargs)  -> [MessageBatch](api/messages/batches.md)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/messages/batches/retrieve.md)

messages.batches.retrieve(strmessage\_batch\_id)  -> [MessageBatch](api/messages/batches.md)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/messages/batches/list.md)

messages.batches.list(BatchListParams\*\*kwargs)  -> SyncPage[[MessageBatch](api/messages/batches.md)]

GET/v1/messages/batches

##### [Cancel a Message Batch](api/messages/batches/cancel.md)

messages.batches.cancel(strmessage\_batch\_id)  -> [MessageBatch](api/messages/batches.md)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/messages/batches/delete.md)

messages.batches.delete(strmessage\_batch\_id)  -> [DeletedMessageBatch](api/messages/batches.md)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/messages/batches/results.md)

messages.batches.results(strmessage\_batch\_id)  -> [MessageBatchIndividualResponse](api/messages/batches.md)

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse



class DeletedMessageBatch: …

id: str

ID of the Message Batch.



type: Literal["message\_batch\_deleted"]

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.



class MessageBatch: …



id: str

Unique object identifier.

The format and length of IDs may change over time.

archived\_at: Optional[datetime]

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

cancel\_initiated\_at: Optional[datetime]

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

created\_at: datetime

RFC 3339 datetime string representing the time at which the Message Batch was created.



ended\_at: Optional[datetime]

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires\_at: datetime

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.



processing\_status: Literal["in\_progress", "canceling", "ended"]

Processing status of the Message Batch.

One of the following:

"in\_progress"

"canceling"

"ended"



request\_counts: [MessageBatchRequestCounts](api/messages/batches.md)

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.



canceled: int

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



errored: int

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



expired: int

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: int

Number of requests in the Message Batch that are processing.



succeeded: int

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



results\_url: Optional[str]

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.



type: Literal["message\_batch"]

Object type.

For Message Batches, this is always `"message_batch"`.



class MessageBatchCanceledResult: …

type: Literal["canceled"]



class MessageBatchErroredResult: …



error: [ErrorResponse](api/$shared.md)



error: [ErrorObject](api/$shared.md)

One of the following:



class InvalidRequestError: …

message: str

type: Literal["invalid\_request\_error"]



class AuthenticationError: …

message: str

type: Literal["authentication\_error"]



class BillingError: …

message: str

type: Literal["billing\_error"]



class PermissionError: …

message: str

type: Literal["permission\_error"]



class NotFoundError: …

message: str

type: Literal["not\_found\_error"]



class RateLimitError: …

message: str

type: Literal["rate\_limit\_error"]



class GatewayTimeoutError: …

message: str

type: Literal["timeout\_error"]



class APIErrorObject: …

message: str

type: Literal["api\_error"]



class OverloadedError: …

message: str

type: Literal["overloaded\_error"]

request\_id: Optional[str]

type: Literal["error"]

type: Literal["errored"]



class MessageBatchExpiredResult: …

type: Literal["expired"]



class MessageBatchIndividualResponse: …

This is a single line in the response `.jsonl` file and does not represent the response as a whole.



custom\_id: str

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.



result: [MessageBatchResult](api/messages/batches.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



class MessageBatchSucceededResult: …



message: [Message](api/messages.md)



id: str

Unique object identifier.

The format and length of IDs may change over time.



container: Optional[Container]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.



content: List[[ContentBlock](api/messages.md)]

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

class TextBlock: …



citations: Optional[List[[TextCitation](api/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class CitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class CitationsSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]



class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]



class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]



class ToolUseBlock: …

id: str



caller: Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: str

type: Literal["tool\_use"]



class ServerToolUseBlock: …

id: str



caller: Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]



name: Literal["web\_search", "web\_fetch", "code\_execution", 4 more]

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]



class WebSearchToolResultBlock: …



caller: Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



class WebSearchToolResultError: …



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]



List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]



class WebFetchToolResultBlock: …



caller: Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



content: Content

One of the following:



class WebFetchToolResultErrorBlock: …

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

type: Literal["web\_fetch\_tool\_result\_error"]



class WebFetchBlock: …



content: [DocumentBlock](api/messages.md)



citations: Optional[CitationsConfig]

Citation configuration for the document

enabled: bool



source: Source

One of the following:



class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]



class CodeExecutionToolResultBlock: …



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultError: …



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]



class CodeExecutionResultBlock: …



content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]



class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.



content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]



class BashCodeExecutionToolResultBlock: …



content: Content

One of the following:



class BashCodeExecutionToolResultError: …



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]



class BashCodeExecutionResultBlock: …



content: List[[BashCodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]



class TextEditorCodeExecutionToolResultBlock: …



content: Content

One of the following:



class TextEditorCodeExecutionToolResultError: …



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]



class TextEditorCodeExecutionViewResultBlock: …

content: str



file\_type: Literal["text", "image", "pdf"]

One of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]



class TextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]



class TextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]



class ToolSearchToolResultBlock: …



content: Content

One of the following:



class ToolSearchToolResultError: …



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]



class ToolSearchToolSearchResultBlock: …



tool\_references: List[[ToolReferenceBlock](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]



class ContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-sonnet-5", "claude-fable-5", "claude-mythos-5", 13 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-sonnet-5` - High-performance model for coding and agents
- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: Optional[RefusalStopDetails]

Structured information about a refusal.



category: Optional[Literal["cyber", "bio", "frontier\_llm", "reasoning\_extraction"]]

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: Literal["refusal"]



stop\_reason: Optional[StopReason]

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

stop\_sequence: Optional[str]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: Literal["message"]

Object type.

For Messages, this is always `"message"`.



usage: [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: Optional[CacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.



output\_tokens\_details: Optional[OutputTokensDetails]

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: int

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.



service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"

type: Literal["succeeded"]



class MessageBatchErroredResult: …



error: [ErrorResponse](api/$shared.md)



error: [ErrorObject](api/$shared.md)

One of the following:



class InvalidRequestError: …

message: str

type: Literal["invalid\_request\_error"]



class AuthenticationError: …

message: str

type: Literal["authentication\_error"]



class BillingError: …

message: str

type: Literal["billing\_error"]



class PermissionError: …

message: str

type: Literal["permission\_error"]



class NotFoundError: …

message: str

type: Literal["not\_found\_error"]



class RateLimitError: …

message: str

type: Literal["rate\_limit\_error"]



class GatewayTimeoutError: …

message: str

type: Literal["timeout\_error"]



class APIErrorObject: …

message: str

type: Literal["api\_error"]



class OverloadedError: …

message: str

type: Literal["overloaded\_error"]

request\_id: Optional[str]

type: Literal["error"]

type: Literal["errored"]



class MessageBatchCanceledResult: …

type: Literal["canceled"]



class MessageBatchExpiredResult: …

type: Literal["expired"]



class MessageBatchRequestCounts: …



canceled: int

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



errored: int

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



expired: int

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: int

Number of requests in the Message Batch that are processing.



succeeded: int

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



[MessageBatchResult](api/messages/batches.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



class MessageBatchSucceededResult: …



message: [Message](api/messages.md)



id: str

Unique object identifier.

The format and length of IDs may change over time.



container: Optional[Container]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.



content: List[[ContentBlock](api/messages.md)]

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

class TextBlock: …



citations: Optional[List[[TextCitation](api/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class CitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class CitationsSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]



class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]



class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]



class ToolUseBlock: …

id: str



caller: Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: str

type: Literal["tool\_use"]



class ServerToolUseBlock: …

id: str



caller: Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]



name: Literal["web\_search", "web\_fetch", "code\_execution", 4 more]

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]



class WebSearchToolResultBlock: …



caller: Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



class WebSearchToolResultError: …



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]



List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]



class WebFetchToolResultBlock: …



caller: Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



content: Content

One of the following:



class WebFetchToolResultErrorBlock: …

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

type: Literal["web\_fetch\_tool\_result\_error"]



class WebFetchBlock: …



content: [DocumentBlock](api/messages.md)



citations: Optional[CitationsConfig]

Citation configuration for the document

enabled: bool



source: Source

One of the following:



class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]



class CodeExecutionToolResultBlock: …



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultError: …



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]



class CodeExecutionResultBlock: …



content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]



class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.



content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]



class BashCodeExecutionToolResultBlock: …



content: Content

One of the following:



class BashCodeExecutionToolResultError: …



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]



class BashCodeExecutionResultBlock: …



content: List[[BashCodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]



class TextEditorCodeExecutionToolResultBlock: …



content: Content

One of the following:



class TextEditorCodeExecutionToolResultError: …



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]



class TextEditorCodeExecutionViewResultBlock: …

content: str



file\_type: Literal["text", "image", "pdf"]

One of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]



class TextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]



class TextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]



class ToolSearchToolResultBlock: …



content: Content

One of the following:



class ToolSearchToolResultError: …



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]



class ToolSearchToolSearchResultBlock: …



tool\_references: List[[ToolReferenceBlock](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]



class ContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-sonnet-5", "claude-fable-5", "claude-mythos-5", 13 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-sonnet-5` - High-performance model for coding and agents
- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: Optional[RefusalStopDetails]

Structured information about a refusal.



category: Optional[Literal["cyber", "bio", "frontier\_llm", "reasoning\_extraction"]]

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: Literal["refusal"]



stop\_reason: Optional[StopReason]

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

stop\_sequence: Optional[str]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: Literal["message"]

Object type.

For Messages, this is always `"message"`.



usage: [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: Optional[CacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.



output\_tokens\_details: Optional[OutputTokensDetails]

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: int

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.



service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"

type: Literal["succeeded"]



class MessageBatchErroredResult: …



error: [ErrorResponse](api/$shared.md)



error: [ErrorObject](api/$shared.md)

One of the following:



class InvalidRequestError: …

message: str

type: Literal["invalid\_request\_error"]



class AuthenticationError: …

message: str

type: Literal["authentication\_error"]



class BillingError: …

message: str

type: Literal["billing\_error"]



class PermissionError: …

message: str

type: Literal["permission\_error"]



class NotFoundError: …

message: str

type: Literal["not\_found\_error"]



class RateLimitError: …

message: str

type: Literal["rate\_limit\_error"]



class GatewayTimeoutError: …

message: str

type: Literal["timeout\_error"]



class APIErrorObject: …

message: str

type: Literal["api\_error"]



class OverloadedError: …

message: str

type: Literal["overloaded\_error"]

request\_id: Optional[str]

type: Literal["error"]

type: Literal["errored"]



class MessageBatchCanceledResult: …

type: Literal["canceled"]



class MessageBatchExpiredResult: …

type: Literal["expired"]



class MessageBatchSucceededResult: …



message: [Message](api/messages.md)



id: str

Unique object identifier.

The format and length of IDs may change over time.



container: Optional[Container]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.



content: List[[ContentBlock](api/messages.md)]

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

class TextBlock: …



citations: Optional[List[[TextCitation](api/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class CitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class CitationsSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]



class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]



class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]



class ToolUseBlock: …

id: str



caller: Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: str

type: Literal["tool\_use"]



class ServerToolUseBlock: …

id: str



caller: Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]



name: Literal["web\_search", "web\_fetch", "code\_execution", 4 more]

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]



class WebSearchToolResultBlock: …



caller: Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



class WebSearchToolResultError: …



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]



List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]



class WebFetchToolResultBlock: …



caller: Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



content: Content

One of the following:



class WebFetchToolResultErrorBlock: …

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

type: Literal["web\_fetch\_tool\_result\_error"]



class WebFetchBlock: …



content: [DocumentBlock](api/messages.md)



citations: Optional[CitationsConfig]

Citation configuration for the document

enabled: bool



source: Source

One of the following:



class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]



class CodeExecutionToolResultBlock: …



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultError: …



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]



class CodeExecutionResultBlock: …



content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]



class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.



content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]



class BashCodeExecutionToolResultBlock: …



content: Content

One of the following:



class BashCodeExecutionToolResultError: …



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]



class BashCodeExecutionResultBlock: …



content: List[[BashCodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]



class TextEditorCodeExecutionToolResultBlock: …



content: Content

One of the following:



class TextEditorCodeExecutionToolResultError: …



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]



class TextEditorCodeExecutionViewResultBlock: …

content: str



file\_type: Literal["text", "image", "pdf"]

One of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]



class TextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]



class TextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]



class ToolSearchToolResultBlock: …



content: Content

One of the following:



class ToolSearchToolResultError: …



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]



class ToolSearchToolSearchResultBlock: …



tool\_references: List[[ToolReferenceBlock](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]



class ContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-sonnet-5", "claude-fable-5", "claude-mythos-5", 13 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-sonnet-5` - High-performance model for coding and agents
- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: Optional[RefusalStopDetails]

Structured information about a refusal.



category: Optional[Literal["cyber", "bio", "frontier\_llm", "reasoning\_extraction"]]

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: Literal["refusal"]



stop\_reason: Optional[StopReason]

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

stop\_sequence: Optional[str]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: Literal["message"]

Object type.

For Messages, this is always `"message"`.



usage: [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: Optional[CacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.



output\_tokens\_details: Optional[OutputTokensDetails]

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: int

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.



service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"

type: Literal["succeeded"]

---

*Copyright © Anthropic. All rights reserved.*
