# List Session Thread Events

Copy page



Ruby

# List Session Thread Events

beta.sessions.threads.events.list(thread\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsSessionEvent](api/beta/sessions/events.md)>

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

List Session Thread Events

##### ParametersExpand Collapse

session\_id: String

thread\_id: String

limit: Integer

Query parameter for limit

page: String

Query parameter for page



betas: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

One of the following:

String = String



AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 25 more

One of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

:"fast-mode-2026-02-01"

:"output-300k-2026-03-24"

:"user-profiles-2026-03-24"

:"advisor-tool-2026-03-01"

:"managed-agents-2026-04-01"

:"cache-diagnosis-2026-04-07"

:"thinking-token-count-2026-05-13"

:"server-side-fallback-2026-06-01"

:"fallback-credit-2026-06-01"

##### ReturnsExpand Collapse



BetaManagedAgentsSessionEvent = [BetaManagedAgentsUserMessageEvent](api/beta/sessions/events.md) { id, content, type, processed\_at }  | [BetaManagedAgentsUserInterruptEvent](api/beta/sessions/events.md) { id, type, processed\_at, session\_thread\_id }  | [BetaManagedAgentsUserToolConfirmationEvent](api/beta/sessions/events.md) { id, result, tool\_use\_id, 4 more }  | 31 more

Union type for all event types in a session.

One of the following:



class BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at } 

A user message event in the session conversation.

id: String

Unique identifier for this event.



content: Array[[BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title } ]

Array of content blocks comprising the user message.

One of the following:



class BetaManagedAgentsTextBlock { text, type } 

Regular text content.

text: String

The text content.

type: :text



class BetaManagedAgentsImageBlock { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource { data, media\_type, type } 

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64



class BetaManagedAgentsURLImageSource { type, url } 

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.



class BetaManagedAgentsFileImageSource { file\_id, type } 

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image



class BetaManagedAgentsDocumentBlock { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource { data, media\_type, type } 

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64



class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type } 

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text



class BetaManagedAgentsURLDocumentSource { type, url } 

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource { file\_id, type } 

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

processed\_at: Time

A timestamp in RFC 3339 format



class BetaManagedAgentsUserInterruptEvent { id, type, processed\_at, session\_thread\_id } 

An interrupt event that pauses agent execution and returns control to the user.

id: String

Unique identifier for this event.

type: :"user.interrupt"

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 4 more } 

A tool confirmation event that approves or denies a pending tool execution.

id: String

Unique identifier for this event.



result: :allow | :deny

UserToolConfirmationResult enum

One of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



class BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 4 more } 

Event sent by the client providing the result of a custom tool execution.

id: String

Unique identifier for this event.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"



content: Array[[BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title }  | [BetaManagedAgentsSearchResultBlock](api/beta/sessions/events.md) { citations, content, source, 2 more } ]

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock { text, type } 

Regular text content.

text: String

The text content.

type: :text



class BetaManagedAgentsImageBlock { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource { data, media\_type, type } 

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64



class BetaManagedAgentsURLImageSource { type, url } 

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.



class BetaManagedAgentsFileImageSource { file\_id, type } 

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image



class BetaManagedAgentsDocumentBlock { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource { data, media\_type, type } 

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64



class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type } 

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text



class BetaManagedAgentsURLDocumentSource { type, url } 

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource { file\_id, type } 

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.



class BetaManagedAgentsSearchResultBlock { citations, content, source, 2 more } 

A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) { enabled } 

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: Array[[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md) { text, type } ]

Array of text content blocks from the search result.

text: String

The text content.

type: :text

source: String

The URL source of the search result.

title: String

The title of the search result.

type: :search\_result

is\_error: bool

Whether the tool execution resulted in an error.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



class BetaManagedAgentsAgentCustomToolUseEvent { id, input, name, 3 more } 

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the custom tool being called.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.custom\_tool\_use"

session\_thread\_id: String

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



class BetaManagedAgentsAgentMessageEvent { id, content, processed\_at, type } 

An agent response event in the session conversation.

id: String

Unique identifier for this event.



content: Array[[BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type } ]

Array of text blocks comprising the agent response.

text: String

The text content.

type: :text

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.message"



class BetaManagedAgentsAgentThinkingEvent { id, processed\_at, type } 

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thinking"



class BetaManagedAgentsAgentMCPToolUseEvent { id, input, mcp\_server\_name, 5 more } 

Event emitted when the agent invokes a tool provided by an MCP server.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

mcp\_server\_name: String

Name of the MCP server providing the tool.

