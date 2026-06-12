# Stream Session Thread Events

Copy page

SDK language

Python

# Stream Session Thread Events

beta.sessions.threads.events.stream(strthread\_id, EventStreamParams\*\*kwargs)  -> [BetaManagedAgentsStreamSessionThreadEvents](api/beta.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

Stream Session Thread Events

##### ParametersExpand Collapse

session\_id: str

thread\_id: str



betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

One of the following:

str



Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

##### ReturnsExpand Collapse



[BetaManagedAgentsStreamSessionThreadEvents](api/beta.md)

Server-sent event in a single thread's stream.

One of the following:



class BetaManagedAgentsUserMessageEvent: …

A user message event in the session conversation.

id: str

Unique identifier for this event.



content: List[Content]

Array of content blocks comprising the user message.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

type: Literal["user.message"]

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format



class BetaManagedAgentsUserInterruptEvent: …

An interrupt event that pauses agent execution and returns control to the user.

id: str

Unique identifier for this event.

type: Literal["user.interrupt"]

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

session\_thread\_id: Optional[str]

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserToolConfirmationEvent: …

A tool confirmation event that approves or denies a pending tool execution.

id: str

Unique identifier for this event.



result: Literal["allow", "deny"]

UserToolConfirmationResult enum

One of the following:

"allow"

"deny"

tool\_use\_id: str

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: Literal["user.tool\_confirmation"]

deny\_message: Optional[str]

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

session\_thread\_id: Optional[str]

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



class BetaManagedAgentsUserCustomToolResultEvent: …

Event sent by the client providing the result of a custom tool execution.

id: str

Unique identifier for this event.

custom\_tool\_use\_id: str

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: Literal["user.custom\_tool\_result"]



content: Optional[List[Content]]

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.



class BetaManagedAgentsSearchResultBlock: …

A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](api/beta.md)

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: List[[BetaManagedAgentsSearchResultContent](api/beta.md)]

Array of text content blocks from the search result.

text: str

The text content.

type: Literal["text"]

source: str

The URL source of the search result.

title: str

The title of the search result.

type: Literal["search\_result"]

is\_error: Optional[bool]

Whether the tool execution resulted in an error.

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

session\_thread\_id: Optional[str]

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



class BetaManagedAgentsAgentCustomToolUseEvent: …

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: str

Unique identifier for this event.

input: Dict[str, object]

Input parameters for the tool call.

name: str

Name of the custom tool being called.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.custom\_tool\_use"]

session\_thread\_id: Optional[str]

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



class BetaManagedAgentsAgentMessageEvent: …

An agent response event in the session conversation.

id: str

Unique identifier for this event.



content: List[[BetaManagedAgentsTextBlock](api/beta.md)]

Array of text blocks comprising the agent response.

text: str

The text content.

type: Literal["text"]

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.message"]



class BetaManagedAgentsAgentThinkingEvent: …

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.thinking"]



class BetaManagedAgentsAgentMCPToolUseEvent: …

Event emitted when the agent invokes a tool provided by an MCP server.

id: str

Unique identifier for this event.

input: Dict[str, object]

Input parameters for the tool call.

mcp\_server\_name: str

Name of the MCP server providing the tool.

name: str

Name of the MCP tool being used.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.mcp\_tool\_use"]



evaluated\_permission: Optional[Literal["allow", "ask", "deny"]]

AgentEvaluatedPermission enum

One of the following:

"allow"

"ask"

"deny"

session\_thread\_id: Optional[str]

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentMCPToolResultEvent: …

Event representing the result of an MCP tool execution.

id: str

Unique identifier for this event.

mcp\_tool\_use\_id: str

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.mcp\_tool\_result"]



content: Optional[List[Content]]

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.



class BetaManagedAgentsSearchResultBlock: …

A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](api/beta.md)

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: List[[BetaManagedAgentsSearchResultContent](api/beta.md)]

Array of text content blocks from the search result.

text: str

The text content.

type: Literal["text"]

source: str

The URL source of the search result.

title: str

The title of the search result.

type: Literal["search\_result"]

is\_error: Optional[bool]

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentToolUseEvent: …

Event emitted when the agent invokes a built-in agent tool.

id: str

Unique identifier for this event.

input: Dict[str, object]

Input parameters for the tool call.

name: str

Name of the agent tool being used.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.tool\_use"]



evaluated\_permission: Optional[Literal["allow", "ask", "deny"]]

