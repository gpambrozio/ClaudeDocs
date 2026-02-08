# Batches

Copy page

TypeScript

# Batches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

client.beta.messages.batches.create(BatchCreateParams { requests, betas } params, RequestOptionsoptions?): [BetaMessageBatch](api/beta.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

post/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

client.beta.messages.batches.retrieve(stringmessageBatchID, BatchRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaMessageBatch](api/beta.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

get/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

client.beta.messages.batches.list(BatchListParams { after\_id, before\_id, limit, betas } params?, RequestOptionsoptions?): Page<[BetaMessageBatch](api/beta.md) { id, archived\_at, cancel\_initiated\_at, 7 more } >

get/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

client.beta.messages.batches.cancel(stringmessageBatchID, BatchCancelParams { betas } params?, RequestOptionsoptions?): [BetaMessageBatch](api/beta.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

post/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

client.beta.messages.batches.delete(stringmessageBatchID, BatchDeleteParams { betas } params?, RequestOptionsoptions?): [BetaDeletedMessageBatch](api/beta.md) { id, type }

delete/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

client.beta.messages.batches.results(stringmessageBatchID, BatchResultsParams { betas } params?, RequestOptionsoptions?): [BetaMessageBatchIndividualResponse](api/beta.md) { custom\_id, result }  | Stream<[BetaMessageBatchIndividualResponse](api/beta.md) { custom\_id, result } >

get/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

BetaDeletedMessageBatch { id, type }

id: string

ID of the Message Batch.

type: "message\_batch\_deleted"

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

"message\_batch\_deleted"

BetaMessageBatch { id, archived\_at, cancel\_initiated\_at, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

archived\_at: string | null

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

formatdate-time

cancel\_initiated\_at: string | null

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

formatdate-time

created\_at: string

RFC 3339 datetime string representing the time at which the Message Batch was created.

formatdate-time

ended\_at: string | null

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires\_at: string

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

formatdate-time

processing\_status: "in\_progress" | "canceling" | "ended"

Processing status of the Message Batch.

Accepts one of the following:

"in\_progress"

"canceling"

"ended"

request\_counts: [BetaMessageBatchRequestCounts](api/beta.md) { canceled, errored, expired, 2 more }

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

canceled: number

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: number

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: number

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: number

Number of requests in the Message Batch that are processing.

succeeded: number

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

results\_url: string | null

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: "message\_batch"

Object type.

For Message Batches, this is always `"message_batch"`.

Accepts one of the following:

"message\_batch"

BetaMessageBatchCanceledResult { type }

type: "canceled"

Accepts one of the following:

"canceled"

BetaMessageBatchErroredResult { error, type }

error: [BetaErrorResponse](api/beta.md) { error, request\_id, type }

error: [BetaError](api/beta.md)

Accepts one of the following:

BetaInvalidRequestError { message, type }

message: string

type: "invalid\_request\_error"

Accepts one of the following:

"invalid\_request\_error"

BetaAuthenticationError { message, type }

message: string

type: "authentication\_error"

Accepts one of the following:

"authentication\_error"

BetaBillingError { message, type }

message: string

type: "billing\_error"

Accepts one of the following:

"billing\_error"

BetaPermissionError { message, type }

message: string

type: "permission\_error"

Accepts one of the following:

"permission\_error"

BetaNotFoundError { message, type }

message: string

type: "not\_found\_error"

Accepts one of the following:

"not\_found\_error"

BetaRateLimitError { message, type }

message: string

type: "rate\_limit\_error"

Accepts one of the following:

"rate\_limit\_error"

BetaGatewayTimeoutError { message, type }

message: string

type: "timeout\_error"

Accepts one of the following:

"timeout\_error"

BetaAPIError { message, type }

message: string

type: "api\_error"

Accepts one of the following:

"api\_error"

BetaOverloadedError { message, type }

message: string

type: "overloaded\_error"

Accepts one of the following:

"overloaded\_error"

request\_id: string | null

type: "error"

Accepts one of the following:

"error"

type: "errored"

Accepts one of the following:

"errored"

BetaMessageBatchExpiredResult { type }

type: "expired"

Accepts one of the following:

"expired"

BetaMessageBatchIndividualResponse { custom\_id, result }

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

custom\_id: string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [BetaMessageBatchResult](api/beta.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

BetaMessageBatchSucceededResult { message, type }

message: [BetaMessage](api/beta.md) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }  | null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

formatdate-time

skills: Array<[BetaSkill](api/beta.md) { skill\_id, type, version } > | null

Skills loaded in the container

skill\_id: string

Skill ID

maxLength64

minLength1

type: "anthropic" | "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: Array<[BetaContentBlock](api/beta.md)>

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

BetaTextBlock { citations, text, type }

citations: Array<[BetaTextCitation](api/beta.md)> | null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

file\_id: string | null

start\_char\_index: number

type: "char\_location"

Accepts one of the following:

"char\_location"

BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

file\_id: string | null

start\_page\_number: number

type: "page\_location"

Accepts one of the following:

"page\_location"

BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_block\_index: number

file\_id: string | null

start\_block\_index: number

type: "content\_block\_location"

Accepts one of the following:

"content\_block\_location"

BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

Accepts one of the following:

"web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string | null

type: "search\_result\_location"

Accepts one of the following:

"search\_result\_location"

text: string

type: "text"

Accepts one of the following:

"text"

BetaThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

BetaRedactedThinkingBlock { data, type }

data: string

type: "redacted\_thinking"

Accepts one of the following:

"redacted\_thinking"

BetaToolUseBlock { id, input, name, 2 more }

id: string

input: Record<string, unknown>

name: string

type: "tool\_use"

Accepts one of the following:

"tool\_use"

caller?: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

Accepts one of the following:

"code\_execution\_20250825"

BetaServerToolUseBlock { id, input, name, 2 more }

id: string

input: Record<string, unknown>

name: "web\_search" | "web\_fetch" | "code\_execution" | 4 more

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

Accepts one of the following:

"server\_tool\_use"

caller?: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

Accepts one of the following:

"code\_execution\_20250825"

BetaWebSearchToolResultBlock { content, tool\_use\_id, type }

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

BetaWebSearchToolResultError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

Accepts one of the following:

"web\_search\_tool\_result\_error"

Array<[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } >

encrypted\_content: string

page\_age: string | null

title: string

type: "web\_search\_result"

Accepts one of the following:

"web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

Accepts one of the following:

"web\_search\_tool\_result"

BetaWebFetchToolResultBlock { content, tool\_use\_id, type }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

Accepts one of the following:

"web\_fetch\_tool\_result\_error"

BetaWebFetchBlock { content, retrieved\_at, type, url }

content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type }

citations: [BetaCitationConfig](api/beta.md) { enabled }  | null

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

Accepts one of the following:

BetaBase64PDFSource { data, media\_type, type }

data: string

media\_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media\_type, type }

data: string

media\_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

title: string | null

The title of the document

type: "document"

Accepts one of the following:

"document"

retrieved\_at: string | null

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

Accepts one of the following:

"web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

Accepts one of the following:

"web\_fetch\_tool\_result"

BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

Accepts one of the following:

"code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array<[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } >

file\_id: string

type: "code\_execution\_output"

Accepts one of the following:

"code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

Accepts one of the following:

"code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

Accepts one of the following:

"code\_execution\_tool\_result"

BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError { error\_code, type }

error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | 2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

Accepts one of the following:

"bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array<[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } >

file\_id: string

type: "bash\_code\_execution\_output"

Accepts one of the following:

"bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

Accepts one of the following:

"bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

Accepts one of the following:

"bash\_code\_execution\_tool\_result"

BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | 2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string | null

type: "text\_editor\_code\_execution\_tool\_result\_error"

Accepts one of the following:

"text\_editor\_code\_execution\_tool\_result\_error"

BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" | "image" | "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: number | null

start\_line: number | null

total\_lines: number | null

type: "text\_editor\_code\_execution\_view\_result"

Accepts one of the following:

"text\_editor\_code\_execution\_view\_result"

BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

Accepts one of the following:

"text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array<string> | null

new\_lines: number | null

new\_start: number | null

old\_lines: number | null

old\_start: number | null

type: "text\_editor\_code\_execution\_str\_replace\_result"

Accepts one of the following:

"text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

Accepts one of the following:

"text\_editor\_code\_execution\_tool\_result"

BetaToolSearchToolResultBlock { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

Accepts one of the following:

BetaToolSearchToolResultError { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | "execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string | null

type: "tool\_search\_tool\_result\_error"

Accepts one of the following:

"tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array<[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } >

tool\_name: string

type: "tool\_reference"

Accepts one of the following:

"tool\_reference"

type: "tool\_search\_tool\_search\_result"

Accepts one of the following:

"tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

Accepts one of the following:

"tool\_search\_tool\_result"

BetaMCPToolUseBlock { id, input, name, 2 more }

id: string

input: Record<string, unknown>

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

Accepts one of the following:

"mcp\_tool\_use"

BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type }

content: string | Array<[BetaTextBlock](api/beta.md) { citations, text, type } >

Accepts one of the following:

string

Array<[BetaTextBlock](api/beta.md) { citations, text, type } >

citations: Array<[BetaTextCitation](api/beta.md)> | null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

file\_id: string | null

start\_char\_index: number

type: "char\_location"

Accepts one of the following:

"char\_location"

BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

file\_id: string | null

start\_page\_number: number

type: "page\_location"

Accepts one of the following:

"page\_location"

BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_block\_index: number

file\_id: string | null

start\_block\_index: number

type: "content\_block\_location"

Accepts one of the following:

"content\_block\_location"

BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

Accepts one of the following:

"web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string | null

type: "search\_result\_location"

Accepts one of the following:

"search\_result\_location"

text: string

type: "text"

Accepts one of the following:

"text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

Accepts one of the following:

"mcp\_tool\_result"

BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

Accepts one of the following:

"container\_upload"

BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string | null

Summary of compacted content, or null if compaction failed

type: "compaction"

Accepts one of the following:

"compaction"

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }  | null

Context management response.

Information about context management strategies applied during the request.

applied\_edits: Array<[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } >

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared\_tool\_uses: number

Number of tool uses that were cleared.

minimum0

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

Accepts one of the following:

"clear\_tool\_uses\_20250919"

BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

minimum0

type: "clear\_thinking\_20251015"

The type of context management edit applied.

Accepts one of the following:

"clear\_thinking\_20251015"

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" | "claude-opus-4-5-20251101" | "claude-opus-4-5" | 18 more

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop\_reason: [BetaStopReason](api/beta.md) | null

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

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string | null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: number | null

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: number | null

The number of input tokens read from the cache.

minimum0

inference\_geo: string | null

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

minimum0

iterations: [BetaIterationsUsage](api/beta.md) | null

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

minimum0

input\_tokens: number

The number of input tokens which were used.

minimum0

output\_tokens: number

The number of output tokens which were used.

minimum0

type: "message"

Usage for a sampling iteration

Accepts one of the following:

"message"

BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

minimum0

input\_tokens: number

The number of input tokens which were used.

minimum0

output\_tokens: number

The number of output tokens which were used.

minimum0

type: "compaction"

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output\_tokens: number

The number of output tokens which were used.

minimum0

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }  | null

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

minimum0

web\_search\_requests: number

The number of web search tool requests.

minimum0

service\_tier: "standard" | "priority" | "batch" | null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: "standard" | "fast" | null

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

type: "succeeded"

Accepts one of the following:

"succeeded"

BetaMessageBatchErroredResult { error, type }

error: [BetaErrorResponse](api/beta.md) { error, request\_id, type }

error: [BetaError](api/beta.md)

Accepts one of the following:

BetaInvalidRequestError { message, type }

message: string

type: "invalid\_request\_error"

Accepts one of the following:

"invalid\_request\_error"

BetaAuthenticationError { message, type }

message: string

type: "authentication\_error"

Accepts one of the following:

"authentication\_error"

BetaBillingError { message, type }

message: string

type: "billing\_error"

Accepts one of the following:

"billing\_error"

BetaPermissionError { message, type }

message: string

type: "permission\_error"

Accepts one of the following:

"permission\_error"

BetaNotFoundError { message, type }

message: string

type: "not\_found\_error"

Accepts one of the following:

"not\_found\_error"

BetaRateLimitError { message, type }

message: string

type: "rate\_limit\_error"

Accepts one of the following:

"rate\_limit\_error"

BetaGatewayTimeoutError { message, type }

message: string

type: "timeout\_error"

Accepts one of the following:

"timeout\_error"

BetaAPIError { message, type }

message: string

type: "api\_error"

Accepts one of the following:

"api\_error"

BetaOverloadedError { message, type }

message: string

type: "overloaded\_error"

Accepts one of the following:

"overloaded\_error"

request\_id: string | null

type: "error"

Accepts one of the following:

"error"

type: "errored"

Accepts one of the following:

"errored"

BetaMessageBatchCanceledResult { type }

type: "canceled"

Accepts one of the following:

"canceled"

BetaMessageBatchExpiredResult { type }

type: "expired"

Accepts one of the following:

"expired"

BetaMessageBatchRequestCounts { canceled, errored, expired, 2 more }

canceled: number

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: number

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: number

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: number

Number of requests in the Message Batch that are processing.

succeeded: number

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

BetaMessageBatchResult = [BetaMessageBatchSucceededResult](api/beta.md) { message, type }  | [BetaMessageBatchErroredResult](api/beta.md) { error, type }  | [BetaMessageBatchCanceledResult](api/beta.md) { type }  | [BetaMessageBatchExpiredResult](api/beta.md) { type }

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

BetaMessageBatchSucceededResult { message, type }

message: [BetaMessage](api/beta.md) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }  | null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

