# Stream Events

Copy page



CLI

# Stream Events

$ ant beta:sessions:events stream

GET/v1/sessions/{session\_id}/events/stream

Stream Events

##### ParametersExpand Collapse

--session-id: string

Path param: Path parameter session\_id

--event-delta: optional array of [BetaManagedAgentsDeltaType](api/beta/sessions.md)

Query param: When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



beta\_managed\_agents\_stream\_session\_events: [BetaManagedAgentsUserMessageEvent](api/beta/sessions/events.md) { id, content, type, processed\_at }  or [BetaManagedAgentsUserInterruptEvent](api/beta/sessions/events.md) { id, type, processed\_at, session\_thread\_id }  or [BetaManagedAgentsUserToolConfirmationEvent](api/beta/sessions/events.md) { id, result, tool\_use\_id, 4 more }  or 33 more

Server-sent event in the session stream.



beta\_managed\_agents\_user\_message\_event: object { id, content, type, processed\_at } 

A user message event in the session conversation.

id: string

Unique identifier for this event.



content: array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title } 

Array of content blocks comprising the user message.



beta\_managed\_agents\_text\_block: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



beta\_managed\_agents\_image\_block: object { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.



beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type } 

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").



type: "base64"

"base64"



beta\_managed\_agents\_url\_image\_source: object { type, url } 

Image referenced by URL.



type: "url"

"url"

url: string

URL of the image to fetch.



beta\_managed\_agents\_file\_image\_source: object { file\_id, type } 

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "image"

"image"



beta\_managed\_agents\_document\_block: object { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.



beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type } 

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").



type: "base64"

"base64"



beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type } 

Plain text document content.

data: string

The plain text content.



media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"



type: "text"

"text"



beta\_managed\_agents\_url\_document\_source: object { type, url } 

Document referenced by URL.



type: "url"

"url"

url: string

URL of the document to fetch.



beta\_managed\_agents\_file\_document\_source: object { file\_id, type } 

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.



type: "user.message"

"user.message"

processed\_at: optional string

A timestamp in RFC 3339 format



beta\_managed\_agents\_user\_interrupt\_event: object { id, type, processed\_at, session\_thread\_id } 

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.



type: "user.interrupt"

"user.interrupt"

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



beta\_managed\_agents\_user\_tool\_confirmation\_event: object { id, result, tool\_use\_id, 4 more } 

A tool confirmation event that approves or denies a pending tool execution.

id: string

Unique identifier for this event.



result: "allow" or "deny"

UserToolConfirmationResult enum

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.



type: "user.tool\_confirmation"

"user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



beta\_managed\_agents\_user\_custom\_tool\_result\_event: object { id, custom\_tool\_use\_id, type, 4 more } 

Event sent by the client providing the result of a custom tool execution.

id: string

Unique identifier for this event.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.



type: "user.custom\_tool\_result"

"user.custom\_tool\_result"



content: optional array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](api/beta/sessions/events.md) { citations, content, source, 2 more } 

The result content returned by the tool.



beta\_managed\_agents\_text\_block: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



beta\_managed\_agents\_image\_block: object { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.



beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type } 

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").



type: "base64"

"base64"



beta\_managed\_agents\_url\_image\_source: object { type, url } 

Image referenced by URL.



type: "url"

"url"

url: string

URL of the image to fetch.



beta\_managed\_agents\_file\_image\_source: object { file\_id, type } 

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "image"

"image"



beta\_managed\_agents\_document\_block: object { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.



beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type } 

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").



type: "base64"

"base64"



beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type } 

Plain text document content.

data: string

The plain text content.



media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"



type: "text"

"text"



beta\_managed\_agents\_url\_document\_source: object { type, url } 

Document referenced by URL.



type: "url"

"url"

url: string

URL of the document to fetch.



beta\_managed\_agents\_file\_document\_source: object { file\_id, type } 

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.



beta\_managed\_agents\_search\_result\_block: object { citations, content, source, 2 more } 

A block containing a web search result.



citations: object { enabled } 

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.



content: array of [BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md) { text, type } 

Array of text content blocks from the search result.

text: string

The text content.



type: "text"

"text"

source: string

The URL source of the search result.

title: string

The title of the search result.



type: "search\_result"

"search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



beta\_managed\_agents\_agent\_custom\_tool\_use\_event: object { id, input, name, 3 more } 

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the custom tool being called.

processed\_at: string

A timestamp in RFC 3339 format



type: "agent.custom\_tool\_use"

"agent.custom\_tool\_use"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



beta\_managed\_agents\_agent\_message\_event: object { id, content, processed\_at, type } 

An agent response event in the session conversation.

id: string

Unique identifier for this event.



content: array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type } 

Array of text blocks comprising the agent response.

text: string

The text content.



type: "text"

"text"

processed\_at: string

A timestamp in RFC 3339 format



type: "agent.message"

"agent.message"



beta\_managed\_agents\_agent\_thinking\_event: object { id, processed\_at, type } 

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



type: "agent.thinking"

"agent.thinking"



beta\_managed\_agents\_agent\_mcp\_tool\_use\_event: object { id, input, mcp\_server\_name, 5 more } 

Event emitted when the agent invokes a tool provided by an MCP server.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

mcp\_server\_name: string

Name of the MCP server providing the tool.

name: string

Name of the MCP tool being used.

processed\_at: string

A timestamp in RFC 3339 format



type: "agent.mcp\_tool\_use"

"agent.mcp\_tool\_use"



evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

"allow"

"ask"

"deny"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



beta\_managed\_agents\_agent\_mcp\_tool\_result\_event: object { id, mcp\_tool\_use\_id, processed\_at, 3 more } 

Event representing the result of an MCP tool execution.

id: string

Unique identifier for this event.

mcp\_tool\_use\_id: string

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: string

A timestamp in RFC 3339 format



type: "agent.mcp\_tool\_result"

"agent.mcp\_tool\_result"



content: optional array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](api/beta/sessions/events.md) { citations, content, source, 2 more } 

The result content returned by the tool.



beta\_managed\_agents\_text\_block: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



beta\_managed\_agents\_image\_block: object { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.



beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type } 

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").



type: "base64"

"base64"



beta\_managed\_agents\_url\_image\_source: object { type, url } 

Image referenced by URL.



type: "url"

"url"

url: string

URL of the image to fetch.



beta\_managed\_agents\_file\_image\_source: object { file\_id, type } 

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "image"

"image"



beta\_managed\_agents\_document\_block: object { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.



beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type } 

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").



type: "base64"

"base64"



beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type } 

Plain text document content.

data: string

The plain text content.



media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"



type: "text"

"text"



beta\_managed\_agents\_url\_document\_source: object { type, url } 

Document referenced by URL.



type: "url"

"url"

url: string

URL of the document to fetch.



beta\_managed\_agents\_file\_document\_source: object { file\_id, type } 

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.



beta\_managed\_agents\_search\_result\_block: object { citations, content, source, 2 more } 

A block containing a web search result.



citations: object { enabled } 

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.



content: array of [BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md) { text, type } 

Array of text content blocks from the search result.

text: string

The text content.



type: "text"

"text"

source: string

The URL source of the search result.

title: string

The title of the search result.



type: "search\_result"

"search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.



beta\_managed\_agents\_agent\_tool\_use\_event: object { id, input, name, 4 more } 

Event emitted when the agent invokes a built-in agent tool.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the agent tool being used.

processed\_at: string

A timestamp in RFC 3339 format