AgentEvaluatedPermission enum

One of the following:

"allow"

"ask"

"deny"

session\_thread\_id: Optional[str]

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentToolResultEvent: …

Event representing the result of an agent tool execution.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

tool\_use\_id: str

The id of the `agent.tool_use` event this result corresponds to.

type: Literal["agent.tool\_result"]



content: Optional[List[Content]]

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.



class BetaManagedAgentsSearchResultBlock: …

A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](api/beta.md)

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: List[[BetaManagedAgentsSearchResultContent](api/beta.md)]

Array of text content blocks from the search result.

text: str

The text content.

type: Literal["text"]

source: str

The URL source of the search result.

title: str

The title of the search result.

type: Literal["search\_result"]

is\_error: Optional[bool]

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentThreadMessageReceivedEvent: …

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

id: str

Unique identifier for this event.



content: List[Content]

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

from\_session\_thread\_id: str

Public `sthr_` ID of the thread that sent the message.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.thread\_message\_received"]

from\_agent\_name: Optional[str]

Name of the callable agent this message came from. Absent when received from the primary agent.



class BetaManagedAgentsAgentThreadMessageSentEvent: …

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

id: str

Unique identifier for this event.



content: List[Content]

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

processed\_at: datetime

A timestamp in RFC 3339 format

to\_session\_thread\_id: str

Public `sthr_` ID of the thread the message was sent to.

type: Literal["agent.thread\_message\_sent"]

to\_agent\_name: Optional[str]

Name of the callable agent this message was sent to. Absent when sent to the primary agent.



class BetaManagedAgentsAgentThreadContextCompactedEvent: …

Indicates that context compaction (summarization) occurred during the session.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.thread\_context\_compacted"]



class BetaManagedAgentsSessionErrorEvent: …

An error event indicating a problem occurred during session execution.

id: str

Unique identifier for this event.



error: Error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

One of the following:



class BetaManagedAgentsUnknownError: …

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: str

Human-readable error description.



retry\_status: RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]



class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]



class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["unknown\_error"]



class BetaManagedAgentsModelOverloadedError: …

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: str

Human-readable error description.



retry\_status: RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]



class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]



class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["model\_overloaded\_error"]



class BetaManagedAgentsModelRateLimitedError: …

The model request was rate-limited.

message: str

Human-readable error description.



retry\_status: RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]



class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]



class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["model\_rate\_limited\_error"]



class BetaManagedAgentsModelRequestFailedError: …

A model request failed for a reason other than overload or rate-limiting.

message: str

Human-readable error description.



retry\_status: RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]



class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]



class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["model\_request\_failed\_error"]



class BetaManagedAgentsMCPConnectionFailedError: …

Failed to connect to an MCP server.

mcp\_server\_name: str

Name of the MCP server that failed to connect.

message: str

Human-readable error description.



retry\_status: RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]



class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]



class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["mcp\_connection\_failed\_error"]



class BetaManagedAgentsMCPAuthenticationFailedError: …

Authentication to an MCP server failed.

mcp\_server\_name: str

Name of the MCP server that failed authentication.

message: str

Human-readable error description.



retry\_status: RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]



class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]



class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["mcp\_authentication\_failed\_error"]



class BetaManagedAgentsBillingError: …

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: str

Human-readable error description.



retry\_status: RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]



class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]



class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["billing\_error"]



class BetaManagedAgentsCredentialHostUnreachableError: …

An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

credential\_id: str

ID of the affected credential.

message: str

Human-readable error description.



retry\_status: RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]



class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]



class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["credential\_host\_unreachable\_error"]

vault\_id: str

ID of the vault containing the affected credential.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.error"]



class BetaManagedAgentsSessionStatusRescheduledEvent: …

Indicates the session is recovering from an error state and is rescheduled for execution.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.status\_rescheduled"]



class BetaManagedAgentsSessionStatusRunningEvent: …

Indicates the session is actively running and the agent is working.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.status\_running"]



class BetaManagedAgentsSessionStatusIdleEvent: …

Indicates the agent has paused and is awaiting user input.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format



stop\_reason: StopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn: …

The agent completed its turn naturally and is ready for the next user message.

type: Literal["end\_turn"]



class BetaManagedAgentsSessionRequiresAction: …

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: List[str]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: Literal["requires\_action"]



class BetaManagedAgentsSessionRetriesExhausted: …

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: Literal["retries\_exhausted"]