formatdate-time

skills: Array<[BetaSkill](api/beta.md) { skill\_id, type, version } > | null

Skills loaded in the container

skill\_id: string

Skill ID

maxLength64

minLength1

type: "anthropic" | "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: Array<[BetaContentBlock](api/beta.md)>

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

BetaTextBlock { citations, text, type }

citations: Array<[BetaTextCitation](api/beta.md)> | null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

file\_id: string | null

start\_char\_index: number

type: "char\_location"

Accepts one of the following:

"char\_location"

BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

file\_id: string | null

start\_page\_number: number

type: "page\_location"

Accepts one of the following:

"page\_location"

BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_block\_index: number

file\_id: string | null

start\_block\_index: number

type: "content\_block\_location"

Accepts one of the following:

"content\_block\_location"

BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

Accepts one of the following:

"web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string | null

type: "search\_result\_location"

Accepts one of the following:

"search\_result\_location"

text: string

type: "text"

Accepts one of the following:

"text"

BetaThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

BetaRedactedThinkingBlock { data, type }

data: string

type: "redacted\_thinking"

Accepts one of the following:

"redacted\_thinking"

BetaToolUseBlock { id, input, name, 2 more }

id: string

input: Record<string, unknown>

name: string

type: "tool\_use"

Accepts one of the following:

"tool\_use"

caller?: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

Accepts one of the following:

"code\_execution\_20250825"

BetaServerToolUseBlock { id, input, name, 2 more }

id: string

input: Record<string, unknown>

name: "web\_search" | "web\_fetch" | "code\_execution" | 4 more

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

Accepts one of the following:

"server\_tool\_use"

caller?: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

Accepts one of the following:

"code\_execution\_20250825"

BetaWebSearchToolResultBlock { content, tool\_use\_id, type }

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

BetaWebSearchToolResultError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

Accepts one of the following:

"web\_search\_tool\_result\_error"

Array<[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } >

encrypted\_content: string

page\_age: string | null

title: string

type: "web\_search\_result"

Accepts one of the following:

"web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

Accepts one of the following:

"web\_search\_tool\_result"

BetaWebFetchToolResultBlock { content, tool\_use\_id, type }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

Accepts one of the following:

"web\_fetch\_tool\_result\_error"

BetaWebFetchBlock { content, retrieved\_at, type, url }

content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type }

citations: [BetaCitationConfig](api/beta.md) { enabled }  | null

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

Accepts one of the following:

BetaBase64PDFSource { data, media\_type, type }

data: string

media\_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media\_type, type }

data: string

media\_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

title: string | null

The title of the document

type: "document"