type: "agent.tool\_use"

"agent.tool\_use"



evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

"allow"

"ask"

"deny"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



beta\_managed\_agents\_agent\_tool\_result\_event: object { id, processed\_at, tool\_use\_id, 3 more } 

Event representing the result of an agent tool execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to.



type: "agent.tool\_result"

"agent.tool\_result"



content: optional array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](api/beta/sessions/events.md) { citations, content, source, 2 more } 

The result content returned by the tool.



beta\_managed\_agents\_text\_block: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



beta\_managed\_agents\_image\_block: object { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.



beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type } 

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").



type: "base64"

"base64"



beta\_managed\_agents\_url\_image\_source: object { type, url } 

Image referenced by URL.



type: "url"

"url"

url: string

URL of the image to fetch.



beta\_managed\_agents\_file\_image\_source: object { file\_id, type } 

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "image"

"image"



beta\_managed\_agents\_document\_block: object { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.



beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type } 

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").



type: "base64"

"base64"



beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type } 

Plain text document content.

data: string

The plain text content.



media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"



type: "text"

"text"



beta\_managed\_agents\_url\_document\_source: object { type, url } 

Document referenced by URL.



type: "url"

"url"

url: string

URL of the document to fetch.



beta\_managed\_agents\_file\_document\_source: object { file\_id, type } 

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.



beta\_managed\_agents\_search\_result\_block: object { citations, content, source, 2 more } 

A block containing a web search result.



citations: object { enabled } 

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.



content: array of [BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md) { text, type } 

Array of text content blocks from the search result.

text: string

The text content.



type: "text"

"text"

source: string

The URL source of the search result.

title: string

The title of the search result.



type: "search\_result"

"search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.



beta\_managed\_agents\_agent\_thread\_message\_received\_event: object { id, content, from\_session\_thread\_id, 3 more } 

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

id: string

Unique identifier for this event.



content: array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title } 

Message content blocks.



beta\_managed\_agents\_text\_block: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



beta\_managed\_agents\_image\_block: object { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.



beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type } 

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").



type: "base64"

"base64"



beta\_managed\_agents\_url\_image\_source: object { type, url } 

Image referenced by URL.



type: "url"

"url"

url: string

URL of the image to fetch.



beta\_managed\_agents\_file\_image\_source: object { file\_id, type } 

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "image"

"image"



beta\_managed\_agents\_document\_block: object { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.



beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type } 

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").



type: "base64"

"base64"



beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type } 

Plain text document content.

data: string

The plain text content.



media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"



type: "text"

"text"



beta\_managed\_agents\_url\_document\_source: object { type, url } 

Document referenced by URL.



type: "url"

"url"

url: string

URL of the document to fetch.



beta\_managed\_agents\_file\_document\_source: object { file\_id, type } 

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

from\_session\_thread\_id: string

Public `sthr_` ID of the thread that sent the message.

processed\_at: string

A timestamp in RFC 3339 format



type: "agent.thread\_message\_received"

"agent.thread\_message\_received"

from\_agent\_name: optional string

Name of the callable agent this message came from. Absent when received from the primary agent.



beta\_managed\_agents\_agent\_thread\_message\_sent\_event: object { id, content, processed\_at, 3 more } 

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

id: string

Unique identifier for this event.



content: array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title } 

Message content blocks.



beta\_managed\_agents\_text\_block: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



beta\_managed\_agents\_image\_block: object { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.



beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type } 

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").



type: "base64"

"base64"



beta\_managed\_agents\_url\_image\_source: object { type, url } 

Image referenced by URL.



type: "url"

"url"

url: string

URL of the image to fetch.



beta\_managed\_agents\_file\_image\_source: object { file\_id, type } 

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "image"

"image"



beta\_managed\_agents\_document\_block: object { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.



beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type } 

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").



type: "base64"

"base64"



beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type } 

Plain text document content.

data: string

The plain text content.



media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"



type: "text"

"text"



beta\_managed\_agents\_url\_document\_source: object { type, url } 

Document referenced by URL.



type: "url"

"url"

url: string

URL of the document to fetch.



beta\_managed\_agents\_file\_document\_source: object { file\_id, type } 

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

processed\_at: string

A timestamp in RFC 3339 format

to\_session\_thread\_id: string

Public `sthr_` ID of the thread the message was sent to.



type: "agent.thread\_message\_sent"

"agent.thread\_message\_sent"

to\_agent\_name: optional string

Name of the callable agent this message was sent to. Absent when sent to the primary agent.



beta\_managed\_agents\_agent\_thread\_context\_compacted\_event: object { id, processed\_at, type } 

Indicates that context compaction (summarization) occurred during the session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



type: "agent.thread\_context\_compacted"

"agent.thread\_context\_compacted"



beta\_managed\_agents\_session\_error\_event: object { id, error, processed\_at, type } 

An error event indicating a problem occurred during session execution.

id: string

Unique identifier for this event.



error: [BetaManagedAgentsUnknownError](api/beta/sessions/events.md) { message, retry\_status, type }  or [BetaManagedAgentsModelOverloadedError](api/beta/sessions/events.md) { message, retry\_status, type }  or [BetaManagedAgentsModelRateLimitedError](api/beta/sessions/events.md) { message, retry\_status, type }  or 5 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.



beta\_managed\_agents\_unknown\_error: object { message, retry\_status, type } 

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: string

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.