type: Literal["session.status\_idle"]



class BetaManagedAgentsSessionStatusTerminatedEvent: …

Indicates the session has terminated, either due to an error or completion.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.status\_terminated"]



class BetaManagedAgentsSessionThreadCreatedEvent: …

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

id: str

Unique identifier for this event.

agent\_name: str

Name of the callable agent the thread runs.

processed\_at: datetime

A timestamp in RFC 3339 format

session\_thread\_id: str

Public `sthr_` ID of the newly created thread.

type: Literal["session.thread\_created"]



class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …

Emitted when an outcome evaluation cycle begins.

id: str

Unique identifier for this event.

iteration: int

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

outcome\_id: str

The `outc_` ID of the outcome being evaluated.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["span.outcome\_evaluation\_start"]



class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

id: str

Unique identifier for this event.

explanation: str

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

iteration: int

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_evaluation\_start\_id: str

The id of the corresponding `span.outcome_evaluation_start` event.

outcome\_id: str

The `outc_` ID of the outcome being evaluated.

processed\_at: datetime

A timestamp in RFC 3339 format

result: str

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

type: Literal["span.outcome\_evaluation\_end"]



usage: [BetaManagedAgentsSpanModelUsage](api/beta.md)

Token usage for a single model request.

cache\_creation\_input\_tokens: int

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: int

Tokens read from prompt cache in this request.

input\_tokens: int

Input tokens consumed by this request.

output\_tokens: int

Output tokens generated by this request.



speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



class BetaManagedAgentsSpanModelRequestStartEvent: …

Emitted when a model request is initiated by the agent.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["span.model\_request\_start"]



class BetaManagedAgentsSpanModelRequestEndEvent: …

Emitted when a model request completes.

id: str

Unique identifier for this event.

is\_error: Optional[bool]

Whether the model request resulted in an error.

model\_request\_start\_id: str

The id of the corresponding `span.model_request_start` event.



model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta.md)

Token usage for a single model request.

cache\_creation\_input\_tokens: int

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: int

Tokens read from prompt cache in this request.

input\_tokens: int

Input tokens consumed by this request.

output\_tokens: int

Output tokens generated by this request.



speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["span.model\_request\_end"]



class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

id: str

Unique identifier for this event.

iteration: int

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_id: str

The `outc_` ID of the outcome being evaluated.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["span.outcome\_evaluation\_ongoing"]



class BetaManagedAgentsUserDefineOutcomeEvent: …

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

id: str

Unique identifier for this event.

description: str

What the agent should produce. Copied from the input event.

max\_iterations: Optional[int]

Evaluate-then-revise cycles before giving up. Default 3, max 20.

outcome\_id: str

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

processed\_at: datetime

A timestamp in RFC 3339 format



rubric: Rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric: …

Rubric referenced by a file uploaded via the Files API.

file\_id: str

ID of the rubric file.

type: Literal["file"]



class BetaManagedAgentsTextRubric: …

Rubric content provided inline as text.

content: str

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: Literal["text"]

type: Literal["user.define\_outcome"]



class BetaManagedAgentsSessionDeletedEvent: …

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.deleted"]



class BetaManagedAgentsSessionThreadStatusRunningEvent: …

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: str

Unique identifier for this event.

agent\_name: str

Name of the agent the thread runs.

processed\_at: datetime

A timestamp in RFC 3339 format

session\_thread\_id: str

Public sthr\_ ID of the thread that started running.

type: Literal["session.thread\_status\_running"]



class BetaManagedAgentsSessionThreadStatusIdleEvent: …

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: str

Unique identifier for this event.

agent\_name: str

Name of the agent the thread runs.

processed\_at: datetime

A timestamp in RFC 3339 format

session\_thread\_id: str

Public sthr\_ ID of the thread that went idle.



stop\_reason: StopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn: …

The agent completed its turn naturally and is ready for the next user message.

type: Literal["end\_turn"]



class BetaManagedAgentsSessionRequiresAction: …

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: List[str]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: Literal["requires\_action"]



class BetaManagedAgentsSessionRetriesExhausted: …

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: Literal["retries\_exhausted"]

type: Literal["session.thread\_status\_idle"]



class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: str

Unique identifier for this event.

agent\_name: str

Name of the agent the thread runs.

processed\_at: datetime

A timestamp in RFC 3339 format

session\_thread\_id: str

Public sthr\_ ID of the thread that terminated.

