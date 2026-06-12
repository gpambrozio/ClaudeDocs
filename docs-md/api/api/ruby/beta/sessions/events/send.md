# Send Events

Copy page

SDK language

Ruby

# Send Events

beta.sessions.events.send\_(session\_id, \*\*kwargs) -> [BetaManagedAgentsSendSessionEvents](api/beta.md) { data }

POST/v1/sessions/{session\_id}/events

Send Events

##### ParametersExpand Collapse

session\_id: String



events: Array[[BetaManagedAgentsEventParams](api/beta.md)]

Events to send to the `session`.

One of the following:



class BetaManagedAgentsUserMessageEventParams { content, type } 

Parameters for sending a user message to the session.



content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks for the user message.

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

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type } 

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

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type } 

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



class BetaManagedAgentsUserInterruptEventParams { type, session\_thread\_id } 

Parameters for sending an interrupt to pause the agent.

type: :"user.interrupt"

session\_thread\_id: String

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserToolConfirmationEventParams { result, tool\_use\_id, type, deny\_message } 

Parameters for confirming or denying a tool execution request.

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



class BetaManagedAgentsUserCustomToolResultEventParams { custom\_tool\_use\_id, type, content, is\_error } 

Parameters for providing the result of a custom tool execution.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"



content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }  | [BetaManagedAgentsSearchResultBlock](api/beta.md) { citations, content, source, 2 more } ]

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

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type } 

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

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type } 

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

citations: [BetaManagedAgentsSearchResultCitations](api/beta.md) { enabled } 

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: Array[[BetaManagedAgentsSearchResultContent](api/beta.md) { text, type } ]

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

class BetaManagedAgentsUserDefineOutcomeEventParams { description, rubric, type, max\_iterations } 

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

description: String

What the agent should produce. This is the task specification.



rubric: [BetaManagedAgentsFileRubricParams](api/beta.md) { file\_id, type }  | [BetaManagedAgentsTextRubricParams](api/beta.md) { content, type } 

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubricParams { file\_id, type } 

Rubric referenced by a file uploaded via the Files API.

file\_id: String

ID of the rubric file.

type: :file



class BetaManagedAgentsTextRubricParams { content, type } 

Rubric content provided inline as text.

content: String

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

type: :text

type: :"user.define\_outcome"

max\_iterations: Integer

Eval→revision cycles before giving up. Default 3, max 20.



class BetaManagedAgentsUserToolResultEventParams { tool\_use\_id, type, content, is\_error } 

Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

tool\_use\_id: String

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_result"



content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }  | [BetaManagedAgentsSearchResultBlock](api/beta.md) { citations, content, source, 2 more } ]

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

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type } 

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

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type } 

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

citations: [BetaManagedAgentsSearchResultCitations](api/beta.md) { enabled } 

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: Array[[BetaManagedAgentsSearchResultContent](api/beta.md) { text, type } ]

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

class BetaManagedAgentsSystemMessageEventParams { content, type } 

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.



content: Array[[BetaManagedAgentsSystemContentBlock](api/beta.md) { text, type } ]

System content blocks to append. Text-only.

text: String

The text content.

type: :text

type: :"system.message"

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

class BetaManagedAgentsSendSessionEvents { data } 

Events that were successfully sent to the session.



data: Array[[BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  | [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at, session\_thread\_id }  | [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 4 more }  | 4 more]

Sent events

One of the following:



class BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at } 

A user message event in the session conversation.

id: String

Unique identifier for this event.



content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

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

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type } 

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

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type } 

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

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }  | [BetaManagedAgentsSearchResultBlock](api/beta.md) { citations, content, source, 2 more } ]

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

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type } 

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

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type } 

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

citations: [BetaManagedAgentsSearchResultCitations](api/beta.md) { enabled } 

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: Array[[BetaManagedAgentsSearchResultContent](api/beta.md) { text, type } ]

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

rubric: [BetaManagedAgentsFileRubric](api/beta.md) { file\_id, type }  | [BetaManagedAgentsTextRubric](api/beta.md) { content, type } 

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

class BetaManagedAgentsUserToolResultEvent { id, tool\_use\_id, type, 4 more } 

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

id: String

Unique identifier for this event.

tool\_use\_id: String

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_result"



content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }  | [BetaManagedAgentsSearchResultBlock](api/beta.md) { citations, content, source, 2 more } ]

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

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type } 

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

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type } 

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

citations: [BetaManagedAgentsSearchResultCitations](api/beta.md) { enabled } 

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: Array[[BetaManagedAgentsSearchResultContent](api/beta.md) { text, type } ]

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

class BetaManagedAgentsSystemMessageEvent { id, content, type, processed\_at } 

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

id: String

Unique identifier for this event.



content: Array[[BetaManagedAgentsSystemContentBlock](api/beta.md) { text, type } ]

System content blocks. Text-only.

text: String

The text content.

type: :text

type: :"system.message"

processed\_at: Time

A timestamp in RFC 3339 format

Send Events

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_send_session_events = anthropic.beta.sessions.events.send_(
  "sesn_011CZkZAtmR3yMPDzynEDxu7",
  events: [{content: [{text: "Where is my order #1234?", type: :text}], type: :"user.message"}]
)

puts(beta_managed_agents_send_session_events)
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
  ]
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
  ]
}
```

---

*Copyright © Anthropic. All rights reserved.*