name: String

Name of the MCP tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_use"



evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

One of the following:

:allow

:ask

:deny

session\_thread\_id: String

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentMCPToolResultEvent { id, mcp\_tool\_use\_id, processed\_at, 3 more } 

Event representing the result of an MCP tool execution.

id: String

Unique identifier for this event.

mcp\_tool\_use\_id: String

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_result"



content: Array[[BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title }  | [BetaManagedAgentsSearchResultBlock](api/beta/sessions/events.md) { citations, content, source, 2 more } ]

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock { text, type } 

Regular text content.

text: String

The text content.

type: :text



class BetaManagedAgentsImageBlock { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource { data, media\_type, type } 

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64



class BetaManagedAgentsURLImageSource { type, url } 

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.



class BetaManagedAgentsFileImageSource { file\_id, type } 

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image



class BetaManagedAgentsDocumentBlock { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource { data, media\_type, type } 

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64



class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type } 

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text



class BetaManagedAgentsURLDocumentSource { type, url } 

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource { file\_id, type } 

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.



class BetaManagedAgentsSearchResultBlock { citations, content, source, 2 more } 

A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) { enabled } 

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: Array[[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md) { text, type } ]

Array of text content blocks from the search result.

text: String

The text content.

type: :text

source: String

The URL source of the search result.

title: String

The title of the search result.

type: :search\_result

is\_error: bool

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentToolUseEvent { id, input, name, 4 more } 

Event emitted when the agent invokes a built-in agent tool.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the agent tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.tool\_use"



evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

One of the following:

:allow

:ask

:deny

session\_thread\_id: String

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentToolResultEvent { id, processed\_at, tool\_use\_id, 3 more } 

Event representing the result of an agent tool execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

tool\_use\_id: String

The id of the `agent.tool_use` event this result corresponds to.

type: :"agent.tool\_result"



content: Array[[BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title }  | [BetaManagedAgentsSearchResultBlock](api/beta/sessions/events.md) { citations, content, source, 2 more } ]

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock { text, type } 

Regular text content.

text: String

The text content.

type: :text



class BetaManagedAgentsImageBlock { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource { data, media\_type, type } 

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64



class BetaManagedAgentsURLImageSource { type, url } 

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.



class BetaManagedAgentsFileImageSource { file\_id, type } 

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image



class BetaManagedAgentsDocumentBlock { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource { data, media\_type, type } 

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64



class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type } 

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text



class BetaManagedAgentsURLDocumentSource { type, url } 

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource { file\_id, type } 

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.



class BetaManagedAgentsSearchResultBlock { citations, content, source, 2 more } 

A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) { enabled } 

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: Array[[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md) { text, type } ]

Array of text content blocks from the search result.

text: String

The text content.

type: :text

source: String

The URL source of the search result.

title: String

The title of the search result.

type: :search\_result

is\_error: bool

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentThreadMessageReceivedEvent { id, content, from\_session\_thread\_id, 3 more } 

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

id: String

Unique identifier for this event.



content: Array[[BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title } ]

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock { text, type } 

Regular text content.

text: String

The text content.

type: :text