type: Literal["session.thread\_status\_terminated"]



class BetaManagedAgentsUserToolResultEvent: …

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

id: str

Unique identifier for this event.

tool\_use\_id: str

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: Literal["user.tool\_result"]



content: Optional[List[Content]]

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.



class BetaManagedAgentsSearchResultBlock: …

A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](api/beta.md)

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: List[[BetaManagedAgentsSearchResultContent](api/beta.md)]

Array of text content blocks from the search result.

text: str

The text content.

type: Literal["text"]

source: str

The URL source of the search result.

title: str

The title of the search result.

type: Literal["search\_result"]

is\_error: Optional[bool]

Whether the tool execution resulted in an error.

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

session\_thread\_id: Optional[str]

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.



class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: str

Unique identifier for this event.

agent\_name: str

Name of the agent the thread runs.

processed\_at: datetime

A timestamp in RFC 3339 format

session\_thread\_id: str

Public sthr\_ ID of the thread that is retrying.

type: Literal["session.thread\_status\_rescheduled"]



class BetaManagedAgentsSessionUpdatedEvent: …

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.updated"]



agent: Optional[BetaManagedAgentsSessionAgent]

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: str

description: Optional[str]



mcp\_servers: List[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md)]

name: str

type: Literal["url"]

url: str



model: [BetaManagedAgentsModelConfig](api/beta.md)

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-opus-4-8", "claude-opus-4-7", 8 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

One of the following:

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

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

str



speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]

Resolved coordinator topology with full agent definitions for each roster member.



agents: List[[BetaManagedAgentsSessionThreadAgent](api/beta.md)]

Full `agent` definitions the coordinator may spawn as session threads.

id: str

description: Optional[str]



mcp\_servers: List[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md)]

name: str

type: Literal["url"]

url: str



model: [BetaManagedAgentsModelConfig](api/beta.md)

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-opus-4-8", "claude-opus-4-7", 8 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

One of the following:

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

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

str



speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: str



skills: List[Skill]

One of the following:



class BetaManagedAgentsAnthropicSkill: …

A resolved Anthropic-managed skill.

skill\_id: str

type: Literal["anthropic"]

version: str



class BetaManagedAgentsCustomSkill: …

A resolved user-created custom skill.

skill\_id: str

type: Literal["custom"]

version: str

system: Optional[str]



tools: List[Tool]

One of the following:



class BetaManagedAgentsAgentToolset20260401: …



configs: List[[BetaManagedAgentsAgentToolConfig](api/beta.md)]

enabled: bool



name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md)

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

type: Literal["agent\_toolset\_20260401"]



class BetaManagedAgentsMCPToolset: …



configs: List[[BetaManagedAgentsMCPToolConfig](api/beta.md)]

enabled: bool

name: str



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md)

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

mcp\_server\_name: str

type: Literal["mcp\_toolset"]



class BetaManagedAgentsCustomTool: …

A custom tool as returned in API responses.

description: str



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

type: Literal["custom"]

type: Literal["agent"]

version: int

type: Literal["coordinator"]

name: str



skills: List[Skill]

One of the following:



class BetaManagedAgentsAnthropicSkill: …

A resolved Anthropic-managed skill.

skill\_id: str

type: Literal["anthropic"]

version: str



class BetaManagedAgentsCustomSkill: …

A resolved user-created custom skill.

skill\_id: str

type: Literal["custom"]

version: str

system: Optional[str]



tools: List[Tool]

One of the following:



class BetaManagedAgentsAgentToolset20260401: …



configs: List[[BetaManagedAgentsAgentToolConfig](api/beta.md)]

enabled: bool



name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md)

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

type: Literal["agent\_toolset\_20260401"]



class BetaManagedAgentsMCPToolset: …



configs: List[[BetaManagedAgentsMCPToolConfig](api/beta.md)]

enabled: bool

name: str



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md)

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

mcp\_server\_name: str

type: Literal["mcp\_toolset"]



class BetaManagedAgentsCustomTool: …

A custom tool as returned in API responses.

description: str



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

type: Literal["custom"]

type: Literal["agent"]

version: int

metadata: Optional[Dict[str, str]]

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

title: Optional[str]

The session's new title. Present only when the update changed it.



class BetaManagedAgentsSystemMessageEvent: …

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

id: str

Unique identifier for this event.



content: List[[BetaManagedAgentsSystemContentBlock](api/beta.md)]

