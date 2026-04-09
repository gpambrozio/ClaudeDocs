# Events

Copy page

Ruby

# Events

##### [List Events](api/beta/sessions/events/list.md)

beta.sessions.events.list(session\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsSessionEvent](api/beta.md)>

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

beta.sessions.events.send\_(session\_id, \*\*kwargs) -> [BetaManagedAgentsSendSessionEvents](api/beta.md) { data }

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

beta.sessions.events.stream(session\_id, \*\*kwargs) -> [BetaManagedAgentsStreamSessionEvents](api/beta.md)

GET/v1/sessions/{session\_id}/events/stream

##### ModelsExpand Collapse

class BetaManagedAgentsAgentCustomToolUseEvent { id, input, name, 2 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the custom tool being called.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.custom\_tool\_use"

class BetaManagedAgentsAgentMCPToolResultEvent { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: String

Unique identifier for this event.

mcp\_tool\_use\_id: String

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentMCPToolUseEvent { id, input, mcp\_server\_name, 4 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

mcp\_server\_name: String

Name of the MCP server providing the tool.

name: String

Name of the MCP tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

class BetaManagedAgentsAgentMessageEvent { id, content, processed\_at, type }

An agent response event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type } ]

Array of text blocks comprising the agent response.

text: String

The text content.

type: :text

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.message"

class BetaManagedAgentsAgentThinkingEvent { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thinking"

class BetaManagedAgentsAgentThreadContextCompactedEvent { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thread\_context\_compacted"

class BetaManagedAgentsAgentToolResultEvent { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

tool\_use\_id: String

The id of the `agent.tool_use` event this result corresponds to.

type: :"agent.tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent { id, input, name, 3 more }

Event emitted when the agent invokes a built-in agent tool.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the agent tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsBillingError { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :billing\_error

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

BetaManagedAgentsEventParams = [BetaManagedAgentsUserMessageEventParams](api/beta.md) { content, type }  | [BetaManagedAgentsUserInterruptEventParams](api/beta.md) { type }  | [BetaManagedAgentsUserToolConfirmationEventParams](api/beta.md) { result, tool\_use\_id, type, deny\_message }  | [BetaManagedAgentsUserCustomToolResultEventParams](api/beta.md) { custom\_tool\_use\_id, type, content, is\_error }

Union type for event parameters that can be sent to a session.

Accepts one of the following:

class BetaManagedAgentsUserMessageEventParams { content, type }

Parameters for sending a user message to the session.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks for the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

class BetaManagedAgentsUserInterruptEventParams { type }

Parameters for sending an interrupt to pause the agent.

type: :"user.interrupt"

class BetaManagedAgentsUserToolConfirmationEventParams { result, tool\_use\_id, type, deny\_message }

Parameters for confirming or denying a tool execution request.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

class BetaManagedAgentsUserCustomToolResultEventParams { custom\_tool\_use\_id, type, content, is\_error }

Parameters for providing the result of a custom tool execution.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: String

Name of the MCP server that failed authentication.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_authentication\_failed\_error

class BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: String

Name of the MCP server that failed to connect.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_connection\_failed\_error

class BetaManagedAgentsModelOverloadedError { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_overloaded\_error

class BetaManagedAgentsModelRateLimitedError { message, retry\_status, type }

The model request was rate-limited.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_rate\_limited\_error

class BetaManagedAgentsModelRequestFailedError { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_request\_failed\_error

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

class BetaManagedAgentsSendSessionEvents { data }

Events that were successfully sent to the session.

data: Array[[BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  | [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at }  | [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 3 more }  | [BetaManagedAgentsUserCustomToolResultEvent](api/beta.md) { id, custom\_tool\_use\_id, type, 3 more } ]

Sent events

Accepts one of the following:

class BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at }

A user message event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: String

Unique identifier for this event.

type: :"user.interrupt"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: String

Unique identifier for this event.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: String

Unique identifier for this event.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsSessionDeletedEvent { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.deleted"

class BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn

class BetaManagedAgentsSessionErrorEvent { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: String

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelOverloadedError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelRateLimitedError](api/beta.md) { message, retry\_status, type }  | 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :unknown\_error

class BetaManagedAgentsModelOverloadedError { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_overloaded\_error

class BetaManagedAgentsModelRateLimitedError { message, retry\_status, type }

The model request was rate-limited.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_rate\_limited\_error

class BetaManagedAgentsModelRequestFailedError { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_request\_failed\_error

class BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: String

Name of the MCP server that failed to connect.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_connection\_failed\_error

class BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: String

Name of the MCP server that failed authentication.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_authentication\_failed\_error

class BetaManagedAgentsBillingError { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :billing\_error

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.error"

BetaManagedAgentsSessionEvent = [BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  | [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at }  | [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 3 more }  | 17 more

Union type for all event types in a session.

Accepts one of the following:

class BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at }

A user message event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: String

Unique identifier for this event.

type: :"user.interrupt"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: String

Unique identifier for this event.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: String

Unique identifier for this event.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsAgentCustomToolUseEvent { id, input, name, 2 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the custom tool being called.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.custom\_tool\_use"

class BetaManagedAgentsAgentMessageEvent { id, content, processed\_at, type }

An agent response event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type } ]

Array of text blocks comprising the agent response.

text: String

The text content.

type: :text

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.message"

class BetaManagedAgentsAgentThinkingEvent { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thinking"

class BetaManagedAgentsAgentMCPToolUseEvent { id, input, mcp\_server\_name, 4 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

mcp\_server\_name: String

Name of the MCP server providing the tool.

name: String

Name of the MCP tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

class BetaManagedAgentsAgentMCPToolResultEvent { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: String

Unique identifier for this event.

mcp\_tool\_use\_id: String

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent { id, input, name, 3 more }

Event emitted when the agent invokes a built-in agent tool.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the agent tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

class BetaManagedAgentsAgentToolResultEvent { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

tool\_use\_id: String

The id of the `agent.tool_use` event this result corresponds to.

type: :"agent.tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadContextCompactedEvent { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thread\_context\_compacted"

class BetaManagedAgentsSessionErrorEvent { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: String

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelOverloadedError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelRateLimitedError](api/beta.md) { message, retry\_status, type }  | 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :unknown\_error

class BetaManagedAgentsModelOverloadedError { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_overloaded\_error

class BetaManagedAgentsModelRateLimitedError { message, retry\_status, type }

The model request was rate-limited.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_rate\_limited\_error

class BetaManagedAgentsModelRequestFailedError { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_request\_failed\_error

class BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: String

Name of the MCP server that failed to connect.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_connection\_failed\_error

class BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: String

Name of the MCP server that failed authentication.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_authentication\_failed\_error

class BetaManagedAgentsBillingError { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :billing\_error

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.error"

class BetaManagedAgentsSessionStatusRescheduledEvent { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_rescheduled"

class BetaManagedAgentsSessionStatusRunningEvent { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_running"

class BetaManagedAgentsSessionStatusIdleEvent { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn

class BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action

class BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

type: :"session.status\_idle"

class BetaManagedAgentsSessionStatusTerminatedEvent { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_terminated"

class BetaManagedAgentsSpanModelRequestStartEvent { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_start"

class BetaManagedAgentsSpanModelRequestEndEvent { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: String

Unique identifier for this event.

is\_error: bool

Whether the model request resulted in an error.

model\_request\_start\_id: String

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_end"

class BetaManagedAgentsSessionDeletedEvent { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.deleted"

class BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action

class BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

class BetaManagedAgentsSessionStatusIdleEvent { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn

class BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action

class BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

type: :"session.status\_idle"

class BetaManagedAgentsSessionStatusRescheduledEvent { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_rescheduled"

class BetaManagedAgentsSessionStatusRunningEvent { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_running"

class BetaManagedAgentsSessionStatusTerminatedEvent { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_terminated"

class BetaManagedAgentsSpanModelRequestEndEvent { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: String

Unique identifier for this event.

is\_error: bool

Whether the model request resulted in an error.

model\_request\_start\_id: String

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_end"

class BetaManagedAgentsSpanModelRequestStartEvent { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_start"

class BetaManagedAgentsSpanModelUsage { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

BetaManagedAgentsStreamSessionEvents = [BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  | [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at }  | [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 3 more }  | 17 more

Server-sent event in the session stream.

Accepts one of the following:

class BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at }

A user message event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: String

Unique identifier for this event.

type: :"user.interrupt"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: String

Unique identifier for this event.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: String

Unique identifier for this event.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsAgentCustomToolUseEvent { id, input, name, 2 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the custom tool being called.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.custom\_tool\_use"

class BetaManagedAgentsAgentMessageEvent { id, content, processed\_at, type }

An agent response event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type } ]

Array of text blocks comprising the agent response.

text: String

The text content.

type: :text

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.message"

class BetaManagedAgentsAgentThinkingEvent { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thinking"

class BetaManagedAgentsAgentMCPToolUseEvent { id, input, mcp\_server\_name, 4 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

mcp\_server\_name: String

Name of the MCP server providing the tool.

name: String

Name of the MCP tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

class BetaManagedAgentsAgentMCPToolResultEvent { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: String

Unique identifier for this event.

mcp\_tool\_use\_id: String

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent { id, input, name, 3 more }

Event emitted when the agent invokes a built-in agent tool.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the agent tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

class BetaManagedAgentsAgentToolResultEvent { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

tool\_use\_id: String

The id of the `agent.tool_use` event this result corresponds to.

type: :"agent.tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadContextCompactedEvent { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thread\_context\_compacted"

class BetaManagedAgentsSessionErrorEvent { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: String

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelOverloadedError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelRateLimitedError](api/beta.md) { message, retry\_status, type }  | 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :unknown\_error

class BetaManagedAgentsModelOverloadedError { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_overloaded\_error

class BetaManagedAgentsModelRateLimitedError { message, retry\_status, type }

The model request was rate-limited.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_rate\_limited\_error

class BetaManagedAgentsModelRequestFailedError { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_request\_failed\_error

class BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: String

Name of the MCP server that failed to connect.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_connection\_failed\_error

class BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: String

Name of the MCP server that failed authentication.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_authentication\_failed\_error

class BetaManagedAgentsBillingError { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :billing\_error

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.error"

class BetaManagedAgentsSessionStatusRescheduledEvent { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_rescheduled"

class BetaManagedAgentsSessionStatusRunningEvent { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_running"

class BetaManagedAgentsSessionStatusIdleEvent { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn

class BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action

class BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

type: :"session.status\_idle"

class BetaManagedAgentsSessionStatusTerminatedEvent { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_terminated"

class BetaManagedAgentsSpanModelRequestStartEvent { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_start"

class BetaManagedAgentsSpanModelRequestEndEvent { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: String

Unique identifier for this event.

is\_error: bool

Whether the model request resulted in an error.

model\_request\_start\_id: String

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_end"

class BetaManagedAgentsSessionDeletedEvent { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.deleted"

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsUnknownError { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :unknown\_error

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: String

Unique identifier for this event.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEventParams { custom\_tool\_use\_id, type, content, is\_error }

Parameters for providing the result of a custom tool execution.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsUserInterruptEvent { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: String

Unique identifier for this event.

type: :"user.interrupt"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEventParams { type }

Parameters for sending an interrupt to pause the agent.

type: :"user.interrupt"

class BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at }

A user message event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserMessageEventParams { content, type }

Parameters for sending a user message to the session.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks for the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

class BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: String

Unique identifier for this event.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEventParams { result, tool\_use\_id, type, deny\_message }

Parameters for confirming or denying a tool execution request.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

---

*Copyright © Anthropic. All rights reserved.*