class BetaManagedAgentsImageBlock { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource { data, media\_type, type } 

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64



class BetaManagedAgentsURLImageSource { type, url } 

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.



class BetaManagedAgentsFileImageSource { file\_id, type } 

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image



class BetaManagedAgentsDocumentBlock { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource { data, media\_type, type } 

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64



class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type } 

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text



class BetaManagedAgentsURLDocumentSource { type, url } 

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource { file\_id, type } 

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

from\_session\_thread\_id: String

Public `sthr_` ID of the thread that sent the message.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thread\_message\_received"

from\_agent\_name: String

Name of the callable agent this message came from. Absent when received from the primary agent.



class BetaManagedAgentsAgentThreadMessageSentEvent { id, content, processed\_at, 3 more } 

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

id: String

Unique identifier for this event.



content: Array[[BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title } ]

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock { text, type } 

Regular text content.

text: String

The text content.

type: :text



class BetaManagedAgentsImageBlock { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource { data, media\_type, type } 

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64



class BetaManagedAgentsURLImageSource { type, url } 

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.



class BetaManagedAgentsFileImageSource { file\_id, type } 

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image



class BetaManagedAgentsDocumentBlock { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource { data, media\_type, type } 

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64



class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type } 

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text



class BetaManagedAgentsURLDocumentSource { type, url } 

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource { file\_id, type } 

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

processed\_at: Time

A timestamp in RFC 3339 format

to\_session\_thread\_id: String

Public `sthr_` ID of the thread the message was sent to.

type: :"agent.thread\_message\_sent"

to\_agent\_name: String

Name of the callable agent this message was sent to. Absent when sent to the primary agent.



class BetaManagedAgentsAgentThreadContextCompactedEvent { id, processed\_at, type } 

Indicates that context compaction (summarization) occurred during the session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thread\_context\_compacted"



class BetaManagedAgentsSessionErrorEvent { id, error, processed\_at, type } 

An error event indicating a problem occurred during session execution.

id: String

Unique identifier for this event.



error: [BetaManagedAgentsUnknownError](api/beta/sessions/events.md) { message, retry\_status, type }  | [BetaManagedAgentsModelOverloadedError](api/beta/sessions/events.md) { message, retry\_status, type }  | [BetaManagedAgentsModelRateLimitedError](api/beta/sessions/events.md) { message, retry\_status, type }  | 5 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

One of the following:



class BetaManagedAgentsUnknownError { message, retry\_status, type } 

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: String

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying



class BetaManagedAgentsRetryStatusExhausted { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted



class BetaManagedAgentsRetryStatusTerminal { type } 

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :unknown\_error



class BetaManagedAgentsModelOverloadedError { message, retry\_status, type } 

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: String

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying



class BetaManagedAgentsRetryStatusExhausted { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted



class BetaManagedAgentsRetryStatusTerminal { type } 

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_overloaded\_error



class BetaManagedAgentsModelRateLimitedError { message, retry\_status, type } 

The model request was rate-limited.

message: String

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying



class BetaManagedAgentsRetryStatusExhausted { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted



class BetaManagedAgentsRetryStatusTerminal { type } 

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_rate\_limited\_error



class BetaManagedAgentsModelRequestFailedError { message, retry\_status, type } 

A model request failed for a reason other than overload or rate-limiting.

message: String

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying



class BetaManagedAgentsRetryStatusExhausted { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted



class BetaManagedAgentsRetryStatusTerminal { type } 

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_request\_failed\_error



class BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type } 

Failed to connect to an MCP server.

mcp\_server\_name: String

Name of the MCP server that failed to connect.

message: String

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying



class BetaManagedAgentsRetryStatusExhausted { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted



class BetaManagedAgentsRetryStatusTerminal { type } 

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_connection\_failed\_error



class BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type } 

Authentication to an MCP server failed.

mcp\_server\_name: String

Name of the MCP server that failed authentication.

message: String

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying



class BetaManagedAgentsRetryStatusExhausted { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted



class BetaManagedAgentsRetryStatusTerminal { type } 

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_authentication\_failed\_error



class BetaManagedAgentsBillingError { message, retry\_status, type } 

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: String

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying



class BetaManagedAgentsRetryStatusExhausted { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted



class BetaManagedAgentsRetryStatusTerminal { type } 

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :billing\_error



class BetaManagedAgentsCredentialHostUnreachableError { credential\_id, message, retry\_status, 2 more } 

An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

credential\_id: String

ID of the affected credential.

message: String

Human-readable error description.



retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md) { type } 

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying { type } 

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying



class BetaManagedAgentsRetryStatusExhausted { type } 

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted



class BetaManagedAgentsRetryStatusTerminal { type } 

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :credential\_host\_unreachable\_error

vault\_id: String

ID of the vault containing the affected credential.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.error"



class BetaManagedAgentsSessionStatusRescheduledEvent { id, processed\_at, type } 

Indicates the session is recovering from an error state and is rescheduled for execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_rescheduled"



class BetaManagedAgentsSessionStatusRunningEvent { id, processed\_at, type } 

Indicates the session is actively running and the agent is working.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_running"



class BetaManagedAgentsSessionStatusIdleEvent { id, processed\_at, stop\_reason, type } 

Indicates the agent has paused and is awaiting user input.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format



stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta/sessions/events.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta/sessions/events.md) { type } 

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn { type } 

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn



class BetaManagedAgentsSessionRequiresAction { event\_ids, type } 

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action



class BetaManagedAgentsSessionRetriesExhausted { type } 

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

type: :"session.status\_idle"



class BetaManagedAgentsSessionStatusTerminatedEvent { id, processed\_at, type } 

Indicates the session has terminated, either due to an error or completion.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_terminated"



class BetaManagedAgentsSessionThreadCreatedEvent { id, agent\_name, processed\_at, 2 more } 

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

id: String

Unique identifier for this event.

agent\_name: String

Name of the callable agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public `sthr_` ID of the newly created thread.

type: :"session.thread\_created"



class BetaManagedAgentsSpanOutcomeEvaluationStartEvent { id, iteration, outcome\_id, 2 more } 

Emitted when an outcome evaluation cycle begins.

id: String

Unique identifier for this event.

iteration: Integer

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

outcome\_id: String

The `outc_` ID of the outcome being evaluated.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.outcome\_evaluation\_start"



class BetaManagedAgentsSpanOutcomeEvaluationEndEvent { id, explanation, iteration, 6 more } 

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

id: String

Unique identifier for this event.

explanation: String

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

iteration: Integer

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_evaluation\_start\_id: String

The id of the corresponding `span.outcome_evaluation_start` event.

outcome\_id: String

The `outc_` ID of the outcome being evaluated.

processed\_at: Time

A timestamp in RFC 3339 format

result: String

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

type: :"span.outcome\_evaluation\_end"



usage: [BetaManagedAgentsSpanModelUsage](api/beta/sessions/events.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more } 

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.



speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

:standard

:fast



class BetaManagedAgentsSpanModelRequestStartEvent { id, processed\_at, type } 

Emitted when a model request is initiated by the agent.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_start"



class BetaManagedAgentsSpanModelRequestEndEvent { id, is\_error, model\_request\_start\_id, 3 more } 

Emitted when a model request completes.

id: String

Unique identifier for this event.

is\_error: bool

Whether the model request resulted in an error.

model\_request\_start\_id: String

The id of the corresponding `span.model_request_start` event.



model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta/sessions/events.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more } 

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.



speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

:standard

:fast

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_end"



class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent { id, iteration, outcome\_id, 2 more } 

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

id: String

Unique identifier for this event.

iteration: Integer

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_id: String

The `outc_` ID of the outcome being evaluated.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.outcome\_evaluation\_ongoing"



class BetaManagedAgentsUserDefineOutcomeEvent { id, description, max\_iterations, 4 more } 

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

id: String

Unique identifier for this event.

description: String

What the agent should produce. Copied from the input event.

max\_iterations: Integer

Evaluate-then-revise cycles before giving up. Default 3, max 20.

outcome\_id: String

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

processed\_at: Time

A timestamp in RFC 3339 format



rubric: [BetaManagedAgentsFileRubric](api/beta/sessions/events.md) { file\_id, type }  | [BetaManagedAgentsTextRubric](api/beta/sessions/events.md) { content, type } 

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric { file\_id, type } 

Rubric referenced by a file uploaded via the Files API.

file\_id: String

ID of the rubric file.

type: :file



class BetaManagedAgentsTextRubric { content, type } 

Rubric content provided inline as text.

content: String

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: :text

type: :"user.define\_outcome"



class BetaManagedAgentsSessionDeletedEvent { id, processed\_at, type } 

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.deleted"



class BetaManagedAgentsSessionThreadStatusRunningEvent { id, agent\_name, processed\_at, 2 more } 

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that started running.

type: :"session.thread\_status\_running"



class BetaManagedAgentsSessionThreadStatusIdleEvent { id, agent\_name, processed\_at, 3 more } 

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that went idle.



stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta/sessions/events.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta/sessions/events.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta/sessions/events.md) { type } 

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn { type } 

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn



class BetaManagedAgentsSessionRequiresAction { event\_ids, type } 

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action



class BetaManagedAgentsSessionRetriesExhausted { type } 

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

type: :"session.thread\_status\_idle"



class BetaManagedAgentsSessionThreadStatusTerminatedEvent { id, agent\_name, processed\_at, 2 more } 

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that terminated.

type: :"session.thread\_status\_terminated"



class BetaManagedAgentsUserToolResultEvent { id, tool\_use\_id, type, 4 more } 

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

id: String

Unique identifier for this event.

tool\_use\_id: String

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_result"



content: Array[[BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title }  | [BetaManagedAgentsSearchResultBlock](api/beta/sessions/events.md) { citations, content, source, 2 more } ]

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock { text, type } 

Regular text content.

text: String

The text content.

type: :text



class BetaManagedAgentsImageBlock { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource { data, media\_type, type } 

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64



class BetaManagedAgentsURLImageSource { type, url } 

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.



class BetaManagedAgentsFileImageSource { file\_id, type } 

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image



class BetaManagedAgentsDocumentBlock { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource { data, media\_type, type } 

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64



class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type } 

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text



class BetaManagedAgentsURLDocumentSource { type, url } 

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource { file\_id, type } 

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.



class BetaManagedAgentsSearchResultBlock { citations, content, source, 2 more } 

A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) { enabled } 

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: Array[[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md) { text, type } ]

Array of text content blocks from the search result.

text: String

The text content.

type: :text

source: String

The URL source of the search result.

title: String

The title of the search result.

type: :search\_result

is\_error: bool

Whether the tool execution resulted in an error.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.



class BetaManagedAgentsSessionThreadStatusRescheduledEvent { id, agent\_name, processed\_at, 2 more } 

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that is retrying.

type: :"session.thread\_status\_rescheduled"



class BetaManagedAgentsSessionUpdatedEvent { id, processed\_at, type, 3 more } 

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.updated"



agent: [BetaManagedAgentsSessionAgent](api/beta/sessions.md) { id, description, mcp\_servers, 8 more } 

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: String

description: String



mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } ]

name: String

type: :url

url: String



model: [BetaManagedAgentsModelConfig](api/beta/agents.md) { id, speed } 

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



BetaManagedAgentsModel = :"claude-fable-5" | :"claude-opus-4-8" | :"claude-opus-4-7" | 8 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-6"

Most intelligent model for building agents and coding

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

String = String



speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

:standard

:fast



multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](api/beta/sessions.md) { agents, type } 

