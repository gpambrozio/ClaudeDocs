# List Events

Copy page

Java

# List Events

EventListPage beta().sessions().events().list(EventListParamsparams = EventListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/events

List Events

##### ParametersExpand Collapse

EventListParams params

Optional<String> sessionId

Optional<Long> limit

Query parameter for limit

Optional<[Order](api/beta/sessions/events/list.md)> order

Sort direction for results, ordered by created\_at. Defaults to asc (chronological).

ASC("asc")

DESC("desc")

Optional<String> page

Opaque pagination cursor from a previous response's next\_page.

Optional<List<AnthropicBeta>> betas

Optional header to specify the beta version(s) you want to use.

MESSAGE\_BATCHES\_2024\_09\_24("message-batches-2024-09-24")

PROMPT\_CACHING\_2024\_07\_31("prompt-caching-2024-07-31")

COMPUTER\_USE\_2024\_10\_22("computer-use-2024-10-22")

COMPUTER\_USE\_2025\_01\_24("computer-use-2025-01-24")

PDFS\_2024\_09\_25("pdfs-2024-09-25")

TOKEN\_COUNTING\_2024\_11\_01("token-counting-2024-11-01")

TOKEN\_EFFICIENT\_TOOLS\_2025\_02\_19("token-efficient-tools-2025-02-19")

OUTPUT\_128K\_2025\_02\_19("output-128k-2025-02-19")

FILES\_API\_2025\_04\_14("files-api-2025-04-14")

MCP\_CLIENT\_2025\_04\_04("mcp-client-2025-04-04")

MCP\_CLIENT\_2025\_11\_20("mcp-client-2025-11-20")

DEV\_FULL\_THINKING\_2025\_05\_14("dev-full-thinking-2025-05-14")

INTERLEAVED\_THINKING\_2025\_05\_14("interleaved-thinking-2025-05-14")

CODE\_EXECUTION\_2025\_05\_22("code-execution-2025-05-22")

EXTENDED\_CACHE\_TTL\_2025\_04\_11("extended-cache-ttl-2025-04-11")

CONTEXT\_1M\_2025\_08\_07("context-1m-2025-08-07")

CONTEXT\_MANAGEMENT\_2025\_06\_27("context-management-2025-06-27")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED\_2025\_08\_26("model-context-window-exceeded-2025-08-26")

SKILLS\_2025\_10\_02("skills-2025-10-02")

FAST\_MODE\_2026\_02\_01("fast-mode-2026-02-01")

OUTPUT\_300K\_2026\_03\_24("output-300k-2026-03-24")

ADVISOR\_TOOL\_2026\_03\_01("advisor-tool-2026-03-01")

USER\_PROFILES\_2026\_03\_24("user-profiles-2026-03-24")

##### ReturnsExpand Collapse

class BetaManagedAgentsSessionEvent: A class that can be one of several variants.union

Union type for all event types in a session.

class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

String id

Unique identifier for this event.

List<Content> content

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

String id

Unique identifier for this event.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

String id

Unique identifier for this event.

Result result

UserToolConfirmationResult enum

Accepts one of the following:

ALLOW("allow")

DENY("deny")

String toolUseId

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<String> denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

String id

Unique identifier for this event.

String customToolUseId

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<List<Content>> content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the custom tool being called.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

String id

Unique identifier for this event.

List<[BetaManagedAgentsTextBlock](api/beta.md)> content

Array of text blocks comprising the agent response.

String text

The text content.

Type type

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String mcpServerName

Name of the MCP server providing the tool.

String name

Name of the MCP tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

String id

Unique identifier for this event.

String mcpToolUseId

The id of the `agent.mcp_tool_use` event this result corresponds to.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<List<Content>> content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Optional<Boolean> isError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the agent tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String toolUseId

The id of the `agent.tool_use` event this result corresponds to.

Type type

Optional<List<Content>> content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Optional<Boolean> isError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

String id

Unique identifier for this event.

Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

String mcpServerName

Name of the MCP server that failed to connect.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

String mcpServerName

Name of the MCP server that failed authentication.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type

Type type

class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

String id

Unique identifier for this event.

Optional<Boolean> isError

Whether the model request resulted in an error.

String modelRequestStartId

The id of the corresponding `span.model_request_start` event.

[BetaManagedAgentsSpanModelUsage](api/beta.md) modelUsage

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.

Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

List Events

Java

```shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.events.EventListPage;
import com.anthropic.models.beta.sessions.events.EventListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        EventListPage page = client.beta().sessions().events().list("sesn_011CZkZAtmR3yMPDzynEDxu7");
    }
}
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