System content blocks. Text-only.

text: str

The text content.

type: Literal["text"]

type: Literal["system.message"]

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format



[BetaManagedAgentsStreamSessionThreadEvents](api/beta.md)

Server-sent event in a single thread's stream.

One of the following:



class BetaManagedAgentsUserMessageEvent: …

A user message event in the session conversation.

id: str

Unique identifier for this event.



content: List[Content]

Array of content blocks comprising the user message.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

type: Literal["user.message"]

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format



class BetaManagedAgentsUserInterruptEvent: …

An interrupt event that pauses agent execution and returns control to the user.

id: str

Unique identifier for this event.

type: Literal["user.interrupt"]

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

session\_thread\_id: Optional[str]

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserToolConfirmationEvent: …

A tool confirmation event that approves or denies a pending tool execution.

id: str

Unique identifier for this event.



result: Literal["allow", "deny"]

UserToolConfirmationResult enum

One of the following:

"allow"

"deny"

tool\_use\_id: str

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: Literal["user.tool\_confirmation"]

deny\_message: Optional[str]

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

session\_thread\_id: Optional[str]

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



class BetaManagedAgentsUserCustomToolResultEvent: …

Event sent by the client providing the result of a custom tool execution.

id: str

Unique identifier for this event.

custom\_tool\_use\_id: str

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: Literal["user.custom\_tool\_result"]



content: Optional[List[Content]]

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.



class BetaManagedAgentsSearchResultBlock: …

A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](api/beta.md)

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: List[[BetaManagedAgentsSearchResultContent](api/beta.md)]

Array of text content blocks from the search result.

text: str

The text content.

type: Literal["text"]

source: str

The URL source of the search result.

title: str

The title of the search result.

type: Literal["search\_result"]

is\_error: Optional[bool]

Whether the tool execution resulted in an error.

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

session\_thread\_id: Optional[str]

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



class BetaManagedAgentsAgentCustomToolUseEvent: …

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: str

Unique identifier for this event.

input: Dict[str, object]

Input parameters for the tool call.

name: str

Name of the custom tool being called.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.custom\_tool\_use"]

session\_thread\_id: Optional[str]

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



class BetaManagedAgentsAgentMessageEvent: …

An agent response event in the session conversation.

id: str

Unique identifier for this event.



content: List[[BetaManagedAgentsTextBlock](api/beta.md)]

Array of text blocks comprising the agent response.

text: str

The text content.

type: Literal["text"]

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.message"]



class BetaManagedAgentsAgentThinkingEvent: …

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.thinking"]



class BetaManagedAgentsAgentMCPToolUseEvent: …

Event emitted when the agent invokes a tool provided by an MCP server.

id: str

Unique identifier for this event.

input: Dict[str, object]

Input parameters for the tool call.

mcp\_server\_name: str

Name of the MCP server providing the tool.

name: str

Name of the MCP tool being used.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.mcp\_tool\_use"]



evaluated\_permission: Optional[Literal["allow", "ask", "deny"]]

AgentEvaluatedPermission enum

One of the following:

"allow"

"ask"

"deny"

session\_thread\_id: Optional[str]

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentMCPToolResultEvent: …

Event representing the result of an MCP tool execution.

id: str

Unique identifier for this event.

mcp\_tool\_use\_id: str

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.mcp\_tool\_result"]



content: Optional[List[Content]]

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.



class BetaManagedAgentsSearchResultBlock: …

A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](api/beta.md)

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: List[[BetaManagedAgentsSearchResultContent](api/beta.md)]

Array of text content blocks from the search result.

text: str

The text content.

type: Literal["text"]

source: str

The URL source of the search result.

title: str

The title of the search result.

type: Literal["search\_result"]

is\_error: Optional[bool]

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentToolUseEvent: …

Event emitted when the agent invokes a built-in agent tool.

id: str

Unique identifier for this event.

input: Dict[str, object]

Input parameters for the tool call.

name: str

Name of the agent tool being used.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.tool\_use"]



evaluated\_permission: Optional[Literal["allow", "ask", "deny"]]

AgentEvaluatedPermission enum

One of the following:

"allow"

"ask"

"deny"

session\_thread\_id: Optional[str]

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentToolResultEvent: …

Event representing the result of an agent tool execution.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

tool\_use\_id: str

The id of the `agent.tool_use` event this result corresponds to.

type: Literal["agent.tool\_result"]