beta\_managed\_agents\_retry\_status\_retrying: object { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.



type: "retrying"

"retrying"



beta\_managed\_agents\_retry\_status\_exhausted: object { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.



type: "exhausted"

"exhausted"



beta\_managed\_agents\_retry\_status\_terminal: object { type } 

The session encountered a terminal error and will transition to `terminated` state.



type: "terminal"

"terminal"



type: "unknown\_error"

"unknown\_error"



beta\_managed\_agents\_model\_overloaded\_error: object { message, retry\_status, type } 

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: string

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.



beta\_managed\_agents\_retry\_status\_retrying: object { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.



type: "retrying"

"retrying"



beta\_managed\_agents\_retry\_status\_exhausted: object { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.



type: "exhausted"

"exhausted"



beta\_managed\_agents\_retry\_status\_terminal: object { type } 

The session encountered a terminal error and will transition to `terminated` state.



type: "terminal"

"terminal"



type: "model\_overloaded\_error"

"model\_overloaded\_error"



beta\_managed\_agents\_model\_rate\_limited\_error: object { message, retry\_status, type } 

The model request was rate-limited.

message: string

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.



beta\_managed\_agents\_retry\_status\_retrying: object { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.



type: "retrying"

"retrying"



beta\_managed\_agents\_retry\_status\_exhausted: object { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.



type: "exhausted"

"exhausted"



beta\_managed\_agents\_retry\_status\_terminal: object { type } 

The session encountered a terminal error and will transition to `terminated` state.



type: "terminal"

"terminal"



type: "model\_rate\_limited\_error"

"model\_rate\_limited\_error"



beta\_managed\_agents\_model\_request\_failed\_error: object { message, retry\_status, type } 

A model request failed for a reason other than overload or rate-limiting.

message: string

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.



beta\_managed\_agents\_retry\_status\_retrying: object { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.



type: "retrying"

"retrying"



beta\_managed\_agents\_retry\_status\_exhausted: object { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.



type: "exhausted"

"exhausted"



beta\_managed\_agents\_retry\_status\_terminal: object { type } 

The session encountered a terminal error and will transition to `terminated` state.



type: "terminal"

"terminal"



type: "model\_request\_failed\_error"

"model\_request\_failed\_error"



beta\_managed\_agents\_mcp\_connection\_failed\_error: object { mcp\_server\_name, message, retry\_status, type } 

Failed to connect to an MCP server.

mcp\_server\_name: string

Name of the MCP server that failed to connect.

message: string

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.



beta\_managed\_agents\_retry\_status\_retrying: object { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.



type: "retrying"

"retrying"



beta\_managed\_agents\_retry\_status\_exhausted: object { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.



type: "exhausted"

"exhausted"



beta\_managed\_agents\_retry\_status\_terminal: object { type } 

The session encountered a terminal error and will transition to `terminated` state.



type: "terminal"

"terminal"



type: "mcp\_connection\_failed\_error"

"mcp\_connection\_failed\_error"



beta\_managed\_agents\_mcp\_authentication\_failed\_error: object { mcp\_server\_name, message, retry\_status, type } 

Authentication to an MCP server failed.

mcp\_server\_name: string

Name of the MCP server that failed authentication.

message: string

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.



beta\_managed\_agents\_retry\_status\_retrying: object { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.



type: "retrying"

"retrying"



beta\_managed\_agents\_retry\_status\_exhausted: object { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.



type: "exhausted"

"exhausted"



beta\_managed\_agents\_retry\_status\_terminal: object { type } 

The session encountered a terminal error and will transition to `terminated` state.



type: "terminal"

"terminal"



type: "mcp\_authentication\_failed\_error"

"mcp\_authentication\_failed\_error"



beta\_managed\_agents\_billing\_error: object { message, retry\_status, type } 

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: string

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.



beta\_managed\_agents\_retry\_status\_retrying: object { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.



type: "retrying"

"retrying"



beta\_managed\_agents\_retry\_status\_exhausted: object { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.



type: "exhausted"

"exhausted"



beta\_managed\_agents\_retry\_status\_terminal: object { type } 

The session encountered a terminal error and will transition to `terminated` state.



type: "terminal"

"terminal"



type: "billing\_error"

"billing\_error"



beta\_managed\_agents\_credential\_host\_unreachable\_error: object { credential\_id, message, retry\_status, 2 more } 

An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

credential\_id: string

ID of the affected credential.

message: string

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.



beta\_managed\_agents\_retry\_status\_retrying: object { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.



type: "retrying"

"retrying"



beta\_managed\_agents\_retry\_status\_exhausted: object { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.



type: "exhausted"

"exhausted"



beta\_managed\_agents\_retry\_status\_terminal: object { type } 

The session encountered a terminal error and will transition to `terminated` state.



type: "terminal"

"terminal"



type: "credential\_host\_unreachable\_error"

"credential\_host\_unreachable\_error"

vault\_id: string

ID of the vault containing the affected credential.

processed\_at: string

A timestamp in RFC 3339 format



type: "session.error"

"session.error"



beta\_managed\_agents\_session\_status\_rescheduled\_event: object { id, processed\_at, type } 

Indicates the session is recovering from an error state and is rescheduled for execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



type: "session.status\_rescheduled"

"session.status\_rescheduled"



beta\_managed\_agents\_session\_status\_running\_event: object { id, processed\_at, type } 

Indicates the session is actively running and the agent is working.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



type: "session.status\_running"

"session.status\_running"



beta\_managed\_agents\_session\_status\_idle\_event: object { id, processed\_at, stop\_reason, type } 

Indicates the agent has paused and is awaiting user input.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsSessionRequiresAction](api/beta/sessions/events.md) { event\_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](api/beta/sessions/events.md) { type } 

The agent completed its turn naturally and is ready for the next user message.



beta\_managed\_agents\_session\_end\_turn: object { type } 

The agent completed its turn naturally and is ready for the next user message.



type: "end\_turn"

"end\_turn"



beta\_managed\_agents\_session\_requires\_action: object { event\_ids, type } 

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.



type: "requires\_action"

"requires\_action"



beta\_managed\_agents\_session\_retries\_exhausted: object { type } 

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).



type: "retries\_exhausted"

"retries\_exhausted"



type: "session.status\_idle"

"session.status\_idle"



beta\_managed\_agents\_session\_status\_terminated\_event: object { id, processed\_at, type } 

Indicates the session has terminated, either due to an error or completion.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



type: "session.status\_terminated"

"session.status\_terminated"



beta\_managed\_agents\_session\_thread\_created\_event: object { id, agent\_name, processed\_at, 2 more } 

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

id: string

Unique identifier for this event.

agent\_name: string

Name of the callable agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public `sthr_` ID of the newly created thread.



type: "session.thread\_created"

"session.thread\_created"



beta\_managed\_agents\_span\_outcome\_evaluation\_start\_event: object { id, iteration, outcome\_id, 2 more } 

Emitted when an outcome evaluation cycle begins.

id: string

Unique identifier for this event.

iteration: number

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format



type: "span.outcome\_evaluation\_start"

"span.outcome\_evaluation\_start"



beta\_managed\_agents\_span\_outcome\_evaluation\_end\_event: object { id, explanation, iteration, 6 more } 

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

id: string

Unique identifier for this event.

explanation: string

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

iteration: number

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_evaluation\_start\_id: string

The id of the corresponding `span.outcome_evaluation_start` event.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format

result: string

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.



type: "span.outcome\_evaluation\_end"

"span.outcome\_evaluation\_end"



usage: object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more } 

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"



beta\_managed\_agents\_span\_model\_request\_start\_event: object { id, processed\_at, type } 

Emitted when a model request is initiated by the agent.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



type: "span.model\_request\_start"

"span.model\_request\_start"



beta\_managed\_agents\_span\_model\_request\_end\_event: object { id, is\_error, model\_request\_start\_id, 3 more } 

Emitted when a model request completes.

id: string

Unique identifier for this event.

is\_error: boolean

Whether the model request resulted in an error.

model\_request\_start\_id: string

The id of the corresponding `span.model_request_start` event.



model\_usage: object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more } 

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"

processed\_at: string

A timestamp in RFC 3339 format



type: "span.model\_request\_end"

"span.model\_request\_end"



beta\_managed\_agents\_span\_outcome\_evaluation\_ongoing\_event: object { id, iteration, outcome\_id, 2 more } 

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

id: string

Unique identifier for this event.

iteration: number

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format



type: "span.outcome\_evaluation\_ongoing"

"span.outcome\_evaluation\_ongoing"



beta\_managed\_agents\_user\_define\_outcome\_event: object { id, description, max\_iterations, 4 more } 

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

id: string

Unique identifier for this event.

description: string

What the agent should produce. Copied from the input event.

max\_iterations: number

Evaluate-then-revise cycles before giving up. Default 3, max 20.

outcome\_id: string

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

processed\_at: string

A timestamp in RFC 3339 format



rubric: [BetaManagedAgentsFileRubric](api/beta/sessions/events.md) { file\_id, type }  or [BetaManagedAgentsTextRubric](api/beta/sessions/events.md) { content, type } 

Rubric for grading the quality of an outcome.



beta\_managed\_agents\_file\_rubric: object { file\_id, type } 

Rubric referenced by a file uploaded via the Files API.

file\_id: string

ID of the rubric file.



type: "file"

"file"



beta\_managed\_agents\_text\_rubric: object { content, type } 

Rubric content provided inline as text.

content: string

Rubric content. Plain text or markdown — the grader treats it as freeform text.



type: "text"

"text"



type: "user.define\_outcome"

"user.define\_outcome"



beta\_managed\_agents\_session\_deleted\_event: object { id, processed\_at, type } 

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



type: "session.deleted"

"session.deleted"



beta\_managed\_agents\_session\_thread\_status\_running\_event: object { id, agent\_name, processed\_at, 2 more } 

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that started running.



type: "session.thread\_status\_running"

"session.thread\_status\_running"



beta\_managed\_agents\_session\_thread\_status\_idle\_event: object { id, agent\_name, processed\_at, 3 more } 

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that went idle.



stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsSessionRequiresAction](api/beta/sessions/events.md) { event\_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](api/beta/sessions/events.md) { type } 

The agent completed its turn naturally and is ready for the next user message.



beta\_managed\_agents\_session\_end\_turn: object { type } 

The agent completed its turn naturally and is ready for the next user message.



type: "end\_turn"

"end\_turn"



beta\_managed\_agents\_session\_requires\_action: object { event\_ids, type } 

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.



type: "requires\_action"

"requires\_action"



beta\_managed\_agents\_session\_retries\_exhausted: object { type } 

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).



type: "retries\_exhausted"

"retries\_exhausted"



type: "session.thread\_status\_idle"

"session.thread\_status\_idle"



beta\_managed\_agents\_session\_thread\_status\_terminated\_event: object { id, agent\_name, processed\_at, 2 more } 

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that terminated.



type: "session.thread\_status\_terminated"

"session.thread\_status\_terminated"



beta\_managed\_agents\_user\_tool\_result\_event: object { id, tool\_use\_id, type, 4 more } 

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

id: string

Unique identifier for this event.

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.



type: "user.tool\_result"

"user.tool\_result"



content: optional array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](api/beta/sessions/events.md) { citations, content, source, 2 more } 

The result content returned by the tool.



beta\_managed\_agents\_text\_block: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



beta\_managed\_agents\_image\_block: object { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.



beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type } 

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").



type: "base64"

"base64"



beta\_managed\_agents\_url\_image\_source: object { type, url } 

Image referenced by URL.



type: "url"

"url"

url: string

URL of the image to fetch.



beta\_managed\_agents\_file\_image\_source: object { file\_id, type } 

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "image"

"image"



beta\_managed\_agents\_document\_block: object { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.



beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type } 

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").



type: "base64"

"base64"



beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type } 

Plain text document content.

data: string

The plain text content.



media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"



type: "text"

"text"



beta\_managed\_agents\_url\_document\_source: object { type, url } 

Document referenced by URL.



type: "url"

"url"

url: string

URL of the document to fetch.



beta\_managed\_agents\_file\_document\_source: object { file\_id, type } 

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.



beta\_managed\_agents\_search\_result\_block: object { citations, content, source, 2 more } 

A block containing a web search result.



citations: object { enabled } 

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.



content: array of [BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md) { text, type } 

Array of text content blocks from the search result.

text: string

The text content.



type: "text"

"text"

source: string

The URL source of the search result.

title: string

The title of the search result.



type: "search\_result"

"search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.



beta\_managed\_agents\_session\_thread\_status\_rescheduled\_event: object { id, agent\_name, processed\_at, 2 more } 

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that is retrying.



type: "session.thread\_status\_rescheduled"

"session.thread\_status\_rescheduled"



beta\_managed\_agents\_session\_updated\_event: object { id, processed\_at, type, 3 more } 

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



type: "session.updated"

"session.updated"



agent: optional object { id, description, mcp\_servers, 8 more } 

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string



type: "url"

"url"

url: string



model: object { id, speed } 

Model identifier and configuration.



id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-4-8" or 9 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-sonnet-5"

High-performance model for coding and agents

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



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"



multiagent: object { agents, type } 

Resolved coordinator topology with full agent definitions for each roster member.



agents: array of [BetaManagedAgentsSessionThreadAgent](api/beta/agents.md) { id, description, mcp\_servers, 7 more } 

Full `agent` definitions the coordinator may spawn as session threads.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string



type: "url"

"url"

url: string



model: object { id, speed } 

Model identifier and configuration.



id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-4-8" or 9 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-sonnet-5"

High-performance model for coding and agents

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



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 



beta\_managed\_agents\_anthropic\_skill: object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string



type: "anthropic"

"anthropic"

version: string



beta\_managed\_agents\_custom\_skill: object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string



type: "custom"

"custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 



beta\_managed\_agents\_agent\_toolset20260401: object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



type: "agent\_toolset\_20260401"

"agent\_toolset\_20260401"



beta\_managed\_agents\_mcp\_toolset: object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"

mcp\_server\_name: string



type: "mcp\_toolset"

"mcp\_toolset"



beta\_managed\_agents\_custom\_tool: object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: object { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string



type: "custom"

"custom"



type: "agent"

"agent"

version: number



type: "coordinator"

"coordinator"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 



beta\_managed\_agents\_anthropic\_skill: object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string



type: "anthropic"

"anthropic"

version: string



beta\_managed\_agents\_custom\_skill: object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string



type: "custom"

"custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 



beta\_managed\_agents\_agent\_toolset20260401: object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



type: "agent\_toolset\_20260401"

"agent\_toolset\_20260401"



beta\_managed\_agents\_mcp\_toolset: object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"

mcp\_server\_name: string



type: "mcp\_toolset"

"mcp\_toolset"



beta\_managed\_agents\_custom\_tool: object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: object { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string



type: "custom"

"custom"



type: "agent"

"agent"

version: number

metadata: optional map[string]

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

title: optional string

The session's new title. Present only when the update changed it.



beta\_managed\_agents\_start\_event: object { event, type } 

Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event\_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model\_request\_end closes the preview. Only sent on stream connections that opt in via event\_deltas; never appears in event history.



event: [BetaManagedAgentsAgentMessagePreview](api/beta/sessions.md) { id, type }  or [BetaManagedAgentsAgentThinkingPreview](api/beta/sessions.md) { id, type } 

The previewed event's type and id. The event type determines which delta types the preview's event\_delta events carry: agent.message events stream content\_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.



beta\_managed\_agents\_agent\_message\_preview: object { id, type } 

id: string

The id the buffered agent.message will carry if it is emitted. Matches the event\_id on this preview's event\_delta events.



type: "agent.message"

"agent.message"



beta\_managed\_agents\_agent\_thinking\_preview: object { id, type } 

id: string

The id the buffered agent.thinking will carry if it is emitted. Start-only — no event\_delta events follow.



type: "agent.thinking"

"agent.thinking"



type: "event\_start"

"event\_start"



beta\_managed\_agents\_delta\_event: object { delta, event\_id, type } 

An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event\_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model\_request\_end closes the preview. Only sent on stream connections that opt in via event\_deltas; never appears in event history.



delta: object { content, type, index } 

One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content\_delta fragments, each a partial element of the content array.



content: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



type: "content\_delta"

"content\_delta"

index: optional number

Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

event\_id: string

The id of the event being previewed. Matches event.id on the corresponding event\_start and the buffered event that reconciles the preview.



type: "event\_delta"

"event\_delta"



beta\_managed\_agents\_system\_message\_event: object { id, content, type, processed\_at } 

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

id: string

Unique identifier for this event.



content: array of [BetaManagedAgentsSystemContentBlock](api/beta/sessions.md) { text, type } 

System content blocks. Text-only.

text: string

The text content.



type: "text"

"text"



type: "system.message"

"system.message"

processed\_at: optional string

A timestamp in RFC 3339 format



beta\_managed\_agents\_stream\_session\_events: [BetaManagedAgentsUserMessageEvent](api/beta/sessions/events.md) { id, content, type, processed\_at }  or [BetaManagedAgentsUserInterruptEvent](api/beta/sessions/events.md) { id, type, processed\_at, session\_thread\_id }  or [BetaManagedAgentsUserToolConfirmationEvent](api/beta/sessions/events.md) { id, result, tool\_use\_id, 4 more }  or 33 more

Server-sent event in the session stream.



beta\_managed\_agents\_user\_message\_event: object { id, content, type, processed\_at } 

A user message event in the session conversation.

id: string

Unique identifier for this event.



content: array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title } 

Array of content blocks comprising the user message.



beta\_managed\_agents\_text\_block: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



beta\_managed\_agents\_image\_block: object { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.



beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type } 

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").



type: "base64"

"base64"



beta\_managed\_agents\_url\_image\_source: object { type, url } 

Image referenced by URL.



type: "url"

"url"

url: string

URL of the image to fetch.



beta\_managed\_agents\_file\_image\_source: object { file\_id, type } 

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "image"

"image"



beta\_managed\_agents\_document\_block: object { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.



beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type } 

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").



type: "base64"

"base64"



beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type } 

Plain text document content.

data: string

The plain text content.



media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"



type: "text"

"text"



beta\_managed\_agents\_url\_document\_source: object { type, url } 

Document referenced by URL.



type: "url"

"url"

url: string

URL of the document to fetch.



beta\_managed\_agents\_file\_document\_source: object { file\_id, type } 

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.



type: "user.message"

"user.message"

processed\_at: optional string

A timestamp in RFC 3339 format



beta\_managed\_agents\_user\_interrupt\_event: object { id, type, processed\_at, session\_thread\_id } 

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.



type: "user.interrupt"

"user.interrupt"

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



beta\_managed\_agents\_user\_tool\_confirmation\_event: object { id, result, tool\_use\_id, 4 more } 

A tool confirmation event that approves or denies a pending tool execution.

id: string

Unique identifier for this event.



result: "allow" or "deny"

UserToolConfirmationResult enum

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.



type: "user.tool\_confirmation"

"user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



beta\_managed\_agents\_user\_custom\_tool\_result\_event: object { id, custom\_tool\_use\_id, type, 4 more } 

Event sent by the client providing the result of a custom tool execution.

id: string

Unique identifier for this event.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.



type: "user.custom\_tool\_result"

"user.custom\_tool\_result"



content: optional array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](api/beta/sessions/events.md) { citations, content, source, 2 more } 

The result content returned by the tool.



beta\_managed\_agents\_text\_block: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



beta\_managed\_agents\_image\_block: object { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.



beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type } 

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").



type: "base64"

"base64"



beta\_managed\_agents\_url\_image\_source: object { type, url } 

Image referenced by URL.



type: "url"

"url"

url: string

URL of the image to fetch.



beta\_managed\_agents\_file\_image\_source: object { file\_id, type } 

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "image"

"image"



beta\_managed\_agents\_document\_block: object { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.



beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type } 

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").



type: "base64"

"base64"



beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type } 

Plain text document content.

data: string

The plain text content.



media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"



type: "text"

"text"



beta\_managed\_agents\_url\_document\_source: object { type, url } 

Document referenced by URL.



type: "url"

"url"

url: string

URL of the document to fetch.



beta\_managed\_agents\_file\_document\_source: object { file\_id, type } 

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.



beta\_managed\_agents\_search\_result\_block: object { citations, content, source, 2 more } 

A block containing a web search result.



citations: object { enabled } 

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.



content: array of [BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md) { text, type } 

Array of text content blocks from the search result.

text: string

The text content.



type: "text"

"text"

source: string

The URL source of the search result.

title: string

The title of the search result.



type: "search\_result"

"search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



beta\_managed\_agents\_agent\_custom\_tool\_use\_event: object { id, input, name, 3 more } 

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the custom tool being called.

processed\_at: string

A timestamp in RFC 3339 format



type: "agent.custom\_tool\_use"

"agent.custom\_tool\_use"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



beta\_managed\_agents\_agent\_message\_event: object { id, content, processed\_at, type } 

An agent response event in the session conversation.

id: string

Unique identifier for this event.



content: array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type } 

Array of text blocks comprising the agent response.

text: string

The text content.



type: "text"

"text"

processed\_at: string

A timestamp in RFC 3339 format



type: "agent.message"

"agent.message"



beta\_managed\_agents\_agent\_thinking\_event: object { id, processed\_at, type } 

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



type: "agent.thinking"

"agent.thinking"



beta\_managed\_agents\_agent\_mcp\_tool\_use\_event: object { id, input, mcp\_server\_name, 5 more } 

Event emitted when the agent invokes a tool provided by an MCP server.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

mcp\_server\_name: string

Name of the MCP server providing the tool.

name: string

Name of the MCP tool being used.

processed\_at: string

A timestamp in RFC 3339 format



type: "agent.mcp\_tool\_use"

"agent.mcp\_tool\_use"



evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

"allow"

"ask"

"deny"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



beta\_managed\_agents\_agent\_mcp\_tool\_result\_event: object { id, mcp\_tool\_use\_id, processed\_at, 3 more } 

Event representing the result of an MCP tool execution.

id: string

Unique identifier for this event.

mcp\_tool\_use\_id: string

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: string

A timestamp in RFC 3339 format



type: "agent.mcp\_tool\_result"

"agent.mcp\_tool\_result"



content: optional array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](api/beta/sessions/events.md) { citations, content, source, 2 more } 

The result content returned by the tool.



beta\_managed\_agents\_text\_block: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



beta\_managed\_agents\_image\_block: object { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.



beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type } 

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").



type: "base64"

"base64"



beta\_managed\_agents\_url\_image\_source: object { type, url } 

Image referenced by URL.



type: "url"

"url"

url: string

URL of the image to fetch.



beta\_managed\_agents\_file\_image\_source: object { file\_id, type } 

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "image"

"image"



beta\_managed\_agents\_document\_block: object { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.



beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type } 

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").



type: "base64"

"base64"



beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type } 

Plain text document content.

data: string

The plain text content.



media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"



type: "text"

"text"



beta\_managed\_agents\_url\_document\_source: object { type, url } 

Document referenced by URL.



type: "url"

"url"

url: string

URL of the document to fetch.



beta\_managed\_agents\_file\_document\_source: object { file\_id, type } 

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.



beta\_managed\_agents\_search\_result\_block: object { citations, content, source, 2 more } 

A block containing a web search result.



citations: object { enabled } 

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.



content: array of [BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md) { text, type } 

Array of text content blocks from the search result.

text: string

The text content.



type: "text"

"text"

source: string

The URL source of the search result.

title: string

The title of the search result.



type: "search\_result"

"search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.



beta\_managed\_agents\_agent\_tool\_use\_event: object { id, input, name, 4 more } 

Event emitted when the agent invokes a built-in agent tool.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the agent tool being used.

processed\_at: string

A timestamp in RFC 3339 format



type: "agent.tool\_use"

"agent.tool\_use"



evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

"allow"

"ask"

"deny"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



beta\_managed\_agents\_agent\_tool\_result\_event: object { id, processed\_at, tool\_use\_id, 3 more } 

Event representing the result of an agent tool execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to.



type: "agent.tool\_result"

"agent.tool\_result"



content: optional array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](api/beta/sessions/events.md) { citations, content, source, 2 more } 

The result content returned by the tool.



beta\_managed\_agents\_text\_block: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



beta\_managed\_agents\_image\_block: object { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.



beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type } 

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").



type: "base64"

"base64"



beta\_managed\_agents\_url\_image\_source: object { type, url } 

Image referenced by URL.



type: "url"

"url"

url: string

URL of the image to fetch.



beta\_managed\_agents\_file\_image\_source: object { file\_id, type } 

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "image"

"image"



beta\_managed\_agents\_document\_block: object { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.



beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type } 

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").



type: "base64"

"base64"



beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type } 

Plain text document content.

data: string

The plain text content.



media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"



type: "text"

"text"



beta\_managed\_agents\_url\_document\_source: object { type, url } 

Document referenced by URL.



type: "url"

"url"

url: string

URL of the document to fetch.



beta\_managed\_agents\_file\_document\_source: object { file\_id, type } 

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.



beta\_managed\_agents\_search\_result\_block: object { citations, content, source, 2 more } 

A block containing a web search result.



citations: object { enabled } 

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.



content: array of [BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md) { text, type } 

Array of text content blocks from the search result.

text: string

The text content.



type: "text"

"text"

source: string

The URL source of the search result.

title: string

The title of the search result.



type: "search\_result"

"search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.



beta\_managed\_agents\_agent\_thread\_message\_received\_event: object { id, content, from\_session\_thread\_id, 3 more } 

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

id: string

Unique identifier for this event.



content: array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title } 