Resolved coordinator topology with full agent definitions for each roster member.



agents: Array[[BetaManagedAgentsSessionThreadAgent](api/beta/agents.md) { id, description, mcp\_servers, 7 more } ]

Full `agent` definitions the coordinator may spawn as session threads.

id: String

description: String



mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } ]

name: String

type: :url

url: String



model: [BetaManagedAgentsModelConfig](api/beta/agents.md) { id, speed } 

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



BetaManagedAgentsModel = :"claude-fable-5" | :"claude-opus-4-8" | :"claude-opus-4-7" | 8 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-6"

Most intelligent model for building agents and coding

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

String = String



speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

:standard

:fast

name: String



skills: Array[[BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } ]

One of the following:



class BetaManagedAgentsAnthropicSkill { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: String

type: :anthropic

version: String



class BetaManagedAgentsCustomSkill { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: String

type: :custom

version: String

system\_: String



tools: Array[[BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } ]

One of the following:



class BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type } 



configs: Array[[BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } ]

enabled: bool



name: :bash | :edit | :read | 5 more

Built-in agent tool identifier.

One of the following:

:bash

:edit

:read

:write

:glob

:grep

:web\_fetch

:web\_search



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask

type: :agent\_toolset\_20260401



class BetaManagedAgentsMCPToolset { configs, default\_config, mcp\_server\_name, type } 



configs: Array[[BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } ]

enabled: bool

name: String



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask

mcp\_server\_name: String

type: :mcp\_toolset



class BetaManagedAgentsCustomTool { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: String



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: :object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

type: :custom

type: :agent

version: Integer

type: :coordinator

name: String



skills: Array[[BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } ]

One of the following:



class BetaManagedAgentsAnthropicSkill { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: String

type: :anthropic

version: String



class BetaManagedAgentsCustomSkill { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: String

type: :custom

version: String

system\_: String



tools: Array[[BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } ]

One of the following:



class BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type } 



configs: Array[[BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } ]

enabled: bool



name: :bash | :edit | :read | 5 more

Built-in agent tool identifier.

One of the following:

:bash

:edit

:read

:write

:glob

:grep

:web\_fetch

:web\_search



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask

type: :agent\_toolset\_20260401



class BetaManagedAgentsMCPToolset { configs, default\_config, mcp\_server\_name, type } 



configs: Array[[BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } ]

enabled: bool

name: String



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask

mcp\_server\_name: String

type: :mcp\_toolset



class BetaManagedAgentsCustomTool { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: String



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: :object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

type: :custom

type: :agent

version: Integer

metadata: Hash[Symbol, String]

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

title: String

The session's new title. Present only when the update changed it.



class BetaManagedAgentsSystemMessageEvent { id, content, type, processed\_at } 

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

id: String

Unique identifier for this event.



content: Array[[BetaManagedAgentsSystemContentBlock](api/beta/sessions.md) { text, type } ]

System content blocks. Text-only.

text: String

The text content.

type: :text

type: :"system.message"

processed\_at: Time

A timestamp in RFC 3339 format

List Session Thread Events

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.sessions.threads.events.list(
  "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7"
)

puts(page)
```

Response 200



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
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



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
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