content: Optional[List[Content]]

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.



class BetaManagedAgentsSearchResultBlock: …

A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](api/beta.md)

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: List[[BetaManagedAgentsSearchResultContent](api/beta.md)]

Array of text content blocks from the search result.

text: str

The text content.

type: Literal["text"]

source: str

The URL source of the search result.

title: str

The title of the search result.

type: Literal["search\_result"]

is\_error: Optional[bool]

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentThreadMessageReceivedEvent: …

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

id: str

Unique identifier for this event.



content: List[Content]

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

from\_session\_thread\_id: str

Public `sthr_` ID of the thread that sent the message.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.thread\_message\_received"]

from\_agent\_name: Optional[str]

Name of the callable agent this message came from. Absent when received from the primary agent.



class BetaManagedAgentsAgentThreadMessageSentEvent: …

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

id: str

Unique identifier for this event.



content: List[Content]

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

processed\_at: datetime

A timestamp in RFC 3339 format

to\_session\_thread\_id: str

Public `sthr_` ID of the thread the message was sent to.

type: Literal["agent.thread\_message\_sent"]

to\_agent\_name: Optional[str]

Name of the callable agent this message was sent to. Absent when sent to the primary agent.



class BetaManagedAgentsAgentThreadContextCompactedEvent: …

Indicates that context compaction (summarization) occurred during the session.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.thread\_context\_compacted"]



class BetaManagedAgentsSessionErrorEvent: …

An error event indicating a problem occurred during session execution.

id: str

Unique identifier for this event.



error: Error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

One of the following:



class BetaManagedAgentsUnknownError: …

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: str

Human-readable error description.



retry\_status: RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]



class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]



class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["unknown\_error"]



class BetaManagedAgentsModelOverloadedError: …

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: str

Human-readable error description.



retry\_status: RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]



class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]



class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["model\_overloaded\_error"]



class BetaManagedAgentsModelRateLimitedError: …

The model request was rate-limited.

message: str

Human-readable error description.



retry\_status: RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]



class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]



class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["model\_rate\_limited\_error"]



class BetaManagedAgentsModelRequestFailedError: …

A model request failed for a reason other than overload or rate-limiting.

message: str

Human-readable error description.



retry\_status: RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]



class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]



class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["model\_request\_failed\_error"]



class BetaManagedAgentsMCPConnectionFailedError: …

Failed to connect to an MCP server.

mcp\_server\_name: str

Name of the MCP server that failed to connect.

message: str

Human-readable error description.



retry\_status: RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]



class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]



class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["mcp\_connection\_failed\_error"]



class BetaManagedAgentsMCPAuthenticationFailedError: …

Authentication to an MCP server failed.

mcp\_server\_name: str

Name of the MCP server that failed authentication.

message: str

Human-readable error description.



retry\_status: RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]



class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]



class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["mcp\_authentication\_failed\_error"]



class BetaManagedAgentsBillingError: …

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: str

Human-readable error description.



retry\_status: RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]



class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]



class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["billing\_error"]



class BetaManagedAgentsCredentialHostUnreachableError: …

An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

credential\_id: str

ID of the affected credential.

message: str

Human-readable error description.



retry\_status: RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]



class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]



class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["credential\_host\_unreachable\_error"]

vault\_id: str

ID of the vault containing the affected credential.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.error"]



class BetaManagedAgentsSessionStatusRescheduledEvent: …

Indicates the session is recovering from an error state and is rescheduled for execution.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.status\_rescheduled"]



class BetaManagedAgentsSessionStatusRunningEvent: …

Indicates the session is actively running and the agent is working.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.status\_running"]



class BetaManagedAgentsSessionStatusIdleEvent: …

Indicates the agent has paused and is awaiting user input.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format



stop\_reason: StopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn: …

The agent completed its turn naturally and is ready for the next user message.

type: Literal["end\_turn"]



class BetaManagedAgentsSessionRequiresAction: …

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: List[str]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: Literal["requires\_action"]



class BetaManagedAgentsSessionRetriesExhausted: …

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: Literal["retries\_exhausted"]

type: Literal["session.status\_idle"]



class BetaManagedAgentsSessionStatusTerminatedEvent: …

Indicates the session has terminated, either due to an error or completion.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.status\_terminated"]



class BetaManagedAgentsSessionThreadCreatedEvent: …

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

id: str

Unique identifier for this event.

agent\_name: str

Name of the callable agent the thread runs.