Message content blocks.



beta\_managed\_agents\_text\_block: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



beta\_managed\_agents\_image\_block: object { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.



beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type } 

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").



type: "base64"

"base64"



beta\_managed\_agents\_url\_image\_source: object { type, url } 

Image referenced by URL.



type: "url"

"url"

url: string

URL of the image to fetch.



beta\_managed\_agents\_file\_image\_source: object { file\_id, type } 

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "image"

"image"



beta\_managed\_agents\_document\_block: object { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.



beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type } 

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").



type: "base64"

"base64"



beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type } 

Plain text document content.

data: string

The plain text content.



media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"



type: "text"

"text"



beta\_managed\_agents\_url\_document\_source: object { type, url } 

Document referenced by URL.



type: "url"

"url"

url: string

URL of the document to fetch.



beta\_managed\_agents\_file\_document\_source: object { file\_id, type } 

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

from\_session\_thread\_id: string

Public `sthr_` ID of the thread that sent the message.

processed\_at: string

A timestamp in RFC 3339 format



type: "agent.thread\_message\_received"

"agent.thread\_message\_received"

from\_agent\_name: optional string

Name of the callable agent this message came from. Absent when received from the primary agent.



beta\_managed\_agents\_agent\_thread\_message\_sent\_event: object { id, content, processed\_at, 3 more } 

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