Accepts one of the following:

"document"

retrieved\_at: string | null

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

Accepts one of the following:

"web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

Accepts one of the following:

"web\_fetch\_tool\_result"

BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

Accepts one of the following:

"code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array<[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } >

file\_id: string

type: "code\_execution\_output"

Accepts one of the following:

"code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

Accepts one of the following:

"code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

Accepts one of the following:

"code\_execution\_tool\_result"

BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError { error\_code, type }

error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | 2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

Accepts one of the following:

"bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array<[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } >

file\_id: string

type: "bash\_code\_execution\_output"

Accepts one of the following:

"bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

Accepts one of the following:

"bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

Accepts one of the following:

"bash\_code\_execution\_tool\_result"

BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | 2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string | null

type: "text\_editor\_code\_execution\_tool\_result\_error"

Accepts one of the following:

"text\_editor\_code\_execution\_tool\_result\_error"

BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" | "image" | "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: number | null

start\_line: number | null

total\_lines: number | null

type: "text\_editor\_code\_execution\_view\_result"

Accepts one of the following:

"text\_editor\_code\_execution\_view\_result"

BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

Accepts one of the following:

"text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array<string> | null

new\_lines: number | null

new\_start: number | null

old\_lines: number | null

old\_start: number | null

type: "text\_editor\_code\_execution\_str\_replace\_result"

