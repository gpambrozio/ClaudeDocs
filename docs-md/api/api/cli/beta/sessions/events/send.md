# Send Events

Copy page

SDK language

CLI

# Send Events

$ ant beta:sessions:events send

POST/v1/sessions/{session\_id}/events

Send Events

##### ParametersExpand Collapse

--session-id: string

Path param: Path parameter session\_id

--event: array of [BetaManagedAgentsEventParams](api/beta.md)

Body param: Events to send to the `session`.

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



beta\_managed\_agents\_send\_session\_events: object { data } 

Events that were successfully sent to the session.



data: optional array of [BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  or [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at, session\_thread\_id }  or [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 4 more }  or 4 more

Sent events



beta\_managed\_agents\_user\_message\_event: object { id, content, type, processed\_at } 

A user message event in the session conversation.

id: string

Unique identifier for this event.



content: array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } 

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

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type } 

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

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type } 

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

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](api/beta.md) { citations, content, source, 2 more } 

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

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type } 

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

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type } 

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

content: array of [BetaManagedAgentsSearchResultContent](api/beta.md) { text, type } 

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

rubric: [BetaManagedAgentsFileRubric](api/beta.md) { file\_id, type }  or [BetaManagedAgentsTextRubric](api/beta.md) { content, type } 

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

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](api/beta.md) { citations, content, source, 2 more } 

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

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type } 

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

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type } 

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

content: array of [BetaManagedAgentsSearchResultContent](api/beta.md) { text, type } 

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

beta\_managed\_agents\_system\_message\_event: object { id, content, type, processed\_at } 

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

id: string

Unique identifier for this event.



content: array of [BetaManagedAgentsSystemContentBlock](api/beta.md) { text, type } 

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

Send Events

CLI

```shiki
ant beta:sessions:events send \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --event "{content: [{text: 'Where is my order #1234?', type: text}], type: user.message}"
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
