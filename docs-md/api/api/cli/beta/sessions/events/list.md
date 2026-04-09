# List Events

Copy page

CLI

# List Events

$ ant beta:sessions:events list

GET/v1/sessions/{session\_id}/events

List Events

##### ParametersExpand Collapse

--session-id: string

Path param: Path parameter session\_id

--limit: optional number

Query param: Query parameter for limit

--order: optional "asc" or "desc"

Query param: Sort direction for results, ordered by created\_at. Defaults to asc (chronological).

--page: optional string

Query param: Opaque pagination cursor from a previous response's next\_page.

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

BetaManagedAgentsListSessionEvents: object { data, next\_page }

Paginated list of events for a `session`.

data: optional array of [BetaManagedAgentsSessionEvent](api/beta.md)

Events for the session, ordered by `created_at`.

beta\_managed\_agents\_user\_message\_event: object { id, content, type, processed\_at }

A user message event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

Array of content blocks comprising the user message.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

"user.message"

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_user\_interrupt\_event: object { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.

type: "user.interrupt"

"user.interrupt"

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_user\_tool\_confirmation\_event: object { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: string

Unique identifier for this event.

result: "allow" or "deny"

UserToolConfirmationResult enum

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

"user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_user\_custom\_tool\_result\_event: object { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: string

Unique identifier for this event.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

"user.custom\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

The result content returned by the tool.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_agent\_custom\_tool\_use\_event: object { id, input, name, 2 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the custom tool being called.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.custom\_tool\_use"

"agent.custom\_tool\_use"

beta\_managed\_agents\_agent\_message\_event: object { id, content, processed\_at, type }

An agent response event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }

Array of text blocks comprising the agent response.

text: string

The text content.

type: "text"

"text"

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.message"

"agent.message"

beta\_managed\_agents\_agent\_thinking\_event: object { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thinking"

"agent.thinking"

beta\_managed\_agents\_agent\_mcp\_tool\_use\_event: object { id, input, mcp\_server\_name, 4 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

mcp\_server\_name: string

Name of the MCP server providing the tool.

name: string

Name of the MCP tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_use"

"agent.mcp\_tool\_use"

evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

"allow"

"ask"

"deny"

beta\_managed\_agents\_agent\_mcp\_tool\_result\_event: object { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: string

Unique identifier for this event.

mcp\_tool\_use\_id: string

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_result"

"agent.mcp\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

The result content returned by the tool.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

is\_error: optional boolean

Whether the tool execution resulted in an error.

beta\_managed\_agents\_agent\_tool\_use\_event: object { id, input, name, 3 more }

Event emitted when the agent invokes a built-in agent tool.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the agent tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.tool\_use"

"agent.tool\_use"

evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

"allow"

"ask"

"deny"

beta\_managed\_agents\_agent\_tool\_result\_event: object { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to.

type: "agent.tool\_result"

"agent.tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

The result content returned by the tool.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

is\_error: optional boolean

Whether the tool execution resulted in an error.

beta\_managed\_agents\_agent\_thread\_context\_compacted\_event: object { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thread\_context\_compacted"

"agent.thread\_context\_compacted"

beta\_managed\_agents\_session\_error\_event: object { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: string

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](api/beta.md) { message, retry\_status, type }  or [BetaManagedAgentsModelOverloadedError](api/beta.md) { message, retry\_status, type }  or [BetaManagedAgentsModelRateLimitedError](api/beta.md) { message, retry\_status, type }  or 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

beta\_managed\_agents\_unknown\_error: object { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "unknown\_error"

"unknown\_error"

beta\_managed\_agents\_model\_overloaded\_error: object { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "model\_overloaded\_error"

"model\_overloaded\_error"

beta\_managed\_agents\_model\_rate\_limited\_error: object { message, retry\_status, type }

The model request was rate-limited.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "model\_rate\_limited\_error"

"model\_rate\_limited\_error"

beta\_managed\_agents\_model\_request\_failed\_error: object { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "model\_request\_failed\_error"

"model\_request\_failed\_error"

beta\_managed\_agents\_mcp\_connection\_failed\_error: object { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: string

Name of the MCP server that failed to connect.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "mcp\_connection\_failed\_error"

"mcp\_connection\_failed\_error"

beta\_managed\_agents\_mcp\_authentication\_failed\_error: object { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: string

Name of the MCP server that failed authentication.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "mcp\_authentication\_failed\_error"

"mcp\_authentication\_failed\_error"

beta\_managed\_agents\_billing\_error: object { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "billing\_error"

"billing\_error"

processed\_at: string

A timestamp in RFC 3339 format

type: "session.error"

"session.error"

beta\_managed\_agents\_session\_status\_rescheduled\_event: object { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_rescheduled"

"session.status\_rescheduled"

beta\_managed\_agents\_session\_status\_running\_event: object { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_running"

"session.status\_running"

beta\_managed\_agents\_session\_status\_idle\_event: object { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  or [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

beta\_managed\_agents\_session\_end\_turn: object { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

"end\_turn"

beta\_managed\_agents\_session\_requires\_action: object { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

"requires\_action"

beta\_managed\_agents\_session\_retries\_exhausted: object { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

"retries\_exhausted"

type: "session.status\_idle"

"session.status\_idle"

beta\_managed\_agents\_session\_status\_terminated\_event: object { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_terminated"

"session.status\_terminated"

beta\_managed\_agents\_span\_model\_request\_start\_event: object { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_start"

"span.model\_request\_start"

beta\_managed\_agents\_span\_model\_request\_end\_event: object { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: string

Unique identifier for this event.

is\_error: boolean

Whether the model request resulted in an error.

model\_request\_start\_id: string

The id of the corresponding `span.model_request_start` event.

model\_usage: object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_end"

"span.model\_request\_end"

beta\_managed\_agents\_session\_deleted\_event: object { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.deleted"

"session.deleted"

next\_page: optional string

Opaque cursor for the next page. Null when no more results.

List Events

CLI

```shiki
ant beta:sessions:events list \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

Response 200

```shiki
{
  "data": [
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
    },
    {
      "id": "sevt_011CZkZHPq1jCdq5lbRTjiVnz",
      "content": [
        {
          "text": "Let me look up order #1234 for you.",
          "type": "text"
        }
      ],
      "processed_at": "2026-03-15T10:00:00Z",
      "type": "agent.message"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200

```shiki
{
  "data": [
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
    },
    {
      "id": "sevt_011CZkZHPq1jCdq5lbRTjiVnz",
      "content": [
        {
          "text": "Let me look up order #1234 for you.",
          "type": "text"
        }
      ],
      "processed_at": "2026-03-15T10:00:00Z",
      "type": "agent.message"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
