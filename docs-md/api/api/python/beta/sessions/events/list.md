# List Events

Copy page

Python

# List Events

beta.sessions.events.list(strsession\_id, EventListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsSessionEvent](api/beta.md)]

GET/v1/sessions/{session\_id}/events

List Events

##### ParametersExpand Collapse

session\_id: str

limit: Optional[int]

Query parameter for limit

order: Optional[Literal["asc", "desc"]]

Sort direction for results, ordered by created\_at. Defaults to asc (chronological).

Accepts one of the following:

"asc"

"desc"

page: Optional[str]

Opaque pagination cursor from a previous response's next\_page.

betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

str

Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 19 more]

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

"advisor-tool-2026-03-01"

##### ReturnsExpand Collapse

[BetaManagedAgentsSessionEvent](api/beta.md)

Union type for all event types in a session.

Accepts one of the following:

class BetaManagedAgentsUserMessageEvent: …

A user message event in the session conversation.

id: str

Unique identifier for this event.

content: List[Content]

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]

class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.

source: Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]

class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.

class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]

class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]

class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]

class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

type: Literal["user.message"]

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent: …

An interrupt event that pauses agent execution and returns control to the user.

id: str

Unique identifier for this event.

type: Literal["user.interrupt"]

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEvent: …

A tool confirmation event that approves or denies a pending tool execution.

id: str

Unique identifier for this event.

result: Literal["allow", "deny"]

UserToolConfirmationResult enum

Accepts one of the following:

"allow"

"deny"

tool\_use\_id: str

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: Literal["user.tool\_confirmation"]

deny\_message: Optional[str]

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEvent: …

Event sent by the client providing the result of a custom tool execution.

id: str

Unique identifier for this event.

custom\_tool\_use\_id: str

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: Literal["user.custom\_tool\_result"]

content: Optional[List[Content]]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]

class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.

source: Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]

class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.

class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]

class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]

class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]

class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

is\_error: Optional[bool]

Whether the tool execution resulted in an error.

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

class BetaManagedAgentsAgentCustomToolUseEvent: …

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: str

Unique identifier for this event.

input: Dict[str, object]

Input parameters for the tool call.

name: str

Name of the custom tool being called.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.custom\_tool\_use"]

class BetaManagedAgentsAgentMessageEvent: …

An agent response event in the session conversation.

id: str

Unique identifier for this event.

content: List[[BetaManagedAgentsTextBlock](api/beta.md)]

Array of text blocks comprising the agent response.

text: str

The text content.

type: Literal["text"]

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.message"]

class BetaManagedAgentsAgentThinkingEvent: …

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.thinking"]

class BetaManagedAgentsAgentMCPToolUseEvent: …

Event emitted when the agent invokes a tool provided by an MCP server.

id: str

Unique identifier for this event.

input: Dict[str, object]

Input parameters for the tool call.

mcp\_server\_name: str

Name of the MCP server providing the tool.

name: str

Name of the MCP tool being used.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.mcp\_tool\_use"]

evaluated\_permission: Optional[Literal["allow", "ask", "deny"]]

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"

"ask"

"deny"

class BetaManagedAgentsAgentMCPToolResultEvent: …

Event representing the result of an MCP tool execution.

id: str

Unique identifier for this event.

mcp\_tool\_use\_id: str

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.mcp\_tool\_result"]

content: Optional[List[Content]]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]

class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.

source: Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]

class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.

class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]

class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]

class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]

class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

is\_error: Optional[bool]

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent: …

Event emitted when the agent invokes a built-in agent tool.

id: str

Unique identifier for this event.

input: Dict[str, object]

Input parameters for the tool call.

name: str

Name of the agent tool being used.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.tool\_use"]

evaluated\_permission: Optional[Literal["allow", "ask", "deny"]]

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"

"ask"

"deny"

class BetaManagedAgentsAgentToolResultEvent: …

Event representing the result of an agent tool execution.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

tool\_use\_id: str

The id of the `agent.tool_use` event this result corresponds to.

type: Literal["agent.tool\_result"]

content: Optional[List[Content]]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]

class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.

source: Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]

class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.

class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]

class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]

class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]

class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

is\_error: Optional[bool]

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadContextCompactedEvent: …

Indicates that context compaction (summarization) occurred during the session.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.thread\_context\_compacted"]

class BetaManagedAgentsSessionErrorEvent: …

An error event indicating a problem occurred during session execution.

id: str

Unique identifier for this event.

error: Error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError: …

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: str

Human-readable error description.

retry\_status: RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]

class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]

class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["unknown\_error"]

class BetaManagedAgentsModelOverloadedError: …

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: str

Human-readable error description.

retry\_status: RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]

class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]

class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["model\_overloaded\_error"]

class BetaManagedAgentsModelRateLimitedError: …

The model request was rate-limited.

message: str

Human-readable error description.

retry\_status: RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]

class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]

class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["model\_rate\_limited\_error"]

class BetaManagedAgentsModelRequestFailedError: …

A model request failed for a reason other than overload or rate-limiting.

message: str

Human-readable error description.

retry\_status: RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]

class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]

class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["model\_request\_failed\_error"]

class BetaManagedAgentsMCPConnectionFailedError: …

Failed to connect to an MCP server.

mcp\_server\_name: str

Name of the MCP server that failed to connect.

message: str

Human-readable error description.

retry\_status: RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]

class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]

class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["mcp\_connection\_failed\_error"]

class BetaManagedAgentsMCPAuthenticationFailedError: …

Authentication to an MCP server failed.

mcp\_server\_name: str

Name of the MCP server that failed authentication.

message: str

Human-readable error description.

retry\_status: RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]

class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]

class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["mcp\_authentication\_failed\_error"]

class BetaManagedAgentsBillingError: …

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: str

Human-readable error description.

retry\_status: RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]

class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]

class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["billing\_error"]

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.error"]

class BetaManagedAgentsSessionStatusRescheduledEvent: …

Indicates the session is recovering from an error state and is rescheduled for execution.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.status\_rescheduled"]

class BetaManagedAgentsSessionStatusRunningEvent: …

Indicates the session is actively running and the agent is working.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.status\_running"]

class BetaManagedAgentsSessionStatusIdleEvent: …

Indicates the agent has paused and is awaiting user input.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

stop\_reason: StopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn: …

The agent completed its turn naturally and is ready for the next user message.

type: Literal["end\_turn"]

class BetaManagedAgentsSessionRequiresAction: …

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: List[str]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: Literal["requires\_action"]

class BetaManagedAgentsSessionRetriesExhausted: …

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: Literal["retries\_exhausted"]

type: Literal["session.status\_idle"]

class BetaManagedAgentsSessionStatusTerminatedEvent: …

Indicates the session has terminated, either due to an error or completion.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.status\_terminated"]

class BetaManagedAgentsSpanModelRequestStartEvent: …

Emitted when a model request is initiated by the agent.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["span.model\_request\_start"]

class BetaManagedAgentsSpanModelRequestEndEvent: …

Emitted when a model request completes.

id: str

Unique identifier for this event.

is\_error: Optional[bool]

Whether the model request resulted in an error.

model\_request\_start\_id: str

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta.md)

Token usage for a single model request.

cache\_creation\_input\_tokens: int

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: int

Tokens read from prompt cache in this request.

input\_tokens: int

Input tokens consumed by this request.

output\_tokens: int

Output tokens generated by this request.

speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["span.model\_request\_end"]

class BetaManagedAgentsSessionDeletedEvent: …

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.deleted"]

List Events

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.sessions.events.list(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
page = page.data[0]
print(page)
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