id: string

Unique identifier for this event.



content: array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title } 

Message content blocks.



beta\_managed\_agents\_text\_block: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



beta\_managed\_agents\_image\_block: object { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.



beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type } 

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").



type: "base64"

"base64"



beta\_managed\_agents\_url\_image\_source: object { type, url } 

Image referenced by URL.



type: "url"

"url"

url: string

URL of the image to fetch.



beta\_managed\_agents\_file\_image\_source: object { file\_id, type } 

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "image"

"image"



beta\_managed\_agents\_document\_block: object { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.



beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type } 

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").



type: "base64"

"base64"



beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type } 

Plain text document content.

data: string

The plain text content.



media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"



type: "text"

"text"



beta\_managed\_agents\_url\_document\_source: object { type, url } 

Document referenced by URL.



type: "url"

"url"

url: string

URL of the document to fetch.



beta\_managed\_agents\_file\_document\_source: object { file\_id, type } 

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

processed\_at: string

A timestamp in RFC 3339 format

to\_session\_thread\_id: string

Public `sthr_` ID of the thread the message was sent to.



type: "agent.thread\_message\_sent"

"agent.thread\_message\_sent"

to\_agent\_name: optional string

Name of the callable agent this message was sent to. Absent when sent to the primary agent.



beta\_managed\_agents\_agent\_thread\_context\_compacted\_event: object { id, processed\_at, type } 