processed\_at: datetime

A timestamp in RFC 3339 format

session\_thread\_id: str

Public `sthr_` ID of the newly created thread.

type: Literal["session.thread\_created"]



class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …

Emitted when an outcome evaluation cycle begins.

id: str

Unique identifier for this event.

iteration: int

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

outcome\_id: str

The `outc_` ID of the outcome being evaluated.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["span.outcome\_evaluation\_start"]



class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

id: str

Unique identifier for this event.

explanation: str

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

iteration: int

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_evaluation\_start\_id: str

The id of the corresponding `span.outcome_evaluation_start` event.

outcome\_id: str

The `outc_` ID of the outcome being evaluated.

processed\_at: datetime

A timestamp in RFC 3339 format

result: str

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

type: Literal["span.outcome\_evaluation\_end"]



usage: [BetaManagedAgentsSpanModelUsage](api/beta.md)

Token usage for a single model request.

cache\_creation\_input\_tokens: int

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: int

Tokens read from prompt cache in this request.

input\_tokens: int

Input tokens consumed by this request.

output\_tokens: int

Output tokens generated by this request.



speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



class BetaManagedAgentsSpanModelRequestStartEvent: …

Emitted when a model request is initiated by the agent.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["span.model\_request\_start"]



class BetaManagedAgentsSpanModelRequestEndEvent: …

Emitted when a model request completes.

id: str

Unique identifier for this event.

is\_error: Optional[bool]

Whether the model request resulted in an error.

model\_request\_start\_id: str

The id of the corresponding `span.model_request_start` event.



model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta.md)

Token usage for a single model request.

cache\_creation\_input\_tokens: int

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: int

Tokens read from prompt cache in this request.

input\_tokens: int

Input tokens consumed by this request.

output\_tokens: int

Output tokens generated by this request.



speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["span.model\_request\_end"]



class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

id: str

Unique identifier for this event.

iteration: int

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_id: str

The `outc_` ID of the outcome being evaluated.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["span.outcome\_evaluation\_ongoing"]



class BetaManagedAgentsUserDefineOutcomeEvent: …

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

id: str

Unique identifier for this event.

description: str

What the agent should produce. Copied from the input event.

max\_iterations: Optional[int]

Evaluate-then-revise cycles before giving up. Default 3, max 20.

outcome\_id: str

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

processed\_at: datetime

A timestamp in RFC 3339 format



rubric: Rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric: …

Rubric referenced by a file uploaded via the Files API.

file\_id: str

ID of the rubric file.

type: Literal["file"]



class BetaManagedAgentsTextRubric: …

Rubric content provided inline as text.

content: str

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: Literal["text"]

type: Literal["user.define\_outcome"]



class BetaManagedAgentsSessionDeletedEvent: …

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.deleted"]



class BetaManagedAgentsSessionThreadStatusRunningEvent: …

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: str

Unique identifier for this event.

agent\_name: str

Name of the agent the thread runs.

processed\_at: datetime

A timestamp in RFC 3339 format

session\_thread\_id: str

Public sthr\_ ID of the thread that started running.

type: Literal["session.thread\_status\_running"]



class BetaManagedAgentsSessionThreadStatusIdleEvent: …

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: str

Unique identifier for this event.

agent\_name: str

Name of the agent the thread runs.

processed\_at: datetime

A timestamp in RFC 3339 format

session\_thread\_id: str

Public sthr\_ ID of the thread that went idle.



stop\_reason: StopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn: …

The agent completed its turn naturally and is ready for the next user message.

type: Literal["end\_turn"]



class BetaManagedAgentsSessionRequiresAction: …

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: List[str]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: Literal["requires\_action"]



class BetaManagedAgentsSessionRetriesExhausted: …

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: Literal["retries\_exhausted"]

type: Literal["session.thread\_status\_idle"]



class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: str

Unique identifier for this event.

agent\_name: str

Name of the agent the thread runs.

processed\_at: datetime

A timestamp in RFC 3339 format

session\_thread\_id: str

Public sthr\_ ID of the thread that terminated.

type: Literal["session.thread\_status\_terminated"]



class BetaManagedAgentsUserToolResultEvent: …

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

id: str

Unique identifier for this event.

tool\_use\_id: str

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: Literal["user.tool\_result"]



content: Optional[List[Content]]

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.



class BetaManagedAgentsSearchResultBlock: …