Accepts one of the following:

"text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

Accepts one of the following:

"text\_editor\_code\_execution\_tool\_result"

BetaToolSearchToolResultBlock { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

Accepts one of the following:

BetaToolSearchToolResultError { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | "execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string | null

type: "tool\_search\_tool\_result\_error"

Accepts one of the following:

"tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array<[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } >

tool\_name: string

type: "tool\_reference"

Accepts one of the following:

"tool\_reference"

type: "tool\_search\_tool\_search\_result"

Accepts one of the following:

"tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

Accepts one of the following:

"tool\_search\_tool\_result"

BetaMCPToolUseBlock { id, input, name, 2 more }

id: string

input: Record<string, unknown>

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

Accepts one of the following:

"mcp\_tool\_use"

BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type }

content: string | Array<[BetaTextBlock](api/beta.md) { citations, text, type } >

Accepts one of the following:

string

Array<[BetaTextBlock](api/beta.md) { citations, text, type } >

citations: Array<[BetaTextCitation](api/beta.md)> | null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

file\_id: string | null

start\_char\_index: number

type: "char\_location"

Accepts one of the following:

"char\_location"

BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

file\_id: string | null

start\_page\_number: number

type: "page\_location"

Accepts one of the following:

"page\_location"

BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_block\_index: number

file\_id: string | null

start\_block\_index: number

type: "content\_block\_location"

Accepts one of the following:

"content\_block\_location"

BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

Accepts one of the following:

"web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string | null

type: "search\_result\_location"

Accepts one of the following:

"search\_result\_location"

text: string

type: "text"

Accepts one of the following:

"text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

Accepts one of the following:

"mcp\_tool\_result"

BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

Accepts one of the following:

"container\_upload"

BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string | null

Summary of compacted content, or null if compaction failed

type: "compaction"

Accepts one of the following:

"compaction"

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }  | null

Context management response.

Information about context management strategies applied during the request.

applied\_edits: Array<[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } >

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared\_tool\_uses: number

Number of tool uses that were cleared.

minimum0

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

Accepts one of the following:

"clear\_tool\_uses\_20250919"

BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

minimum0

type: "clear\_thinking\_20251015"

The type of context management edit applied.

Accepts one of the following:

"clear\_thinking\_20251015"

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" | "claude-opus-4-5-20251101" | "claude-opus-4-5" | 18 more

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop\_reason: [BetaStopReason](api/beta.md) | null

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

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string | null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: number | null

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: number | null

The number of input tokens read from the cache.

minimum0

inference\_geo: string | null

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

minimum0

iterations: [BetaIterationsUsage](api/beta.md) | null

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

minimum0

input\_tokens: number

The number of input tokens which were used.

minimum0

output\_tokens: number

The number of output tokens which were used.

minimum0

type: "message"

Usage for a sampling iteration

Accepts one of the following:

"message"

BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

minimum0

input\_tokens: number

The number of input tokens which were used.

minimum0

output\_tokens: number

The number of output tokens which were used.

minimum0

type: "compaction"

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output\_tokens: number

The number of output tokens which were used.

minimum0

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }  | null

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

minimum0

web\_search\_requests: number

The number of web search tool requests.

minimum0

service\_tier: "standard" | "priority" | "batch" | null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: "standard" | "fast" | null

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

type: "succeeded"

Accepts one of the following:

"succeeded"

BetaMessageBatchErroredResult { error, type }

error: [BetaErrorResponse](api/beta.md) { error, request\_id, type }

error: [BetaError](api/beta.md)

Accepts one of the following:

BetaInvalidRequestError { message, type }

message: string

type: "invalid\_request\_error"

Accepts one of the following:

"invalid\_request\_error"

BetaAuthenticationError { message, type }

message: string

type: "authentication\_error"

Accepts one of the following:

"authentication\_error"

BetaBillingError { message, type }

message: string

type: "billing\_error"

Accepts one of the following:

"billing\_error"

BetaPermissionError { message, type }

message: string

type: "permission\_error"

Accepts one of the following:

"permission\_error"

BetaNotFoundError { message, type }

message: string

type: "not\_found\_error"

Accepts one of the following:

"not\_found\_error"

BetaRateLimitError { message, type }

message: string

type: "rate\_limit\_error"

Accepts one of the following:

"rate\_limit\_error"

BetaGatewayTimeoutError { message, type }

message: string

type: "timeout\_error"

Accepts one of the following:

"timeout\_error"

BetaAPIError { message, type }

message: string

type: "api\_error"

Accepts one of the following:

"api\_error"

BetaOverloadedError { message, type }

message: string

type: "overloaded\_error"

Accepts one of the following:

"overloaded\_error"

request\_id: string | null

type: "error"

Accepts one of the following:

"error"

type: "errored"

Accepts one of the following:

"errored"

BetaMessageBatchCanceledResult { type }

type: "canceled"

Accepts one of the following:

"canceled"

BetaMessageBatchExpiredResult { type }

type: "expired"

Accepts one of the following:

"expired"

BetaMessageBatchSucceededResult { message, type }

message: [BetaMessage](api/beta.md) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }  | null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

formatdate-time

skills: Array<[BetaSkill](api/beta.md) { skill\_id, type, version } > | null

Skills loaded in the container

skill\_id: string

Skill ID

maxLength64

minLength1

type: "anthropic" | "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: Array<[BetaContentBlock](api/beta.md)>

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

BetaTextBlock { citations, text, type }

citations: Array<[BetaTextCitation](api/beta.md)> | null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

file\_id: string | null

start\_char\_index: number

type: "char\_location"

Accepts one of the following:

"char\_location"

BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

file\_id: string | null

start\_page\_number: number

type: "page\_location"

Accepts one of the following:

"page\_location"

BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_block\_index: number

file\_id: string | null

start\_block\_index: number

type: "content\_block\_location"

Accepts one of the following:

"content\_block\_location"

BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

Accepts one of the following:

"web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string | null

type: "search\_result\_location"

Accepts one of the following:

"search\_result\_location"

text: string

type: "text"

Accepts one of the following:

"text"

BetaThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

BetaRedactedThinkingBlock { data, type }

data: string

type: "redacted\_thinking"

Accepts one of the following:

"redacted\_thinking"

BetaToolUseBlock { id, input, name, 2 more }

id: string

input: Record<string, unknown>

name: string

type: "tool\_use"

Accepts one of the following:

"tool\_use"

caller?: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

Accepts one of the following:

"code\_execution\_20250825"

BetaServerToolUseBlock { id, input, name, 2 more }

id: string

input: Record<string, unknown>

name: "web\_search" | "web\_fetch" | "code\_execution" | 4 more

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

Accepts one of the following:

"server\_tool\_use"

caller?: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

Accepts one of the following:

"code\_execution\_20250825"

BetaWebSearchToolResultBlock { content, tool\_use\_id, type }

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

BetaWebSearchToolResultError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

Accepts one of the following:

"web\_search\_tool\_result\_error"

Array<[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } >

encrypted\_content: string

page\_age: string | null

title: string

type: "web\_search\_result"

Accepts one of the following:

"web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

Accepts one of the following:

"web\_search\_tool\_result"

BetaWebFetchToolResultBlock { content, tool\_use\_id, type }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

Accepts one of the following:

"web\_fetch\_tool\_result\_error"

BetaWebFetchBlock { content, retrieved\_at, type, url }

content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type }

citations: [BetaCitationConfig](api/beta.md) { enabled }  | null

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

Accepts one of the following:

BetaBase64PDFSource { data, media\_type, type }

data: string

media\_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media\_type, type }

data: string

media\_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

title: string | null

The title of the document

type: "document"

Accepts one of the following:

"document"

retrieved\_at: string | null

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

Accepts one of the following:

"web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

Accepts one of the following:

"web\_fetch\_tool\_result"

BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

Accepts one of the following:

"code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array<[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } >

file\_id: string

type: "code\_execution\_output"

Accepts one of the following:

"code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

Accepts one of the following:

"code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

Accepts one of the following:

"code\_execution\_tool\_result"

BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError { error\_code, type }

error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | 2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

Accepts one of the following:

"bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array<[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } >

file\_id: string