Indicates that context compaction (summarization) occurred during the session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



type: "agent.thread\_context\_compacted"

"agent.thread\_context\_compacted"



beta\_managed\_agents\_session\_error\_event: object { id, error, processed\_at, type } 

An error event indicating a problem occurred during session execution.

id: string

Unique identifier for this event.



error: [BetaManagedAgentsUnknownError](api/beta/sessions/events.md) { message, retry\_status, type }  or [BetaManagedAgentsModelOverloadedError](api/beta/sessions/events.md) { message, retry\_status, type }  or [BetaManagedAgentsModelRateLimitedError](api/beta/sessions/events.md) { message, retry\_status, type }  or 5 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.



beta\_managed\_agents\_unknown\_error: object { message, retry\_status, type } 

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: string

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.



beta\_managed\_agents\_retry\_status\_retrying: object { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.



type: "retrying"

"retrying"



beta\_managed\_agents\_retry\_status\_exhausted: object { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.



type: "exhausted"

"exhausted"



beta\_managed\_agents\_retry\_status\_terminal: object { type } 

The session encountered a terminal error and will transition to `terminated` state.



type: "terminal"

"terminal"



type: "unknown\_error"

"unknown\_error"



beta\_managed\_agents\_model\_overloaded\_error: object { message, retry\_status, type } 

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: string

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.



beta\_managed\_agents\_retry\_status\_retrying: object { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.



type: "retrying"

"retrying"



beta\_managed\_agents\_retry\_status\_exhausted: object { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.



type: "exhausted"

"exhausted"



beta\_managed\_agents\_retry\_status\_terminal: object { type } 

The session encountered a terminal error and will transition to `terminated` state.



type: "terminal"

"terminal"



type: "model\_overloaded\_error"

"model\_overloaded\_error"



beta\_managed\_agents\_model\_rate\_limited\_error: object { message, retry\_status, type } 

The model request was rate-limited.

message: string

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.



beta\_managed\_agents\_retry\_status\_retrying: object { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.



type: "retrying"

"retrying"



beta\_managed\_agents\_retry\_status\_exhausted: object { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.



type: "exhausted"

"exhausted"



beta\_managed\_agents\_retry\_status\_terminal: object { type } 

The session encountered a terminal error and will transition to `terminated` state.



type: "terminal"

"terminal"



type: "model\_rate\_limited\_error"

"model\_rate\_limited\_error"



beta\_managed\_agents\_model\_request\_failed\_error: object { message, retry\_status, type } 

A model request failed for a reason other than overload or rate-limiting.

message: string

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.



beta\_managed\_agents\_retry\_status\_retrying: object { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.



type: "retrying"

"retrying"



beta\_managed\_agents\_retry\_status\_exhausted: object { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.



type: "exhausted"

"exhausted"



beta\_managed\_agents\_retry\_status\_terminal: object { type } 

The session encountered a terminal error and will transition to `terminated` state.



type: "terminal"

"terminal"



type: "model\_request\_failed\_error"

"model\_request\_failed\_error"



beta\_managed\_agents\_mcp\_connection\_failed\_error: object { mcp\_server\_name, message, retry\_status, type } 

Failed to connect to an MCP server.

mcp\_server\_name: string

Name of the MCP server that failed to connect.

message: string

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.



beta\_managed\_agents\_retry\_status\_retrying: object { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.



type: "retrying"

"retrying"



beta\_managed\_agents\_retry\_status\_exhausted: object { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.



type: "exhausted"

"exhausted"



beta\_managed\_agents\_retry\_status\_terminal: object { type } 

The session encountered a terminal error and will transition to `terminated` state.



type: "terminal"

"terminal"



type: "mcp\_connection\_failed\_error"

"mcp\_connection\_failed\_error"



beta\_managed\_agents\_mcp\_authentication\_failed\_error: object { mcp\_server\_name, message, retry\_status, type } 

Authentication to an MCP server failed.

mcp\_server\_name: string

Name of the MCP server that failed authentication.

message: string

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.



beta\_managed\_agents\_retry\_status\_retrying: object { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.



type: "retrying"

"retrying"



beta\_managed\_agents\_retry\_status\_exhausted: object { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.



type: "exhausted"

"exhausted"



beta\_managed\_agents\_retry\_status\_terminal: object { type } 

The session encountered a terminal error and will transition to `terminated` state.



type: "terminal"

"terminal"



type: "mcp\_authentication\_failed\_error"

"mcp\_authentication\_failed\_error"



beta\_managed\_agents\_billing\_error: object { message, retry\_status, type } 

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: string

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.



beta\_managed\_agents\_retry\_status\_retrying: object { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.



type: "retrying"

"retrying"



beta\_managed\_agents\_retry\_status\_exhausted: object { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.



type: "exhausted"

"exhausted"



beta\_managed\_agents\_retry\_status\_terminal: object { type } 

The session encountered a terminal error and will transition to `terminated` state.



type: "terminal"

"terminal"



type: "billing\_error"

"billing\_error"



beta\_managed\_agents\_credential\_host\_unreachable\_error: object { credential\_id, message, retry\_status, 2 more } 

An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

credential\_id: string

ID of the affected credential.

message: string

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.



beta\_managed\_agents\_retry\_status\_retrying: object { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.



type: "retrying"

"retrying"



beta\_managed\_agents\_retry\_status\_exhausted: object { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.



type: "exhausted"

"exhausted"



beta\_managed\_agents\_retry\_status\_terminal: object { type } 

The session encountered a terminal error and will transition to `terminated` state.



type: "terminal"

"terminal"



type: "credential\_host\_unreachable\_error"

"credential\_host\_unreachable\_error"

vault\_id: string

ID of the vault containing the affected credential.

processed\_at: string

A timestamp in RFC 3339 format



type: "session.error"

"session.error"



beta\_managed\_agents\_session\_status\_rescheduled\_event: object { id, processed\_at, type } 

Indicates the session is recovering from an error state and is rescheduled for execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



type: "session.status\_rescheduled"

"session.status\_rescheduled"



beta\_managed\_agents\_session\_status\_running\_event: object { id, processed\_at, type } 

Indicates the session is actively running and the agent is working.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



type: "session.status\_running"

"session.status\_running"



beta\_managed\_agents\_session\_status\_idle\_event: object { id, processed\_at, stop\_reason, type } 

Indicates the agent has paused and is awaiting user input.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsSessionRequiresAction](api/beta/sessions/events.md) { event\_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](api/beta/sessions/events.md) { type } 

The agent completed its turn naturally and is ready for the next user message.



beta\_managed\_agents\_session\_end\_turn: object { type } 

The agent completed its turn naturally and is ready for the next user message.



type: "end\_turn"

"end\_turn"



beta\_managed\_agents\_session\_requires\_action: object { event\_ids, type } 

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.



type: "requires\_action"

"requires\_action"



beta\_managed\_agents\_session\_retries\_exhausted: object { type } 

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).



type: "retries\_exhausted"

"retries\_exhausted"



type: "session.status\_idle"

"session.status\_idle"



beta\_managed\_agents\_session\_status\_terminated\_event: object { id, processed\_at, type } 

Indicates the session has terminated, either due to an error or completion.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



type: "session.status\_terminated"

"session.status\_terminated"



beta\_managed\_agents\_session\_thread\_created\_event: object { id, agent\_name, processed\_at, 2 more } 

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

id: string

Unique identifier for this event.

agent\_name: string

Name of the callable agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public `sthr_` ID of the newly created thread.



type: "session.thread\_created"

"session.thread\_created"



beta\_managed\_agents\_span\_outcome\_evaluation\_start\_event: object { id, iteration, outcome\_id, 2 more } 

Emitted when an outcome evaluation cycle begins.

id: string

Unique identifier for this event.

iteration: number

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format



type: "span.outcome\_evaluation\_start"

"span.outcome\_evaluation\_start"



beta\_managed\_agents\_span\_outcome\_evaluation\_end\_event: object { id, explanation, iteration, 6 more } 

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

id: string

Unique identifier for this event.

explanation: string

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

iteration: number

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_evaluation\_start\_id: string

The id of the corresponding `span.outcome_evaluation_start` event.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format

result: string

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.



type: "span.outcome\_evaluation\_end"

"span.outcome\_evaluation\_end"



usage: object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more } 

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"



beta\_managed\_agents\_span\_model\_request\_start\_event: object { id, processed\_at, type } 

Emitted when a model request is initiated by the agent.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



type: "span.model\_request\_start"

"span.model\_request\_start"



beta\_managed\_agents\_span\_model\_request\_end\_event: object { id, is\_error, model\_request\_start\_id, 3 more } 

Emitted when a model request completes.

id: string

Unique identifier for this event.

is\_error: boolean

Whether the model request resulted in an error.

model\_request\_start\_id: string

The id of the corresponding `span.model_request_start` event.



model\_usage: object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more } 

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"

processed\_at: string

A timestamp in RFC 3339 format



type: "span.model\_request\_end"

"span.model\_request\_end"



beta\_managed\_agents\_span\_outcome\_evaluation\_ongoing\_event: object { id, iteration, outcome\_id, 2 more } 

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

id: string

Unique identifier for this event.

iteration: number

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format



type: "span.outcome\_evaluation\_ongoing"

"span.outcome\_evaluation\_ongoing"



beta\_managed\_agents\_user\_define\_outcome\_event: object { id, description, max\_iterations, 4 more } 

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

id: string

Unique identifier for this event.

description: string

What the agent should produce. Copied from the input event.

max\_iterations: number

Evaluate-then-revise cycles before giving up. Default 3, max 20.

outcome\_id: string

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

processed\_at: string

A timestamp in RFC 3339 format



rubric: [BetaManagedAgentsFileRubric](api/beta/sessions/events.md) { file\_id, type }  or [BetaManagedAgentsTextRubric](api/beta/sessions/events.md) { content, type } 

Rubric for grading the quality of an outcome.



beta\_managed\_agents\_file\_rubric: object { file\_id, type } 

Rubric referenced by a file uploaded via the Files API.

file\_id: string

ID of the rubric file.



type: "file"

"file"



beta\_managed\_agents\_text\_rubric: object { content, type } 

Rubric content provided inline as text.

content: string

Rubric content. Plain text or markdown — the grader treats it as freeform text.



type: "text"

"text"



type: "user.define\_outcome"

"user.define\_outcome"



beta\_managed\_agents\_session\_deleted\_event: object { id, processed\_at, type } 

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



type: "session.deleted"

"session.deleted"



beta\_managed\_agents\_session\_thread\_status\_running\_event: object { id, agent\_name, processed\_at, 2 more } 

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that started running.



type: "session.thread\_status\_running"

"session.thread\_status\_running"



beta\_managed\_agents\_session\_thread\_status\_idle\_event: object { id, agent\_name, processed\_at, 3 more } 

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that went idle.



stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta/sessions/events.md) { type }  or [BetaManagedAgentsSessionRequiresAction](api/beta/sessions/events.md) { event\_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](api/beta/sessions/events.md) { type } 

The agent completed its turn naturally and is ready for the next user message.



beta\_managed\_agents\_session\_end\_turn: object { type } 

The agent completed its turn naturally and is ready for the next user message.



type: "end\_turn"

"end\_turn"



beta\_managed\_agents\_session\_requires\_action: object { event\_ids, type } 

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.



type: "requires\_action"

"requires\_action"



beta\_managed\_agents\_session\_retries\_exhausted: object { type } 

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).



type: "retries\_exhausted"

"retries\_exhausted"



type: "session.thread\_status\_idle"

"session.thread\_status\_idle"



beta\_managed\_agents\_session\_thread\_status\_terminated\_event: object { id, agent\_name, processed\_at, 2 more } 

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that terminated.



type: "session.thread\_status\_terminated"

"session.thread\_status\_terminated"



beta\_managed\_agents\_user\_tool\_result\_event: object { id, tool\_use\_id, type, 4 more } 

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

id: string

Unique identifier for this event.

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.



type: "user.tool\_result"

"user.tool\_result"



content: optional array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](api/beta/sessions/events.md) { citations, content, source, 2 more } 

The result content returned by the tool.



beta\_managed\_agents\_text\_block: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



beta\_managed\_agents\_image\_block: object { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.



beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type } 

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").



type: "base64"

"base64"



beta\_managed\_agents\_url\_image\_source: object { type, url } 

Image referenced by URL.



type: "url"

"url"

url: string

URL of the image to fetch.



beta\_managed\_agents\_file\_image\_source: object { file\_id, type } 

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "image"

"image"



beta\_managed\_agents\_document\_block: object { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.



beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type } 

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").



type: "base64"

"base64"



beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type } 

Plain text document content.

data: string

The plain text content.



media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"



type: "text"

"text"



beta\_managed\_agents\_url\_document\_source: object { type, url } 

Document referenced by URL.



type: "url"

"url"

url: string

URL of the document to fetch.



beta\_managed\_agents\_file\_document\_source: object { file\_id, type } 

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.



beta\_managed\_agents\_search\_result\_block: object { citations, content, source, 2 more } 

A block containing a web search result.



citations: object { enabled } 

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.



content: array of [BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md) { text, type } 

Array of text content blocks from the search result.

text: string

The text content.



type: "text"

"text"

source: string

The URL source of the search result.

title: string

The title of the search result.



type: "search\_result"

"search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.



beta\_managed\_agents\_session\_thread\_status\_rescheduled\_event: object { id, agent\_name, processed\_at, 2 more } 

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that is retrying.



type: "session.thread\_status\_rescheduled"

"session.thread\_status\_rescheduled"



beta\_managed\_agents\_session\_updated\_event: object { id, processed\_at, type, 3 more } 

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



type: "session.updated"

"session.updated"



agent: optional object { id, description, mcp\_servers, 8 more } 

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string



type: "url"

"url"

url: string



model: object { id, speed } 

Model identifier and configuration.



id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-4-8" or 9 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-sonnet-5"

High-performance model for coding and agents

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



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"



multiagent: object { agents, type } 

Resolved coordinator topology with full agent definitions for each roster member.



agents: array of [BetaManagedAgentsSessionThreadAgent](api/beta/agents.md) { id, description, mcp\_servers, 7 more } 

Full `agent` definitions the coordinator may spawn as session threads.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string



type: "url"

"url"

url: string



model: object { id, speed } 

Model identifier and configuration.



id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-4-8" or 9 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-sonnet-5"

High-performance model for coding and agents

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



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 



beta\_managed\_agents\_anthropic\_skill: object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string



type: "anthropic"

"anthropic"

version: string



beta\_managed\_agents\_custom\_skill: object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string



type: "custom"

"custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 



beta\_managed\_agents\_agent\_toolset20260401: object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



type: "agent\_toolset\_20260401"

"agent\_toolset\_20260401"



beta\_managed\_agents\_mcp\_toolset: object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"

mcp\_server\_name: string



type: "mcp\_toolset"

"mcp\_toolset"



beta\_managed\_agents\_custom\_tool: object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: object { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string



type: "custom"

"custom"



type: "agent"

"agent"

version: number



type: "coordinator"

"coordinator"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 



beta\_managed\_agents\_anthropic\_skill: object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string



type: "anthropic"

"anthropic"

version: string



beta\_managed\_agents\_custom\_skill: object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string



type: "custom"

"custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 



beta\_managed\_agents\_agent\_toolset20260401: object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



type: "agent\_toolset\_20260401"

"agent\_toolset\_20260401"



beta\_managed\_agents\_mcp\_toolset: object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"

mcp\_server\_name: string



type: "mcp\_toolset"

"mcp\_toolset"



beta\_managed\_agents\_custom\_tool: object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: object { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string



type: "custom"

"custom"



type: "agent"

"agent"

version: number

metadata: optional map[string]

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

title: optional string

The session's new title. Present only when the update changed it.



beta\_managed\_agents\_start\_event: object { event, type } 

Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event\_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model\_request\_end closes the preview. Only sent on stream connections that opt in via event\_deltas; never appears in event history.



event: [BetaManagedAgentsAgentMessagePreview](api/beta/sessions.md) { id, type }  or [BetaManagedAgentsAgentThinkingPreview](api/beta/sessions.md) { id, type } 

The previewed event's type and id. The event type determines which delta types the preview's event\_delta events carry: agent.message events stream content\_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.



beta\_managed\_agents\_agent\_message\_preview: object { id, type } 

id: string

The id the buffered agent.message will carry if it is emitted. Matches the event\_id on this preview's event\_delta events.



type: "agent.message"

"agent.message"



beta\_managed\_agents\_agent\_thinking\_preview: object { id, type } 

id: string

The id the buffered agent.thinking will carry if it is emitted. Start-only — no event\_delta events follow.



type: "agent.thinking"

"agent.thinking"



type: "event\_start"

"event\_start"



beta\_managed\_agents\_delta\_event: object { delta, event\_id, type } 

An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event\_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model\_request\_end closes the preview. Only sent on stream connections that opt in via event\_deltas; never appears in event history.



delta: object { content, type, index } 

One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content\_delta fragments, each a partial element of the content array.



content: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



type: "content\_delta"

"content\_delta"

index: optional number

Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

event\_id: string

The id of the event being previewed. Matches event.id on the corresponding event\_start and the buffered event that reconciles the preview.



type: "event\_delta"

"event\_delta"



beta\_managed\_agents\_system\_message\_event: object { id, content, type, processed\_at } 

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

id: string

Unique identifier for this event.



content: array of [BetaManagedAgentsSystemContentBlock](api/beta/sessions.md) { text, type } 

System content blocks. Text-only.

text: string

The text content.



type: "text"

"text"



type: "system.message"

"system.message"

processed\_at: optional string

A timestamp in RFC 3339 format

Stream Events

CLI

```shiki
ant beta:sessions:events stream \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
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
