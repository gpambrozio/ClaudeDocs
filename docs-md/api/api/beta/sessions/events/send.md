# Send Events

Copy page

cURL

# Send Events

POST/v1/sessions/{session\_id}/events

Send Events

##### Path ParametersExpand Collapse

session\_id: string

##### Header ParametersExpand Collapse

"anthropic-beta": optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

UnionMember0 = string

UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 18 more

Accepts one of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

##### Body ParametersJSONExpand Collapse

events: array of [BetaManagedAgentsEventParams](api/beta.md)

Events to send to the `session`.

Accepts one of the following:

BetaManagedAgentsUserMessageEventParams = object { content, type }

Parameters for sending a user message to the session.

content: array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

Array of content blocks for the user message.

Accepts one of the following:

BetaManagedAgentsTextBlock = object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock = object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource = object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource = object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource = object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock = object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource = object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource = object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource = object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource = object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

BetaManagedAgentsUserInterruptEventParams = object { type }

Parameters for sending an interrupt to pause the agent.

type: "user.interrupt"

BetaManagedAgentsUserToolConfirmationEventParams = object { result, tool\_use\_id, type, deny\_message }

Parameters for confirming or denying a tool execution request.

result: "allow" or "deny"

UserToolConfirmationResult enum

Accepts one of the following:

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

BetaManagedAgentsUserCustomToolResultEventParams = object { custom\_tool\_use\_id, type, content, is\_error }

Parameters for providing the result of a custom tool execution.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

The result content returned by the tool.

Accepts one of the following:

BetaManagedAgentsTextBlock = object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock = object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource = object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource = object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource = object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock = object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource = object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource = object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource = object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource = object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

is\_error: optional boolean

Whether the tool execution resulted in an error.

##### ReturnsExpand Collapse

BetaManagedAgentsSendSessionEvents = object { data }

Events that were successfully sent to the session.

data: optional array of [BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  or [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at }  or [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 3 more }  or [BetaManagedAgentsUserCustomToolResultEvent](api/beta.md) { id, custom\_tool\_use\_id, type, 3 more }

Sent events

Accepts one of the following:

BetaManagedAgentsUserMessageEvent = object { id, content, type, processed\_at }

A user message event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

Array of content blocks comprising the user message.

Accepts one of the following:

BetaManagedAgentsTextBlock = object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock = object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource = object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource = object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource = object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock = object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource = object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource = object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource = object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource = object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

processed\_at: optional string

A timestamp in RFC 3339 format

BetaManagedAgentsUserInterruptEvent = object { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.

type: "user.interrupt"

processed\_at: optional string

A timestamp in RFC 3339 format

BetaManagedAgentsUserToolConfirmationEvent = object { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: string

Unique identifier for this event.

result: "allow" or "deny"

UserToolConfirmationResult enum

Accepts one of the following:

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: optional string

A timestamp in RFC 3339 format

BetaManagedAgentsUserCustomToolResultEvent = object { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: string

Unique identifier for this event.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

The result content returned by the tool.

Accepts one of the following:

BetaManagedAgentsTextBlock = object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock = object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource = object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource = object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource = object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock = object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource = object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource = object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource = object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource = object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

Send Events

cURL

```shiki
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/events \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "events": [
            {
              "content": [
                {
                  "text": "Where is my order #1234?",
                  "type": "text"
                }
              ],
              "type": "user.message"
            }
          ]
        }'
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
    }
  ]
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
    }
  ]
}
```

---

*Copyright © Anthropic. All rights reserved.*
