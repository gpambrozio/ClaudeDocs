# Send Events

Copy page



Python

# Send Events

beta.sessions.events.send(strsession\_id, EventSendParams\*\*kwargs)  -> [BetaManagedAgentsSendSessionEvents](api/beta/sessions/events.md)

POST/v1/sessions/{session\_id}/events

Send Events

##### ParametersExpand Collapse

session\_id: str



events: Iterable[[BetaManagedAgentsEventParams](api/beta/sessions/events.md)]

Events to send to the `session`.

One of the following:



class BetaManagedAgentsUserMessageEventParams: …

Parameters for sending a user message to the session.



content: List[Content]

Array of content blocks for the user message.

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



class BetaManagedAgentsUserInterruptEventParams: …

Parameters for sending an interrupt to pause the agent.

type: Literal["user.interrupt"]

session\_thread\_id: Optional[str]

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserToolConfirmationEventParams: …

Parameters for confirming or denying a tool execution request.

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



class BetaManagedAgentsUserCustomToolResultEventParams: …

Parameters for providing the result of a custom tool execution.

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

citations: [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md)

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: List[[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)]

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

class BetaManagedAgentsUserDefineOutcomeEventParams: …

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

description: str

What the agent should produce. This is the task specification.



rubric: Rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubricParams: …

Rubric referenced by a file uploaded via the Files API.

file\_id: str

ID of the rubric file.

type: Literal["file"]



class BetaManagedAgentsTextRubricParams: …

Rubric content provided inline as text.

content: str

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

type: Literal["text"]

type: Literal["user.define\_outcome"]

max\_iterations: Optional[int]

Eval→revision cycles before giving up. Default 3, max 20.



class BetaManagedAgentsUserToolResultEventParams: …

Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

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

citations: [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md)

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: List[[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)]

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

class BetaManagedAgentsSystemMessageEventParams: …

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.



content: List[[BetaManagedAgentsSystemContentBlock](api/beta/sessions.md)]

System content blocks to append. Text-only.

text: str

The text content.

type: Literal["text"]

type: Literal["system.message"]



betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

One of the following:

str



Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]

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

"agent-memory-2026-07-22"

##### ReturnsExpand Collapse



class BetaManagedAgentsSendSessionEvents: …

Events that were successfully sent to the session.



data: Optional[List[Data]]

Sent events

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

citations: [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md)

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: List[[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)]

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

citations: [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md)

Citation settings for a search result.

enabled: bool

Whether citations are enabled for this search result.



content: List[[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)]

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

class BetaManagedAgentsSystemMessageEvent: …

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

id: str

Unique identifier for this event.



content: List[[BetaManagedAgentsSystemContentBlock](api/beta/sessions.md)]

System content blocks. Text-only.

text: str

The text content.

type: Literal["text"]

type: Literal["system.message"]

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

Send Events

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_send_session_events = client.beta.sessions.events.send(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
    events=[{
        "content": [{
            "text": "Where is my order #1234?",
            "type": "text",
        }],
        "type": "user.message",
    }],
)
print(beta_managed_agents_send_session_events.data)
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