type: "bash\_code\_execution\_output"

Accepts one of the following:

"bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

Accepts one of the following:

"bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

Accepts one of the following:

"bash\_code\_execution\_tool\_result"

BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | 2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string | null

type: "text\_editor\_code\_execution\_tool\_result\_error"

Accepts one of the following:

"text\_editor\_code\_execution\_tool\_result\_error"

BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" | "image" | "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: number | null

start\_line: number | null

total\_lines: number | null

type: "text\_editor\_code\_execution\_view\_result"

Accepts one of the following:

"text\_editor\_code\_execution\_view\_result"

BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

Accepts one of the following:

"text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array<string> | null

new\_lines: number | null

new\_start: number | null

old\_lines: number | null

old\_start: number | null

type: "text\_editor\_code\_execution\_str\_replace\_result"

Accepts one of the following:

"text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

Accepts one of the following:

"text\_editor\_code\_execution\_tool\_result"

BetaToolSearchToolResultBlock { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

Accepts one of the following:

BetaToolSearchToolResultError { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" | "unavailable" | "too\_many\_requests" | "execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string | null

type: "tool\_search\_tool\_result\_error"

Accepts one of the following:

"tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array<[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } >

tool\_name: string

type: "tool\_reference"

Accepts one of the following:

"tool\_reference"

type: "tool\_search\_tool\_search\_result"

Accepts one of the following:

"tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

Accepts one of the following:

"tool\_search\_tool\_result"

BetaMCPToolUseBlock { id, input, name, 2 more }

id: string

input: Record<string, unknown>

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

Accepts one of the following:

"mcp\_tool\_use"

BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type }

content: string | Array<[BetaTextBlock](api/beta.md) { citations, text, type } >

Accepts one of the following:

string

Array<[BetaTextBlock](api/beta.md) { citations, text, type } >

citations: Array<[BetaTextCitation](api/beta.md)> | null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_char\_index: number

file\_id: string | null

start\_char\_index: number

type: "char\_location"

Accepts one of the following:

"char\_location"

BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_page\_number: number

file\_id: string | null

start\_page\_number: number

type: "page\_location"

Accepts one of the following:

"page\_location"

BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string | null

end\_block\_index: number

file\_id: string | null

start\_block\_index: number

type: "content\_block\_location"

Accepts one of the following:

"content\_block\_location"

BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string | null

type: "web\_search\_result\_location"

Accepts one of the following:

"web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string | null

type: "search\_result\_location"

Accepts one of the following:

"search\_result\_location"

text: string

type: "text"

Accepts one of the following:

"text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

Accepts one of the following:

"mcp\_tool\_result"

BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

Accepts one of the following:

"container\_upload"

BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string | null

Summary of compacted content, or null if compaction failed

type: "compaction"

Accepts one of the following:

"compaction"

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }  | null

Context management response.

Information about context management strategies applied during the request.

applied\_edits: Array<[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } >

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared\_tool\_uses: number

Number of tool uses that were cleared.

minimum0

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

Accepts one of the following:

"clear\_tool\_uses\_20250919"

BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

minimum0

type: "clear\_thinking\_20251015"

The type of context management edit applied.

Accepts one of the following:

"clear\_thinking\_20251015"

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" | "claude-opus-4-5-20251101" | "claude-opus-4-5" | 18 more

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop\_reason: [BetaStopReason](api/beta.md) | null

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

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string | null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: number | null

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: number | null

The number of input tokens read from the cache.

minimum0

inference\_geo: string | null

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

minimum0

iterations: [BetaIterationsUsage](api/beta.md) | null

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

minimum0

input\_tokens: number

The number of input tokens which were used.

minimum0

output\_tokens: number

The number of output tokens which were used.

minimum0

type: "message"

Usage for a sampling iteration

Accepts one of the following:

"message"

BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }  | null

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

minimum0

input\_tokens: number

The number of input tokens which were used.

minimum0

output\_tokens: number

The number of output tokens which were used.

minimum0

type: "compaction"

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output\_tokens: number

The number of output tokens which were used.

minimum0

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }  | null

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

minimum0

web\_search\_requests: number

The number of web search tool requests.

minimum0

service\_tier: "standard" | "priority" | "batch" | null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: "standard" | "fast" | null

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

type: "succeeded"

Accepts one of the following:

"succeeded"

---

*Copyright © Anthropic. All rights reserved.*