A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](api/beta.md)

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: List[[BetaManagedAgentsSearchResultContent](api/beta.md)]

Array of text content blocks from the search result.

text: str

The text content.

type: Literal["text"]

source: str

The URL source of the search result.

title: str

The title of the search result.

type: Literal["search\_result"]

is\_error: Optional[bool]

Whether the tool execution resulted in an error.

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

session\_thread\_id: Optional[str]

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.



class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: str

Unique identifier for this event.

agent\_name: str

Name of the agent the thread runs.

processed\_at: datetime

A timestamp in RFC 3339 format

session\_thread\_id: str

Public sthr\_ ID of the thread that is retrying.

type: Literal["session.thread\_status\_rescheduled"]



class BetaManagedAgentsSessionUpdatedEvent: …

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.updated"]



agent: Optional[BetaManagedAgentsSessionAgent]

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: str

description: Optional[str]



mcp\_servers: List[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md)]

name: str

type: Literal["url"]

url: str



model: [BetaManagedAgentsModelConfig](api/beta.md)

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-opus-4-8", "claude-opus-4-7", 8 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

One of the following:

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

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

str



speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]

Resolved coordinator topology with full agent definitions for each roster member.



agents: List[[BetaManagedAgentsSessionThreadAgent](api/beta.md)]

Full `agent` definitions the coordinator may spawn as session threads.

id: str

description: Optional[str]



mcp\_servers: List[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md)]

name: str

type: Literal["url"]

url: str



model: [BetaManagedAgentsModelConfig](api/beta.md)

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-opus-4-8", "claude-opus-4-7", 8 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

One of the following:

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

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

str



speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: str



skills: List[Skill]

One of the following:



class BetaManagedAgentsAnthropicSkill: …

A resolved Anthropic-managed skill.

skill\_id: str

type: Literal["anthropic"]

version: str



class BetaManagedAgentsCustomSkill: …

A resolved user-created custom skill.

skill\_id: str

type: Literal["custom"]

version: str

system: Optional[str]



tools: List[Tool]

One of the following:



class BetaManagedAgentsAgentToolset20260401: …



configs: List[[BetaManagedAgentsAgentToolConfig](api/beta.md)]

enabled: bool



name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md)

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

type: Literal["agent\_toolset\_20260401"]



class BetaManagedAgentsMCPToolset: …



configs: List[[BetaManagedAgentsMCPToolConfig](api/beta.md)]

enabled: bool

name: str



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md)

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

mcp\_server\_name: str

type: Literal["mcp\_toolset"]



class BetaManagedAgentsCustomTool: …

A custom tool as returned in API responses.

description: str



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

type: Literal["custom"]

type: Literal["agent"]

version: int

type: Literal["coordinator"]

name: str



skills: List[Skill]

One of the following:



class BetaManagedAgentsAnthropicSkill: …

A resolved Anthropic-managed skill.

skill\_id: str

type: Literal["anthropic"]

version: str



class BetaManagedAgentsCustomSkill: …

A resolved user-created custom skill.

skill\_id: str

type: Literal["custom"]

version: str

system: Optional[str]



tools: List[Tool]

One of the following:



class BetaManagedAgentsAgentToolset20260401: …



configs: List[[BetaManagedAgentsAgentToolConfig](api/beta.md)]

enabled: bool



name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md)

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

type: Literal["agent\_toolset\_20260401"]



class BetaManagedAgentsMCPToolset: …



configs: List[[BetaManagedAgentsMCPToolConfig](api/beta.md)]

enabled: bool

name: str



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md)

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]



class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

mcp\_server\_name: str

type: Literal["mcp\_toolset"]



class BetaManagedAgentsCustomTool: …

A custom tool as returned in API responses.

description: str



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

type: Literal["custom"]

type: Literal["agent"]

version: int

metadata: Optional[Dict[str, str]]

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

title: Optional[str]

The session's new title. Present only when the update changed it.



class BetaManagedAgentsSystemMessageEvent: …

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

id: str

Unique identifier for this event.



content: List[[BetaManagedAgentsSystemContentBlock](api/beta.md)]

System content blocks. Text-only.

text: str

The text content.

type: Literal["text"]

type: Literal["system.message"]

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

Stream Session Thread Events

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
for event in client.beta.sessions.threads.events.stream(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
):
  print(event)
```

Response 200



```shiki
{
  "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```

---

*Copyright © Anthropic. All rights reserved.*
